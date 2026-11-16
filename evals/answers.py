"""The answer run: every testset item through `answer`, one row each, and a summary (spec §6).

The summary needs no judge (that is step 19): it counts what code can check.
- found: answers that are not the not-found text;
- context_recall: answerable labelled items with a relevant chunk in the prompt;
- citation_recall: the same items whose answer cites a relevant chunk;
- the cost, from `usage` of every call (a cached call reports what it cost when it was made).
"""

from evals.testset import TestItem
from src.rag.answer import answer
from src.rag.config import RagConfig
from src.rag.index import Index

MAX_CHUNK_TOKENS = 480  # the hard maximum of a structure chunk (spec §4)


def run_id(model: str, prompt_version: str, effort: str, k: int) -> str:
    return f"{model}__{prompt_version}__{effort}__k{k}"


def sweep_budget(k: int, default_budget: int) -> int:
    """A context budget that holds k chunks of the hard maximum, never below the default."""
    return max(default_budget, k * MAX_CHUNK_TOKENS)


def run_items(
    items: list[TestItem], index: Index, llm, cfg: RagConfig, *, k: int, budget: int
) -> list[dict]:
    rows = []
    for it in items:
        record = answer(it.question, index, llm, cfg, k=k, budget=budget)
        rows.append({"id": it.id, **record.model_dump(mode="json")})
    return rows


def summarize(rows: list[dict], items: list[TestItem]) -> dict:
    by_id = {it.id: it for it in items}
    labelled = [
        r
        for r in rows
        if by_id[r["id"]].answerable and by_id[r["id"]].relevant_chunk_ids
    ]

    def share(hit) -> float:
        return sum(1 for r in labelled if hit(r)) / len(labelled) if labelled else 0.0

    def relevant(r) -> set[str]:
        return set(by_id[r["id"]].relevant_chunk_ids)

    def cited(r) -> set[str]:
        return {ref["chunk_id"] for c in r["claims"] for ref in c["refs"]}

    cost = sum(r["cost_usd"] for r in rows)
    called = [r for r in rows if r["stop_reason"] is not None]
    return {
        "items": len(rows),
        "found": sum(r["found"] for r in rows),
        "context_recall": share(lambda r: set(r["in_context"]) & relevant(r)),
        "citation_recall": share(lambda r: cited(r) & relevant(r)),
        "dropped_labels": sum(len(r["dropped_labels"]) for r in rows),
        "uncited_claims": sum(r["uncited_claims"] for r in rows),
        "stop_reasons": sorted({r["stop_reason"] for r in called}),
        "avg_input_tokens": (
            sum(r["input_tokens"] for r in called) / len(called) if called else 0.0
        ),
        "avg_output_tokens": (
            sum(r["output_tokens"] for r in called) / len(called) if called else 0.0
        ),
        "cost_usd": cost,
        "usd_per_1000": cost / len(rows) * 1000 if rows else 0.0,
        "not_found_ids": [r["id"] for r in rows if not r["found"]],
    }
