"""The local JSONL trace, the record the evals read, and the sink interface for Langfuse (spec §12).

ADR-0013: one JSON line per request is written locally, always; Langfuse mirrors it. A sink is any
object with the methods `start`, `model_call`, `tool_call`, `end` and `score` (Task 22.9 plugs the
Langfuse client in behind them). Every sink call goes through `_sink`, which catches and logs, so a
missing key or a Langfuse outage never fails a request or a test.
"""

import json
import logging
import os
import sys
import time
import uuid
from collections.abc import Callable, Iterator, Mapping
from contextlib import ExitStack, contextmanager
from pathlib import Path
from typing import Any, TextIO

from src.agent.llm import Turn
from src.agent.loop import CallRecord, TurnResult

log = logging.getLogger(__name__)

RESULT_CHARS = 500
TRACE_KEYS = (
    "trace_id",
    "session_id",
    "question",
    "prompt_version",
    "faults",
    "model_calls",
    "tool_calls",
    "critic",
    "retrieved_chunk_ids",
    "stop",
    "totals",
    "answer",
)


def _clip(text: str) -> str:
    """At most RESULT_CHARS: the head and the end, so a note appended to a result stays visible."""
    if len(text) <= RESULT_CHARS:
        return text
    tail = 140
    return text[: RESULT_CHARS - tail - 3] + " … " + text[-tail:]


def _model_call(t: Turn) -> dict:
    return {
        "stop_reason": t.stop_reason,
        "input_tokens": t.input_tokens,
        "output_tokens": t.output_tokens,
        "cache_read_tokens": t.cache_read_tokens,
        "cache_write_tokens": t.cache_write_tokens,
        "usd": t.cost_usd,
        "latency_ms": t.latency_ms,
        "attempts": t.attempts,
        "tool_uses": [u.name for u in t.tool_uses],
        "text": t.text[:RESULT_CHARS],
    }


def _tool_call(r: CallRecord) -> dict:
    return {
        "step": r.step,
        "name": r.name,
        "input": r.input,
        "result": _clip(r.outcome.text),
        "is_error": r.outcome.is_error,
        "attempts": r.outcome.attempts,
        "faults": r.outcome.faults,
        "data": r.outcome.data,
        "ms": r.ms,
    }


class RequestTrace:
    def __init__(self, tracer: "Tracer", session_id: int, question: str, meta: dict):
        self.tracer = tracer
        self.trace_id = uuid.uuid4().hex
        self._started = time.perf_counter()
        self.line: dict[str, Any] = {
            "trace_id": self.trace_id,
            "session_id": session_id,
            "question": question,
            "prompt_version": meta.get("prompt_version"),
            "faults": list(meta.get("faults", [])),
            "model_calls": [],
            "tool_calls": [],
            "critic": [],
            "retrieved_chunk_ids": [],
            "stop": None,
            "totals": {},
            "answer": None,
        }
        self._ended = False

    def model_call(self, t: Turn) -> None:
        entry = _model_call(t)
        self.line["model_calls"].append(entry)
        self.tracer._sink("model_call", self.trace_id, entry)

    def tool_call(self, record: CallRecord) -> None:
        entry = _tool_call(record)
        self.line["tool_calls"].append(entry)
        if record.name == "search_corpus" and not record.outcome.is_error:
            for chunk_id in (record.outcome.data or {}).get("labels", {}).values():
                if chunk_id not in self.line["retrieved_chunk_ids"]:
                    self.line["retrieved_chunk_ids"].append(chunk_id)
        self.tracer._sink("tool_call", self.trace_id, entry)

    def critic(self, verdict: list[str]) -> None:
        self.line["critic"].append(list(verdict))

    def end(self, result: TurnResult) -> None:
        state = result.state
        self.line["stop"] = result.stop
        self.line["answer"] = result.answer
        self.line["totals"] = {
            "steps": state.steps,
            "tokens": state.tokens,
            "usd": round(state.usd, 6),
            "ms": round((time.perf_counter() - self._started) * 1000),
            "partial": result.partial,
        }
        self._ended = True

    def _fail(self, error: BaseException) -> None:
        self.line["stop"] = "error"
        self.line["answer"] = f"{type(error).__name__}: {error}"
        # the calls made before the error were paid: their cost stays in the totals (finding 6)
        calls = self.line["model_calls"]
        self.line["totals"] = {
            "steps": len(calls),
            "tokens": sum(
                c["input_tokens"]
                + c["output_tokens"]
                + c["cache_read_tokens"]
                + c["cache_write_tokens"]
                for c in calls
            ),
            "usd": round(sum(c["usd"] for c in calls), 6),
            "ms": round((time.perf_counter() - self._started) * 1000),
            "partial": True,
        }


class Tracer:
    def __init__(self, path: Path, *, langfuse: Any = None):
        self.path = Path(path)
        self.langfuse = langfuse
        self._warned = False

    @contextmanager
    def request(
        self, session_id: int, question: str, meta: dict
    ) -> Iterator[RequestTrace]:
        t = RequestTrace(self, session_id, question, meta)
        self._sink("start", t.trace_id, session_id, question, meta)
        try:
            yield t
        except BaseException as error:
            t._fail(error)
            raise
        finally:
            self._write(t.line)
            self._sink("end", t.trace_id, t.line)

    def score(
        self, trace_id: str, name: str, value: float, comment: str | None
    ) -> None:
        self._sink("score", trace_id, name, value, comment)

    def _write(self, line: dict) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False, default=str) + "\n")

    def _sink(self, method: str, *args: Any) -> None:
        """Call the sink if there is one; a failure is logged (once loudly), never raised."""
        if self.langfuse is None:
            return
        try:
            getattr(self.langfuse, method)(*args)
        except Exception as error:  # noqa: BLE001 - tracing never fails a request (D16)
            level = logging.DEBUG if self._warned else logging.WARNING
            log.log(level, "Langfuse sink %s failed: %s", method, error)
            self._warned = True


# --- Langfuse sink (Task 22.9, D16) ---------------------------------------------------------
#
# Langfuse Python SDK 5.2 (uv add langfuse resolved 5.2.0; spec §12 named v4). The calls below were
# checked on 25.11 against the installed signatures and the Langfuse docs (Context7
# /langfuse/langfuse-docs): `start_as_current_observation(trace_context={"trace_id": …})` gives the
# trace our own id, `propagate_attributes(session_id=…, tags=…, metadata=…)` puts the session on the
# observations created inside it, `start_observation(as_type="generation" | "tool")` adds the children,
# `create_score(trace_id=…)` scores a trace, `flush()` sends what is buffered. The keys come from
# LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY and LANGFUSE_BASE_URL (LANGFUSE_HOST is deprecated).

KEYS = ("LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY")


class LangfuseSink:
    """The sink protocol of `Tracer` over the Langfuse client: one trace per request."""

    def __init__(self, client: Any, *, propagate: Any = None):
        if propagate is None:
            from langfuse import propagate_attributes as propagate
        self.client = client
        self.propagate = propagate
        self._open: dict[str, tuple[ExitStack, Any, dict]] = {}

    def start(self, trace_id: str, session_id: int, question: str, meta: dict) -> None:
        run_id = meta.get("run_id")
        session = f"{run_id}-s{session_id}" if run_id else f"chat-s{session_id}"
        tags = [f"prompt:{meta.get('prompt_version')}"]
        tags += [f"faults:{f}" for f in meta.get("faults", [])]
        if run_id:
            tags.append(f"run:{run_id}")
        stack = ExitStack()
        try:
            root = stack.enter_context(
                self.client.start_as_current_observation(
                    trace_context={"trace_id": trace_id},
                    name="agent-request",
                    as_type="agent",
                    input=question,
                )
            )
            stack.enter_context(
                self.propagate(
                    session_id=session,
                    tags=tags,
                    metadata={k: str(v) for k, v in meta.items() if k != "faults"},
                    trace_name="agent-request",
                )
            )
        except BaseException:
            stack.close()
            raise
        self._open[trace_id] = (stack, root, meta)

    def model_call(self, trace_id: str, entry: dict) -> None:
        _, root, meta = self._open[trace_id]
        root.start_observation(
            name="claude",
            as_type="generation",
            model=meta.get("model"),
            output=entry["text"],
            usage_details={
                "input": entry["input_tokens"],
                "output": entry["output_tokens"],
                "cache_read_input_tokens": entry["cache_read_tokens"],
                "cache_creation_input_tokens": entry["cache_write_tokens"],
            },
            cost_details={"total": entry["usd"]},
            metadata={
                "stop_reason": entry["stop_reason"],
                "latency_ms": entry["latency_ms"],
                "attempts": entry["attempts"],
                "tool_uses": entry["tool_uses"],
            },
        ).end()

    def tool_call(self, trace_id: str, entry: dict) -> None:
        _, root, _ = self._open[trace_id]
        root.start_observation(
            name=entry["name"],
            as_type="tool",
            input=entry["input"],
            output=entry["result"],
            level="ERROR" if entry["is_error"] else "DEFAULT",
            metadata={
                "attempts": entry["attempts"],
                "faults": entry["faults"],
                "ms": entry["ms"],
            },
        ).end()

    def end(self, trace_id: str, line: dict) -> None:
        opened = self._open.pop(trace_id, None)
        if opened is None:
            return
        stack, root, _ = opened
        try:
            root.update(
                output=line["answer"],
                metadata={"stop": line["stop"], "totals": line["totals"]},
                level="ERROR" if line["stop"] == "error" else "DEFAULT",
            )
        finally:
            stack.close()
            self.client.flush()

    def score(
        self, trace_id: str, name: str, value: float, comment: str | None
    ) -> None:
        self.client.create_score(
            name=name, value=value, trace_id=trace_id, comment=comment
        )
        self.client.flush()


def make_langfuse(
    env: Mapping[str, str] | None = None,
    *,
    client_factory: Callable[..., Any] | None = None,
) -> LangfuseSink | None:
    """The Langfuse sink, or None (one warning) when the keys are missing or the client fails."""
    env = os.environ if env is None else env
    missing = [k for k in KEYS if not env.get(k)]
    if missing:
        log.warning(
            "Langfuse is off: %s not set; the local trace is still written",
            ", ".join(missing),
        )
        return None
    try:
        from langfuse import Langfuse, is_langfuse_span

        factory = client_factory or Langfuse
        # Export only the spans this code creates: Langfuse 5.2 would also export the Anthropic
        # SDK's own OpenTelemetry span of every call, which doubles each generation and its cost.
        return LangfuseSink(factory(should_export_span=is_langfuse_span))
    except Exception as error:  # noqa: BLE001 - tracing never fails a request (D16)
        log.warning("Langfuse is off: the client failed to start: %s", error)
        return None


def langfuse_check(
    env: Mapping[str, str] | None = None,
    *,
    client_factory: Callable[..., Any] | None = None,
    out: TextIO = sys.stdout,
) -> int:
    """`make langfuse-check`: one test trace, no Claude call ($0); exit 0 when Langfuse took it."""
    env = os.environ if env is None else env
    missing = [k for k in KEYS if not env.get(k)]
    if missing:
        out.write(f"Langfuse keys missing in .env: {', '.join(missing)}\n")
        return 1
    if client_factory is None:
        from langfuse import Langfuse as client_factory
    client = client_factory()
    base_url = env.get("LANGFUSE_BASE_URL", "https://cloud.langfuse.com")
    if not client.auth_check():
        out.write(
            f"Langfuse rejected the keys at {base_url}: check the keys and the region\n"
        )
        return 1
    with client.start_as_current_observation(
        name="langfuse-check",
        as_type="span",
        input="test trace from make langfuse-check",
    ) as span:
        span.update(output="ok")
        trace_id = span.trace_id
    client.flush()
    out.write(
        f"Langfuse accepted the keys at {base_url}; test trace: {client.get_trace_url(trace_id=trace_id)}\n"
    )
    return 0


if __name__ == "__main__":
    import argparse

    from dotenv import load_dotenv

    parser = argparse.ArgumentParser(description="Langfuse sink of the agent trace")
    parser.add_argument("--check", action="store_true", help="send one test trace ($0)")
    if parser.parse_args().check:
        load_dotenv()
        sys.exit(langfuse_check())
