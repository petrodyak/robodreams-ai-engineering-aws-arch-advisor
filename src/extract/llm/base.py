"""The shared provider interface: one call to a model, with transport retry.

A provider only sends messages and returns the raw answer text. Validation against the
schema and the one repair call (contract item 16) live once in the pipeline, so Claude and
Ollama are judged by exactly the same logic.
"""

import json
import time
from collections.abc import Callable
from dataclasses import dataclass
from functools import cache
from pathlib import Path
from typing import Any, Protocol

import anthropic

from src.extract.schema import Sampling, ServiceDocument, Usage

MAX_ATTEMPTS = 3  # contract item 15
BASE_DELAY_S = 1.0  # backoff: 1 s, then 2 s
# A server's retry-after is obeyed up to this; one document must not stall a run for minutes.
MAX_RETRY_AFTER_S = 60.0
# A readable copy of llm_schema() in Git; `make schema` (run by `make check`) rewrites it.
SCHEMA_FILE = (
    Path(__file__).resolve().parents[3] / "docs" / "service-document.schema.json"
)


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
    """A provider: Claude (claude.py) or the local model through Ollama (ollama.py)."""

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


def llm_schema_json() -> str:
    """llm_schema() as the text of SCHEMA_FILE: stable, so a diff shows only real changes."""
    return json.dumps(llm_schema(), indent=2, ensure_ascii=False) + "\n"


def call_with_retry[T](
    fn: Callable[[], T],
    is_transient: Callable[[Exception], bool],
    *,
    retry_after: Callable[[Exception], float | None] = lambda _: None,
    max_attempts: int = MAX_ATTEMPTS,
    sleep: Callable[[float], None] = time.sleep,
) -> tuple[T, int]:
    """Run `fn` until it succeeds; return its result and the number of attempts.

    Transient errors (timeouts, rate limits, 5xx) are retried with exponential backoff,
    or after the server's `retry_after(error)` seconds when that is longer (capped);
    any other error, or the last transient one, is re-raised with `.attempts` attached.
    """
    for attempt in range(1, max_attempts + 1):
        try:
            return fn(), attempt
        except Exception as error:
            if not is_transient(error) or attempt == max_attempts:
                error.attempts = attempt  # type: ignore[attr-defined]
                raise
            delay = BASE_DELAY_S * 2 ** (attempt - 1)
            hint = retry_after(error)
            if hint is not None:
                delay = max(delay, min(hint, MAX_RETRY_AFTER_S))
            sleep(delay)
    raise AssertionError("unreachable")  # the loop always returns or raises
