"""The Claude client of the agent: one Messages API call with tools (spec §6, D18, D19).

- D19: no `temperature` / `top_p` / `top_k`, no assistant prefill, no `thinking` parameter (Haiku 5.5
  thinks adaptively by default); `effort` is sent explicitly inside `output_config`.
- The whole `response.content` is kept in `Turn.content`, thinking blocks included, so the loop can
  append it to the history unchanged; Haiku 5.5 rejects an edited replay of its thinking (spec §6).
- A response cut at the per-call `max_tokens` is never parsed for tool calls: a half-built call would
  run with arguments the model never finished (spec §6, stop reason `truncated`).
- Prompt caching: tools render before system, so one breakpoint on the last tool and one on the last
  system block cover the stable prefix. Whether it caches (Haiku 5.5's minimum is 512 tokens) is read
  from `cache_read_tokens` / `cache_write_tokens`, not assumed.
- The transport retry is the one of HW 1 and HW 2 (`call_with_retry`), imported, not copied.
"""

import time
from collections.abc import Callable
from typing import Any

import anthropic
from pydantic import BaseModel, ConfigDict

from src.extract.llm.base import call_with_retry
from src.extract.llm.claude import is_transient, retry_after
from src.rag.llm import HAIKU_PRICE_LIMIT, PRICES

TIMEOUT_S = 120  # per attempt; the loop passes a shorter one when max_seconds is closer
# Prompt caching docs (claude-api skill, shared/prompt-caching.md, checked 25.11): a cache read costs
# 0.1x the base input price, a write with the default 5-minute TTL 1.25x.
CACHE_READ_FACTOR = 0.1
CACHE_WRITE_FACTOR = 1.25
EPHEMERAL = {"type": "ephemeral"}
HIGH_TIER_FACTOR = (
    5  # Haiku 5.5 above 100K prompt tokens: $0.50 / $2.50 against $0.10 / $0.50
)


class ToolUse(BaseModel):
    id: str
    name: str
    input: dict


class Turn(BaseModel):
    """One model call: its blocks for the history, what it asked for, and what it cost."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    content: list[Any]
    text: str
    tool_uses: list[ToolUse]
    stop_reason: str
    input_tokens: int
    output_tokens: int
    cache_read_tokens: int
    cache_write_tokens: int
    cost_usd: float
    latency_ms: int
    attempts: int


class PriceTierExceeded(ValueError):
    """A call above Haiku 5.5's 100K price tier; `.turn` holds the paid call at the higher price."""

    def __init__(self, turn: Turn):
        super().__init__("prompt above 100K tokens: Haiku 5.5's higher price tier")
        self.turn = turn


def turn_cost(
    model: str, input_tokens: int, output_tokens: int, cache_read: int, cache_write: int
) -> float:
    price_in, price_out = PRICES[model]
    return (
        input_tokens * price_in
        + output_tokens * price_out
        + cache_read * price_in * CACHE_READ_FACTOR
        + cache_write * price_in * CACHE_WRITE_FACTOR
    ) / 1_000_000


def _with_breakpoint(blocks: list[dict]) -> list[dict]:
    """A copy of `blocks` whose last block carries `cache_control`; the input is not edited."""
    if not blocks:
        return []
    return [*blocks[:-1], {**blocks[-1], "cache_control": EPHEMERAL}]


class ToolUseLLM:
    def __init__(
        self,
        model: str,
        effort: str,
        max_tokens: int,
        *,
        client: Any = None,
        sleep: Callable[[float], None] = time.sleep,
        clock: Callable[[], float] = time.perf_counter,
    ):
        if model not in PRICES:
            raise ValueError(f"no price for {model}: add it to PRICES")
        self.model = model
        self.effort = effort
        self.max_tokens = max_tokens
        # max_retries=0: call_with_retry retries, so the attempt count is known.
        # The key comes from ANTHROPIC_API_KEY (.env); tests inject `client`.
        self._client = client or anthropic.Anthropic(timeout=TIMEOUT_S, max_retries=0)
        self._sleep = sleep
        self._clock = clock

    def call(
        self,
        system: list[dict],
        tools: list[dict],
        messages: list[dict],
        *,
        timeout_s: float | None = None,
    ) -> Turn:
        kwargs: dict[str, Any] = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "system": _with_breakpoint(system),
            "tools": _with_breakpoint(tools),
            "messages": messages,
            "output_config": {"effort": self.effort},
        }
        if timeout_s is not None:
            kwargs["timeout"] = timeout_s

        started = self._clock()
        response, attempts = call_with_retry(
            lambda: self._client.messages.create(**kwargs),
            is_transient,
            retry_after=retry_after,
            sleep=self._sleep,
        )
        usage = response.usage
        cache_read = usage.cache_read_input_tokens or 0
        cache_write = usage.cache_creation_input_tokens or 0
        prompt_tokens = usage.input_tokens + cache_read + cache_write
        over_tier = (
            self.model == "claude-haiku-5-5" and prompt_tokens > HAIKU_PRICE_LIMIT
        )

        stop_reason = response.stop_reason or "unknown"
        content = list(response.content)
        texts = [b.text for b in content if b.type == "text"]
        tool_uses = []
        if stop_reason == "tool_use":
            tool_uses = [
                ToolUse(id=b.id, name=b.name, input=dict(b.input))
                for b in content
                if b.type == "tool_use"
            ]
        turn = Turn(
            content=content,
            text="".join(texts),
            tool_uses=tool_uses,
            stop_reason=stop_reason,
            input_tokens=usage.input_tokens,
            output_tokens=usage.output_tokens,
            cache_read_tokens=cache_read,
            cache_write_tokens=cache_write,
            cost_usd=turn_cost(
                self.model,
                usage.input_tokens,
                usage.output_tokens,
                cache_read,
                cache_write,
            ),
            latency_ms=round((self._clock() - started) * 1000),
            attempts=attempts,
        )
        if over_tier:
            # One agent call is a few thousand tokens; this many means a bug upstream. The call
            # was paid at the higher tier ($0.50 / $2.50 per MTok above 100K, 5x the PRICES entry),
            # so the turn carries that cost and the loop stops the request (final review, finding 6).
            raise PriceTierExceeded(
                turn.model_copy(update={"cost_usd": turn.cost_usd * HIGH_TIER_FACTOR})
            )
        return turn

    def count_tokens(
        self, system: list[dict], tools: list[dict], messages: list[dict]
    ) -> int:
        """Input tokens of one request, tools included, from the free count_tokens endpoint."""
        return self._client.messages.count_tokens(
            model=self.model, system=system, tools=tools, messages=messages
        ).input_tokens
