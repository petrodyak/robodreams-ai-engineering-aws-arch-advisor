"""The two LLM judges (evals/judge.py, spec §7), with a fake LLM behind the real eval cache."""

import json

from evals.cache import CachedLLM, EvalCache
from evals.judge import FaithVerdict, Verdict, judge_correctness, judge_faithfulness
from src.rag.llm import LLMResult
from tests.test_evals_scorers import item, record


class FakeJudge:
    model = "claude-sonnet-5-5"
    effort = "medium"

    def __init__(self, reply: dict):
        self.reply = reply
        self.calls = []

    def complete_json(self, system, user, schema):
        self.calls.append((system, user, schema))
        return LLMResult(
            text=json.dumps(self.reply),
            stop_reason="end_turn",
            input_tokens=900,
            output_tokens=120,
            latency_ms=10,
            attempts=1,
            cost_usd=0.003,
        )


def test_judge_parses_and_caches(tmp_path):
    fake = FakeJudge({"passed": True, "reason": "states the RPO"})
    llm = CachedLLM(fake, EvalCache(tmp_path / "judge.jsonl", live=True))

    first = judge_correctness(item(), record(), llm)
    second = judge_correctness(item(), record(), llm)

    assert first == second == Verdict(passed=True, reason="states the RPO")
    assert len(fake.calls) == 1
    system, user, _ = fake.calls[0]
    assert "reference answer decides" in system
    assert "question one01" in user and "Set an rpo" in user
    assert "Reference answer: x" in user


def test_correctness_skips_no_answer_items_and_not_found_answers():
    fake = FakeJudge({"passed": True, "reason": "x"})

    assert judge_correctness(item("none01", kind="no_answer"), record(), fake) is None
    assert judge_correctness(item(), record(found=False), fake) is None
    assert fake.calls == []


def test_faithfulness_score():
    fake = FakeJudge({"supported": [True, False, True]})
    rec = record()
    rec.claims = rec.claims * 3

    verdict = judge_faithfulness(rec, lambda chunk_id: f"text of {chunk_id}", fake)

    assert verdict.supported == [True, False, True]
    assert verdict.score == 2 / 3
    _, user, _ = fake.calls[0]
    assert "text of wa-reliability#0188" in user and "Claim 3" in user


def test_faithfulness_length_mismatch_has_no_score():
    fake = FakeJudge({"supported": [True]})
    rec = record()
    rec.claims = rec.claims * 2

    verdict = judge_faithfulness(rec, lambda chunk_id: "t", fake)

    assert verdict == FaithVerdict(supported=[True], score=None)


def test_no_claims_no_call():
    fake = FakeJudge({"supported": []})

    assert judge_faithfulness(record(found=False), lambda c: "t", fake) is None
    assert fake.calls == []
