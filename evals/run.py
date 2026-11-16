"""Eval runner. Step 17: `python -m evals.run retrieval` (spec §5).

Builds the structure-chunk index (with the reranker) and the fixed-chunk index, runs the labelled
answerable items through the five configurations of spec §5 and writes
evals/results/retrieval.json. Models run locally (fastembed): no API call, no cost.
"""

import argparse
import json
import sys
from pathlib import Path

from evals.retrieval import evaluate_retrieval, relevant_fixed_ids
from evals.testset import TestItem, load_testset
from src.rag.config import load_config
from src.rag.index import Index, default_embed_fn, default_rerank_fn, load_chunks
from src.rag.search import search

CHUNKS = Path("data/rag/chunks.jsonl")
CHUNKS_FIXED = Path("data/rag/chunks_fixed.jsonl")
TESTSET = Path("evals/testset.jsonl")
RESULTS = Path("evals/results/retrieval.json")
DEPTH = 10  # recall@10 and MRR read the top 10


def labelled(items: list[TestItem]) -> list[TestItem]:
    return [it for it in items if it.answerable and it.relevant_chunk_ids]


def retrieval(config_path: Path = Path("config/rag.yaml")) -> dict:
    cfg = load_config(config_path)
    items = labelled(load_testset(TESTSET))
    if not items:
        sys.exit(
            "no labelled items in evals/testset.jsonl: label relevant_chunk_ids first"
        )

    structure = load_chunks(CHUNKS)
    fixed = load_chunks(CHUNKS_FIXED)
    by_id = {c.chunk_id: c for c in structure}
    embed_fn = default_embed_fn(cfg.embed_model)
    index = Index(
        structure, embed_fn=embed_fn, rerank_fn=default_rerank_fn(cfg.rerank_model)
    )
    fixed_index = Index(fixed, embed_fn=embed_fn)

    fixed_relevant = {
        it.id: relevant_fixed_ids(fixed, by_id, set(it.relevant_chunk_ids))
        for it in items
    }

    def run(idx: Index, mode: str):
        def fn(query: str) -> list[str]:
            hits = search(
                idx,
                query,
                k=DEPTH,
                mode=mode,
                candidates=cfg.candidates,
                rrf_k=cfg.rrf_k,
            )
            return [h.chunk.chunk_id for h in hits]

        return fn

    def structure_labels(it: TestItem) -> set[str]:
        return set(it.relevant_chunk_ids)

    rows = {
        "vector (fixed chunks)": evaluate_retrieval(
            run(fixed_index, "vector"), items, lambda it: fixed_relevant[it.id]
        )
    }
    for mode in ["vector", "bm25", "hybrid", "hybrid_rerank"]:
        rows[mode] = evaluate_retrieval(run(index, mode), items, structure_labels)

    result = {
        "items": len(items),
        "chunks": len(structure),
        "chunks_fixed": len(fixed),
        "embed_model": cfg.embed_model,
        "rerank_model": cfg.rerank_model,
        "candidates": cfg.candidates,
        "rrf_k": cfg.rrf_k,
        "configs": rows,
    }
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(
        f"{len(items)} labelled items | {len(structure)} chunks | {len(fixed)} fixed chunks"
    )
    print(
        f"\n{'config':<24}{'recall@5':>10}{'recall@10':>11}{'MRR':>7}{'ms/q':>8}   misses"
    )
    for name, r in rows.items():
        misses = " ".join(r["misses"]) or "-"
        print(
            f"{name:<24}{r['recall@5']:>10.2f}{r['recall@10']:>11.2f}"
            f"{r['mrr']:>7.2f}{r['ms']:>8.0f}   {misses}"
        )
    print(f"\nwritten {RESULTS}")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("what", choices=["retrieval"])
    args = parser.parse_args()
    if args.what == "retrieval":
        retrieval()


if __name__ == "__main__":
    main()
