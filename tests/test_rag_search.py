"""Search modes and filters (src/rag/search.py) on six fixture chunks with a fake embedder."""

from datetime import date

import pytest

from src.rag.index import Index
from src.rag.search import Filters, Hit, rrf, search
from tests.rag_search_fixtures import CHUNKS, fake_embed

MODES = ["vector", "bm25", "hybrid"]


@pytest.fixture(scope="module")
def index() -> Index:
    return Index(CHUNKS, embed_fn=fake_embed)


@pytest.mark.parametrize("query", ["rel09-bp01", "REL09-BP01", "REL09-BP01."])
def test_bm25_finds_id_in_any_form(index, query):
    """Review Focus 1: an ID in lower case or with trailing punctuation still ranks first."""
    hits = search(index, query, k=3, mode="bm25")
    assert hits[0].chunk.chunk_id == "wa-reliability#0000"
    assert hits[0].rank == 1


def test_rrf_prefers_both_lists():
    fused = rrf([["a", "b", "c"], ["d", "b", "e"]], rrf_k=60)
    assert fused[0][0] == "b"  # rank 2 in both lists beats rank 1 in one list
    assert fused[0][1] == pytest.approx(2 / 62)


def test_hits_are_ranked_from_one(index):
    hits = search(index, "data backup", k=4, mode="hybrid")
    assert [h.rank for h in hits] == [1, 2, 3, 4]
    assert all(isinstance(h, Hit) for h in hits)
    assert hits[0].score >= hits[-1].score


def test_rerank_reorders():
    plain = Index(CHUNKS, embed_fn=fake_embed)
    candidates = [h.chunk.chunk_id for h in search(plain, "data", k=20, mode="hybrid")]

    def last_is_best(query: str, docs: list[str]) -> list[float]:
        return [float(i) for i in range(len(docs))]

    reranked = Index(CHUNKS, embed_fn=fake_embed, rerank_fn=last_is_best)
    hits = search(reranked, "data", k=3, mode="hybrid_rerank")
    assert hits[0].chunk.chunk_id == candidates[-1]
    assert hits[0].score == float(len(candidates) - 1)


@pytest.mark.parametrize("mode", MODES)
def test_filters(index, mode):
    # a term in exactly half of the six chunks has BM25Okapi idf log(1) = 0, so the query uses
    # words that tell the documents apart: iceberg (lens, guide), encryption, deploy (pillars)
    query = "iceberg encryption deploy"
    pillars = search(
        index, query, k=6, mode=mode, filters=Filters(doc_types=["pillar"])
    )
    assert pillars and {h.chunk.doc_type for h in pillars} == {"pillar"}

    no_framework = search(
        index, "framework reliability", k=6, mode=mode,
        filters=Filters(exclude_doc_types=["framework"]),
    )  # fmt: skip
    assert "framework" not in {h.chunk.doc_type for h in no_framework}

    recent = search(
        index, query, k=6, mode=mode, filters=Filters(published_from=date(2024, 1, 1))
    )
    assert recent and all(h.chunk.published >= date(2024, 1, 1) for h in recent)


@pytest.mark.parametrize("mode", MODES)
def test_filters_leave_nothing(index, mode):
    """Review Focus 2: filters that match no chunk give [] and do not raise."""
    flt = Filters(doc_types=["lens"], published_from=date(2030, 1, 1))
    assert search(index, "iceberg", k=5, mode=mode, filters=flt) == []


def test_hybrid_rerank_without_reranker_raises(index):
    with pytest.raises(ValueError, match="rerank_fn"):
        search(index, "data", mode="hybrid_rerank")
