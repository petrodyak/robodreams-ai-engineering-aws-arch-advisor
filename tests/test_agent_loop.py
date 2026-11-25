"""The agent loop: tool calls, limits, wrap-up and the partial result (spec §6; src/agent/loop.py)."""

from pydantic import BaseModel, ConfigDict

from src.agent.config import Limits
from src.agent.loop import (
    WRAP_UP,
    CallRecord,
    LoopState,
    check_limits,
    needs_wrap_up,
    partial_result,
    run_turn,
)
from src.agent.tools import ToolEntry, ToolOutcome
from tests.agent_fixtures import FakeLLM, turn

LIMITS = Limits(
    max_steps=12,
    max_tokens=200_000,
    max_usd=0.05,
    max_seconds=240,
    tool_timeout_s=10,
    max_repeats=2,
    max_calls_per_tool={
        "search_corpus": 8,
        "get_architecture": 3,
        "get_service_quota": 4,
    },
)
SYSTEM = [{"type": "text", "text": "rules"}]
TOOLS = [{"name": "search_corpus"}]


class Query(BaseModel):
    model_config = ConfigDict(extra="forbid")
    query: str


class Clock:
    def __init__(self):
        self.now = 1000.0

    def __call__(self) -> float:
        return self.now


def registry(calls: list[str] | None = None, *, clock: Clock | None = None):
    seen = calls if calls is not None else []

    def search(args: Query) -> ToolOutcome:
        seen.append(args.query)
        return ToolOutcome(text=f"<document>{args.query}</document>", is_error=False)

    def failing(_args: Query) -> ToolOutcome:
        return ToolOutcome(text="ERROR: broken", is_error=True)

    def slow_confirm(args: Query) -> str:
        if clock is not None:
            clock.now += 300  # the person thinks for 5 minutes at the [y/N] prompt
        return "recorded"

    return {
        "search_corpus": ToolEntry(fn=search, args_model=Query, read_only=True),
        "broken": ToolEntry(fn=failing, args_model=Query, read_only=True),
        "record_finding": ToolEntry(fn=slow_confirm, args_model=Query, read_only=False),
        "get_architecture": ToolEntry(fn=search, args_model=Query, read_only=True),
    }


def go(llm, *, reg=None, limits=LIMITS, clock=None, messages=None):
    msgs = (
        messages if messages is not None else [{"role": "user", "content": "question"}]
    )
    kwargs = {"clock": clock} if clock is not None else {}
    result = run_turn(
        llm, SYSTEM, TOOLS, msgs, reg or registry(clock=clock), limits, **kwargs
    )
    return result, msgs


def test_answer_without_tools():
    result, _ = go(FakeLLM(turn("No tool needed.")))
    assert result.stop == "answer"
    assert result.answer == "No tool needed."
    assert result.partial is False
    assert result.state.steps == 1


def test_parallel_tool_results_in_one_message():
    first = turn(
        tool_uses=[("search_corpus", {"query": "a"}), ("broken", {"query": "b"})]
    )
    llm = FakeLLM(first, turn("done"))
    result, msgs = go(llm)
    assert msgs[1] == {"role": "assistant", "content": first.content}
    assert msgs[1]["content"] is first.content
    results = msgs[2]
    assert results["role"] == "user"
    assert [b["tool_use_id"] for b in results["content"]] == ["toolu_1", "toolu_2"]
    assert [b["type"] for b in results["content"]] == ["tool_result", "tool_result"]
    assert result.stop == "answer"
    assert len(msgs) == 4  # question, tool turn, results, final answer


def test_error_result_flagged():
    llm = FakeLLM(turn(tool_uses=[("broken", {"query": "b"})]), turn("done"))
    _, msgs = go(llm)
    block = msgs[2]["content"][0]
    assert block["is_error"] is True
    assert block["content"] == "ERROR: broken"


def test_six_parallel_calls_run_in_block_order():
    calls: list[str] = []
    pillars = ["ops", "sec", "rel", "perf", "cost", "sus"]
    llm = FakeLLM(
        turn(tool_uses=[("search_corpus", {"query": p}) for p in pillars]),
        turn("review"),
    )
    result, msgs = go(llm, reg=registry(calls))
    assert calls == pillars
    assert result.state.steps == 2
    assert len(msgs[2]["content"]) == 6


def test_wrap_up_before_last_step():
    endless = turn(tool_uses=[("search_corpus", {"query": "x"})])
    script = [
        turn(tool_uses=[("search_corpus", {"query": f"q{i}"})]) for i in range(11)
    ]
    llm = FakeLLM(
        *script,
        turn(
            "Partial review: Reliability only.",
            [("search_corpus", {"query": "z"})],
            stop="tool_use",
        ),
        endless,
    )
    calls: list[str] = []
    result, _ = go(llm, reg=registry(calls))
    wrap_requests = [
        i
        for i, r in enumerate(llm.requests)
        if any(m.get("content") == WRAP_UP for m in r["messages"])
    ]
    assert wrap_requests[0] == 11  # the 12th call carries it
    sent = [m for m in llm.requests[11]["messages"] if m.get("role") == "system"]
    assert len(sent) == 1
    assert result.answer == "Partial review: Reliability only."
    assert result.stop == "max_steps"
    assert result.partial is True
    assert "z" not in calls  # the wrap-up response's tool call is not run
    assert len(llm.requests) == 12


def test_wrap_up_message_position():
    script = [
        turn(tool_uses=[("search_corpus", {"query": f"q{i}"})]) for i in range(11)
    ]
    llm = FakeLLM(*script, turn("final"))
    go(llm)
    messages = llm.requests[11]["messages"]
    assert messages[-1] == {"role": "system", "content": WRAP_UP}
    assert messages[-2]["role"] == "user"
    assert messages[-2]["content"][0]["type"] == "tool_result"


def test_max_steps_hard_partial():
    script = [
        turn(tool_uses=[("search_corpus", {"query": f"q{i}"})]) for i in range(12)
    ]
    llm = FakeLLM(*script)
    result, _ = go(llm)
    assert len(llm.requests) == 12
    assert result.stop == "max_steps"
    assert result.partial is True
    assert result.answer.startswith("Stopped (max_steps)")
    assert '"q0"' in result.answer


def test_partial_result_from_trace_only():
    state = LoopState(started=0.0)
    state.calls = [
        CallRecord(
            step=1,
            name="get_architecture",
            input={"architecture_id": "lakehouse-iceberg"},
            outcome=ToolOutcome(text="{...}", is_error=False),
            ms=3,
        ),
        CallRecord(
            step=1,
            name="search_corpus",
            input={"query": "data lake backup"},
            outcome=ToolOutcome(
                text="...", is_error=False, data={"labels": {"S1": "a#1"}}
            ),
            ms=3,
        ),
        CallRecord(
            step=2,
            name="get_service_quota",
            input={"service": "AWS Glue"},
            outcome=ToolOutcome(text="ERROR: service unavailable (503)", is_error=True),
            ms=3,
        ),
    ]
    text = partial_result(state, "max_usd")
    assert text.startswith("Stopped (max_usd)")
    assert "lakehouse-iceberg" in text
    assert '"data lake backup"' in text
    assert "S1" in text
    assert "get_service_quota" in text
    assert "Finding" not in text


def test_max_usd_stops_before_call():
    llm = FakeLLM(
        turn(tool_uses=[("search_corpus", {"query": "q"})], usd=0.03),
        turn(tool_uses=[("search_corpus", {"query": "r"})], usd=0.03),
        turn("never"),
    )
    result, _ = go(llm)
    assert len(llm.requests) == 2
    assert result.stop == "max_usd"
    assert result.partial is True


def test_max_repeats():
    same = ("search_corpus", {"query": "same"})
    llm = FakeLLM(
        turn(tool_uses=[same]),
        turn(tool_uses=[same]),
        turn(tool_uses=[same]),
        turn("never"),
    )
    calls: list[str] = []
    result, _ = go(llm, reg=registry(calls))
    assert calls == ["same", "same"]
    assert result.stop == "max_repeats"
    assert result.partial is True


def test_truncated_response():
    calls: list[str] = []
    llm = FakeLLM(turn("half", [("search_corpus", {"query": "x"})], stop="max_tokens"))
    result, _ = go(llm, reg=registry(calls))
    assert result.stop == "truncated"
    assert calls == []


def test_confirm_wait_not_counted():
    clock = Clock()
    llm = FakeLLM(
        turn(tool_uses=[("record_finding", {"query": "x"})]), turn("recorded it")
    )
    result, _ = go(llm, clock=clock)
    assert clock.now - 1000.0 >= 300
    assert result.stop == "answer"


def test_max_seconds_counts_model_time():
    clock = Clock()

    class SlowLLM(FakeLLM):
        def call(self, *a, **k):
            clock.now += 150
            return super().call(*a, **k)

    llm = SlowLLM(
        turn(tool_uses=[("search_corpus", {"query": "a"})]),
        turn(tool_uses=[("search_corpus", {"query": "b"})]),
        turn("never"),
    )
    result, _ = go(llm, clock=clock)
    assert result.stop == "max_seconds"
    assert len(llm.requests) == 2
    assert llm.requests[1]["timeout_s"] <= 90


def test_max_calls_per_tool():
    script = [turn(tool_uses=[("search_corpus", {"query": f"q{i}"})]) for i in range(9)]
    llm = FakeLLM(*script, turn("answer with what I have"))
    calls: list[str] = []
    limits = LIMITS.model_copy(update={"max_steps": 20, "max_usd": 1.0})
    result, msgs = go(llm, reg=registry(calls), limits=limits)
    assert len(calls) == 8
    ninth = msgs[18]["content"][0]
    assert (
        ninth["content"]
        == "budget for this tool is used up: answer with what you have or say not found"
    )
    assert result.stop == "answer"


def test_refusal_stop():
    result, _ = go(FakeLLM(turn(stop="refusal")))
    assert result.stop == "refusal"
    assert "refused" in result.answer


def test_check_limits_and_wrap_up_thresholds():
    state = LoopState(started=0.0)
    assert check_limits(state, LIMITS, now=1.0) is None
    state.steps = 11
    assert needs_wrap_up(state, LIMITS) == "max_steps"
    state.steps = 12
    assert check_limits(state, LIMITS, now=1.0) == "max_steps"
    state = LoopState(started=0.0, usd=0.041)
    assert needs_wrap_up(state, LIMITS) == "max_usd"
    state = LoopState(started=0.0, tokens=200_000)
    assert check_limits(state, LIMITS, now=1.0) == "max_tokens"


def test_price_tier_exceeded_is_counted_and_stops():
    # final review, finding 6: a call above Haiku's 100K tier was paid; count it, stop with `error`
    from src.agent.llm import PriceTierExceeded

    paid = turn("x", usd=0.07, input_tokens=120_000)

    class OverLLM(FakeLLM):
        def call(self, *a, **k):
            super().call(*a, **k)
            raise PriceTierExceeded(paid)

    result, _ = go(OverLLM(turn("never")))
    assert result.stop == "error"
    assert result.partial is True
    assert result.state.steps == 1
    assert result.state.usd == 0.07


def test_loop_critic_retry_once():
    seen: list[list[str]] = []

    def critic(answer: str, _state) -> list[str]:
        return ["label [S9] is not a label of this session"] if "[S9]" in answer else []

    def on_event(kind: str, data: dict) -> None:
        if kind == "critic":
            seen.append(data["problems"])

    llm = FakeLLM(turn("Back up [S9]."), turn("Still [S9]."), turn("never"))
    msgs = [{"role": "user", "content": "question"}]
    result = run_turn(
        llm,
        SYSTEM,
        TOOLS,
        msgs,
        registry(),
        LIMITS,
        critic=critic,
        critic_retries=1,
        on_event=on_event,
    )
    assert len(llm.requests) == 2
    retry = llm.requests[1]["messages"]
    assert [m["role"] for m in retry[-3:]] == ["assistant", "user", "system"]
    assert (
        result.answer == "Still [S9]."
    )  # the second answer is shown even if it fails again
    assert result.stop == "answer"
    assert len(seen) == 2


def test_loop_clean_answer_no_retry():
    llm = FakeLLM(turn("Fine [S1]."))
    result = run_turn(
        llm,
        SYSTEM,
        TOOLS,
        [{"role": "user", "content": "q"}],
        registry(),
        LIMITS,
        critic=lambda *_: [],
        critic_retries=1,
    )
    assert len(llm.requests) == 1
    assert result.answer == "Fine [S1]."


def test_no_critic_retry_when_the_next_call_is_wrap_up():
    # review I4: a retry queued right before the wrap-up or a limit would throw away a full answer
    script = [
        turn(tool_uses=[("search_corpus", {"query": f"q{i}"})]) for i in range(10)
    ]
    llm = FakeLLM(*script, turn("Answer with [S9]."), turn("never"))
    result = run_turn(
        llm,
        SYSTEM,
        TOOLS,
        [{"role": "user", "content": "q"}],
        registry(),
        LIMITS,
        critic=lambda answer, _s: ["bad label"] if "[S9]" in answer else [],
        critic_retries=1,
    )
    assert len(llm.requests) == 11
    assert result.answer == "Answer with [S9]."
    assert result.stop == "answer"
