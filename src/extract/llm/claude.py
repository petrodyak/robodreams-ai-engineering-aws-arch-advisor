"""Claude provider: claude-haiku-4-5 with structured outputs (contract item 14).

`messages.create()` with `output_config.format`, not `messages.parse()`: parse() would
validate without the service context (which now fails by design) and would hide the raw
text that the repair call needs.
"""

import time
from collections.abc import Callable
from typing import Any

import anthropic

from src.extract.llm.base import LLMCallError, LLMReply, call_with_retry, llm_schema
from src.extract.schema import Sampling, Usage

MODEL = "claude-haiku-4-5"
# Per attempt. Measured ≈147 output tokens/s (S3 trial, 21.10), so a full MAX_TOKENS
# answer takes ≈220 s; 120 s was too tight.
TIMEOUT_S = 300
# A provider constant (contract item 14). Finding F1: a complete S3 answer (254 Endpoint
# Rows) is ≈14.4k tokens, and the S3 trial was cut off at 16384. 32000 leaves headroom and
# stays below Haiku 4.5's 64k limit. Non-streaming still works: the SDK's "streaming is
# required" guard only applies when no explicit timeout is passed, and we always pass one.
MAX_TOKENS = 32000
# List prices, USD per million tokens (claude-haiku-4-5); cost per 1,000 documents (item 19).
PRICE_PER_MTOK = {"input": 1.00, "output": 5.00}

# 408 timeout, 409 conflict, 429 rate limit: worth another try, like any 5xx (529 overloaded).
_RETRYABLE_STATUS = {408, 409, 429}


def is_transient(error: Exception) -> bool:
    """A transport failure that may succeed on retry (contract item 15)."""
    if isinstance(error, anthropic.APIConnectionError):  # includes APITimeoutError
        return True
    if isinstance(error, anthropic.APIStatusError):
        return error.status_code in _RETRYABLE_STATUS or error.status_code >= 500
    return False


def retry_after(error: Exception) -> float | None:
    """Seconds the API asks to wait before retrying (`retry-after` on 429/529), if any."""
    if not isinstance(error, anthropic.APIStatusError):
        return None
    try:
        return float(error.response.headers.get("retry-after", ""))
    except ValueError:  # absent, or an HTTP date: the backoff applies
        return None


def _sampling_body(sampling: Sampling) -> dict[str, float]:
    # anthropic 1.x dropped temperature/top_p from the method signatures; the API still
    # accepts them for claude-haiku-4-5, so they travel in extra_body. An unset top_p is
    # not sent at all: the API asks for temperature *or* top_p (contract item 14).
    body = {"temperature": sampling.temperature}
    if sampling.top_p is not None:
        body["top_p"] = sampling.top_p
    return body


class ClaudeClient:
    """The Claude implementation of `LLMClient`."""

    def __init__(
        self,
        model: str = MODEL,
        *,
        timeout: float = TIMEOUT_S,
        max_tokens: int = MAX_TOKENS,
        client: Any = None,
        sleep: Callable[[float], None] = time.sleep,
        clock: Callable[[], float] = time.perf_counter,
    ):
        self.model = model
        self.timeout = timeout
        self.max_tokens = max_tokens
        # max_retries=0: our own loop retries, because the Run Record needs the attempt
        # count and the SDK's built-in retry does not report it. The key comes from
        # ANTHROPIC_API_KEY (.env); `client` is injected only by tests.
        self._client = client or anthropic.Anthropic(timeout=timeout, max_retries=0)
        self._sleep = sleep
        self._clock = clock

    def complete(
        self, system: str, messages: list[dict[str, str]], sampling: Sampling
    ) -> LLMReply:
        def request() -> anthropic.types.Message:
            return self._client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                system=system,
                messages=messages,
                output_config={
                    "format": {"type": "json_schema", "schema": llm_schema()}
                },
                extra_body=_sampling_body(sampling),
                timeout=self.timeout,
            )

        started = self._clock()
        try:
            response, attempts = call_with_retry(
                request, is_transient, retry_after=retry_after, sleep=self._sleep
            )
        except Exception as error:
            raise LLMCallError(
                f"{type(error).__name__}: {error}",
                attempts=getattr(error, "attempts", 1),
                latency_ms=_elapsed_ms(started, self._clock()),
            ) from error

        return LLMReply(
            # Structured outputs return the JSON as text; a refusal may return none.
            text="".join(b.text for b in response.content if b.type == "text"),
            usage=Usage(
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens,
            ),
            latency_ms=_elapsed_ms(started, self._clock()),
            attempts=attempts,
            stop_reason=response.stop_reason,
        )

    def count_input_tokens(self, system: str, messages: list[dict[str, str]]) -> int:
        """Input tokens of one request, schema included, from the free count_tokens
        endpoint: the "money before the run" estimate (Implementation_steps.md §1)."""
        return self._client.messages.count_tokens(
            model=self.model,
            system=system,
            messages=messages,
            output_config={"format": {"type": "json_schema", "schema": llm_schema()}},
        ).input_tokens


def cost_usd(input_tokens: int, output_tokens: int) -> float:
    return (
        input_tokens * PRICE_PER_MTOK["input"]
        + output_tokens * PRICE_PER_MTOK["output"]
    ) / 1_000_000


def _elapsed_ms(started: float, now: float) -> int:
    return round((now - started) * 1000)
