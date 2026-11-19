"""Eval runner: `python -m evals.run <command>`.

- `retrieval` (step 17, spec §5): the labelled answerable items through the five search
  configurations -> evals/results/retrieval.json. Models run locally (fastembed): no cost.
- `estimate` (step 18): the input tokens of every answer request from the free count_tokens
  endpoint, and the dollars for one run and for the k sweep. Run it before paying.
- `answers` (`make eval`, step 18): every testset item through `answer`, behind the eval cache
  (ADR-0008) -> evals/results/<run_id>.jsonl and <run_id>.summary.json.
- `sweep` (step 18): the answer run for k = 3 / 5 / 8 -> evals/results/sweep.json.
- `judge-estimate` (step 19): the judges' input tokens over the latest run, from count_tokens.
- `score` (step 19): scorers + judges over the latest run -> evals/results/<run_id>.json.
- `calibrate` (step 19): the judges on Petro's hand labels -> evals/results/calibration.json.
- `heldout` (`make eval-heldout`, patch 20.7, F32): the held-out no-answer questions of
  evals/testset_heldout.jsonl through `answer`, behind their own cache -> evals/results/heldout__*.
  Not part of the CI gate: the questions were written after prompt v2 and the thresholds.
- `ci` (`make eval-ci`, step 20, spec §8): recall@5 of hybrid_rerank, the answers and the verdicts
  behind the caches, the score, and the thresholds of config/eval_thresholds.yaml -> evals/results/ci/
  (not in Git: the workflow uploads it). Exit 1 on a broken threshold, a stale cache or the cost
  guard. A miss calls Claude only when ANTHROPIC_API_KEY is set (the repository secret in CI).
"""

import argparse
import json
import os
import sys
from pathlib import Path

from evals.answers import load_run, run_id, run_items, summarize, sweep_budget
from evals.cache import (
    MAX_MISSES,
    CachedLLM,
    CostGuardError,
    EvalCache,
    StaleCacheError,
)
from evals.calibration import load_calibration
from evals.judge import JUDGE_MAX_TOKENS
from evals.retrieval import evaluate_retrieval, relevant_fixed_ids
from evals.score import CostMeter, _records, calibrate, score_run
from evals.scorers import abstain_correct
from evals.testset import TestItem, load_testset
from evals.thresholds import check, load_thresholds
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
JUDGE_CACHE = Path("evals/cache/judge.jsonl")
CALIBRATION = Path("evals/labels/calibration.jsonl")
# For `judge-estimate` only: output tokens per judge call (thinking at medium + a short JSON).
JUDGE_OUTPUT_GUESS = 600
# Local cost guard of `score` / `calibrate`: one scored run is 2 judge calls per answer (42 for
# 24 items), above the CI guard of 30 (spec §8), which applies to `make eval-ci` in step 20.
LOCAL_JUDGE_MAX_MISSES = 100
DEPTH = 10  # recall@10 and MRR read the top 10
HELDOUT = Path("evals/testset_heldout.jsonl")
# Its own cache file: the CI gate replays answers.jsonl only, so held-out answers never touch it.
HELDOUT_CACHE = Path("evals/cache/heldout_answers.jsonl")
CI_DIR = RESULTS_DIR / "ci"  # gitignored; uploaded as the workflow artifact

# The config of this run: config/rag.yaml, with `--prompt` applied (set by main()).
_CFG = None


def _config():
    return _CFG if _CFG is not None else load_config()


def labelled(items: list[TestItem]) -> list[TestItem]:
    return [it for it in items if it.answerable and it.relevant_chunk_ids]


def _search_fn(index: Index, mode: str, cfg):
    """The chunk ids of the top DEPTH hits of one search configuration, for evaluate_retrieval."""

    def fn(query: str) -> list[str]:
        hits = search(
            index,
            query,
            k=DEPTH,
            mode=mode,
            candidates=cfg.candidates,
            rrf_k=cfg.rrf_k,
        )
        return [h.chunk.chunk_id for h in hits]

    return fn


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
        return _search_fn(idx, mode, cfg)

    def structure_labels(it: TestItem) -> set[str]:
        return set(it.relevant_chunk_ids)

    rows = {
        "vector (fixed chunks)": evaluate_retrieval(
            run(fixed_index, "vector"), items, lambda it: fixed_relevant[it.id]
        )
    }
    # the fixed windows' labels come from text overlap (several windows per labelled chunk), so
    # the share of them in the top k is not comparable with the structure rows and is not reported
    for key in ("relevant_share@5", "relevant_share@10"):
        del rows["vector (fixed chunks)"][key]
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
        f"\n{'config':<24}{'recall@5':>10}{'recall@10':>11}{'share@5':>9}{'MRR':>7}{'ms/q':>8}   misses"
    )
    for name, r in rows.items():
        misses = " ".join(r["misses"]) or "-"
        share = f"{r['relevant_share@5']:.2f}" if "relevant_share@5" in r else "-"
        print(
            f"{name:<24}{r['recall@5']:>10.2f}{r['recall@10']:>11.2f}"
            f"{share:>9}{r['mrr']:>7.2f}{r['ms']:>8.0f}   {misses}"
        )
    print(f"\nwritten {RESULTS}")
    return result


def _answer_setup():
    from dotenv import load_dotenv

    from src.rag.llm import ClaudeJSON

    load_dotenv()  # ANTHROPIC_API_KEY
    cfg = _config()
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


def _judge_env():
    """The testset, the chunk texts and the judge; no answer run is read here."""
    from dotenv import load_dotenv

    from src.rag.llm import ClaudeJSON

    load_dotenv()  # ANTHROPIC_API_KEY
    cfg = _config()
    items = load_testset(TESTSET)
    texts = {c.chunk_id: c.text for c in load_chunks(CHUNKS)}
    judge = ClaudeJSON(cfg.judge_model, cfg.judge_effort, JUDGE_MAX_TOKENS)
    return cfg, items, texts, judge


def _judge_setup():
    """The judge environment plus the config's answer run (`score`, `judge-estimate`)."""
    cfg, items, texts, judge = _judge_env()
    rid = run_id(cfg.answer_model, cfg.prompt_version, cfg.answer_effort, cfg.k)
    rows = load_run(RESULTS_DIR / f"{rid}.jsonl", items)
    return cfg, items, rid, rows, texts, judge


class _CountOnly:
    """Stands in for the judge in `judge-estimate`: counts each request's input tokens, sends nothing."""

    def __init__(self, llm):
        self.llm, self.model, self.effort = llm, llm.model, llm.effort
        self.tokens, self.calls = 0, 0

    def complete_json(self, system, user, schema):
        from src.rag.llm import LLMResult

        self.tokens += self.llm.count_input_tokens(system, user, schema)
        self.calls += 1
        return LLMResult(
            text=None,
            stop_reason="count_only",
            input_tokens=0,
            output_tokens=0,
            latency_ms=0,
            attempts=0,
            cost_usd=0.0,
        )


def judge_estimate() -> None:
    from src.rag.llm import cost_usd

    _, items, rid, rows, texts, judge = _judge_setup()
    counter = _CountOnly(judge)
    score_run(items, rows, counter, texts.__getitem__)
    usd = cost_usd(judge.model, counter.tokens, JUDGE_OUTPUT_GUESS * counter.calls)
    print(
        f"{rid}: {counter.calls} judge calls on {judge.model}, {counter.tokens} input tokens "
        f"(avg {counter.tokens / max(counter.calls, 1):.0f}), output guess "
        f"{JUDGE_OUTPUT_GUESS}/call: ${usd:.4f}"
    )


def score() -> None:
    _, items, rid, rows, texts, judge = _judge_setup()
    cache = EvalCache(JUDGE_CACHE, live=True, max_misses=LOCAL_JUDGE_MAX_MISSES)
    meter = CostMeter(CachedLLM(judge, cache))
    result = {"run_id": rid, "new_judge_calls": cache.misses}
    result.update(score_run(items, rows, meter, texts.__getitem__))
    result["new_judge_calls"] = cache.misses
    (RESULTS_DIR / f"{rid}.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    m = result["metrics"]
    print(f"{rid}: {len(items)} items, {cache.misses} new judge calls")
    for key in (
        "abstain_accuracy",
        "false_abstain_rate",
        "source_hit",
        "key_facts",
        "citations_valid",
        "retrieved",
        "in_context",
        "context_share",
        "judge_pass_rate",
        "faithfulness",
    ):
        value = m[key]
        print(f"  {key:<20}{'-' if value is None else f'{value:.2f}'}")
    print(f"  failed (scorers)    {' '.join(m['failed']) or '-'}")
    print(f"  failed (judge)      {' '.join(m['judge_failed']) or '-'}")
    c = result["cost"]
    print(
        f"  cost: answers ${c['answers_usd']:.4f} (${c['answers_usd_per_1000']:.2f} per 1,000), "
        f"judges ${c['judge_usd']:.4f} new (${c['judge_usd_all_verdicts']:.4f} for all verdicts)"
    )


def calibrate_judges() -> None:
    """The judges on the hand-labelled answers; each label is read from its own run, so the
    config's run is not needed (it may be a newer prompt version)."""
    _, items, texts, judge = _judge_env()
    labels = [r for r in load_calibration(CALIBRATION) if r.human_pass is not None]
    if not labels:
        sys.exit(f"no hand labels in {CALIBRATION}")
    runs = {
        rid: load_run(RESULTS_DIR / f"{rid}.jsonl", items)
        for rid in sorted({r.run_id for r in labels})
    }
    cache = EvalCache(JUDGE_CACHE, live=True, max_misses=LOCAL_JUDGE_MAX_MISSES)
    out = calibrate(labels, items, runs, CachedLLM(judge, cache), texts.__getitem__)
    out["runs"] = sorted({r.run_id for r in labels})
    out["new_judge_calls"] = cache.misses
    (RESULTS_DIR / "calibration.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="utf-8"
    )
    for name in ("correctness", "faithfulness"):
        j = out[name]
        print(
            f"{name:<13} n={j['n']:<3} agreement {j['agreement']:.2f}  kappa {j['kappa']:.2f}  "
            f"differ: {' '.join(out['disagreements'][name]) or '-'}"
        )


def ci_run(
    items: list[TestItem],
    index: Index,
    answer_llm,
    judge_llm,
    cfg,
    chunk_text,
    recall_at_5: float,
    thresholds: dict[str, float],
    *,
    live: bool,
    answer_cache: Path = ANSWER_CACHE,
    judge_cache: Path = JUDGE_CACHE,
    out: Path = CI_DIR / "ci.json",
    max_misses: int = MAX_MISSES,
) -> int:
    """The CI gate after the retrieval eval: answers and verdicts behind the caches, the score and
    the thresholds. Prints the reason and returns the exit code (0 pass, 1 fail).

    The cost guard counts answers and verdicts together (spec §8: more than 30 misses in one CI
    run), so the judges get what the answers left of `max_misses`.
    """
    answers = EvalCache(answer_cache, live=live, max_misses=max_misses)
    verdicts = None
    try:
        rows = run_items(
            items,
            index,
            CachedLLM(answer_llm, answers),
            cfg,
            k=cfg.k,
            budget=sweep_budget(cfg.k, cfg.context_budget),
        )
        verdicts = EvalCache(
            judge_cache, live=live, max_misses=max_misses - answers.misses
        )
        result = score_run(
            items, rows, CostMeter(CachedLLM(judge_llm, verdicts)), chunk_text
        )
    except (StaleCacheError, CostGuardError) as e:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps({"failures": [str(e)], "new_calls": None}, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"eval-ci FAILED: {e}")
        return 1
    new_calls = answers.misses + verdicts.misses
    metrics = {**result["metrics"], "retrieval_recall_at_5": recall_at_5}
    failures = check(metrics, thresholds)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(
            {
                "run_id": run_id(
                    answer_llm.model, cfg.prompt_version, answer_llm.effort, cfg.k
                ),
                "new_calls": new_calls,
                "thresholds": thresholds,
                "failures": failures,
                "metrics": metrics,
                "cost": result["cost"],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"eval-ci: {len(items)} items, {new_calls} new calls (live={live})")
    for key, limit in thresholds.items():
        name = key[:-4]
        value = metrics.get(name)
        shown = "-" if value is None else f"{value:.2f}"
        sign = ">=" if key.endswith("_min") else "<="
        print(f"  {name:<24}{shown:>6}  {sign} {limit:.2f}")
    if failures:
        print("eval-ci FAILED: " + "; ".join(failures))
        return 1
    print("eval-ci passed")
    return 0


def heldout_run(
    items: list[TestItem],
    index: Index,
    llm,
    cfg,
    *,
    cache_path: Path = HELDOUT_CACHE,
    out_dir: Path = RESULTS_DIR,
) -> dict:
    """The held-out no-answer questions through `answer` (F32).

    The four `none` items of the testset are the ones rule 5 of prompt v2 was written on, so their
    4 / 4 says little. These questions were written after the prompt and the thresholds were fixed
    and neither is edited on their result. A correct answer is a refusal, which code checks
    (`abstain_correct`): no judge is called.
    """
    answerable = [it.id for it in items if it.answerable]
    if answerable:
        sys.exit(f"{HELDOUT} holds no-answer items only, not {answerable}")
    rid = run_id(llm.model, cfg.prompt_version, llm.effort, cfg.k)
    cache = EvalCache(cache_path, live=True)
    rows = run_items(
        items,
        index,
        CachedLLM(llm, cache),
        cfg,
        k=cfg.k,
        budget=sweep_budget(cfg.k, cfg.context_budget),
    )
    recs = _records(rows)
    answered = [it.id for it in items if not abstain_correct(it, recs[it.id])]
    summary = {
        "run_id": rid,
        "items": len(items),
        "abstained": len(items) - len(answered),
        "abstain_accuracy": (len(items) - len(answered)) / len(items),
        "answered_ids": answered,
        "new_calls": cache.misses,
        "cost_usd": sum(r["cost_usd"] for r in rows),
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    lines = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    (out_dir / f"heldout__{rid}.jsonl").write_text(lines, encoding="utf-8")
    (out_dir / f"heldout__{rid}.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def heldout() -> None:
    cfg, _, index, llm = _answer_setup()
    s = heldout_run(load_testset(HELDOUT), index, llm, cfg)
    print(
        f'heldout {s["run_id"]}: right "I don\'t know" {s["abstained"]}/{s["items"]}, '
        f"answered instead: {' '.join(s['answered_ids']) or '-'}, "
        f"new calls {s['new_calls']}, ${s['cost_usd']:.4f}"
    )


def ci_recall(items: list[TestItem], index: Index, cfg) -> float:
    """recall@5 of hybrid_rerank over the labelled items, on the index the answers use.

    The gated retrieval metric only: the five-configuration table (with the fixed-chunk index)
    is `make retrieval-eval`. Embedding the fixed chunks too doubled a cold CI run.
    """
    return evaluate_retrieval(
        _search_fn(index, "hybrid_rerank", cfg),
        labelled(items),
        lambda it: set(it.relevant_chunk_ids),
    )["recall@5"]


def ci() -> None:
    from dotenv import load_dotenv

    load_dotenv()  # a local .env key counts as the CI secret
    live = bool(os.environ.get("ANTHROPIC_API_KEY"))
    print("eval-ci: building the index (a cold .cache/ embeds every chunk first)")
    cfg, items, index, llm = _answer_setup()
    recall = ci_recall(items, index, cfg)
    print(f"eval-ci: retrieval recall@5 {recall:.2f}; answers and verdicts next")
    _, _, texts, judge = _judge_env()
    sys.exit(
        ci_run(
            items,
            index,
            llm,
            judge,
            cfg,
            texts.__getitem__,
            recall,
            load_thresholds(),
            live=live,
        )
    )


COMMANDS = (
    "retrieval",
    "estimate",
    "answers",
    "sweep",
    "judge-estimate",
    "score",
    "calibrate",
    "heldout",
    "ci",
)


def parse_args(argv: list[str] | None = None):
    """The command and its config. `--prompt v2` measures a prompt version without editing
    config/rag.yaml, which switches only when the version is not worse (plan Task 19.4)."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("what", choices=COMMANDS)
    parser.add_argument(
        "--prompt", help="prompt version, e.g. v2 (default: the config's)"
    )
    args = parser.parse_args(argv)
    cfg = load_config()
    if args.prompt:
        cfg = cfg.model_copy(update={"prompt_version": args.prompt})
    return args.what, cfg


def main() -> None:
    global _CFG
    commands = {
        "retrieval": retrieval,
        "estimate": estimate,
        "answers": answers,
        "sweep": sweep,
        "judge-estimate": judge_estimate,
        "score": score,
        "calibrate": calibrate_judges,
        "heldout": heldout,
        "ci": ci,
    }
    what, _CFG = parse_args()
    commands[what]()


if __name__ == "__main__":
    main()
