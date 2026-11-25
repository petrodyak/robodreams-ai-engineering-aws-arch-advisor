"""The agent loop: one request, many model calls, every limit in code (spec §6, D18; lesson 11).

- Limits are checked before every model call: steps, tokens (input + output + cache read + cache
  write, summed over the request), dollars and wall time. The time a person spends at a `[y/N]`
  prompt does not count: a tool that writes runs on this thread and its whole duration is subtracted
  (it is a local write plus the person's answer).
- `max_repeats` (the same tool with the same arguments) is checked before each tool call, so the call
  that would break it never runs. `max_calls_per_tool` refuses the extra call and the loop goes on.
- One step before a limit, a wrap-up system message asks for an answer with what is there (§6); its
  response ends the request, and any tool call in it is not run. Without text, the answer is
  `partial_result`, built from the trace only, so it never claims what the model did not do.
- Append-only (§6): the loop only appends to `messages`; the assistant turn is the response's content
  unchanged, thinking blocks included; all tool results of one turn go back in one user message, in
  block order.
- `stop_reason` `refusal` ends the request; `max_tokens` (the per-call cut) ends it as `truncated`
  and its tool calls are not run.
"""

import json
import time
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from src.agent.config import Limits
from src.agent.critic import critic_messages
from src.agent.llm import TIMEOUT_S, PriceTierExceeded, Turn
from src.agent.tools import ToolEntry, ToolOutcome, execute

WRAP_UP = (
    "Last step: answer now with what you have, name the pillars and architectures you did not "
    "cover and why, call no tool."
)
BUDGET_USED = (
    "budget for this tool is used up: answer with what you have or say not found"
)
REFUSED = "The model refused to answer this request (stop reason: refusal)."
WRAP_UP_SHARE = 0.8  # the wrap-up goes out once 80 % of max_tokens or max_usd is spent


@dataclass
class CallRecord:
    step: int
    name: str
    input: dict
    outcome: ToolOutcome
    ms: int


@dataclass
class LoopState:
    started: float
    steps: int = 0
    tokens: int = 0
    usd: float = 0.0
    waited: float = (
        0.0  # seconds spent waiting for the person; not counted by max_seconds
    )
    calls: list[CallRecord] = field(default_factory=list)
    per_tool: Counter = field(default_factory=Counter)
    repeats: Counter = field(default_factory=Counter)
    wrap_up: str | None = (
        None  # the limit that triggered the wrap-up message, once sent
    )


@dataclass
class TurnResult:
    answer: str
    stop: str
    partial: bool
    state: LoopState
    last_text: str


def elapsed(state: LoopState, now: float) -> float:
    return now - state.started - state.waited


def check_limits(state: LoopState, limits: Limits, now: float) -> str | None:
    """The limit that stops the request before the next model call, or None."""
    if state.steps >= limits.max_steps:
        return "max_steps"
    if state.tokens >= limits.max_tokens:
        return "max_tokens"
    if state.usd >= limits.max_usd:
        return "max_usd"
    if elapsed(state, now) >= limits.max_seconds:
        return "max_seconds"
    return None


def needs_wrap_up(state: LoopState, limits: Limits) -> str | None:
    """The limit the next call is the last before, or None (the plan's `-> bool`, with the reason)."""
    if state.steps == limits.max_steps - 1:
        return "max_steps"
    if state.tokens >= WRAP_UP_SHARE * limits.max_tokens:
        return "max_tokens"
    if state.usd >= WRAP_UP_SHARE * limits.max_usd:
        return "max_usd"
    return None


def partial_result(state: LoopState, stop: str) -> str:
    """What was done, from the trace only: it does not read the model's text (§6)."""

    def ok(name: str) -> list[CallRecord]:
        return [c for c in state.calls if c.name == name and not c.outcome.is_error]

    listed = "yes" if ok("list_architectures") else "no"
    read = sorted({str(c.input.get("architecture_id")) for c in ok("get_architecture")})
    queries = [
        f'"{c.input.get("query")}"' for c in state.calls if c.name == "search_corpus"
    ]
    labels = [
        label
        for c in ok("search_corpus")
        for label in (c.outcome.data or {}).get("labels", {})
    ]
    failed = [
        f"{c.name} ({c.outcome.text[:80]})" for c in state.calls if c.outcome.is_error
    ]
    recorded = [
        f"{c.input.get('best_practice')} on {c.input.get('architecture_id')}"
        for c in ok("record_finding")
        if (c.outcome.data or {}).get("status") in ("recorded", "reopened")
    ]
    lines = [
        (
            f"Stopped ({stop}): the request reached a limit before the answer was complete. "
            "What was done, from the trace:"
        ),
        f"- architectures listed: {listed}",
        f"- architectures read: {', '.join(read) or 'none'}",
        f"- searches run: {'; '.join(queries) or 'none'}",
        f"- sources retrieved: {', '.join(dict.fromkeys(labels)) or 'none'}",
        f"- tools that failed: {'; '.join(failed) or 'none'}",
        f"- recorded in the findings registry: {'; '.join(recorded) or 'nothing'}",
        "Nothing beyond this was checked. Ask again with a narrower request to continue.",
    ]
    return "\n".join(lines)


def _repeat_key(name: str, raw_input: dict) -> str:
    return name + json.dumps(raw_input, sort_keys=True, default=str)


def _account(state: LoopState, t: Turn) -> None:
    state.steps += 1
    state.tokens += (
        t.input_tokens + t.output_tokens + t.cache_read_tokens + t.cache_write_tokens
    )
    state.usd += t.cost_usd


def run_turn(
    llm: Any,
    system: list[dict],
    tools: list[dict],
    messages: list[dict],
    registry: dict[str, ToolEntry],
    limits: Limits,
    *,
    critic: Callable[[str, LoopState], list[str]] | None = None,
    critic_retries: int = 1,
    on_event: Callable[[str, dict], None] = lambda *_: None,
    clock: Callable[[], float] = time.monotonic,
) -> TurnResult:
    """Run one request; `messages` ends with the user's question and is only appended to."""
    state = LoopState(started=clock())
    retries_left = critic_retries if critic is not None else 0
    last_text = ""

    def finish(answer: str, stop: str, partial: bool) -> TurnResult:
        on_event("stop", {"stop": stop, "partial": partial, "steps": state.steps})
        return TurnResult(
            answer=answer, stop=stop, partial=partial, state=state, last_text=last_text
        )

    while True:
        limit = check_limits(state, limits, clock())
        if limit is not None:
            return finish(partial_result(state, limit), limit, True)
        if state.wrap_up is None:
            reason = needs_wrap_up(state, limits)
            if reason is not None:
                state.wrap_up = reason
                messages.append({"role": "system", "content": WRAP_UP})
                on_event("wrap_up", {"reason": reason, "step": state.steps + 1})

        time_left = limits.max_seconds - elapsed(state, clock())
        try:
            t = llm.call(
                system, tools, messages, timeout_s=max(1.0, min(TIMEOUT_S, time_left))
            )
        except PriceTierExceeded as over:
            _account(state, over.turn)
            on_event("model_call", {"step": state.steps, "turn": over.turn})
            return finish(partial_result(state, "error"), "error", True)
        _account(state, t)
        last_text = t.text
        on_event("model_call", {"step": state.steps, "turn": t})
        messages.append({"role": "assistant", "content": t.content})

        if t.stop_reason == "refusal":
            return finish(REFUSED, "refusal", False)
        if t.stop_reason == "max_tokens":
            return finish(
                t.text or partial_result(state, "truncated"), "truncated", True
            )
        if state.wrap_up is not None:
            return finish(
                t.text or partial_result(state, state.wrap_up), state.wrap_up, True
            )
        if not t.tool_uses:
            if (
                critic is not None
            ):  # code checks of the final answer (spec §10, Task 24.1)
                problems = critic(t.text, state)
                on_event("critic", {"problems": problems})
                # no retry when the next call would be the wrap-up or over a limit: the full
                # answer is kept and the problems stay in the trace (review I4)
                next_ok = (
                    check_limits(state, limits, clock()) is None
                    and needs_wrap_up(state, limits) is None
                )
                if problems and retries_left > 0 and next_ok:
                    retries_left -= 1
                    messages.extend(critic_messages(problems))
                    continue
            return finish(t.text, "answer", False)

        results = []
        for use in t.tool_uses:
            key = _repeat_key(use.name, use.input)
            if state.repeats[key] >= limits.max_repeats:
                on_event("repeat", {"name": use.name, "input": use.input})
                return finish(partial_result(state, "max_repeats"), "max_repeats", True)
            cap = limits.max_calls_per_tool.get(use.name)
            if cap is not None and state.per_tool[use.name] >= cap:
                outcome, ms = ToolOutcome(text=BUDGET_USED, is_error=True), 0
            else:
                state.repeats[key] += 1
                state.per_tool[use.name] += 1
                started = clock()
                outcome = execute(
                    use.name, use.input, registry, timeout=limits.tool_timeout_s
                )
                spent = clock() - started
                ms = round(spent * 1000)
                entry = registry.get(use.name)
                if entry is not None and not entry.read_only:
                    # a write tool's time is the person's [y/N] answer
                    state.waited += spent
            record = CallRecord(
                step=state.steps, name=use.name, input=use.input, outcome=outcome, ms=ms
            )
            state.calls.append(record)
            on_event("tool_call", {"record": record})
            results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": use.id,
                    "content": outcome.text,
                    "is_error": outcome.is_error,
                }
            )
        messages.append({"role": "user", "content": results})
