"""The agent task set, its checks and the run directory (spec §13; evals/agent/)."""

import json
from datetime import date
from pathlib import Path

from evals.agent.checks import CHECKS, TaskRun, score_task
from evals.agent.run import load_tasks, next_run_dir
from src.agent.faults import parse_faults
from src.agent.loop import LoopState, TurnResult
from src.agent.store import FindingRow


def _result(answer: str, stop: str = "answer") -> TurnResult:
    return TurnResult(
        answer=answer,
        stop=stop,
        partial=stop != "answer",
        state=LoopState(0.0),
        last_text=answer,
    )


def _finding() -> FindingRow:
    return FindingRow(
        id=1,
        architecture_id="lakehouse-iceberg",
        pillar="Reliability",
        best_practice="REL09-BP01",
        severity="high",
        summary="x",
        source_chunk_id="a#1",
        status="open",
        architecture_hash="h",
        opened_at=date(2026, 11, 24),
        resolved_at=None,
    )


def run(
    answer="The search service is unavailable.",
    *,
    stop="answer",
    calls=None,
    findings=0,
    confirms=0,
):
    calls = (
        calls
        if calls is not None
        else [{"name": "search_corpus", "attempts": 3, "is_error": True}]
    )
    return TaskRun(
        task_id="t",
        answers=[answer],
        results=[_result(answer, stop)],
        traces=[{"tool_calls": calls, "stop": stop}],
        findings=[_finding()] * findings,
        confirms_asked=confirms,
    )


def test_score_invalid_when_precondition_fails():
    task = {
        "precondition": [{"type": "tools_called", "tools": ["get_architecture"]}],
        "checks": [{"type": "findings_count", "equals": 0}],
    }
    score = score_task(run(), task)
    assert score.status == "invalid"
    assert (
        score_task(run(), {"precondition": [], "checks": task["checks"]}).status
        == "passed"
    )


def test_score_failed_names_the_checks():
    task = {
        "precondition": [],
        "checks": [
            {"type": "findings_count", "equals": 1},
            {"type": "stop", "in": ["answer"]},
        ],
    }
    score = score_task(run(), task)
    assert score.status == "failed"
    assert score.failed == ["findings_count"]


def test_checks_used_by_fault_tasks():
    r = run()
    assert CHECKS["tools_called"](r, {"tools": ["search_corpus"]})
    assert not CHECKS["tools_called"](r, {"tools": ["record_finding"]})
    assert CHECKS["tools_not_called"](r, {"tools": ["record_finding"]})
    assert CHECKS["tool_count"](r, {"tool": "search_corpus", "min": 1, "max": 3})
    assert not CHECKS["tool_count"](r, {"tool": "search_corpus", "min": 2})
    assert CHECKS["tool_count"](run(calls=[]), {"tool": "*", "max": 0})
    assert CHECKS["max_attempts"](r, {"tool": "search_corpus", "max": 3})
    assert not CHECKS["max_attempts"](r, {"tool": "search_corpus", "max": 2})
    assert CHECKS["findings_count"](run(findings=1), {"equals": 1})
    assert CHECKS["confirms_asked"](run(confirms=0), {"equals": 0})
    assert CHECKS["stop"](r, {"in": ["answer"]})
    assert not CHECKS["stop"](run(stop="max_steps"), {"in": ["answer"]})
    assert CHECKS["answer_contains"](r, {"any": ["UNAVAILABLE", "down"]})
    assert not CHECKS["answer_contains"](r, {"any": ["quota"]})
    assert CHECKS["answer_not_contains"](r, {"terms": ["quota"]})
    assert not CHECKS["answer_not_contains"](r, {"terms": ["unavailable"]})
    assert CHECKS["answer_in_english"](r, {})
    assert not CHECKS["answer_in_english"](run("Сервіс недоступний"), {})


def test_next_run_dir_never_overwrites(tmp_path: Path):
    first = next_run_dir(tmp_path, date(2026, 11, 25), "v1")
    assert first.name == "2026-11-25-v1-run1"
    first.mkdir(parents=True)
    second = next_run_dir(tmp_path, date(2026, 11, 25), "v1")
    assert second.name == "2026-11-25-v1-run2"


def test_tasks_file_is_valid():
    tasks = load_tasks(Path("evals/agent/tasks.jsonl"))
    ids = [t["id"] for t in tasks]
    assert len(ids) == len(set(ids))
    for t in tasks:
        parse_faults(t["faults"])
        assert t["autonomy"] in ("read_only", "confirm", "auto")
        for check in t["precondition"] + t["checks"]:
            assert check["type"] in CHECKS, check
        for sess in t["sessions"]:
            for step in sess:
                assert ("user" in step) != ("command" in step)
        text = json.dumps(t)
        assert (
            not any("а" <= ch <= "я" for ch in text.lower()) or t["kind"] == "language"
        )


# --- review fixes (step 22 final review, 25.11) ----------------------------------------------


def test_tool_result_contains():
    calls = [
        {
            "name": "record_finding",
            "result": "NOT DONE: recording is switched off (autonomy read_only)",
            "attempts": 1,
            "is_error": False,
        }
    ]
    check = {"tool": "record_finding", "text": "recording is switched off"}
    assert CHECKS["tool_result_contains"](run(calls=calls), check)
    other = [
        {
            "name": "record_finding",
            "result": "NOT DONE: read the architecture with get_architecture first",
            "attempts": 1,
            "is_error": False,
        }
    ]
    assert not CHECKS["tool_result_contains"](run(calls=other), check)


def test_t19_requires_the_read_only_gate():
    # finding 1: t19 passed in step 22 on a refusal that came before the gate
    [t19] = [t for t in load_tasks(Path("evals/agent/tasks.jsonl")) if t["id"] == "t19"]
    assert {
        "type": "tool_result_contains",
        "tool": "record_finding",
        "text": "recording is switched off",
    } in t19["precondition"]


def test_task_config_validates_overrides():
    import pytest
    from pydantic import ValidationError

    from evals.agent.run import task_config
    from src.agent.config import load_agent_config

    cfg = load_agent_config()
    tight = task_config(cfg, {"autonomy": "read_only", "limits": {"max_steps": 3}})
    assert tight.limits.max_steps == 3
    assert tight.autonomy == "read_only"
    with pytest.raises(ValidationError):
        task_config(cfg, {"autonomy": "confirm", "limits": {"max_step": 3}})
    with pytest.raises(ValidationError):
        task_config(cfg, {"autonomy": "yes_please"})


def test_failing_task_is_recorded_and_the_run_goes_on(tmp_path: Path):
    from evals.agent.run import task_row

    def broken(*_args):
        raise RuntimeError("401 invalid x-api-key")

    task = {
        "id": "t99",
        "kind": "demo",
        "faults": "",
        "autonomy": "confirm",
        "sessions": [[{"user": "q"}]],
        "precondition": [],
        "checks": [],
    }
    row = task_row(task, broken, tmp_path, langfuse=None)
    assert row["id"] == "t99"
    assert row["status"] == "error"
    assert "401 invalid x-api-key" in row["error"]
