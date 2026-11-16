"""Search over the index: vector, BM25, hybrid (RRF) and hybrid + rerank, with filters (spec §5).

`search` is the stage-3 tool: the agent will call it with the same signature.

- vector: the query embedded with the same model as the chunks; Qdrant returns the nearest
  chunks by cosine. Filters run inside Qdrant, so a filtered search still returns k hits.
- bm25: keyword scores over the same header + text; finds exact IDs such as REL09-BP01 that
  embeddings blur. Filters are applied to the ranked list with the same rules.
- hybrid: each search gives its top `candidates`; Reciprocal Rank Fusion adds 1 / (rrf_k + rank)
  per list, so the two different score scales never mix (lesson 7).
- hybrid_rerank: the hybrid top `candidates` are re-scored by a cross-encoder, which reads the
  query and the chunk together (lesson 7, TODO 9).
"""

from collections.abc import Hashable, Iterable
from datetime import date
from typing import Literal

from pydantic import BaseModel
from qdrant_client import models

from src.rag.index import Index, index_text, tokenize
from src.rag.models import ChunkRecord

Mode = Literal["vector", "bm25", "hybrid", "hybrid_rerank"]


class Filters(BaseModel):
    doc_types: list[str] | None = None
    exclude_doc_types: list[str] | None = None
    published_from: date | None = None


class Hit(BaseModel):
    chunk: ChunkRecord
    score: float
    rank: int  # 1-based


def _allowed(chunk: ChunkRecord, f: Filters) -> bool:
    if f.doc_types and chunk.doc_type not in f.doc_types:
        return False
    if f.exclude_doc_types and chunk.doc_type in f.exclude_doc_types:
        return False
    return not (f.published_from and chunk.published < f.published_from)


def _qdrant_filter(f: Filters) -> models.Filter | None:
    must: list[models.Condition] = []
    must_not: list[models.Condition] = []
    if f.doc_types:
        must.append(
            models.FieldCondition(
                key="doc_type", match=models.MatchAny(any=f.doc_types)
            )
        )
    if f.exclude_doc_types:
        must_not.append(
            models.FieldCondition(
                key="doc_type", match=models.MatchAny(any=f.exclude_doc_types)
            )
        )
    if f.published_from:
        # `published` is stored as an ISO date string; DatetimeRange compares it as a date
        must.append(
            models.FieldCondition(
                key="published", range=models.DatetimeRange(gte=f.published_from)
            )
        )
    if not must and not must_not:
        return None
    return models.Filter(must=must or None, must_not=must_not or None)


def _vector(index: Index, query: str, n: int, f: Filters) -> list[tuple[int, float]]:
    points = index.client.query_points(
        index.collection,
        query=index.embed_fn([query])[0],
        limit=n,
        query_filter=_qdrant_filter(f),
    ).points
    return [(p.id, p.score) for p in points]


def _bm25(index: Index, query: str, n: int, f: Filters) -> list[tuple[int, float]]:
    scores = index.bm25.get_scores(tokenize(query))
    order = sorted(range(len(index.chunks)), key=lambda i: -scores[i])
    ranked = [
        (i, float(scores[i]))
        for i in order
        if scores[i] > 0 and _allowed(index.chunks[i], f)
    ]
    return ranked[:n]


def rrf(
    rankings: Iterable[list[Hashable]], rrf_k: int = 60
) -> list[tuple[Hashable, float]]:
    """Reciprocal Rank Fusion: score = sum over lists of 1 / (rrf_k + rank), rank from 1."""
    scores: dict[Hashable, float] = {}
    for ranking in rankings:
        for rank, item in enumerate(ranking, 1):
            scores[item] = scores.get(item, 0.0) + 1 / (rrf_k + rank)
    return sorted(scores.items(), key=lambda kv: -kv[1])


def search(
    index: Index,
    query: str,
    k: int = 5,
    mode: Mode = "hybrid_rerank",
    filters: Filters | None = None,
    *,
    candidates: int = 20,
    rrf_k: int = 60,
) -> list[Hit]:
    """Top-k chunks for the query; [] when the filters leave nothing."""
    if mode == "hybrid_rerank" and index.rerank_fn is None:
        raise ValueError("mode 'hybrid_rerank' needs an Index built with rerank_fn")
    f = filters or Filters()
    n = max(k, candidates)

    if mode == "vector":
        ranked = _vector(index, query, k, f)
    elif mode == "bm25":
        ranked = _bm25(index, query, k, f)
    else:
        lists = [_vector(index, query, n, f), _bm25(index, query, n, f)]
        ranked = rrf(([i for i, _ in lst] for lst in lists), rrf_k)
        if mode == "hybrid_rerank":
            pool = [i for i, _ in ranked[:candidates]]
            scores = index.rerank_fn(query, [index_text(index.chunks[i]) for i in pool])
            ranked = sorted(zip(pool, scores, strict=True), key=lambda kv: -kv[1])
        ranked = ranked[:k]

    return [
        Hit(chunk=index.chunks[i], score=s, rank=r)
        for r, (i, s) in enumerate(ranked, 1)
    ]
