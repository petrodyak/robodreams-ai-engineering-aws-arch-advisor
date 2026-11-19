"""The eval runner (evals/run.py): the prompt override, measured before the config switches to it
(plan Task 19.4), and the `ci` gate (step 20, spec §8)."""

import json

from evals.run import ci_recall, ci_run, heldout_run, parse_args
from evals.testset import TestItem
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
    report = json.loads((tmp_path / "ci.json").read_text())  # the artifact says why
    assert "cache is stale" in report["failures"][0]


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


def test_ci_recall_is_recall_at_5_of_the_answer_index():
    """CI gates recall@5 of hybrid_rerank on the index the answers use (no second index)."""
    items = [item(1, ["wa-reliability#0000"]), item(2, ["missing#0000"])]

    assert ci_recall(items, index(), CFG) == 0.5  # missing#0000 is in no corpus


# --- `heldout` (patch 20.7, F32): no-answer questions the prompt was not written on ---


class RefuseSecond(ScriptLLM):
    """Answers the first question and refuses the second."""

    def complete_json(self, system, user, schema):
        result = super().complete_json(system, user, schema)
        if self.calls == 2:
            result = result.model_copy(
                update={"text": json.dumps({"found": False, "claims": []})}
            )
        return result


def _none(i: int, question: str) -> TestItem:
    return TestItem(
        id=f"held{i:02d}",
        question=question,
        kind="no_answer",
        expected_answer="Not in the corpus.",
        key_facts=[],
        expected_sources=[],
        relevant_chunk_ids=[],
        answerable=False,
        verified_by="Petro",
        verified_on="2026-11-19",
    )


def test_heldout_counts_refusals_and_names_the_answered(tmp_path):
    items = [_none(1, "REL09-BP01 backup data"), _none(2, "REL09-BP02 secure backups")]
    kwargs = {"cache_path": tmp_path / "heldout.jsonl", "out_dir": tmp_path}

    first = heldout_run(items, index(), RefuseSecond(), CFG, **kwargs)

    assert (first["abstained"], first["items"]) == (1, 2)
    assert first["abstain_accuracy"] == 0.5
    assert first["answered_ids"] == ["held01"]
    assert first["new_calls"] == 2
    rows = (tmp_path / f"heldout__{first['run_id']}.jsonl").read_text().splitlines()
    assert [json.loads(r)["id"] for r in rows] == ["held01", "held02"]

    replay = heldout_run(items, index(), ScriptLLM(), CFG, **kwargs)  # from the cache
    assert replay["new_calls"] == 0
    assert replay["answered_ids"] == ["held01"]
