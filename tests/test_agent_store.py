"""The SQLite store of the agent (spec §11, D13, D14)."""

from datetime import date, datetime, timedelta

from src.agent.store import FindingRow, Store

TODAY = date(2026, 11, 24)


def _finding(**overrides) -> FindingRow:
    values = {
        "id": None,
        "architecture_id": "lakehouse-iceberg",
        "pillar": "Reliability",
        "best_practice": "REL09-BP01",
        "severity": "high",
        "summary": "No backup of the Glue Data Catalog.",
        "source_chunk_id": "wa-reliability#0042",
        "status": "open",
        "architecture_hash": "hash-1",
        "opened_at": TODAY,
        "resolved_at": None,
    }
    values.update(overrides)
    return FindingRow(**values)


def test_finding_insert_then_duplicate():
    store = Store(":memory:")
    first = store.insert_or_reopen_finding(_finding())
    second = store.insert_or_reopen_finding(
        _finding(opened_at=TODAY + timedelta(days=1))
    )
    assert first.status == "recorded"
    assert second.status == "already_open"
    assert second.since == TODAY
    assert second.finding_id == first.finding_id
    assert len(store.findings()) == 1


def test_finding_resolved_then_reopened():
    store = Store(":memory:")
    first = store.insert_or_reopen_finding(_finding())
    assert store.resolve_finding(first.finding_id, TODAY + timedelta(days=2)) is True
    assert store.findings(status="resolved")[0].resolved_at == TODAY + timedelta(days=2)

    again = store.insert_or_reopen_finding(
        _finding(architecture_hash="hash-2", opened_at=TODAY + timedelta(days=5))
    )
    assert again.status == "reopened"
    assert again.finding_id == first.finding_id
    rows = store.findings()
    assert len(rows) == 1
    row = rows[0]
    assert row.status == "open"
    assert row.reopened_count == 1
    assert row.architecture_hash == "hash-2"
    assert row.resolved_at is None


def test_resolve_unknown_finding_is_false():
    store = Store(":memory:")
    assert store.resolve_finding(999, TODAY) is False


def test_labels_are_per_session():
    store = Store(":memory:")
    s1 = store.new_session("data-platform")
    s2 = store.new_session("data-platform")
    store.add_labels(s1, {f"S{i}": f"doc#{i:04d}" for i in range(1, 6)})
    assert store.label_map(s1)["S3"] == "doc#0003"
    assert store.label_map(s2) == {}
    assert store.next_label(s1) == 6
    assert store.next_label(s2) == 1


def test_messages_round_trip():
    store = Store(":memory:")
    sid = store.new_session("data-platform")
    store.add_message(sid, "user", "Review lakehouse-iceberg", {"turn": 1})
    store.add_message(sid, "assistant", "Findings: …", {"turn": 1, "stop": "answer"})
    history = store.history(sid)
    assert [m.role for m in history] == ["user", "assistant"]
    assert history[1].meta == {"turn": 1, "stop": "answer"}
    assert isinstance(history[0].created_at, datetime)


def test_purge_keeps_findings_and_episodes():
    store = Store(":memory:")
    old = store.new_session("data-platform", started_at=datetime(2026, 10, 1, 9, 0))
    new = store.new_session("data-platform", started_at=datetime(2026, 11, 20, 9, 0))
    for sid in (old, new):
        store.add_message(sid, "user", "question", {})
        store.add_labels(sid, {"S1": "doc#0001"})
    store.add_episode(old, "Reviewed lakehouse-iceberg.", datetime(2026, 10, 1, 10, 0))
    store.insert_or_reopen_finding(_finding())

    assert store.purge_sessions(TODAY, days=30) == 1

    assert store.history(old) == []
    assert store.label_map(old) == {}
    assert len(store.history(new)) == 1
    assert store.label_map(new) == {"S1": "doc#0001"}
    assert len(store.findings()) == 1
    assert store.episodes() == ["Reviewed lakehouse-iceberg."]
