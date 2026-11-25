"""The FAULTS= wrapper around every tool call (spec §7).

`FAULTS=timeout,503,429,schema,duplicate` (or `--faults`) replaces real responses so the evals can check
how the agent behaves when a tool fails. A fault may be limited to one tool: `503:search_corpus`.

- `timeout`, `503`, `429` are injected here (`inject`): the tool is not called at all, the error is
  raised at once (no real wait). `schema` and `duplicate` are applied by their owners through
  `faults_for` (the MCP client, Task 23.3; `record_finding`, Task 22.5).
- `with_retries` retries **read-only** tools only: at most 2 retries, backoff 0.5 s then 1 s, with the
  sleep injected so tests and evals never wait. A tool that writes is never retried automatically: a
  retried write is exactly the duplicate the idempotency key guards against.
- The retries are attempts of one call: `attempts` goes to the trace, `max_repeats` does not count them.
"""

import time
from collections.abc import Callable
from dataclasses import replace
from typing import Literal

from pydantic import BaseModel

from src.agent.tools import Attempted, ToolEntry, ToolTimeout, ToolUnavailable

__all__ = [
    "ConnectionDropped",
    "Fault",
    "ToolUnavailable",
    "apply_faults",
    "faults_for",
    "inject",
    "parse_faults",
    "with_retries",
]

FaultKind = Literal["timeout", "503", "429", "schema", "duplicate"]
KINDS: tuple[str, ...] = ("timeout", "503", "429", "schema", "duplicate")
INJECTED = ("timeout", "503", "429")
BACKOFF_S = (0.5, 1.0)  # one value per retry: 2 retries, 3 attempts in all
# the faults applied by their owner touch only that tool, so only that tool's calls carry them
OWNERS = {"schema": "get_service_quota", "duplicate": "record_finding"}


class Fault(BaseModel):
    kind: FaultKind
    tool: str | None


class ConnectionDropped(Exception):
    """The `duplicate` fault: the write committed, then the connection "dropped" (spec §7)."""


def parse_faults(spec: str) -> list[Fault]:
    """`"503:search_corpus,duplicate"` → two faults; an unknown kind raises ValueError."""
    faults = []
    for item in filter(None, (part.strip() for part in spec.split(","))):
        kind, _, tool = item.partition(":")
        if kind not in KINDS:
            raise ValueError(
                f"unknown fault {kind!r}: expected one of {', '.join(KINDS)}"
            )
        faults.append(Fault(kind=kind, tool=tool or None))
    return faults


def faults_for(tool: str, faults: list[Fault]) -> list[Fault]:
    return [f for f in faults if f.tool in (None, tool)]


def inject(kind: str, entry: ToolEntry) -> ToolEntry:
    """An entry that fails with `kind` on every call and never reaches the real tool."""
    if kind not in INJECTED:
        raise ValueError(f"{kind!r} is applied by its tool's owner, not injected here")

    def failing(_args):
        if kind == "timeout":
            raise ToolTimeout()
        raise ToolUnavailable(kind)

    return replace(entry, fn=failing)


def with_retries(
    entry: ToolEntry,
    faults: list[Fault],
    *,
    sleep: Callable[[float], None] = time.sleep,
) -> ToolEntry:
    """Retry a read-only tool on `ToolUnavailable`; tag every result with its attempts and faults."""
    kinds = [f.kind for f in faults]
    attempts_allowed = len(BACKOFF_S) + 1 if entry.read_only else 1
    inner = entry.fn

    def run(args):
        for attempt in range(1, attempts_allowed + 1):
            try:
                return Attempted(value=inner(args), attempts=attempt, faults=kinds)
            except ToolUnavailable as error:
                if attempt == attempts_allowed:
                    error.attempts = attempt
                    error.faults = kinds
                    raise
                sleep(BACKOFF_S[attempt - 1])
        raise AssertionError("unreachable")

    return replace(entry, fn=run)


def apply_faults(
    registry: dict[str, ToolEntry],
    faults: list[Fault],
    *,
    sleep: Callable[[float], None] = time.sleep,
) -> dict[str, ToolEntry]:
    """Wrap every tool: injected faults first, then the retry layer (which also covers real 503s)."""
    wrapped = {}
    for name, entry in registry.items():
        mine = [f for f in faults_for(name, faults) if OWNERS.get(f.kind, name) == name]
        for fault in mine:
            if fault.kind in INJECTED:
                entry = inject(fault.kind, entry)
        wrapped[name] = with_retries(entry, mine, sleep=sleep)
    return wrapped
