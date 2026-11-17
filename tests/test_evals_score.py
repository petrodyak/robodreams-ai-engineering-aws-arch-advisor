"""Scoring a run and calibrating the judges (evals/score.py), with a fake judge."""

import json

import pytest

from evals.calibration import CalibrationRow
from evals.score import CostMeter, calibrate, score_run
from src.rag.llm import LLMResult
from tests.test_evals_scorers import item, record


class ScriptJudge:
    """Correctness: passes; faithfulness: the first claim supported, the rest not."""

    model = "claude-sonnet-5-5"
    effort = "medium"

    def complete_json(self, system, user, schema):
        if "supported" in json.dumps(schema):
            n = int(user.split("The answer has ")[1].split(" ")[0])
            reply = {"supported": [True] + [False] * (n - 1)}
        else:
            reply = {"passed": True, "reason": "ok"}
        return LLMResult(
            text=json.dumps(reply),
            stop_reason="end_turn",
            input_tokens=1000,
            output_tokens=100,
            latency_ms=1,
            attempts=1,
            cost_usd=0.003,
        )


def rows_for(items, recs):
    return [{"id": it.id, **r.model_dump(mode="json")} for it, r in zip(items, recs)]


def test_score_run():
    items = [item("one01"), item("one02"), item("none01", kind="no_answer")]
    recs = [
        record("question one01"),
        record("question one02", found=False),
        record("question none01", found=False),
    ]
    meter = CostMeter(ScriptJudge())

    result = score_run(items, rows_for(items, recs), meter, lambda c: "text")

    m = result["metrics"]
    assert m["judge_pass_rate"] == pytest.approx(0.5)  # one02 abstained: a fail
    assert m["faithfulness"] == 1.0  # one claim, supported
    assert m["false_abstain_rate"] == pytest.approx(0.5)
    assert m["abstain_accuracy"] == 1.0
    assert result["items"]["one01"]["judge"] == {"passed": True, "reason": "ok"}
    assert result["items"]["one02"]["judge"] is None
    assert meter.calls == 2 and meter.cost_usd == pytest.approx(0.006)
    assert result["cost"]["judge_usd"] == pytest.approx(0.006)
    assert result["cost"]["answers_usd"] == pytest.approx(0.0006)


def test_calibrate():
    items = [item("one01"), item("one02")]
    recs = [record("question one01"), record("question one02")]
    labels = [
        CalibrationRow(
            item_id="one01",
            run_id="r",
            human_pass=True,
            human_unsupported=False,
            labelled_on="2026-11-17",
        ),
        CalibrationRow(
            item_id="one02",
            run_id="r",
            human_pass=False,
            human_unsupported=True,
            labelled_on="2026-11-17",
        ),
    ]

    out = calibrate(
        labels, items, {"r": rows_for(items, recs)}, ScriptJudge(), lambda c: "t"
    )

    assert out["correctness"]["n"] == 2
    assert out["correctness"]["agreement"] == pytest.approx(0.5)  # judge passes both
    assert out["faithfulness"]["agreement"] == pytest.approx(0.5)  # judge supports both
    assert out["disagreements"]["correctness"] == ["one02@r"]


def test_calibrate_reads_each_label_from_its_own_run():
    """The same item labelled in two runs: each label is judged against that run's answer."""
    items = [item("one01")]
    runs = {
        "k5": rows_for(items, [record("question one01")]),
        "k3": rows_for(items, [record("question one01", found=False)]),
    }
    labels = [
        CalibrationRow(
            item_id="one01",
            run_id=run,
            human_pass=False,
            human_unsupported=False,
            labelled_on="2026-11-17",
        )
        for run in ("k5", "k3")
    ]

    out = calibrate(labels, items, runs, ScriptJudge(), lambda c: "t")

    # k5 has an answer: judged (pass vs human fail); k3 is not found: a fail without a call
    assert out["correctness"]["n"] == 2
    assert out["disagreements"]["correctness"] == ["one01@k5"]


class ShortFaithJudge(ScriptJudge):
    """Faithfulness: one value whatever the number of claims."""

    def complete_json(self, system, user, schema):
        if "supported" in json.dumps(schema):
            return LLMResult(
                text=json.dumps({"supported": [True]}),
                stop_reason="end_turn",
                input_tokens=1,
                output_tokens=1,
                latency_ms=1,
                attempts=1,
                cost_usd=0.0,
            )
        return super().complete_json(system, user, schema)


def label(item_id, human_pass, human_unsupported=False, run="r"):
    return CalibrationRow(
        item_id=item_id,
        run_id=run,
        human_pass=human_pass,
        human_unsupported=human_unsupported,
        labelled_on="2026-11-17",
    )


def test_calibrate_skips_a_faithfulness_verdict_of_the_wrong_length():
    items = [item("one01")]
    rec = record("question one01")
    rec.claims = rec.claims * 3  # three claims, the judge returns one value

    out = calibrate(
        [label("one01", True)],
        items,
        {"r": rows_for(items, [rec])},
        ShortFaithJudge(),
        str,
    )

    assert out["faithfulness"]["n"] == 0
    assert out["correctness"]["n"] == 1


def test_calibrate_counts_a_not_found_answer_as_a_judge_fail():
    """A false abstain fails without a judge call, as in score_run; the human fail is kept."""
    items = [item("one01")]
    rows = rows_for(items, [record("question one01", found=False)])

    out = calibrate([label("one01", False)], items, {"r": rows}, ScriptJudge(), str)

    assert out["correctness"]["n"] == 1
    assert out["correctness"]["agreement"] == 1.0


def test_cost_meter_separates_new_spend_from_cached_calls(tmp_path):
    from evals.cache import CachedLLM, EvalCache

    meter = CostMeter(
        CachedLLM(ScriptJudge(), EvalCache(tmp_path / "j.jsonl", live=True))
    )

    meter.complete_json("s", "u", {"x": 1})
    meter.complete_json("s", "u", {"x": 1})  # the same request: a cache hit

    assert meter.calls == 2
    assert meter.cost_usd == pytest.approx(0.006)  # what the 2 verdicts cost when made
    assert meter.new_cost_usd == pytest.approx(0.003)  # what this run spent
