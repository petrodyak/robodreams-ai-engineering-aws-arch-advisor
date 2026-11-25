"""Tool definitions and their execution (spec §5, §6; lesson 11 `execute`).

- Descriptions live in `prompts/agent_tools_<version>.json` (the lesson-11 `tools-vN.json` shape), so
  they are versioned like prompts; argument schemas are Pydantic models in the tool modules.
- Claude gets the **strict subset** of each schema (`strict: true`). The strict-mode limits are from the
  Claude docs ("JSON Schema Limitations", claude-api skill, checked 25.11): no numeric bounds, no
  `minLength` / `maxLength`, no complex array constraints, `additionalProperties: false` on every
  object. `pattern` is not in the supported list, so it is dropped too. The Pydantic model checks all of
  them again in code before a tool runs.
- `execute` never raises: an unknown tool, invalid arguments, an exception or a timeout come back as an
  `ERROR: …` text the model can act on (`is_error: true`).
- Threads (spec §9): a read-only tool runs in a worker thread with a timeout; a tool that writes runs on
  the calling (main) thread, which owns the SQLite connection, so no write is left running in an
  abandoned thread. `finish`, when given, turns a read-only tool's raw result into the outcome on the
  main thread (where `search_corpus` assigns its labels).
"""

import json
import threading
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ValidationError

PROMPTS_DIR = Path("prompts")

# Keywords strict tool use does not accept (see the module docstring); `title` and `default` carry no
# meaning for the model, and `default` is not in the supported list either.
_DROPPED = {
    "minimum",
    "maximum",
    "exclusiveMinimum",
    "exclusiveMaximum",
    "multipleOf",
    "minLength",
    "maxLength",
    "minItems",
    "maxItems",
    "uniqueItems",
    "pattern",
    "default",
    "title",
}


class ToolOutcome(BaseModel):
    """What one tool call gives back to the model, plus what the trace records about it."""

    text: str
    is_error: bool
    attempts: int = 1
    faults: list[str] = []
    data: dict | None = None


@dataclass
class ToolEntry:
    fn: Callable[[BaseModel], Any]
    args_model: type[BaseModel]
    read_only: bool
    finish: Callable[[Any], ToolOutcome] | None = None


@dataclass
class Attempted:
    """A tool result wrapped by the retry layer (src/agent/faults.py) with its attempt count."""

    value: Any
    attempts: int
    faults: list[str] = field(default_factory=list)


class ToolUnavailable(Exception):
    """The tool's service did not answer: a 503, a 429 or a timeout (spec §7)."""

    def __init__(self, kind: str):
        super().__init__(kind)
        self.kind = kind
        self.attempts = 1
        self.faults: list[str] = []


class ToolTimeout(ToolUnavailable):
    def __init__(self) -> None:
        super().__init__("timeout")


def load_descriptions(version: str, prompts_dir: Path = PROMPTS_DIR) -> dict[str, dict]:
    path = prompts_dir / f"agent_tools_{version}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def strict_schema(schema: dict) -> dict:
    """The strict subset of a Pydantic JSON schema: every property required, nullable when optional."""
    if isinstance(schema, list):
        return [strict_schema(item) for item in schema]
    if not isinstance(schema, dict):
        return schema
    out = {k: strict_schema(v) for k, v in schema.items() if k not in _DROPPED}
    if "properties" in out:
        out["properties"] = {
            name: strict_schema(p) for name, p in schema["properties"].items()
        }
        out["required"] = list(out["properties"])
        out["additionalProperties"] = False
    if "$defs" in out:
        out["$defs"] = {name: strict_schema(d) for name, d in schema["$defs"].items()}
    return out


def tool_spec(name: str, args_model: type[BaseModel], descriptions: dict) -> dict:
    """The Anthropic tool definition: description and parameter texts from the versioned JSON."""
    text = descriptions[name]
    schema = strict_schema(args_model.model_json_schema())
    if "properties" not in schema:  # a tool without arguments
        schema = {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        }
    for param, prop in schema["properties"].items():
        if param in text["params"]:
            prop["description"] = text["params"][param]
    return {
        "name": name,
        "description": text["description"],
        "input_schema": schema,
        "strict": True,
    }


def call_with_timeout(fn: Callable[[Any], Any], args: Any, timeout: float) -> Any:
    """Run `fn(args)` in a daemon thread; raise `ToolTimeout` if it takes longer than `timeout`.

    Used for read-only tools only: a call that times out may still finish in its thread, which is
    harmless because it writes nothing.
    """
    box: dict[str, Any] = {}

    def run() -> None:
        try:
            box["value"] = fn(args)
        except BaseException as error:  # noqa: BLE001 - re-raised in the calling thread below
            box["error"] = error

    worker = threading.Thread(target=run, daemon=True)
    worker.start()
    worker.join(timeout)
    if worker.is_alive():
        raise ToolTimeout()
    if "error" in box:
        raise box["error"]
    return box["value"]


def _validation_text(name: str, error: ValidationError) -> str:
    problems = "; ".join(
        f"{'.'.join(str(p) for p in e['loc']) or 'arguments'}: {e['msg']}"
        for e in error.errors()
    )
    return f"ERROR: invalid arguments for {name}: {problems}. Fix the arguments and call again."


def _unavailable_text(error: ToolUnavailable) -> str:
    plural = "s" if error.attempts != 1 else ""
    return (
        f"ERROR: service unavailable ({error.kind}) after {error.attempts} attempt{plural}; "
        "tell the user, do not guess"
    )


def _to_outcome(raw: Any) -> ToolOutcome:
    if isinstance(raw, ToolOutcome):
        return raw
    if isinstance(raw, str):
        return ToolOutcome(text=raw, is_error=False)
    return ToolOutcome(
        text=json.dumps(raw, ensure_ascii=False, default=str), is_error=False
    )


def execute(
    name: str, raw_input: dict, registry: dict[str, ToolEntry], *, timeout: float
) -> ToolOutcome:
    entry = registry.get(name)
    if entry is None:
        available = ", ".join(sorted(registry)) or "none"
        return ToolOutcome(
            text=f"ERROR: unknown tool '{name}'; the available tools are: {available}",
            is_error=True,
        )
    try:
        args = entry.args_model.model_validate(raw_input)
    except ValidationError as error:
        return ToolOutcome(text=_validation_text(name, error), is_error=True)
    try:
        raw = (
            call_with_timeout(entry.fn, args, timeout)
            if entry.read_only
            else entry.fn(args)
        )
        attempts, faults = 1, []
        if isinstance(raw, Attempted):
            raw, attempts, faults = raw.value, raw.attempts, raw.faults
        outcome = entry.finish(raw) if entry.finish else _to_outcome(raw)
        merged = outcome.faults + [f for f in faults if f not in outcome.faults]
        return outcome.model_copy(update={"attempts": attempts, "faults": merged})
    except ToolUnavailable as error:
        return ToolOutcome(
            text=_unavailable_text(error),
            is_error=True,
            attempts=error.attempts,
            faults=error.faults,
        )
    except Exception as error:  # noqa: BLE001 - execute never raises (spec §6)
        return ToolOutcome(
            text=f"ERROR: {name} failed: {type(error).__name__}: {error}",
            is_error=True,
        )
