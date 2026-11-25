"""Feedback: /up, /down, /reject, and rejections attached to the architecture (spec §6.1, §11)."""

import json
from pathlib import Path

from src.agent.config import load_agent_config
from src.agent.findings import canonical_hash
from src.agent.mcp_client import McpTools
from src.agent.session import AgentSession, rejection_note
from src.agent.store import Store
from src.agent.tracing import Tracer
from src.rag.index import Index
from tests.agent_fixtures import FakeLLM, turn
from tests.rag_search_fixtures import CHUNKS, fake_embed
from tests.test_agent_mcp_client import LAKEHOUSE, FakeClient

CFG = load_agent_config()
READ = ("get_architecture", {"architecture_id": "lakehouse-iceberg"})
SEARCH = (
    "search_corpus",
    {"query": "back up all data", "doc_types": None, "published_from": None},
)
RECORD = (
    "record_finding",
    {
        "architecture_id": "lakehouse-iceberg",
        "best_practice": "REL09-BP01",
        "severity": "high",
        "summary": "No backup.",
        "source": "[S1]",
    },
)


def fake_rerank(query: str, docs: list[str]) -> list[float]:
    words = set(query.lower().split())
    return [float(len(words & set(d.lower().split()))) for d in docs]


class Scores:
    def __init__(self):
        self.sent: list[tuple] = []

    def score(self, trace_id, name, value, comment):
        self.sent.append((trace_id, name, value, comment))


def make(tmp_path: Path, llm, mcp=None, store=None, confirm=lambda *_: True):
    tracer = Tracer(tmp_path / "trace.jsonl")
    s = AgentSession(
        CFG,
        llm=llm,
        index=Index(CHUNKS, embed_fn=fake_embed, rerank_fn=fake_rerank),
        store=store or Store(":memory:"),
        tracer=tracer,
        team="data-platform",
        confirm=confirm,
        sleep=lambda _: None,
        mcp=mcp,
        candidates_path=tmp_path / "feedback_candidates.jsonl",
    )
    return s, tracer


def test_down_stores_rule_and_candidate(tmp_path: Path):
    s, _ = make(tmp_path, FakeLLM(turn("A long answer.")))
    s.ask("What does REL09-BP01 ask for?")
    assert s.feedback_down("shorter") == "noted: later answers follow: shorter"
    for i in range(6):
        s.feedback_down(f"rule {i}")
    s.feedback_down("rule 5")  # no duplicates
    assert s.store.rules() == ["rule 1", "rule 2", "rule 3", "rule 4", "rule 5"]
    [row] = [
        json.loads(line)
        for line in (tmp_path / "feedback_candidates.jsonl").read_text().splitlines()
    ][:1]
    assert row == {
        "question": "What does REL09-BP01 ask for?",
        "answer": "A long answer.",
        "comment": "shorter",
    }
    assert s.store.scores()[0]["value"] == 0


def test_up_scores_trace(tmp_path: Path):
    s, tracer = make(tmp_path, FakeLLM(turn("Good.")))
    scores = Scores()
    tracer.langfuse = scores
    s.ask("q")
    s.feedback_up()
    assert s.store.scores()[-1]["value"] == 1
    assert scores.sent == [(s.last_trace_id, "user_feedback", 1.0, None)]


def test_down_without_comment(tmp_path: Path):
    s, _ = make(tmp_path, FakeLLM(turn("x")))
    s.ask("q")
    s.feedback_down("")
    assert s.store.rules() == []
    assert s.store.scores()[-1]["value"] == 0


def test_feedback_before_any_answer(tmp_path: Path):
    s, _ = make(tmp_path, FakeLLM(turn("x")))
    assert s.feedback_up() == "nothing to rate yet: ask a question first"


def test_reject_needs_reviewed_architecture(tmp_path: Path):
    s, _ = make(tmp_path, FakeLLM(turn("x")))
    assert s.reject("REL09-BP01", "we copy nightly") == "review an architecture first"


def _read_then(tmp_path, *after, store=None, confirm=lambda *_: True):
    llm = FakeLLM(turn(tool_uses=[READ]), turn("read it"), *after)
    mcp = McpTools("data-platform", client_factory=lambda _p: FakeClient()).__enter__()
    s, _ = make(tmp_path, llm, mcp=mcp, store=store, confirm=confirm)
    s.ask("Review lakehouse-iceberg")
    return s, llm, mcp


def test_rejection_attached_to_architecture(tmp_path: Path):
    s, llm, mcp = _read_then(tmp_path, turn(tool_uses=[READ]), turn("again"))
    try:
        assert s.reject("rel09-bp01", "we copy the bucket nightly") == (
            "noted: REL09-BP01 will not be raised again for this version of lakehouse-iceberg"
        )
        s.ask("Review lakehouse-iceberg again")
        result = [
            b
            for m in llm.requests[-1]["messages"]
            if isinstance(m["content"], list)
            for b in m["content"]
            if b.get("type") == "tool_result"
        ][-1]
        assert result["content"].endswith(
            "Rejected by the user for this version: REL09-BP01 (we copy the bucket nightly)"
        )
        first_user = llm.requests[-1]["messages"][0]["content"]
        assert (
            "REL09-BP01" not in first_user.split("Earlier in this session")[0]
        )  # not in the memory block
        assert s.rejected_bp() == {"REL09-BP01"}
    finally:
        mcp.__exit__(None, None, None)


def test_record_rejected_bp_not_done(tmp_path: Path):
    asked: list[str] = []
    s, _llm, mcp = _read_then(
        tmp_path,
        turn(tool_uses=[SEARCH]),
        turn(tool_uses=[RECORD]),
        turn("tried"),
        confirm=lambda p, _a: asked.append(p) or True,
    )
    try:
        s.reject("REL09-BP01", "copied nightly")
        s.ask("Record REL09-BP01 for lakehouse-iceberg")
        outcome = next(
            c for c in s.last_result.state.calls if c.name == "record_finding"
        ).outcome
        assert outcome.text.startswith("NOT DONE: rejected by the user on ")
        assert outcome.text.endswith(": copied nightly")
        assert asked == []
        assert s.store.findings() == []
    finally:
        mcp.__exit__(None, None, None)


def test_rejection_void_on_new_hash(tmp_path: Path):
    s, _, mcp = _read_then(tmp_path)
    try:
        s.reject("REL09-BP01", "copied nightly")
        changed = {**LAKEHOUSE, "name": "Lakehouse v2"}
        assert s.store.rejections("lakehouse-iceberg", canonical_hash(changed)) == []
        assert rejection_note(
            s.store.rejections("lakehouse-iceberg", canonical_hash(LAKEHOUSE))
        ).startswith("Rejected")
    finally:
        mcp.__exit__(None, None, None)


def test_hash_ignores_updated_field():
    assert canonical_hash(LAKEHOUSE) == canonical_hash(
        {**LAKEHOUSE, "updated": "2027-01-01"}
    )


def test_reject_resolves_open_finding(tmp_path: Path):
    s, _llm, mcp = _read_then(
        tmp_path, turn(tool_uses=[SEARCH]), turn(tool_uses=[RECORD]), turn("recorded")
    )
    try:
        s.ask("Record REL09-BP01")
        assert s.store.findings()[0].status == "open"
        s.reject("REL09-BP01", "copied nightly")
        row = s.store.findings()[0]
        assert row.status == "resolved"
        assert row.resolved_at is not None
    finally:
        mcp.__exit__(None, None, None)
