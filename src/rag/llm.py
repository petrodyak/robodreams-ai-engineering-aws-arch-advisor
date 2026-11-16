"""The Claude client of the RAG stage: one structured-output call (spec §6, D4).

- Structured outputs (`output_config.format`) return the answer as JSON text that matches the
  schema, so the code never parses free text.
- Spec D4: no `temperature` / `top_p` / `top_k` and no assistant prefill; Haiku 5.5 and Sonnet 5.5
  reject non-default sampling values. `thinking` is not sent, so the model's default adaptive
  thinking applies; `effort` is sent explicitly, inside `output_config`.
- The transport retry is the one of HW 1 (`call_with_retry`, `is_transient`, `retry_after`),
  imported, not copied, so both stages retry the same way and report the attempt count.
"""

import time
from collections.abc import Callable
from typing import Any

import anthropic
from pydantic import BaseModel

from src.extract.llm.base import call_with_retry
from src.extract.llm.claude import is_transient, retry_after

# USD per million tokens (input, output), from the Claude API model table (checked 16.11).
# Haiku 5.5's price holds for prompts of up to 100K tokens; above it the rate is higher.
PRICES = {"claude-haiku-5-5": (0.10, 0.50), "claude-sonnet-5-5": (2.00, 10.00)}
HAIKU_PRICE_LIMIT = 100_000
TIMEOUT_S = 120  # per attempt; a RAG answer is a few hundred tokens


class LLMResult(BaseModel):
    """One call: the answer text (None when the model gave no text block) and what it cost."""

    text: str | None
    stop_reason: str
    input_tokens: int
    output_tokens: int
    latency_ms: int
    attempts: int
    cost_usd: float


def cost_usd(model: str, input_tokens: int, output_tokens: int) -> float:
    price_in, price_out = PRICES[model]
    return (input_tokens * price_in + output_tokens * price_out) / 1_000_000


class ClaudeJSON:
    """`complete_json(system, user, schema)`: one user message in, the schema's JSON out."""

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

    def complete_json(self, system: str, user: str, schema: dict) -> LLMResult:
        def request() -> anthropic.types.Message:
            return self._client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                system=system,
                messages=[{"role": "user", "content": user}],
                output_config={
                    "format": {"type": "json_schema", "schema": schema},
                    "effort": self.effort,
                },
            )

        started = self._clock()
        response, attempts = call_with_retry(
            request, is_transient, retry_after=retry_after, sleep=self._sleep
        )
        # Thinking blocks come first; the answer is in the text blocks. A refusal or a
        # cut-off answer may carry none: text is then None and the stop reason says why.
        texts = [b.text for b in response.content if b.type == "text"]
        usage = response.usage
        if self.model == "claude-haiku-5-5" and usage.input_tokens > HAIKU_PRICE_LIMIT:
            # A RAG prompt is a few thousand tokens; this many means a bug upstream, and
            # the cost would be under-reported, so it fails loudly.
            raise ValueError(
                f"{usage.input_tokens} input tokens: PRICES holds Haiku 5.5 only up to 100K"
            )
        return LLMResult(
            text="".join(texts) if texts else None,
            stop_reason=response.stop_reason or "unknown",
            input_tokens=usage.input_tokens,
            output_tokens=usage.output_tokens,
            latency_ms=round((self._clock() - started) * 1000),
            attempts=attempts,
            cost_usd=cost_usd(self.model, usage.input_tokens, usage.output_tokens),
        )

    def count_input_tokens(self, system: str, user: str, schema: dict) -> int:
        """Input tokens of one request, schema included, from the free count_tokens endpoint."""
        return self._client.messages.count_tokens(
            model=self.model,
            system=system,
            messages=[{"role": "user", "content": user}],
            output_config={"format": {"type": "json_schema", "schema": schema}},
        ).input_tokens
