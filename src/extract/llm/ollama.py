"""Ollama provider: the local qwen2.5:7b with JSON-schema constrained output (step 6).

The same `LLMClient` interface as Claude, so the pipeline (validation, the one repair call,
Run Records) is shared unchanged. The model receives the identical schema, `llm_schema()`,
through Ollama's `format` parameter.

Ollama does not report a cut-off context: when input plus output reach `num_ctx` it drops
tokens silently. A reply that fills the window is therefore reported as cut off
(`stop_reason = "max_tokens"`), like one that hits `num_predict`, and the pipeline fails it
without a repair call (contract item 16).
"""

import os
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

import httpx  # Ollama's own HTTP client: its timeouts surface as httpx exceptions
import ollama
import yaml

from src.extract.llm.base import LLMCallError, LLMReply, call_with_retry, llm_schema
from src.extract.schema import Sampling, Usage

MODEL = "qwen2.5:7b"
# Per attempt. A local 7B model writes tens of tokens per second, so a long answer takes
# minutes; the S3 trial of step 6 measures it.
TIMEOUT_S = 900
# The output cap, Ollama's counterpart of Claude's max_tokens (contract item 14). A complete
# S3 answer is ≈16.6k Claude tokens; qwen's tokenizer counts this text ≈0.73× as many.
NUM_PREDICT = 16384
# Keep the model loaded between the documents of a run instead of reloading it each time.
KEEP_ALIVE = "30m"
SAMPLING_CONFIG = Path(__file__).resolve().parents[3] / "config" / "sampling.yaml"


def num_ctx(path: Path = SAMPLING_CONFIG) -> int:
    """The context window, a provider constant in config/sampling.yaml (finding F2)."""
    return int(yaml.safe_load(path.read_text())["providers"]["ollama"]["num_ctx"])


def is_transient(error: Exception) -> bool:
    """A transport failure that may succeed on retry (contract item 15): the server is down
    or restarting, the call timed out, or the server failed (5xx) or is busy (429)."""
    if isinstance(error, (ConnectionError, httpx.TransportError)):
        return True
    if isinstance(error, ollama.ResponseError):
        return error.status_code == 429 or error.status_code >= 500
    return False


def _options(sampling: Sampling, window: int, num_predict: int) -> dict[str, Any]:
    # top_p is not sent when the configuration leaves it unset, as for Claude (item 14).
    options = {
        "temperature": sampling.temperature,
        "num_ctx": window,
        "num_predict": num_predict,
    }
    if sampling.top_p is not None:
        options["top_p"] = sampling.top_p
    return options


class OllamaClient:
    """The Ollama implementation of `LLMClient`."""

    def __init__(
        self,
        model: str = MODEL,
        *,
        timeout: float = TIMEOUT_S,
        num_predict: int = NUM_PREDICT,
        window: int | None = None,
        client: Any = None,
        sleep: Callable[[float], None] = time.sleep,
        clock: Callable[[], float] = time.perf_counter,
    ):
        self.model = model
        self.num_predict = num_predict
        self.window = window if window is not None else num_ctx()
        # OLLAMA_HOST from .env (default http://localhost:11434); `client` only in tests.
        self._client = client or ollama.Client(
            host=os.environ.get("OLLAMA_HOST"), timeout=timeout
        )
        self._sleep = sleep
        self._clock = clock

    def complete(
        self, system: str, messages: list[dict[str, str]], sampling: Sampling
    ) -> LLMReply:
        def request() -> Any:
            return self._client.chat(
                model=self.model,
                messages=[{"role": "system", "content": system}, *messages],
                format=llm_schema(),
                options=_options(sampling, self.window, self.num_predict),
                keep_alive=KEEP_ALIVE,
            )

        started = self._clock()
        try:
            response, attempts = call_with_retry(
                request, is_transient, sleep=self._sleep
            )
        except Exception as error:
            raise LLMCallError(
                f"{type(error).__name__}: {error}",
                attempts=getattr(error, "attempts", 1),
                latency_ms=_elapsed_ms(started, self._clock()),
            ) from error

        tokens_in = response.prompt_eval_count or 0
        tokens_out = response.eval_count or 0
        cut_off = (
            response.done_reason == "length" or tokens_in + tokens_out >= self.window
        )
        return LLMReply(
            text=response.message.content or "",
            usage=Usage(input_tokens=tokens_in, output_tokens=tokens_out),
            latency_ms=_elapsed_ms(started, self._clock()),
            attempts=attempts,
            stop_reason="max_tokens" if cut_off else response.done_reason,
        )


def _elapsed_ms(started: float, now: float) -> int:
    return round((now - started) * 1000)
