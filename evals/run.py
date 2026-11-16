"""Eval runner: `python -m evals.run <command>`.

- `retrieval` (step 17, spec §5): the labelled answerable items through the five search
  configurations -> evals/results/retrieval.json. Models run locally (fastembed): no cost.
- `estimate` (step 18): the input tokens of every answer request from the free count_tokens
  endpoint, and the dollars for one run and for the k sweep. Run it before paying.
- `answers` (`make eval`, step 18): every testset item through `answer`, behind the eval cache
  (ADR-0008) -> evals/results/<run_id>.jsonl and <run_id>.summary.json.
- `sweep` (step 18): the answer run for k = 3 / 5 / 8 -> evals/results/sweep.json.
"""

import argparse
import json
import sys
from pathlib import Path

from evals.answers import run_id, run_items, summarize, sweep_budget
from evals.cache import CachedLLM, EvalCache
from evals.retrieval import evaluate_retrieval, relevant_fixed_ids
from evals.testset import TestItem, load_testset
from src.rag.config import load_config
from src.rag.index import Index, default_embed_fn, default_rerank_fn, load_chunks
from src.rag.search import search

CHUNKS = Path("data/rag/chunks.jsonl")
CHUNKS_FIXED = Path("data/rag/chunks_fixed.jsonl")
TESTSET = Path("evals/testset.jsonl")
RESULTS = Path("evals/results/retrieval.json")
RESULTS_DIR = Path("evals/results")
ANSWER_CACHE = Path("evals/cache/answers.jsonl")
SWEEP_K = [3, 5, 8]
# For `estimate` only: output tokens per answer (adaptive thinking at medium effort + the JSON).
# The live run replaces this guess with `usage`.
OUTPUT_TOKENS_GUESS = 1000
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


def _answer_setup():
    from dotenv import load_dotenv

    from src.rag.llm import ClaudeJSON

    load_dotenv()  # ANTHROPIC_API_KEY
    cfg = load_config()
    items = load_testset(TESTSET)
    index = Index(
        load_chunks(CHUNKS),
        embed_fn=default_embed_fn(cfg.embed_model),
        rerank_fn=default_rerank_fn(cfg.rerank_model),
    )
    llm = ClaudeJSON(cfg.answer_model, cfg.answer_effort, cfg.answer_max_tokens)
    return cfg, items, index, llm


def estimate() -> None:
    """Input tokens from count_tokens (free) for k = 3 / 5 / 8; output is OUTPUT_TOKENS_GUESS."""
    from src.rag.answer import answer_schema, prepare
    from src.rag.llm import cost_usd

    cfg, items, index, llm = _answer_setup()
    schema = answer_schema()
    total = 0.0
    print(
        f"{len(items)} items, model {llm.model}, output guess {OUTPUT_TOKENS_GUESS}/answer"
    )
    for k in SWEEP_K:
        budget = sweep_budget(k, cfg.context_budget)
        tokens = [
            llm.count_input_tokens(p.prompt.system, p.user, schema)
            for p in (
                prepare(it.question, index, cfg, k=k, budget=budget) for it in items
            )
            if p.sources
        ]
        usd = cost_usd(llm.model, sum(tokens), OUTPUT_TOKENS_GUESS * len(tokens))
        total += usd
        print(
            f"k={k} budget={budget}: {len(tokens)} calls, {sum(tokens)} input tokens "
            f"(avg {sum(tokens) / max(len(tokens), 1):.0f}), ${usd:.4f}"
        )
    print(f"sweep total (k=5 is the make eval run): ${total:.4f}")


def _answer_run(cfg, items, index, llm, k: int) -> dict:
    rid = run_id(llm.model, cfg.prompt_version, llm.effort, k)
    cache = EvalCache(ANSWER_CACHE, live=True)
    rows = run_items(
        items,
        index,
        CachedLLM(llm, cache),
        cfg,
        k=k,
        budget=sweep_budget(k, cfg.context_budget),
    )
    summary = {
        "run_id": rid,
        "k": k,
        "new_calls": cache.misses,
        **summarize(rows, items),
    }
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    lines = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    (RESULTS_DIR / f"{rid}.jsonl").write_text(lines, encoding="utf-8")
    (RESULTS_DIR / f"{rid}.summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def _print_summary(s: dict) -> None:
    print(
        f"{s['run_id']}: found {s['found']}/{s['items']}, context recall "
        f"{s['context_recall']:.2f}, citation recall {s['citation_recall']:.2f}, "
        f"dropped labels {s['dropped_labels']}, uncited claims {s['uncited_claims']}, "
        f"avg in/out {s['avg_input_tokens']:.0f}/{s['avg_output_tokens']:.0f}, "
        f"${s['cost_usd']:.4f} (${s['usd_per_1000']:.2f} per 1,000), "
        f"new calls {s['new_calls']}, not found: {' '.join(s['not_found_ids']) or '-'}"
    )


def answers() -> None:
    cfg, items, index, llm = _answer_setup()
    _print_summary(_answer_run(cfg, items, index, llm, cfg.k))


def sweep() -> None:
    cfg, items, index, llm = _answer_setup()
    runs = [_answer_run(cfg, items, index, llm, k) for k in SWEEP_K]
    for s in runs:
        _print_summary(s)
    (RESULTS_DIR / "sweep.json").write_text(
        json.dumps(runs, indent=2) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("what", choices=["retrieval", "estimate", "answers", "sweep"])
    args = parser.parse_args()
    {"retrieval": retrieval, "estimate": estimate, "answers": answers, "sweep": sweep}[
        args.what
    ]()


if __name__ == "__main__":
    main()
