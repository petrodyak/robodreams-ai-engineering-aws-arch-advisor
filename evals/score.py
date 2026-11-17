"""Scoring an answer run and calibrating the judges against Petro's labels (spec §7, §8).

- `score_run`: the deterministic scorers over every item, plus the two judges: correctness on
  answerable items with an answer (a not-found answer counts as a fail of `judge_pass_rate`),
  faithfulness on every answer with claims. Every gated metric of spec §8 except retrieval
  recall@5, which `evals.run retrieval` measures.
- `calibrate`: the judges on the hand-labelled answers, each from its own run; agreement and Cohen's kappa per judge, and
  the items where judge and human differ (the input of a judge prompt v2).
"""

from collections.abc import Callable

from evals.calibration import CalibrationRow, agreement, cohens_kappa
from evals.judge import judge_correctness, judge_faithfulness
from evals.scorers import aggregate
from evals.testset import TestItem
from src.rag.answer import AnswerRecord
from src.rag.llm import LLMResult


class CostMeter:
    """Wraps a judge LLM and adds up what its calls cost (cache hits report their original cost)."""

    def __init__(self, llm):
        self.llm = llm
        self.model = llm.model
        self.effort = llm.effort
        self.calls = 0
        self.cost_usd = 0.0

    def complete_json(self, system: str, user: str, schema: dict) -> LLMResult:
        result = self.llm.complete_json(system, user, schema)
        self.calls += 1
        self.cost_usd += result.cost_usd
        return result


def _records(rows: list[dict]) -> dict[str, AnswerRecord]:
    return {
        r["id"]: AnswerRecord.model_validate({k: v for k, v in r.items() if k != "id"})
        for r in rows
    }


def score_run(
    items: list[TestItem], rows: list[dict], judge_llm, chunk_text: Callable[[str], str]
) -> dict:
    recs = _records(rows)
    ordered = [recs[it.id] for it in items]
    per_item, judged, faith = {}, [], []
    for it, rec in zip(items, ordered):
        verdict = judge_correctness(it, rec, judge_llm)
        fv = judge_faithfulness(rec, chunk_text, judge_llm)
        if it.answerable:
            judged.append(bool(verdict and verdict.passed))
        if fv is not None and fv.score is not None:
            faith.append(fv.score)
        per_item[it.id] = {
            "judge": verdict.model_dump() if verdict else None,
            "faithfulness": fv.model_dump() if fv else None,
        }
    metrics = aggregate(items, ordered)
    metrics["judge_pass_rate"] = sum(judged) / len(judged) if judged else None
    metrics["faithfulness"] = sum(faith) / len(faith) if faith else None
    metrics["judge_failed"] = [
        it.id
        for it in items
        if it.answerable and not (per_item[it.id]["judge"] or {}).get("passed")
    ]
    answers_usd = sum(r.cost_usd for r in ordered)
    return {
        "metrics": metrics,
        "items": per_item,
        "cost": {
            "answers_usd": answers_usd,
            "judge_usd": judge_llm.cost_usd if hasattr(judge_llm, "cost_usd") else None,
            "answers_usd_per_1000": answers_usd / len(ordered) * 1000
            if ordered
            else 0.0,
        },
    }


def calibrate(
    labels: list[CalibrationRow],
    items: list[TestItem],
    runs: dict[str, list[dict]],
    judge_llm,
    chunk_text: Callable[[str], str],
) -> dict:
    """`runs` maps a run id to its answer rows; each label is judged against the answer of its own run,
    so one item can be labelled in two runs. Disagreements are named `<item>@<run>`."""
    by_id = {it.id: it for it in items}
    recs = {rid: _records(rows) for rid, rows in runs.items()}
    pairs = {"correctness": [], "faithfulness": []}
    differ = {"correctness": [], "faithfulness": []}
    for row in labels:
        it, rec = by_id[row.item_id], recs[row.run_id][row.item_id]
        name = f"{row.item_id}@{row.run_id}"
        verdict = judge_correctness(it, rec, judge_llm)
        if row.human_pass is not None and verdict is not None:
            pairs["correctness"].append((row.human_pass, verdict.passed))
            if row.human_pass != verdict.passed:
                differ["correctness"].append(name)
        fv = judge_faithfulness(rec, chunk_text, judge_llm)
        if row.human_unsupported is not None and fv is not None and fv.supported:
            judge_unsupported = not all(fv.supported)
            pairs["faithfulness"].append((row.human_unsupported, judge_unsupported))
            if row.human_unsupported != judge_unsupported:
                differ["faithfulness"].append(name)
    out = {
        name: {
            "n": len(p),
            "agreement": agreement(p) if p else None,
            "kappa": cohens_kappa(p) if p else None,
        }
        for name, p in pairs.items()
    }
    out["disagreements"] = differ
    return out
