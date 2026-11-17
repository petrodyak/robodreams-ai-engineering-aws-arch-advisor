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

    # k5 has an answer: judged (pass vs human fail); k3 is not found: no correctness verdict
    assert out["correctness"]["n"] == 1
    assert out["disagreements"]["correctness"] == ["one01@k5"]
