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
    # t23: no "None" term (case-insensitive, it failed "none of"); the gold number is checked instead
    t23_types = [c["type"] for c in tasks["t23"]["checks"]]
    assert "gold_absent" in t23_types
    assert any(c["type"] == "gold_quota" for c in tasks["t05"]["checks"])


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


# --- Task 25.1: the full set of check types ----------------------------------------------------


def _run_with(
    answer: str, *, calls=None, critic=None, stop="answer", facts=None, commands=None
):
    r = run(answer, stop=stop, calls=calls if calls is not None else [])
    r.traces = [{"tool_calls": calls or [], "stop": stop, "critic": critic or [[]]}]
    r.facts = facts or {}
    r.command_outputs = commands or []
    return r


def test_gold_value_reads_the_region_row():
    from evals.agent.checks import gold_value

    assert (
        gold_value("Amazon Kinesis Data Streams", "Shards per Region", "eu-central-1")
        == "6,000"
    )
    assert gold_value("AWS Glue", "Max task DPUs per account", "eu-central-1") == "500"
    assert gold_value("AWS Glue", "Max task DPUs per account", "us-east-1") == "1,000"
    assert gold_value("Amazon Aurora", "DB clusters", "eu-central-1") == "40"


def test_gold_quota_check():
    check = {
        "service": "Amazon Kinesis Data Streams",
        "quota": "Shards per Region",
        "region": "eu-central-1",
    }
    assert CHECKS["gold_quota"](
        _run_with("In eu-central-1 the default is 6,000 shards."), check
    )
    assert CHECKS["gold_quota"](
        _run_with("eu-central-1: 6000 shards per Region."), check
    )
    assert not CHECKS["gold_quota"](
        _run_with("In eu-central-1 the default is 20,000 shards; others 6,000."), check
    )


def test_pillars_cited():
    six = "\n".join(
        [
            f"Finding {i} [high · {p} · REL09-BP01] x [S{i}]"
            for i, p in enumerate(
                [
                    "Operational Excellence",
                    "Security",
                    "Reliability",
                    "Performance Efficiency",
                    "Cost Optimization",
                ],
                1,
            )
        ]
        + [
            "Sustainability: no gap found in what was retrieved [S6]",
            "Pillars covered: 6 of 6",
        ]
    )
    assert CHECKS["pillars_cited"](_run_with(six), {})
    assert not CHECKS["pillars_cited"](
        _run_with(
            six.replace("Sustainability: no gap found in what was retrieved [S6]", "")
        ),
        {},
    )


def test_budget_stop():
    assert CHECKS["budget_stop"](_run_with("partial", stop="max_steps"), {})
    used = [
        {
            "name": "search_corpus",
            "result": "budget for this tool is used up: answer with what you have",
            "is_error": True,
        }
    ]
    assert CHECKS["budget_stop"](_run_with("partial", calls=used), {})
    assert not CHECKS["budget_stop"](_run_with("done"), {})


def test_asks_user():
    assert CHECKS["asks_user"](
        _run_with("You have two architectures.\n\nWhich one should I review?"), {}
    )
    assert not CHECKS["asks_user"](_run_with("Here is the review."), {})
    wrote = [
        {
            "name": "record_finding",
            "result": "recorded REL09-BP01",
            "is_error": False,
            "data": {"status": "recorded"},
        }
    ]
    assert not CHECKS["asks_user"](
        _run_with("Recorded. Anything else?", calls=wrote), {}
    )


def test_critic_clean_and_unverified_empty():
    assert CHECKS["critic_clean"](_run_with("x", critic=[["bad label"], []]), {})
    assert not CHECKS["critic_clean"](_run_with("x", critic=[["bad label"]]), {})
    numbers = [["these numbers come from no tool result and no user message: 750"]]
    assert not CHECKS["unverified_empty"](_run_with("x", critic=numbers), {})
    assert CHECKS["unverified_empty"](_run_with("x", critic=[["bad label"]]), {})


def test_arg_contains_and_distinct_args():
    calls = [
        {
            "name": "search_corpus",
            "input": {"query": "Redshift distribution key"},
            "result": "",
            "is_error": False,
        },
        {
            "name": "search_corpus",
            "input": {"query": "Redshift Spectrum partition pruning"},
            "result": "",
            "is_error": False,
        },
    ]
    r = _run_with("x", calls=calls)
    assert CHECKS["arg_contains"](
        r, {"tool": "search_corpus", "arg": "query", "any": ["spectrum"]}
    )
    assert not CHECKS["arg_contains"](
        r, {"tool": "search_corpus", "arg": "query", "any": ["snowflake"]}
    )
    assert CHECKS["distinct_args"](r, {"tool": "search_corpus", "min": 2})
    assert not CHECKS["distinct_args"](
        _run_with("x", calls=calls[:1] * 2), {"tool": "search_corpus", "min": 2}
    )


def test_no_fact_and_commands_ok():
    # step 24 review M6 and M5
    assert CHECKS["no_fact"](
        _run_with("x", facts={"region": "eu-central-1"}),
        {"key": "region", "value": "us-east-1"},
    )
    assert not CHECKS["no_fact"](
        _run_with("x", facts={"region": "us-east-1"}),
        {"key": "region", "value": "us-east-1"},
    )
    assert CHECKS["commands_ok"](
        _run_with("x", commands=["noted: REL09-BP01 will not be raised again"]), {}
    )
    assert not CHECKS["commands_ok"](
        _run_with("x", commands=["review an architecture first"]), {}
    )


def test_every_fault_kind_present():
    from src.agent.faults import KINDS

    kinds = {
        f.kind
        for t in load_tasks(Path("evals/agent/tasks.jsonl"))
        for f in parse_faults(t["faults"])
    }
    assert kinds == set(KINDS)


def test_task_set_covers_spec_13():
    ids = {t["id"] for t in load_tasks(Path("evals/agent/tasks.jsonl"))}
    expected = {f"t{i:02d}" for i in range(1, 32)} - {"t22"} | {
        "t18b",
        "t22a",
        "t22b",
        "t22c",
    }
    assert expected <= ids


def test_gold_numbers_are_not_typed_into_tasks():
    text = Path("evals/agent/tasks.jsonl").read_text(encoding="utf-8")
    assert (
        "500" not in text
    )  # t05 / t27 read the Glue quota from data/gold/ (gold_quota)


def test_tasks_md_is_current():
    from evals.agent.tasks_md import render

    assert Path("evals/agent/TASKS.md").read_text(encoding="utf-8") == render(
        load_tasks(Path("evals/agent/tasks.jsonl"))
    )


def test_gold_absent():
    check = {
        "service": "AWS Glue",
        "quota": "Max task DPUs per account",
        "region": "eu-central-1",
    }
    assert CHECKS["gold_absent"](
        _run_with("The quota service is unavailable, so I give no number."), check
    )
    assert not CHECKS["gold_absent"](_run_with("It is probably 500 DPUs."), check)


# --- Task 25.2: metrics, stability, lint, ablations ---------------------------------------------


def _row(
    tid: str,
    status: str,
    *,
    writes=0,
    confirms=0,
    failed=None,
    usd=0.001,
    steps=2,
    stops=("answer",),
    tools=(),
    required=("search_corpus",),
):
    return {
        "required": list(required),
        "id": tid,
        "kind": "k",
        "status": status,
        "failed": failed or [],
        "writes": writes,
        "confirms": confirms,
        "usd": usd,
        "steps": steps,
        "seconds": 1.0,
        "stops": list(stops),
        "tools": list(tools),
    }


def test_aggregate_counts_unconfirmed():
    from evals.agent.run import aggregate

    runs = [
        [
            _row("t16", "passed", writes=1, confirms=1),
            _row("tX", "failed", writes=1, confirms=0, failed=["x"]),
        ]
    ]
    m = aggregate(runs)
    assert m["unconfirmed_actions"] == 1
    assert m["pass_rate"] == {"mean": 0.5, "min": 0.5, "max": 0.5}


def test_aggregate_rates_and_invalid():
    from evals.agent.run import aggregate

    run1 = [
        _row("a", "passed", tools=["get_architecture"]),
        _row("b", "failed", failed=["tools_called"]),
        _row("c", "invalid"),
    ]
    run2 = [_row("a", "passed"), _row("b", "passed"), _row("c", "invalid")]
    m = aggregate([run1, run2])
    assert m["pass_rate"] == {
        "mean": 0.75,
        "min": 0.5,
        "max": 1.0,
    }  # invalid tasks are not in the denominator
    assert m["invalid"] == 2
    assert m["tools_ok"] == 0.75
    assert m["stops"] == {"answer": 6}


def test_stability():
    from evals.agent.run import stability

    runs = [
        [_row("a", "passed"), _row("b", "failed")],
        [_row("a", "passed"), _row("b", "passed")],
    ]
    assert stability(runs) == {"a": 1.0, "b": 0.5}


def test_lint_flags_short_description():
    from evals.agent.lint import lint

    problems = lint([], {"search_corpus": {"description": "Search.", "params": {}}})
    assert any("search_corpus" in p and "description" in p for p in problems)


def test_lint_flags_unknown_tool_and_check():
    from evals.agent.lint import lint

    task = {
        "id": "tz",
        "kind": "k",
        "faults": "explode",
        "autonomy": "confirm",
        "sessions": [[{"user": "q"}]],
        "precondition": [],
        "checks": [{"type": "tools_called", "tools": ["drop_table"]}, {"type": "nope"}],
    }
    problems = lint([task], {})
    assert any("drop_table" in p for p in problems)
    assert any("nope" in p for p in problems)
    assert any("explode" in p for p in problems)


def test_lint_repo_clean():
    from evals.agent.lint import lint
    from src.agent.tools import load_descriptions

    assert (
        lint(load_tasks(Path("evals/agent/tasks.jsonl")), load_descriptions("v1")) == []
    )


def test_estimate_weights_reviews():
    # step 22 review minor 9: the estimate under-counted a six-pillar review about 2.5 times
    from evals.agent.run import estimate
    from src.agent.config import load_agent_config

    class Counter:
        def count_tokens(self, *_a):
            return 3000

    cfg = load_agent_config()
    question = {"id": "q", "sessions": [[{"user": "What does REL09-BP01 ask for?"}]]}
    review = {"id": "r", "sessions": [[{"user": "Review lakehouse-iceberg."}]]}
    one = estimate([question], cfg, Counter(), list)
    two = estimate([review], cfg, Counter(), list)
    assert 2.0 <= two / one <= 3.0


# --- step 25 review fixes ---------------------------------------------------------------------


def test_critic_checks_need_a_critic_verdict():
    # review I1: a truncated or wrap-up answer was never checked, so it must not count as clean
    r = _run_with("x", critic=[])
    r.traces = [{"tool_calls": [], "stop": "truncated", "critic": []}]
    assert not CHECKS["critic_clean"](r, {})
    assert not CHECKS["unverified_empty"](r, {})


def test_no_numbers():
    # review I2: "no invented number" means no number at all after a failed quota tool
    assert CHECKS["no_numbers"](
        _run_with("The quota service is unavailable; I give no number."), {}
    )
    assert not CHECKS["no_numbers"](_run_with("It is probably 1,000 DPUs."), {})
    assert CHECKS["no_numbers"](
        _run_with("Retry in eu-central-1 later; REL09-BP01 [S1] still applies."), {}
    )


def test_budget_stop_is_a_budget():
    # review I3: max_repeats and max_seconds are not the budget of t24
    assert not CHECKS["budget_stop"](_run_with("x", stop="max_repeats"), {})
    assert CHECKS["budget_stop"](_run_with("x", stop="max_usd"), {})


def test_tools_ok_uses_the_required_tools():
    # review I4: a task that should call an MCP tool and did not must count against tools_ok_mcp
    from evals.agent.run import aggregate

    t05 = _row("t05", "failed", failed=["tools_called"], tools=[])
    t05["required"] = ["get_service_quota"]
    t10 = _row("t10", "passed")
    t10["required"] = []
    m = aggregate([[t05, t10]])
    assert m["tools_ok_mcp"] == 0.0
    assert m["tools_ok"] == 0.0  # only tasks with required tools are in the denominator


def test_unconfirmed_counts_yes_answers():
    # review I5: a write after a "no" is an action without permission
    from evals.agent.run import aggregate

    row = _row("t17", "failed", writes=1, confirms=1)
    row["confirmed_yes"] = 0
    assert aggregate([[row]])["unconfirmed_actions"] == 1


def test_broken_check_gives_an_error_row(tmp_path: Path):
    # review I6: a check that raises must not crash the run after the paid calls
    from evals.agent.run import task_row

    task = {
        "id": "tq",
        "kind": "k",
        "faults": "",
        "autonomy": "confirm",
        "sessions": [],
        "precondition": [],
        "checks": [
            {
                "type": "gold_quota",
                "service": "AWS Glue",
                "quota": "No such quota",
                "region": "eu-central-1",
            }
        ],
    }

    class S:
        def new(self): ...
        def close(self): ...

    row = task_row(task, lambda *_a: S(), tmp_path)
    assert row["status"] == "error"
    assert "No such quota" in row["error"] or "StopIteration" in row["error"]


def test_lint_runs_every_check():
    # review I6: lint calls each check once, so a bad argument fails make check, not a paid run
    from evals.agent.lint import lint

    task = {
        "id": "tq",
        "kind": "k",
        "faults": "",
        "autonomy": "confirm",
        "sessions": [[{"user": "q"}]],
        "precondition": [],
        "checks": [
            {
                "type": "gold_quota",
                "service": "AWS Glue",
                "quota": "No such quota",
                "region": "eu-central-1",
            },
            {"type": "tools_called"},
        ],
    }
    problems = lint([task], {})
    assert any("gold_quota" in p for p in problems)
    assert any("tools_called" in p for p in problems)


def test_gold_quota_rejects_other_values_in_the_sentence():
    # review M1
    check = {
        "service": "AWS Glue",
        "quota": "Max task DPUs per account",
        "region": "eu-central-1",
    }
    assert not CHECKS["gold_quota"](
        _run_with("In eu-central-1 the default is 1,000 (500 in the other Regions)."),
        check,
    )


def test_stability_needs_the_same_tasks():
    # review M4
    import pytest

    from evals.agent.run import stability

    with pytest.raises(ValueError):
        stability([[_row("a", "passed")], [_row("b", "passed")]])


def test_no_gold_numbers_typed():
    # review M9: t06's 6,000 too
    text = Path("evals/agent/tasks.jsonl").read_text(encoding="utf-8")
    assert "6,000" not in text and "6000" not in text


def test_t29_and_t24_and_fault_tasks_are_strict():
    tasks = {t["id"]: t for t in load_tasks(Path("evals/agent/tasks.jsonl"))}
    assert {
        "type": "tool_result_contains",
        "tool": "record_finding",
        "text": "rejected by the user",
    } in tasks["t29"]["precondition"]
    t24_terms = next(
        c for c in tasks["t24"]["checks"] if c["type"] == "answer_contains"
    )["any"]
    assert "limit" not in t24_terms
    for tid in ("t07", "t22b", "t23"):
        assert {"type": "no_numbers"} in tasks[tid]["checks"], tid
    assert {"type": "answer_not_contains", "terms": ["None"], "case": True} in tasks[
        "t23"
    ]["checks"]
