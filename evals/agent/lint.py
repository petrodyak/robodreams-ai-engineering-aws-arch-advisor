"""`lint`: problems in the task set and the tool descriptions, run by `make check` (spec §13; lesson 11).

- every tool description is long enough to say when to call the tool, what to pass and what comes back
  (at least 80 characters), and every parameter has a text;
- every task names only existing tools and valid fault kinds, and only known check types.

    uv run python -m evals.agent.lint      (exit 1 when there are problems)
"""

import sys

from evals.agent.checks import CHECKS
from src.agent.faults import parse_faults

TOOLS = (
    "search_corpus",
    "record_finding",
    "remember",
    "list_architectures",
    "get_architecture",
    "get_service_quota",
)
MIN_DESCRIPTION = 80


def _probe():
    from evals.agent.checks import TaskRun
    from src.agent.loop import LoopState, TurnResult

    result = TurnResult(
        answer="", stop="answer", partial=False, state=LoopState(0.0), last_text=""
    )
    return TaskRun(
        task_id="probe",
        answers=[""] * 5,
        results=[result] * 5,
        traces=[{"tool_calls": [], "stop": "answer", "critic": [[]]}] * 5,
        findings=[],
        confirms_asked=0,
    )


_PROBE = _probe()


def lint(tasks: list[dict], descriptions: dict) -> list[str]:
    problems: list[str] = []
    for name, text in descriptions.items():
        description = text.get("description", "")
        if len(description) < MIN_DESCRIPTION:
            problems.append(
                f"tool {name}: description has {len(description)} characters (at least "
                f"{MIN_DESCRIPTION}: when to call it, what to pass, what it returns)"
            )
        problems += [
            f"tool {name}: parameter {p} has no text"
            for p, t in text.get("params", {}).items()
            if not t
        ]
    for task in tasks:
        tid = task.get("id", "?")
        try:
            parse_faults(task.get("faults", ""))
        except ValueError as error:
            problems.append(f"{tid}: {error}")
        for check in task.get("precondition", []) + task.get("checks", []):
            if check.get("type") not in CHECKS:
                problems.append(f"{tid}: unknown check type {check.get('type')!r}")
                continue
            # run the check once on an empty run, so a missing argument or a gold lookup that does
            # not exist fails `make check`, not a paid run (step 25 review, I6)
            try:
                CHECKS[check["type"]](_PROBE, check)
            except (
                KeyError,
                ValueError,
                StopIteration,
                IndexError,
                TypeError,
            ) as error:
                problems.append(
                    f"{tid}: check {check['type']}: {type(error).__name__}: {error}"
                )
            named = list(check.get("tools", [])) + (
                [check["tool"]] if "tool" in check else []
            )
            problems += [
                f"{tid}: unknown tool {t!r}"
                for t in named
                if t != "*" and t not in TOOLS
            ]
    return problems


def main() -> int:
    from evals.agent.run import load_tasks
    from src.agent.tools import load_descriptions

    problems = lint(load_tasks(), load_descriptions("v1"))
    for p in problems:
        sys.stderr.write(p + "\n")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
