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


def test_answer_regex():
    # review Important 3: t05 must check the eu-central-1 number, not any "500"
    check = {"pattern": r"(?i)eu-central-1[^.;\n]*\b500\b|\b500\b[^.;\n]*eu-central-1"}
    assert CHECKS["answer_regex"](run("In eu-central-1 the quota is 500 DPUs."), check)
    assert not CHECKS["answer_regex"](
        run("eu-central-1 has 1,000 DPUs; other Regions have 500."), check
    )


def test_fault_tasks_bound_the_calls():
    # review Important 4: a model that loops on a failing tool must fail its task
    tasks = {t["id"]: t for t in load_tasks(Path("evals/agent/tasks.jsonl"))}
    for task_id, tool in (
        ("t22a", "search_corpus"),
        ("t22b", "get_service_quota"),
        ("t22c", "get_architecture"),
        ("t23", "get_service_quota"),
    ):
        assert {"type": "tool_count", "tool": tool, "max": 2} in tasks[task_id][
            "checks"
        ], task_id
    t23_terms = next(
        c for c in tasks["t23"]["checks"] if c["type"] == "answer_not_contains"
    )["terms"]
    assert "None" not in t23_terms
    assert any(c["type"] == "answer_regex" for c in tasks["t05"]["checks"])


def test_retrieved_and_cites_docs():
    calls = [
        {
            "name": "search_corpus",
            "result": "...",
            "attempts": 1,
            "is_error": False,
            "data": {
                "labels": {"S1": "wa-framework#0078", "S2": "wa-framework-old#0065"}
            },
        }
    ]
    r = TaskRun(
        task_id="t26",
        answers=["Six pillars [S1]; the 2020 edition said five [S2]."],
        results=[_result("x")],
        traces=[
            {
                "tool_calls": calls,
                "stop": "answer",
                "retrieved_chunk_ids": ["wa-framework#0078", "wa-framework-old#0065"],
            }
        ],
        findings=[],
        confirms_asked=0,
    )
    assert CHECKS["retrieved"](
        r, {"chunks": ["wa-framework#0078", "wa-framework-old#0065"]}
    )
    assert not CHECKS["retrieved"](r, {"chunks": ["agent-overlay-adversarial#0000"]})
    assert CHECKS["cites_docs"](r, {"docs": ["wa-framework", "wa-framework-old"]})
    r.answers = ["Six pillars [S1]."]
    assert not CHECKS["cites_docs"](r, {"docs": ["wa-framework", "wa-framework-old"]})


def test_no_task_carries_the_overlay_flag():
    # spec §10: the injection chunk is loaded in every eval task, so a per-task flag would mislead
    assert all("overlay" not in t for t in load_tasks(Path("evals/agent/tasks.jsonl")))


def test_answer_shorter():
    # t30: the answer after /down is at most 60 % as long as the rated one
    r = run("x" * 100)
    r.answers = ["x" * 100, "y" * 55]
    assert CHECKS["answer_shorter"](r, {"ratio": 0.6, "first": 0, "then": 1})
    r.answers = ["x" * 100, "y" * 70]
    assert not CHECKS["answer_shorter"](r, {"ratio": 0.6, "first": 0, "then": 1})


def test_runner_commands():
    from evals.agent.run import run_command

    class S:
        def __init__(self):
            self.calls = []

        def feedback_up(self):
            self.calls.append("up")
            return "noted"

        def feedback_down(self, comment):
            self.calls.append(("down", comment))
            return "noted"

        def reject(self, bp, reason):
            self.calls.append(("reject", bp, reason))
            return "noted"

        def resolve(self, bp):
            self.calls.append(("resolve", bp))
            return "resolved"

    s = S()
    run_command(s, "/up")
    run_command(s, "/down much shorter please")
    run_command(s, "/reject REL09-BP01 we copy nightly")
    run_command(s, "resolve REL09-BP01")
    assert s.calls == [
        "up",
        ("down", "much shorter please"),
        ("reject", "REL09-BP01", "we copy nightly"),
        ("resolve", "REL09-BP01"),
    ]


def test_finding_checks():
    reopened = _finding().model_copy(update={"reopened_count": 1})
    r = run()
    r.findings = [reopened]
    assert CHECKS["finding_field"](
        r, {"bp": "REL09-BP01", "field": "reopened_count", "equals": 1}
    )
    assert not CHECKS["finding_field"](
        r, {"bp": "REL09-BP01", "field": "reopened_count", "equals": 0}
    )
    assert not CHECKS["no_finding"](r, {"bp": "REL09-BP01"})
    assert CHECKS["no_finding"](r, {"bp": "SEC08-BP02"})


def test_no_finding_line():
    check = {"bp": "REL09-BP01"}
    assert CHECKS["no_finding_line"](
        run("Not included: you rejected REL09-BP01."), check
    )
    assert not CHECKS["no_finding_line"](
        run("Finding 1 [high · Reliability · REL09-BP01] x [S1]"), check
    )
    [t29] = [t for t in load_tasks(Path("evals/agent/tasks.jsonl")) if t["id"] == "t29"]
    assert {"type": "no_finding_line", "bp": "REL09-BP01"} in t29["checks"]


def test_no_finding_line_is_line_based():
    # review I3: the eval check must not share the critic's regex blind spot
    check = {"bp": "REL09-BP01"}
    assert not CHECKS["no_finding_line"](
        run("**Finding 1** [high · Reliability · REL09-BP01] x"), check
    )
    assert not CHECKS["no_finding_line"](
        run("Finding 3: [high · Reliability · rel09-bp01] x"), check
    )
    assert CHECKS["no_finding_line"](
        run("You rejected REL09-BP01, so it is left out."), check
    )


def test_runner_sends_candidates_to_the_run_dir(tmp_path: Path):
    # review I1: eval runs must not write into the repository's feedback_candidates.jsonl
    from evals.agent.run import ScriptedConfirm, _session_factory
    from src.agent.config import load_agent_config
    from src.agent.store import Store
    from src.agent.tracing import Tracer
    from src.rag.config import load_config
    from src.rag.index import Index
    from tests.agent_fixtures import FakeLLM, turn
    from tests.rag_search_fixtures import CHUNKS, fake_embed

    index = Index(CHUNKS, embed_fn=fake_embed, rerank_fn=lambda q, d: [0.0] * len(d))
    make = _session_factory(
        load_agent_config(), FakeLLM(turn("x")), index, load_config(), run_dir=tmp_path
    )
    s = make(
        {"id": "t30", "autonomy": "confirm", "faults": ""},
        Store(":memory:"),
        Tracer(tmp_path / "t.jsonl"),
        ScriptedConfirm(),
    )
    assert s.candidates_path == tmp_path / "feedback_candidates.jsonl"
    assert (
        Path("evals/agent/feedback_candidates.jsonl").read_text(encoding="utf-8") == ""
    )
