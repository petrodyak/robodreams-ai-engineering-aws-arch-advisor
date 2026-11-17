"""The CI thresholds (evals/thresholds.py, spec §8): one message per broken threshold."""

from pathlib import Path

from evals.thresholds import check, load_thresholds

GATED = {
    "retrieval_recall_at_5_min",
    "abstain_accuracy_min",
    "false_abstain_rate_max",
    "source_hit_min",
    "faithfulness_min",
    "judge_pass_rate_min",
}


def test_check_min_and_max():
    thresholds = {"faithfulness_min": 0.90, "false_abstain_rate_max": 0.05}

    assert check({"faithfulness": 0.90, "false_abstain_rate": 0.05}, thresholds) == []
    assert check({"faithfulness": 0.71, "false_abstain_rate": 0.0}, thresholds) == [
        "faithfulness 0.71 < 0.90"
    ]
    assert check({"faithfulness": 0.95, "false_abstain_rate": 0.10}, thresholds) == [
        "false_abstain_rate 0.10 > 0.05"
    ]


def test_an_equal_value_passes_despite_float_noise():
    # 15 of 20 judged answers: 0.75 must pass a 0.75 threshold however the mean was summed
    assert check({"judge_pass_rate": 0.1 * 7.5}, {"judge_pass_rate_min": 0.75}) == []


def test_a_missing_or_empty_metric_fails():
    thresholds = {"faithfulness_min": 0.90, "source_hit_min": 0.95}

    assert check({"faithfulness": None}, thresholds) == [
        "faithfulness has no value",
        "source_hit has no value",
    ]


def test_the_config_gates_the_six_metrics_of_spec_8():
    thresholds = load_thresholds(Path("config/eval_thresholds.yaml"))

    assert set(thresholds) == GATED
    assert all(0.0 <= v <= 1.0 for v in thresholds.values())
