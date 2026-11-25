"""Deterministic checks of the agent tasks (spec §13).

A check is `{"type": <name>, ...}` in `evals/agent/tasks.jsonl`; `CHECKS[name](run, check)` says whether
it holds on what the task left behind (`TaskRun`: answers, traces, findings, confirmations asked). A
task whose precondition fails is `invalid`, never `passed`: the thing it tests did not happen.
"""

import re
from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal

from src.agent.loop import TurnResult
from src.agent.store import FindingRow

CYRILLIC = re.compile(r"[Ѐ-ӿ]")


@dataclass
class TaskRun:
    task_id: str
    answers: list[str]
    results: list[TurnResult]
    traces: list[dict]
    findings: list[FindingRow]
    confirms_asked: int

    def tool_calls(self) -> list[dict]:
        return [c for t in self.traces for c in t.get("tool_calls", [])]


@dataclass
class TaskScore:
    status: Literal["passed", "failed", "invalid"]
    failed: list[str]


def _calls(run: TaskRun, tool: str) -> list[dict]:
    return [c for c in run.tool_calls() if tool == "*" or c["name"] == tool]


def _answer(run: TaskRun, check: dict) -> str:
    """The answer of one turn (`turn`, default the last) or of all turns (`turn: "all"`)."""
    which = check.get("turn", -1)
    if which == "all":
        return "\n".join(run.answers)
    return run.answers[which] if run.answers else ""


def tools_called(run: TaskRun, check: dict) -> bool:
    names = {c["name"] for c in run.tool_calls()}
    return all(t in names for t in check["tools"])


def tools_not_called(run: TaskRun, check: dict) -> bool:
    names = {c["name"] for c in run.tool_calls()}
    return not any(t in names for t in check["tools"])


def tool_count(run: TaskRun, check: dict) -> bool:
    n = len(_calls(run, check["tool"]))
    return check.get("min", 0) <= n <= check.get("max", n)


def max_attempts(run: TaskRun, check: dict) -> bool:
    """Every call of `tool` took at most `max` attempts (2 retries = 3 attempts, spec §7)."""
    return all(c.get("attempts", 1) <= check["max"] for c in _calls(run, check["tool"]))


def tool_result_contains(run: TaskRun, check: dict) -> bool:
    """Some call of `tool` returned a result containing `text` (e.g. the read_only gate's refusal)."""
    return any(
        check["text"].lower() in c.get("result", "").lower()
        for c in _calls(run, check["tool"])
    )


def findings_count(run: TaskRun, check: dict) -> bool:
    return len(run.findings) == check["equals"]


def confirms_asked(run: TaskRun, check: dict) -> bool:
    return run.confirms_asked == check["equals"]


def stop(run: TaskRun, check: dict) -> bool:
    return bool(run.results) and run.results[-1].stop in check["in"]


def answer_contains(run: TaskRun, check: dict) -> bool:
    text = _answer(run, check).lower()
    return any(term.lower() in text for term in check["any"])


def answer_not_contains(run: TaskRun, check: dict) -> bool:
    text = _answer(run, {**check, "turn": check.get("turn", "all")}).lower()
    return not any(term.lower() in text for term in check["terms"])


def answer_in_english(run: TaskRun, check: dict) -> bool:
    return not CYRILLIC.search("\n".join(run.answers))


CHECKS: dict[str, Callable[[TaskRun, dict], bool]] = {
    "tools_called": tools_called,
    "tools_not_called": tools_not_called,
    "tool_count": tool_count,
    "max_attempts": max_attempts,
    "tool_result_contains": tool_result_contains,
    "findings_count": findings_count,
    "confirms_asked": confirms_asked,
    "stop": stop,
    "answer_contains": answer_contains,
    "answer_not_contains": answer_not_contains,
    "answer_in_english": answer_in_english,
}


def score_task(run: TaskRun, task: dict) -> TaskScore:
    if not all(CHECKS[c["type"]](run, c) for c in task.get("precondition", [])):
        return TaskScore(status="invalid", failed=["precondition"])
    failed = [c["type"] for c in task["checks"] if not CHECKS[c["type"]](run, c)]
    return TaskScore(status="failed" if failed else "passed", failed=failed)
