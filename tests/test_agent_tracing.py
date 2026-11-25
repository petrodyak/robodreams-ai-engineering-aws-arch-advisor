"""The local JSONL trace and the sink interface (spec §12, ADR-0013; src/agent/tracing.py)."""

import json
from pathlib import Path

import pytest

from src.agent.loop import CallRecord, LoopState, TurnResult
from src.agent.tools import ToolOutcome
from src.agent.tracing import TRACE_KEYS, Tracer
from tests.agent_fixtures import turn

META = {"prompt_version": "v1", "faults": ["503:search_corpus"]}


def _result(answer: str = "The answer [S1].") -> TurnResult:
    state = LoopState(started=0.0, steps=2, tokens=2200, usd=0.002)
    return TurnResult(
        answer=answer, stop="answer", partial=False, state=state, last_text=answer
    )


def _search_record() -> CallRecord:
    return CallRecord(
        step=1,
        name="search_corpus",
        input={"query": "data lake backup"},
        outcome=ToolOutcome(
            text="x" * 2000,
            is_error=False,
            attempts=2,
            faults=["503"],
            data={"labels": {"S1": "wa-reliability#0042", "S2": "wa-reliability#0043"}},
        ),
        ms=12,
    )


def _lines(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def test_trace_line_fields(tmp_path: Path):
    path = tmp_path / "traces" / "chat.jsonl"
    tracer = Tracer(path)
    with tracer.request(7, "Review lakehouse-iceberg", META) as t:
        t.model_call(turn(tool_uses=[("search_corpus", {"query": "data lake backup"})]))
        t.tool_call(_search_record())
        t.model_call(turn("The answer [S1]."))
        t.critic([])
        t.end(_result())
    [line] = _lines(path)
    assert set(line) == set(TRACE_KEYS)
    assert line["session_id"] == 7
    assert line["question"] == "Review lakehouse-iceberg"
    assert line["prompt_version"] == "v1"
    assert line["faults"] == ["503:search_corpus"]
    assert len(line["model_calls"]) == 2
    assert line["model_calls"][0]["stop_reason"] == "tool_use"
    call = line["tool_calls"][0]
    assert len(call["result"]) <= 500
    assert call["attempts"] == 2
    assert call["faults"] == ["503"]
    assert line["retrieved_chunk_ids"] == ["wa-reliability#0042", "wa-reliability#0043"]
    assert line["critic"] == [[]]
    assert line["stop"] == "answer"
    assert line["totals"]["steps"] == 2
    assert line["totals"]["usd"] == pytest.approx(0.002)
    assert "ms" in line["totals"]
    assert line["answer"] == "The answer [S1]."
    assert line["trace_id"] == t.trace_id


def test_trace_without_sink(tmp_path: Path):
    path = tmp_path / "chat.jsonl"
    with Tracer(path, langfuse=None).request(1, "q", META) as t:
        t.end(_result())
    assert len(_lines(path)) == 1


def test_request_that_raises_still_writes_its_line(tmp_path: Path):
    path = tmp_path / "chat.jsonl"
    with pytest.raises(RuntimeError), Tracer(path).request(1, "q", META):
        raise RuntimeError("boom")
    [line] = _lines(path)
    assert line["stop"] == "error"
    assert "boom" in line["answer"]


class BrokenSink:
    def __getattr__(self, name):
        def fail(*_args, **_kwargs):
            raise ConnectionError("langfuse is down")

        return fail


def test_sink_failure_is_logged_not_raised(tmp_path: Path, caplog):
    path = tmp_path / "chat.jsonl"
    tracer = Tracer(path, langfuse=BrokenSink())
    with tracer.request(1, "q", META) as t:
        t.model_call(turn("a"))
        t.end(_result())
    tracer.score(t.trace_id, "user_feedback", 1.0, None)
    assert len(_lines(path)) == 1
    assert "langfuse is down" in caplog.text


# --- Langfuse sink (Task 22.9) -------------------------------------------------------------


class FakeObservation:
    def __init__(self, log: list, name: str, **kwargs):
        self.log = log
        self.name = name
        self.kwargs = kwargs
        self.trace_id = (kwargs.get("trace_context") or {}).get("trace_id")
        log.append(("start", name, kwargs))

    def start_observation(self, *, name: str, **kwargs):
        return FakeObservation(self.log, name, **kwargs)

    def update(self, **kwargs):
        self.log.append(("update", self.name, kwargs))
        return self

    def end(self, **_kwargs):
        self.log.append(("end", self.name, {}))
        return self

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.log.append(("exit", self.name, {}))
        return False


class FakeLangfuse:
    """Records what the sink sends, in the shape of the Langfuse 5.2 client it calls."""

    def __init__(self):
        self.log: list = []
        self.scores: list[dict] = []
        self.flushed = 0

    def start_as_current_observation(self, *, name: str, **kwargs):
        return FakeObservation(self.log, name, **kwargs)

    def create_score(self, **kwargs):
        self.scores.append(kwargs)

    def flush(self):
        self.flushed += 1


def fake_propagate(log: list):
    from contextlib import contextmanager

    @contextmanager
    def propagate(**kwargs):
        log.append(("propagate", "attributes", kwargs))
        yield

    return propagate


def test_langfuse_missing_keys_is_noop(tmp_path: Path, monkeypatch, caplog):
    from src.agent.tracing import make_langfuse

    for key in ("LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_BASE_URL"):
        monkeypatch.delenv(key, raising=False)
    sink = make_langfuse()
    assert sink is None
    assert "LANGFUSE_PUBLIC_KEY" in caplog.text
    path = tmp_path / "chat.jsonl"
    with Tracer(path, langfuse=sink).request(1, "q", META) as t:
        t.end(_result())
    assert len(_lines(path)) == 1


def test_langfuse_failure_never_fails_request(tmp_path: Path):
    from src.agent.tracing import LangfuseSink

    class Down:
        def start_as_current_observation(self, **_kwargs):
            raise ConnectionError("langfuse is down")

        def flush(self):
            raise ConnectionError("langfuse is down")

    path = tmp_path / "chat.jsonl"
    with Tracer(path, langfuse=LangfuseSink(Down())).request(1, "q", META) as t:
        t.model_call(turn("a"))
        t.tool_call(_search_record())
        t.end(_result())
    [line] = _lines(path)
    assert line["answer"] == "The answer [S1]."
    assert line["stop"] == "answer"


def test_langfuse_mapping(tmp_path: Path):
    from src.agent.tracing import LangfuseSink

    client = FakeLangfuse()
    sink = LangfuseSink(client, propagate=fake_propagate(client.log))
    meta = {**META, "model": "claude-haiku-5-5", "run_id": "2026-11-25-v1-run1"}
    with Tracer(tmp_path / "chat.jsonl", langfuse=sink).request(
        7, "Review it", meta
    ) as t:
        t.model_call(turn(tool_uses=[("search_corpus", {"query": "backup"})]))
        t.tool_call(_search_record())
        t.model_call(turn("The answer [S1]."))
        t.end(_result())

    starts = [entry for entry in client.log if entry[0] == "start"]
    root = starts[0]
    assert root[2]["trace_context"] == {"trace_id": t.trace_id}
    assert root[2]["input"] == "Review it"
    [propagated] = [entry[2] for entry in client.log if entry[0] == "propagate"]
    assert propagated["session_id"] == "2026-11-25-v1-run1-s7"
    assert "faults:503:search_corpus" in propagated["tags"]
    assert propagated["metadata"]["prompt_version"] == "v1"
    generations = [s for s in starts if s[2].get("as_type") == "generation"]
    assert len(generations) == 2
    assert generations[0][2]["model"] == "claude-haiku-5-5"
    assert generations[0][2]["usage_details"]["input"] == 1000
    assert "total" in generations[0][2]["cost_details"]
    tools = [s for s in starts if s[2].get("as_type") == "tool"]
    assert [s[1] for s in tools] == ["search_corpus"]
    assert tools[0][2]["metadata"]["attempts"] == 2
    update = [entry for entry in client.log if entry[0] == "update"][-1]
    assert update[2]["output"] == "The answer [S1]."
    assert update[2]["metadata"]["stop"] == "answer"
    assert client.log[-1][0] == "exit"
    assert client.flushed == 1


def test_langfuse_task_score(tmp_path: Path):
    from evals.agent.checks import TaskScore
    from evals.agent.run import send_task_score
    from src.agent.tracing import LangfuseSink

    client = FakeLangfuse()
    tracer = Tracer(
        tmp_path / "t.jsonl",
        langfuse=LangfuseSink(client, propagate=fake_propagate([])),
    )
    send_task_score(
        tracer,
        [{"trace_id": "a" * 32}, {"trace_id": "b" * 32}],
        TaskScore("failed", ["stop"]),
    )
    assert [s["trace_id"] for s in client.scores] == ["a" * 32, "b" * 32]
    assert all(s["name"] == "task_passed" and s["value"] == 0 for s in client.scores)
    assert client.scores[0]["comment"] == "failed: stop"


def test_langfuse_check_without_keys_exits_1(monkeypatch):
    import io

    from src.agent.tracing import langfuse_check

    def never(**_kwargs):
        raise AssertionError("no client may be built without keys")

    out = io.StringIO()
    code = langfuse_check(
        {"LANGFUSE_BASE_URL": "https://cloud.langfuse.com"},
        client_factory=never,
        out=out,
    )
    assert code == 1
    assert "LANGFUSE_PUBLIC_KEY" in out.getvalue()
    assert "LANGFUSE_SECRET_KEY" in out.getvalue()


def test_langfuse_exports_only_its_own_spans():
    # Langfuse 5.2 also exports the Anthropic SDK's own OpenTelemetry span of every call, which
    # doubled each generation and its cost (seen in the first traced request, 25.11).
    from langfuse import is_langfuse_span

    from src.agent.tracing import make_langfuse

    seen: dict = {}

    def factory(**kwargs):
        seen.update(kwargs)
        return FakeLangfuse()

    env = {"LANGFUSE_PUBLIC_KEY": "pk-lf-test", "LANGFUSE_SECRET_KEY": "sk-lf-test"}
    assert make_langfuse(env, client_factory=factory) is not None
    assert seen["should_export_span"] is is_langfuse_span


def test_failed_request_keeps_the_cost_of_its_calls(tmp_path: Path):
    # final review, finding 6: the paid calls of a request that raised must reach the totals
    path = tmp_path / "chat.jsonl"
    with pytest.raises(RuntimeError), Tracer(path).request(1, "q", META) as t:
        t.model_call(turn(tool_uses=[("search_corpus", {"query": "x"})], usd=0.002))
        t.model_call(turn("x", usd=0.003))
        raise RuntimeError("boom")
    [line] = _lines(path)
    assert line["totals"]["steps"] == 2
    assert line["totals"]["usd"] == pytest.approx(0.005)
    assert line["totals"]["tokens"] == 2200


def test_tool_result_keeps_its_end(tmp_path: Path):
    # step 24: a note appended at the end of a long result (rejections) was cut from the trace
    record = _search_record()
    record.outcome = record.outcome.model_copy(
        update={
            "text": "x" * 2000 + " Rejected by the user for this version: REL09-BP01"
        }
    )
    path = tmp_path / "t.jsonl"
    with Tracer(path).request(1, "q", META) as t:
        t.tool_call(record)
        t.end(_result())
    result = _lines(path)[0]["tool_calls"][0]["result"]
    assert len(result) <= 500
    assert result.endswith("REL09-BP01")
