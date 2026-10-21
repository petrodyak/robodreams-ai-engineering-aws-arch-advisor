"""The shared provider interface: one call to a model, with transport retry.

A provider only sends messages and returns the raw answer text. Validation against the
schema and the one repair call (contract item 16) live once in the pipeline, so Claude and
Ollama are judged by exactly the same logic.
"""

import time
from collections.abc import Callable
from dataclasses import dataclass
from functools import cache
from typing import Any, Protocol

import anthropic

from src.extract.schema import Sampling, ServiceDocument, Usage

MAX_ATTEMPTS = 3  # contract item 15
BASE_DELAY_S = 1.0  # backoff: 1 s, then 2 s


@dataclass(frozen=True)
class LLMReply:
    """What one `complete()` call reports back to the pipeline."""

    text: str  # the raw answer; the repair call sends it back with the validation error
    usage: Usage
    latency_ms: int  # wall clock of every attempt and the backoff between them
    attempts: int  # transport attempts: 1 when the first request succeeded
    stop_reason: str | None  # e.g. "max_tokens" means the JSON is truncated


class LLMCallError(Exception):
    """No answer: a non-retryable error, or every transport attempt failed.

    The original exception is chained as `__cause__`.
    """

    def __init__(self, message: str, *, attempts: int, latency_ms: int):
        super().__init__(message)
        self.attempts = attempts
        self.latency_ms = latency_ms


class LLMClient(Protocol):
    """A provider: Claude now (claude.py), Ollama in step 6."""

    model: str  # the full model id written to the Run Record

    def complete(
        self, system: str, messages: list[dict[str, str]], sampling: Sampling
    ) -> LLMReply: ...


@cache
def llm_schema() -> dict[str, Any]:
    """The JSON Schema both providers receive.

    `anthropic.transform_schema` adapts the Pydantic schema to what Claude structured
    outputs accept (e.g. it rewrites `const`); the same dict goes to Ollama so that both
    models see an identical schema (ADR-0003).
    """
    return anthropic.transform_schema(ServiceDocument)


def call_with_retry[T](
    fn: Callable[[], T],
    is_transient: Callable[[Exception], bool],
    *,
    max_attempts: int = MAX_ATTEMPTS,
    sleep: Callable[[float], None] = time.sleep,
) -> tuple[T, int]:
    """Run `fn` until it succeeds; return its result and the number of attempts.

    Transient errors (timeouts, rate limits, 5xx) are retried with exponential backoff;
    any other error, or the last transient one, is re-raised with `.attempts` attached.
    """
    for attempt in range(1, max_attempts + 1):
        try:
            return fn(), attempt
        except Exception as error:
            if not is_transient(error) or attempt == max_attempts:
                error.attempts = attempt  # type: ignore[attr-defined]
                raise
            sleep(BASE_DELAY_S * 2 ** (attempt - 1))
    raise AssertionError("unreachable")  # the loop always returns or raises
