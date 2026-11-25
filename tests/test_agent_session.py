"""AgentSession: the composition root of the chat and the evals (spec §6.1, §11; src/agent/session.py)."""

import json
from datetime import datetime
from pathlib import Path

from src.agent.config import load_agent_config
from src.agent.session import AgentSession, system_blocks
from src.agent.store import Store
from src.agent.tracing import Tracer
from src.rag.index import Index
from tests.agent_fixtures import FakeLLM, turn
from tests.rag_search_fixtures import CHUNKS, fake_embed

CFG = load_agent_config()


def fake_rerank(query: str, docs: list[str]) -> list[float]:
    words = set(query.lower().split())
    return [float(len(words & set(d.lower().split()))) for d in docs]


def session(llm, tmp_path: Path, store: Store | None = None) -> AgentSession:
    return AgentSession(
        CFG,
        llm=llm,
        index=Index(CHUNKS, embed_fn=fake_embed, rerank_fn=fake_rerank),
        store=store or Store(":memory:"),
        tracer=Tracer(tmp_path / "trace.jsonl"),
        team="data-platform",
        confirm=lambda *_: False,
        sleep=lambda _: None,
    )


def test_system_prompt_has_rules():
    text = "\n".join(block["text"] for block in system_blocks(CFG, "data-platform"))
    lower = text.lower()
    assert "English" in text  # 1, D17
    assert (
        "a separate search for each pillar" in lower and "in one step" in lower
    )  # 2, D25
    for pillar in (
        "Operational Excellence",
        "Security",
        "Reliability",
        "Performance Efficiency",
        "Cost Optimization",
        "Sustainability",
    ):
        assert pillar in text
    assert "Pillars covered:" in text  # 2
    assert "best-practice id" in lower and "[Sn]" in text  # 3
    assert "<document>" in text  # 4, ADR-0011
    assert "older edition" in lower and "cite both" in lower  # 5
    assert "do not guess" in lower  # 6
    assert "403" in text  # 7
    assert "only when the user asks to record" in lower  # 8, D23
    assert "do not ask for permission to record" in lower  # 8
    assert "memory block" in lower and "documentation wins" in lower  # 9
    assert (
        "remember" in lower and "states about themself in this turn" in lower
    )  # 10, D24
    assert "null" in lower and "ask the user" in lower  # 10
    assert "2026-11-24" in text
    assert "data-platform" in text


def test_session_ask_writes_messages_and_trace(tmp_path: Path):
    llm = FakeLLM(
        turn(
            tool_uses=[
                (
                    "search_corpus",
                    {
                        "query": "back up all data",
                        "doc_types": None,
                        "published_from": None,
                    },
                )
            ]
        ),
        turn("Back up all data [S1]."),
    )
    store = Store(":memory:")
    s = session(llm, tmp_path, store)
    result = s.ask("How do I back up a data lake?")
    assert result.stop == "answer"
    rows = store.history(s.session_id)
    assert [(r.role, r.text) for r in rows] == [
        ("user", "How do I back up a data lake?"),
        ("assistant", "Back up all data [S1]."),
    ]
    lines = (tmp_path / "trace.jsonl").read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    line = json.loads(lines[0])
    assert line["tool_calls"][0]["name"] == "search_corpus"
    assert line["retrieved_chunk_ids"]
    assert rows[1].meta["trace_id"] == line["trace_id"]


def test_tools_sent_are_strict_and_cached_prefix_is_stable(tmp_path: Path):
    llm = FakeLLM(turn("hello"))
    s = session(llm, tmp_path)
    s.ask("hi")
    s.ask("hi again")
    first, second = llm.requests
    assert [t["name"] for t in first["tools"]] == ["search_corpus", "record_finding"]
    assert all(t["strict"] for t in first["tools"])
    assert first["system"] == second["system"]
    assert first["tools"] == second["tools"]


def test_history_carries_earlier_turns(tmp_path: Path):
    llm = FakeLLM(turn("first answer"), turn("second answer"))
    s = session(llm, tmp_path)
    s.ask("first question")
    s.ask("second question")
    messages = llm.requests[1]["messages"]
    assert [m["role"] for m in messages] == ["user", "assistant", "user"]
    assert messages[1]["content"] == "first answer"


def test_new_saves_episode_and_starts_a_session(tmp_path: Path):
    store = Store(":memory:")
    s = session(FakeLLM(turn("answer")), tmp_path, store)
    first = s.session_id
    s.ask("question")
    s.new()
    assert s.session_id != first
    assert len(store.episodes()) == 1
    s.close()
    assert len(store.episodes()) == 1  # an empty session leaves no episode


def test_session_purges_old_sessions_at_start(tmp_path: Path):
    store = Store(":memory:")
    old = store.new_session("data-platform", started_at=datetime(2026, 9, 1, 9, 0))
    store.add_message(old, "user", "old question", {})
    session(FakeLLM(turn("a")), tmp_path, store)
    assert store.history(old) == []


def test_real_date_for_purge_and_findings(tmp_path: Path):
    # final review, finding 4: cfg.today is frozen for the prompt and editions only
    from datetime import date

    store = Store(":memory:")
    old = store.new_session("data-platform", started_at=datetime(2026, 11, 30, 9, 0))
    store.add_message(old, "user", "december question", {})
    s = AgentSession(
        CFG,
        llm=FakeLLM(turn("a")),
        index=Index(CHUNKS, embed_fn=fake_embed, rerank_fn=fake_rerank),
        store=store,
        tracer=Tracer(tmp_path / "trace.jsonl"),
        team="data-platform",
        confirm=lambda *_: False,
        sleep=lambda _: None,
        today_fn=lambda: date(2027, 1, 10),
    )
    assert store.history(old) == []  # older than 30 days on the real date
    assert s.findings_ctx.today == date(2027, 1, 10)
    assert "2026-11-24" in s.system[0]["text"]  # the prompt keeps the frozen date


def test_architecture_reads_do_not_survive_new(tmp_path: Path):
    # final review, finding 5: "read in this session" (spec §8)
    s = session(FakeLLM(turn("a")), tmp_path)
    s.findings_ctx.arch_hashes["lakehouse-iceberg"] = "hash-1"
    s.new()
    assert s.findings_ctx.arch_hashes == {}
