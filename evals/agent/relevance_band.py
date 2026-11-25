"""Measure the relevance band of search_corpus (spec §10, plan Task 22.4 Step 5). Local, no API cost.

The reranker score is an uncalibrated logit, so a bare number tells the model nothing. This script
takes the top-1 reranker score of every answerable question of `evals/testset.jsonl` and of every
`no_answer` question of `evals/testset.jsonl` and `evals/testset_heldout.jsonl`, and prints both
distributions and the threshold that separates them best. Run: `uv run python -m evals.agent.relevance_band`.
"""

import itertools
import json
from pathlib import Path

from src.agent.search_tool import build_agent_index
from src.rag.config import load_config
from src.rag.search import search

SETS = [Path("evals/testset.jsonl"), Path("evals/testset_heldout.jsonl")]


def top1_scores() -> tuple[list[tuple[str, float]], list[tuple[str, float]]]:
    cfg = load_config()
    index = build_agent_index(cfg, overlay=False)
    answerable, none = [], []
    for path in SETS:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            hits = search(
                index,
                item["question"],
                k=1,
                mode="hybrid_rerank",
                candidates=cfg.candidates,
                rrf_k=cfg.rrf_k,
            )
            score = hits[0].score if hits else float("-inf")
            (none if item["kind"] == "no_answer" else answerable).append(
                (item["id"], score)
            )
    return answerable, none


def best_threshold(answerable: list[float], none: list[float]) -> tuple[float, int]:
    """The midpoint threshold with the fewest errors (answerable below it + none at or above it)."""
    values = sorted(set(answerable + none))
    candidates = [(a + b) / 2 for a, b in itertools.pairwise(values)] or values
    best = min(
        candidates,
        key=lambda t: sum(s < t for s in answerable) + sum(s >= t for s in none),
    )
    errors = sum(s < best for s in answerable) + sum(s >= best for s in none)
    return best, errors


def main() -> None:
    answerable, none = top1_scores()
    for name, rows in (("answerable", answerable), ("no_answer", none)):
        print(f"{name} ({len(rows)}):")
        for item_id, score in sorted(rows, key=lambda r: r[1]):
            print(f"  {item_id:8s} {score:7.2f}")
    threshold, errors = best_threshold([s for _, s in answerable], [s for _, s in none])
    total = len(answerable) + len(none)
    print(f"best threshold {threshold:.2f}: {errors} of {total} on the wrong side")


if __name__ == "__main__":
    main()
