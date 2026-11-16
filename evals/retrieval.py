"""Retrieval metrics (spec §5), adapted from the lesson-7 `evaluate`.

- recall@k: 1 when a relevant chunk is in the top k, else 0; averaged over the questions.
- MRR: 1 / rank of the first relevant chunk in the top 10 (0 when none), averaged.

Fixed-size chunks have their own ids, so Petro's labels (structure chunk ids) are mapped to them by
text overlap: `relevant_fixed_ids`. The rule (Petro, 15.11, option B) ignores the document: a
Framework window that repeats a labelled Reliability Pillar best practice counts as relevant,
because the comparison asks whether the right text was found, not which copy of it.
"""

import time
from collections.abc import Callable

from evals.testset import TestItem
from src.rag.ingest.dedup import shingles
from src.rag.models import ChunkRecord

MRR_DEPTH = 10
FIXED_OVERLAP = 0.5


def recall_at(ranked_ids: list[str], relevant: set[str], k: int) -> float:
    return 1.0 if set(ranked_ids[:k]) & relevant else 0.0


def reciprocal_rank(ranked_ids: list[str], relevant: set[str]) -> float:
    for rank, cid in enumerate(ranked_ids[:MRR_DEPTH], 1):
        if cid in relevant:
            return 1 / rank
    return 0.0


def relevant_fixed_ids(
    fixed: list[ChunkRecord],
    structure_by_id: dict[str, ChunkRecord],
    relevant: set[str],
) -> set[str]:
    """Fixed chunks that share >= 50 % of their own, or of a relevant chunk's, word 5-shingles."""
    targets = [shingles(structure_by_id[cid].text) for cid in relevant]
    out = set()
    for f in fixed:
        own = shingles(f.text)
        for target in targets:
            shared = len(own & target)
            if shared >= FIXED_OVERLAP * len(own) or shared >= FIXED_OVERLAP * len(
                target
            ):
                out.add(f.chunk_id)
                break
    return out


def evaluate_retrieval(
    search_fn: Callable[[str], list[str]],
    items: list[TestItem],
    relevant_of: Callable[[TestItem], set[str]],
    *,
    query_of: Callable[[TestItem], str] = lambda it: it.question,
) -> dict:
    """recall@5, recall@10, MRR, the missed item ids (nothing relevant in the top 10), ms/query."""
    r5, r10, rr, misses, elapsed = [], [], [], [], 0.0
    for it in items:
        relevant = relevant_of(it)
        if not relevant:
            raise ValueError(f"{it.id}: no relevant chunk ids, label the item first")
        start = time.perf_counter()
        ranked = search_fn(query_of(it))[:MRR_DEPTH]
        elapsed += time.perf_counter() - start
        r5.append(recall_at(ranked, relevant, 5))
        r10.append(recall_at(ranked, relevant, 10))
        rr.append(reciprocal_rank(ranked, relevant))
        if not r10[-1]:
            misses.append(it.id)
    n = len(items)
    return {
        "questions": n,
        "recall@5": sum(r5) / n,
        "recall@10": sum(r10) / n,
        "mrr": sum(rr) / n,
        "misses": misses,
        "ms": round(elapsed / n * 1000, 1),
    }
