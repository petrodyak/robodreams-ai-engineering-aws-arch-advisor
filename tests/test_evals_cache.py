"""The eval cache (evals/cache.py, ADR-0008), without network.

A cached answer is replayed instead of a paid call; a miss in CI (live=False) fails with a message
that says what to do; the cost guard stops a run before its 31st new call.
"""

import pytest

from evals.cache import (
    CachedLLM,
    CostGuardError,
    EvalCache,
    StaleCacheError,
    cache_key,
)
from src.rag.llm import LLMResult

SCHEMA = {"type": "object"}


class CountingLLM:
    model = "claude-haiku-5-5"
    effort = "medium"

    def __init__(self):
        self.calls = 0

    def complete_json(self, system, user, schema):
        self.calls += 1
        return LLMResult(
            text=f'{{"n": {self.calls}}}',
            stop_reason="end_turn",
            input_tokens=100,
            output_tokens=10,
            latency_ms=5,
            attempts=1,
            cost_usd=0.00002,
        )


def test_hit_makes_no_call(tmp_path):
    cache = EvalCache(tmp_path / "answers.jsonl", live=True)
    cache.put("k1", {"a": 1})
    assert cache.get("k1") == {"a": 1}
    assert cache.get("other") is None

    inner = CountingLLM()
    llm = CachedLLM(inner, cache)
    first = llm.complete_json("system", "user", SCHEMA)
    second = llm.complete_json("system", "user", SCHEMA)

    assert inner.calls == 1
    assert first == second
    assert cache.misses == 1
    assert (llm.model, llm.effort) == ("claude-haiku-5-5", "medium")


def test_cache_survives_a_reload_and_the_last_line_wins(tmp_path):
    path = tmp_path / "answers.jsonl"
    cache = EvalCache(path, live=True)
    cache.put("k1", {"v": 1})
    cache.put("k1", {"v": 2})

    assert EvalCache(path, live=False).get("k1") == {"v": 2}
    assert len(path.read_text().splitlines()) == 2  # append only


def test_key_changes_with_effort_and_prompt():
    base = cache_key("claude-haiku-5-5", "medium", "system", "user", SCHEMA)

    assert base == cache_key("claude-haiku-5-5", "medium", "system", "user", SCHEMA)
    assert base != cache_key("claude-haiku-5-5", "high", "system", "user", SCHEMA)
    assert base != cache_key("claude-haiku-5-5", "medium", "systen", "user", SCHEMA)
    assert base != cache_key("claude-haiku-5-5", "medium", "system", "user.", SCHEMA)
    assert base != cache_key("claude-haiku-5-5", "medium", "system", "user", {})


def test_stale_without_live(tmp_path):
    inner = CountingLLM()
    llm = CachedLLM(inner, EvalCache(tmp_path / "answers.jsonl", live=False))

    with pytest.raises(StaleCacheError) as error:
        llm.complete_json("system", "user", SCHEMA)

    assert (
        str(error.value)
        == "cache is stale: run make eval locally and commit evals/cache/"
    )
    assert inner.calls == 0


def test_cost_guard(tmp_path):
    inner = CountingLLM()
    llm = CachedLLM(
        inner, EvalCache(tmp_path / "answers.jsonl", live=True, max_misses=2)
    )
    llm.complete_json("s", "u1", SCHEMA)
    llm.complete_json("s", "u2", SCHEMA)

    with pytest.raises(CostGuardError):
        llm.complete_json("s", "u3", SCHEMA)

    assert inner.calls == 2  # stopped before the third call
    llm.complete_json("s", "u1", SCHEMA)  # a hit still works
