"""The agent's MCP client: the three registry tools of `src/mcp_server` as agent tools (spec §9, D12, D15).

- One asyncio loop runs in a background thread for the life of the agent process and holds the MCP
  session (`async with Client(params)`, lesson 12 `host.py`); each call is submitted to it and awaited.
  The agent loop stays synchronous, and lesson 11's thread-based `call_with_timeout` still applies.
- The server gets only `TEAM` and `PATH` (plus the few variables the mcp stdio client itself adds,
  `get_default_environment()`): no Anthropic or Langfuse key reaches it. The command is the agent's own
  Python (`sys.executable -m src.mcp_server`) from the repository root, not `uv run`.
- Every MCP response is validated with a Pydantic model before the model sees it (spec §7 `schema`):
  a mismatch is `is_error` with the field named, and never a silent `None` in the answer.
- A dead server makes the MCP tools return `ERROR: MCP server unavailable`; local tools keep working.
- `get_architecture` records the hash of the version it returned, which `record_finding` needs
  (spec §8, "the architecture was read in this session").
"""

import asyncio
import json
import os
import sys
import threading
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Literal, Self

from mcp import Client, StdioServerParameters
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from src.agent.faults import Fault, faults_for
from src.agent.findings import canonical_hash
from src.agent.tools import ToolEntry, ToolOutcome, strict_schema
from src.mcp_server.quotas import GOLD_SERVICES
from src.mcp_server.registry import ARCH_ID, Architecture

ROOT = Path(__file__).resolve().parents[2]
SERVER_CMD = [sys.executable, "-m", "src.mcp_server"]
UNAVAILABLE = "ERROR: MCP server unavailable"


def server_params(team: str, cmd: list[str] | None = None) -> StdioServerParameters:
    cmd = cmd or SERVER_CMD
    return StdioServerParameters(
        command=cmd[0],
        args=cmd[1:],
        env={"TEAM": team, "PATH": os.environ.get("PATH", "")},
        cwd=str(ROOT),
    )


# arguments, checked by the agent before a call (the server checks them again) -----------------


class ListArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")


class GetArchitectureArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    architecture_id: str = Field(pattern=ARCH_ID)


class QuotaArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    service: Literal[GOLD_SERVICES]  # type: ignore[valid-type]
    quota_name: str | None = Field(default=None, max_length=100)


# responses, validated before the model sees them (spec §7 `schema`) ---------------------------


class ArchitectureRow(BaseModel):
    model_config = ConfigDict(extra="forbid")

    architecture_id: str
    name: str
    updated: date


class ArchitectureList(BaseModel):
    model_config = ConfigDict(extra="forbid")

    architectures: list[ArchitectureRow]
    unreadable_files: list[str]


class QuotaRow(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    default: str
    adjustable: bool
    description: str


class QuotaResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    service: str
    as_of: date
    quotas: list[QuotaRow]
    more: int
    source: str
    note: str | None = None


TOOLS: dict[str, tuple[type[BaseModel], type[BaseModel], str]] = {
    "list_architectures": (ListArgs, ArchitectureList, "registry"),
    "get_architecture": (GetArchitectureArgs, Architecture, "registry"),
    "get_service_quota": (QuotaArgs, QuotaResponse, "quota"),
}


class McpTools:
    """Context manager: start the server and the session, expose its tools, close both on exit."""

    def __init__(
        self,
        team: str,
        *,
        cmd: list[str] | None = None,
        client_factory: Callable[[StdioServerParameters], Any] = Client,
        start_timeout_s: float = 30.0,
    ):
        self.team = team
        self.params = server_params(team, cmd)
        self._factory = client_factory
        self._start_timeout_s = start_timeout_s
        self._ready = threading.Event()
        self._error: BaseException | None = None
        self._loop: asyncio.AbstractEventLoop | None = None
        self._stop: asyncio.Event | None = None
        self._client: Any = None
        self._tools: list = []
        self._thread: threading.Thread | None = None

    # life cycle --------------------------------------------------------------------------------

    async def _main(self) -> None:
        self._loop = asyncio.get_running_loop()
        self._stop = asyncio.Event()
        try:
            async with self._factory(self.params) as client:
                self._client = client
                self._tools = list((await client.list_tools()).tools)
                self._ready.set()
                await self._stop.wait()
        except BaseException as error:  # noqa: BLE001 - reported to the agent thread below
            self._error = error
        finally:
            self._client = None
            self._ready.set()

    def __enter__(self) -> Self:
        self._thread = threading.Thread(
            target=lambda: asyncio.run(self._main()), daemon=True
        )
        self._thread.start()
        if not self._ready.wait(self._start_timeout_s):
            raise RuntimeError(
                f"MCP server did not start: no answer in {self._start_timeout_s:.0f} s"
            )
        if self._error is not None or self._client is None:
            raise RuntimeError(f"MCP server did not start: {_describe(self._error)}")
        return self

    def __exit__(self, *exc: object) -> None:
        if (
            self._loop is not None
            and self._stop is not None
            and not self._loop.is_closed()
        ):
            self._loop.call_soon_threadsafe(self._stop.set)
        if self._thread is not None:
            self._thread.join(timeout=5)

    # tools -------------------------------------------------------------------------------------

    def specs(self) -> list[dict]:
        """The server's tools as Claude tool definitions, in their strict subset (spec §5)."""
        specs = []
        for t in self._tools:
            if (
                t.name not in TOOLS
            ):  # only tools the agent registers are offered (review, minor 3)
                continue
            schema = strict_schema(t.input_schema or {})
            if "properties" not in schema:
                schema = {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                }
            specs.append(
                {
                    "name": t.name,
                    "description": t.description or "",
                    "input_schema": schema,
                    "strict": True,
                }
            )
        return specs

    def call(self, name: str, args: dict, timeout: float) -> Any:
        client, loop = self._client, self._loop
        if client is None or loop is None or loop.is_closed():
            raise ConnectionError("the MCP session is closed")
        future = asyncio.run_coroutine_threadsafe(
            client.call_tool(name, args, read_timeout_seconds=timeout), loop
        )
        return future.result(timeout + 5)

    def entries(
        self, faults: list[Fault], *, arch_hashes: dict[str, str], timeout: float = 10.0
    ) -> dict[str, ToolEntry]:
        """One read-only ToolEntry per server tool: the call in the worker, validation on the main thread."""
        entries = {}
        for t in self._tools:
            if t.name not in TOOLS:
                continue
            args_model, response_model, label = TOOLS[t.name]
            schema_fault = t.name == "get_service_quota" and any(
                f.kind == "schema" for f in faults_for(t.name, faults)
            )
            entries[t.name] = ToolEntry(
                fn=self._caller(t.name, timeout),
                args_model=args_model,
                read_only=True,
                finish=self._finisher(
                    t.name, response_model, label, schema_fault, arch_hashes
                ),
            )
        return entries

    def _caller(self, name: str, timeout: float) -> Callable[[BaseModel], Any]:
        def call(args: BaseModel) -> Any:
            # A slow call is cut by `call_with_timeout` at the same `timeout` and reported as
            # "unavailable (timeout)" without a retry (spec §7, amended 25.11); the mcp read timeout
            # raises MCPError. Any exception here means a dead or closed server.
            try:
                return _Called(
                    self.call(name, args.model_dump(), timeout), args.model_dump()
                )
            except Exception:  # noqa: BLE001 - a dead or closed server, whatever the exception type
                return ToolOutcome(text=UNAVAILABLE, is_error=True)

        return call

    @staticmethod
    def _finisher(
        name: str,
        response_model: type[BaseModel],
        label: str,
        schema_fault: bool,
        arch_hashes: dict[str, str],
    ) -> Callable[[Any], ToolOutcome]:
        def finish(called: Any) -> ToolOutcome:
            if isinstance(called, ToolOutcome):
                return called
            raw, args = called.result, called.args
            text = "".join(getattr(c, "text", "") for c in raw.content or [])
            if raw.is_error:
                text = text.removeprefix(f"Error executing tool {name}: ")
                return ToolOutcome(text=f"ERROR: {text}", is_error=True)
            # mcp 2.3 sends a `-> dict` result as JSON text only (no structured_content)
            data = raw.structured_content
            if data is None:
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    data = None
            if not isinstance(data, dict):
                return ToolOutcome(
                    text=(
                        f"ERROR: the {label} service returned an unexpected format "
                        "(not a JSON object); do not use its numbers"
                    ),
                    is_error=True,
                )
            # the `schema` fault: the API "changed its format", `default` renamed to `value` (§7)
            if schema_fault:
                data = {
                    **data,
                    "quotas": [_rename(row) for row in data.get("quotas", [])],
                }
            try:
                response_model.model_validate(data)
            except ValidationError as error:
                fields = ", ".join(
                    ".".join(str(p) for p in e["loc"]) for e in error.errors()
                )
                return ToolOutcome(
                    text=(
                        f"ERROR: the {label} service returned an unexpected format ({fields}); "
                        "do not use its numbers"
                    ),
                    is_error=True,
                    faults=["schema"] if schema_fault else [],
                )
            out = {"faults": ["schema"]} if schema_fault else {}
            if name == "get_architecture":
                if data.get("id") != args.get("architecture_id"):
                    # only the architecture that was asked for counts as read (review, Important 2)
                    return ToolOutcome(
                        text=(
                            f"ERROR: the {label} service returned an unexpected architecture "
                            f"({data.get('id')!r} for {args.get('architecture_id')!r}); do not use it"
                        ),
                        is_error=True,
                    )
                arch_hashes[data["id"]] = canonical_hash(data)
                return ToolOutcome(
                    text=json.dumps(data, ensure_ascii=False),
                    is_error=False,
                    data={
                        "architecture_id": data["id"],
                        "architecture_hash": arch_hashes[data["id"]],
                    },
                    **out,
                )
            return ToolOutcome(
                text=json.dumps(data, ensure_ascii=False), is_error=False, **out
            )

        return finish


@dataclass
class _Called:
    """A server result together with the arguments it answers (for the id check)."""

    result: Any
    args: dict


def _rename(row: dict) -> dict:
    return {("value" if k == "default" else k): v for k, v in row.items()}


def _describe(error: BaseException | None) -> str:
    """One line for a start-up failure; an ExceptionGroup is flattened to its first leaf."""
    while isinstance(error, BaseExceptionGroup) and error.exceptions:
        error = error.exceptions[0]
    return f"{type(error).__name__}: {error}" if error else "no session"
