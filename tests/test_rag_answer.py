"""Answering with sources (src/rag/answer.py), without network.

The index uses the fake embedder of the search tests and a fake reranker; Claude is a fake that
plays back a fixed LLMResult and counts its calls. The tests pin the context budget (skip, never
cut), the citation check, the not-found answer, and Review Focus 2 and 3.
"""

import json
from datetime import date

import pytest

from src.rag.answer import (
    NOT_FOUND,
    Claim,
    ModelAnswer,
    answer,
    build_context,
    validate,
)
from src.rag.config import load_config
from src.rag.index import Index
from src.rag.llm import LLMResult
from src.rag.search import Filters, Hit
from tests.rag_search_fixtures import CHUNKS, chunk, fake_embed

CFG = load_config()


class FakeLLM:
    model = "claude-haiku-5-5"
    effort = "medium"

    def __init__(self, text: str | None, stop_reason: str = "end_turn"):
        self.result = LLMResult(
            text=text,
            stop_reason=stop_reason,
            input_tokens=2000,
            output_tokens=300,
            latency_ms=900,
            attempts=1,
            cost_usd=0.00035,
        )
        self.calls = []

    def complete_json(self, system: str, user: str, schema: dict) -> LLMResult:
        self.calls.append((system, user, schema))
        return self.result


def index() -> Index:
    # The fake reranker keeps the RRF order: a falling score per position.
    return Index(
        CHUNKS,
        embed_fn=fake_embed,
        rerank_fn=lambda query, docs: [float(-i) for i in range(len(docs))],
    )


def reply(found: bool, claims: list[tuple[str, list[str]]]) -> str:
    return json.dumps(
        {"found": found, "claims": [{"text": t, "citations": c} for t, c in claims]}
    )


def hit(chunk_id: str, tokens: int, rank: int) -> Hit:
    c = chunk(chunk_id, f"text of {chunk_id}").model_copy(update={"n_tokens": tokens})
    return Hit(chunk=c, score=1.0 / rank, rank=rank)


def test_budget_skips_not_truncates():
    hits = [hit("a#0001", 1000, 1), hit("b#0001", 2500, 2), hit("c#0001", 900, 3)]

    context, sources = build_context(hits, budget=3000)

    assert {label: c.chunk_id for label, c in sources.items()} == {
        "S1": "a#0001",
        "S2": "c#0001",
    }
    assert "text of a#0001" in context and "text of c#0001" in context
    assert "b#0001" not in context
    assert context.startswith("[S1] a title · Section · 2024-11-06\ntext of a#0001")


def test_validate_normalizes_and_drops():
    sources = {"S1": CHUNKS[0]}
    ans = ModelAnswer(found=True, claims=[Claim(text="c1", citations=["[s1]", "S9"])])

    claims, dropped, uncited = validate(ans, sources)

    assert [c.citations for c in claims] == [["S1"]]
    assert claims[0].refs[0].chunk_id == CHUNKS[0].chunk_id
    assert dropped == ["S9"]
    assert uncited == 0


def test_uncited_claim_removed():
    sources = {"S1": CHUNKS[0]}
    ans = ModelAnswer(
        found=True,
        claims=[
            Claim(text="kept", citations=["S1"]),
            Claim(text="gone", citations=["S9"]),
        ],
    )

    claims, dropped, uncited = validate(ans, sources)

    assert [c.text for c in claims] == ["kept"]
    assert dropped == ["S9"]
    assert uncited == 1


def test_found_but_nothing_valid_is_not_found():
    llm = FakeLLM(reply(True, [("unsupported", ["S9"])]))

    record = answer("REL09-BP01 backup", index(), llm, CFG)

    assert record.found is False
    assert record.answer.startswith(NOT_FOUND + "\nClosest sources: ")
    assert record.uncited_claims == 1
    assert record.claims == []


def test_no_hits_no_call():
    # Review Focus 2: filters that leave nothing give the not-found answer, no Claude call.
    llm = FakeLLM(reply(True, [("x", ["S1"])]))
    nothing = Filters(doc_types=["lens"], published_from=date(2030, 1, 1))

    record = answer("REL09-BP01 backup", index(), llm, CFG, filters=nothing)

    assert llm.calls == []
    assert record.answer.startswith(NOT_FOUND)
    assert record.found is False
    assert record.retrieved == [] and record.cost_usd == 0


@pytest.mark.parametrize("stop_reason", ["refusal", "max_tokens"])
def test_refusal_and_max_tokens(stop_reason):
    # Review Focus 3: no usable text; the record keeps the stop reason and nothing raises.
    llm = FakeLLM(None, stop_reason=stop_reason)

    record = answer("REL09-BP01 backup", index(), llm, CFG)

    assert record.found is False
    assert record.stop_reason == stop_reason
    assert record.answer.startswith(NOT_FOUND)
    assert record.cost_usd == pytest.approx(0.00035)


def test_cut_json_is_not_found():
    llm = FakeLLM('{"found": true, "claims": [{"text": "cut', stop_reason="max_tokens")

    record = answer("REL09-BP01 backup", index(), llm, CFG)

    assert record.found is False
    assert record.stop_reason == "max_tokens"


def test_answer_text_cites_each_claim():
    llm = FakeLLM(reply(True, [("c1", ["S1"]), ("c2", ["S1", "S2"])]))

    record = answer("REL09-BP01 backup", index(), llm, CFG)

    assert record.found is True
    assert record.answer == "c1 [S1] c2 [S1][S2]"
    assert set(record.sources) >= {"S1", "S2"}
    assert record.in_context == [record.sources[s] for s in sorted(record.sources)]
    assert record.model == "claude-haiku-5-5" and record.prompt_version == "v1"


def test_prompt_carries_question_and_sources():
    llm = FakeLLM(reply(False, []))

    answer("REL09-BP01 backup", index(), llm, CFG)

    system, user, schema = llm.calls[0]
    assert "Answer only from the sources" in system
    assert "<sources>" in user and "[S1]" in user
    assert "REL09-BP01 backup" in user
    assert schema["additionalProperties"] is False
