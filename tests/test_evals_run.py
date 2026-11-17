"""The eval runner (evals/run.py): the prompt override, measured before the config switches to it
(plan Task 19.4), and the `ci` gate (step 20, spec §8)."""

import json

from evals.run import ci_run, parse_args
from src.rag.config import load_config
from tests.test_evals_answers import CFG, ScriptLLM, index, item
from tests.test_evals_score import ScriptJudge


def test_prompt_override_changes_only_the_prompt_version():
    command, cfg = parse_args(["answers", "--prompt", "v2"])

    assert command == "answers"
    assert cfg.prompt_version == "v2"
    assert cfg.k == 5  # everything else comes from config/rag.yaml


def test_no_override_keeps_the_config():
    _, cfg = parse_args(["score"])

    assert cfg == load_config()


# --- `ci` (step 20, spec §8): cached answers and verdicts, score, thresholds, an exit code ---


def _ci(tmp_path, *, live, thresholds=None, recall=1.0, max_misses=30):
    return ci_run(
        [item(1, ["wa-reliability#0000"])],
        index(),
        ScriptLLM(),
        ScriptJudge(),
        CFG,
        lambda chunk_id: "text",
        recall,
        thresholds or {"judge_pass_rate_min": 0.75, "retrieval_recall_at_5_min": 0.95},
        live=live,
        answer_cache=tmp_path / "answers.jsonl",
        judge_cache=tmp_path / "judge.jsonl",
        out=tmp_path / "ci.json",
        max_misses=max_misses,
    )


def test_ci_fails_on_stale_cache(tmp_path, capsys):
    """No key and an empty cache: exit 1 with what to do, and no call is made."""
    assert _ci(tmp_path, live=False) == 1
    assert "cache is stale" in capsys.readouterr().out


def test_ci_passes_on_a_warm_cache_without_a_key(tmp_path, capsys):
    assert _ci(tmp_path, live=True) == 0  # fills the caches: 1 answer + 2 verdicts
    assert _ci(tmp_path, live=False) == 0  # replays them, as CI does
    out = capsys.readouterr().out
    assert "0 new calls" in out
    report = json.loads((tmp_path / "ci.json").read_text())
    assert report["failures"] == [] and report["new_calls"] == 0


def test_ci_fails_on_a_broken_threshold(tmp_path, capsys):
    assert _ci(tmp_path, live=True, recall=0.9) == 1
    assert "retrieval_recall_at_5 0.90 < 0.95" in capsys.readouterr().out


def test_ci_cost_guard_counts_answers_and_verdicts_together(tmp_path, capsys):
    """1 answer + 2 verdicts are 3 new calls: a guard of 2 stops the run before the third."""
    assert _ci(tmp_path, live=True, max_misses=2) == 1
    assert "cost guard" in capsys.readouterr().out
