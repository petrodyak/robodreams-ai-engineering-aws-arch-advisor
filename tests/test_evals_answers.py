"""The answer run (evals/answers.py), without network: rows per item and the run summary."""

import json

import pytest

from evals.answers import run_id, run_items, summarize, sweep_budget
from evals.testset import TestItem
from src.rag.config import load_config
from src.rag.index import Index
from src.rag.llm import LLMResult
from tests.rag_search_fixtures import CHUNKS, fake_embed

CFG = load_config()


class ScriptLLM:
    """Cites S1 for every question; costs 0.001 per call."""

    model = "claude-haiku-5-5"
    effort = "medium"

    def __init__(self):
        self.calls = 0

    def complete_json(self, system, user, schema):
        self.calls += 1
        text = json.dumps(
            {"found": True, "claims": [{"text": "x", "citations": ["S1"]}]}
        )
        return LLMResult(
            text=text,
            stop_reason="end_turn",
            input_tokens=1000,
            output_tokens=200,
            latency_ms=10,
            attempts=1,
            cost_usd=0.001,
        )


def item(i: int, relevant: list[str]) -> TestItem:
    return TestItem(
        id=f"one{i:02d}",
        question="REL09-BP01 backup data",
        kind="single",
        expected_answer="x",
        key_facts=["x"],
        expected_sources=[{"doc_id": "wa-reliability", "section": "s"}],
        relevant_chunk_ids=relevant,
        answerable=True,
        verified_by="Petro",
        verified_on="2026-11-16",
    )


def index() -> Index:
    return Index(
        CHUNKS,
        embed_fn=fake_embed,
        rerank_fn=lambda query, docs: [float(-i) for i in range(len(docs))],
    )


def test_run_items_and_summary():
    llm = ScriptLLM()
    items = [item(1, ["wa-reliability#0000"]), item(2, ["missing#0000"])]

    rows = run_items(items, index(), llm, CFG, k=5, budget=3000)
    summary = summarize(rows, items)

    assert [r["id"] for r in rows] == ["one01", "one02"]
    assert llm.calls == 2
    assert summary["items"] == 2
    assert summary["found"] == 2
    # one02's relevant chunk is not in the corpus, so it is never in the context
    assert summary["context_recall"] == pytest.approx(0.5)
    assert summary["cost_usd"] == pytest.approx(0.002)
    assert summary["usd_per_1000"] == pytest.approx(1.0)
    assert summary["avg_input_tokens"] == pytest.approx(1000)


def test_run_id_and_sweep_budget():
    assert (
        run_id("claude-haiku-5-5", "v1", "medium", 5)
        == "claude-haiku-5-5__v1__medium__k5"
    )
    assert sweep_budget(3, 3000) == 3000  # the default budget already holds 3 chunks
    assert sweep_budget(8, 3000) == 8 * 480  # 8 chunks of the hard maximum
