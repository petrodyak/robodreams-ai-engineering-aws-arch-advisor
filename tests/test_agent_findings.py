"""record_finding: the confirmation gate, the argument checks and idempotency (spec §8, D13, D23)."""

from datetime import date
from pathlib import Path

import pytest

from src.agent.faults import parse_faults
from src.agent.findings import (
    BP_PATTERN,
    FindingContext,
    canonical_hash,
    guard,
    make_record_finding,
    normalize_bp,
    pillar_of,
)
from src.agent.search_tool import best_practice_ids
from src.agent.store import Store
from src.agent.tools import execute
from src.rag.index import load_chunks

TODAY = date(2026, 11, 24)
ARCH = "lakehouse-iceberg"


class ConfirmSpy:
    def __init__(self, answer: bool):
        self.answer = answer
        self.calls: list[str] = []

    def __call__(self, prompt: str, _args: dict) -> bool:
        self.calls.append(prompt)
        return self.answer


def context(*, autonomy="confirm", answer=True, faults="", blocked=None, read=True):
    store = Store(":memory:")
    session = store.new_session("data-platform")
    store.add_labels(
        session,
        {
            "S1": "wa-reliability#0042",
            "S2": "wa-reliability#0043",
            "S3": "wa-framework-old#0001",
        },
    )
    confirm = ConfirmSpy(answer)
    ctx = FindingContext(
        store=store,
        session_id=session,
        autonomy=autonomy,
        confirm=confirm,
        known_bp={"REL09-BP01", "SEC08-BP02", "GENSEC01-BP01"},
        arch_hashes={ARCH: "hash-1"} if read else {},
        blocked_docs=blocked or set(),
        today=TODAY,
        faults=parse_faults(faults),
    )
    return ctx, store, confirm


def args(**overrides) -> dict:
    values = {
        "architecture_id": ARCH,
        "best_practice": "REL09-BP01",
        "severity": "high",
        "summary": "The Glue Data Catalog has no backup.",
        "source": "[S1]",
    }
    values.update(overrides)
    return values


def record(ctx, **overrides):
    return execute(
        "record_finding",
        args(**overrides),
        {"record_finding": make_record_finding(ctx)},
        timeout=1.0,
    )


def test_guard_confirm_false_writes_nothing():
    ctx, store, confirm = context(answer=False)
    outcome = record(ctx)
    assert outcome.text == "NOT DONE: the person did not confirm; do not retry"
    assert store.findings() == []
    assert len(confirm.calls) == 1


def test_guard_without_model():
    confirm = ConfirmSpy(False)
    assert guard("record_finding", args(), "confirm", confirm) == (
        "NOT DONE: the person did not confirm; do not retry"
    )
    assert guard("record_finding", args(), "auto", confirm) is None
    assert len(confirm.calls) == 1


def test_read_only_never_asks():
    ctx, store, confirm = context(autonomy="read_only")
    outcome = record(ctx)
    assert outcome.text.startswith("NOT DONE: recording is switched off")
    assert confirm.calls == []
    assert store.findings() == []


def test_confirm_line_shows_what_is_written():
    ctx, _, confirm = context()
    record(ctx)
    assert confirm.calls == [
        'Record [high · Reliability · REL09-BP01] "The Glue Data Catalog has no backup."?'
    ]


def test_unknown_label_rejected():
    ctx, store, _ = context()
    outcome = record(ctx, source="[S9]")
    assert outcome.text == "NOT DONE: unknown source label S9 in this session"
    assert store.findings() == []


def test_bp_normalised():
    ctx, store, _ = context()
    first = record(ctx, best_practice=" rel09-bp01. ")
    assert first.text.startswith("recorded REL09-BP01")
    assert store.findings()[0].best_practice == "REL09-BP01"
    second = record(ctx, best_practice="REL09-BP01")
    assert second.text == f"already open since {TODAY.isoformat()}"
    assert len(store.findings()) == 1


def test_normalize_bp():
    assert normalize_bp(" rel09-bp01. ") == "REL09-BP01"
    assert normalize_bp("SEC08-BP02;") == "SEC08-BP02"


def test_bp_not_in_corpus():
    ctx, store, confirm = context()
    outcome = record(ctx, best_practice="REL99-BP99")
    assert outcome.text.startswith("NOT DONE: REL99-BP99 does not occur in the corpus")
    assert "report" in outcome.text
    assert store.findings() == []
    assert confirm.calls == []


def test_bp_bad_pattern():
    ctx, store, _ = context()
    outcome = record(ctx, best_practice="Back up data")
    assert outcome.is_error
    assert "not a Well-Architected best-practice id" in outcome.text
    assert store.findings() == []


def test_architecture_not_read():
    ctx, store, _ = context(read=False)
    outcome = record(ctx)
    assert outcome.text == "NOT DONE: read the architecture with get_architecture first"
    assert store.findings() == []


def test_duplicate_fault_one_row():
    ctx, store, _ = context(faults="duplicate")
    first = record(ctx)
    assert first.is_error
    assert "connection lost after the write; the result is unknown" in first.text
    assert first.faults == ["duplicate"]
    second = record(ctx)
    assert second.text.startswith("already open")
    assert len(store.findings()) == 1


def test_source_stored_as_chunk_id():
    ctx, store, _ = context()
    record(ctx, source="S2")
    assert store.findings()[0].source_chunk_id == "wa-reliability#0043"


def test_null_severity_asks_user():
    ctx, store, confirm = context()
    outcome = record(ctx, severity=None)
    assert outcome.is_error
    assert outcome.text == "ERROR: severity is missing: ask the user"
    outcome = record(ctx, best_practice=None)
    assert outcome.is_error
    assert "search the corpus" in outcome.text
    assert "ask the user" in outcome.text
    assert confirm.calls == []
    assert store.findings() == []


def test_pillar_derived_from_id():
    assert pillar_of("REL09-BP01") == "Reliability"
    assert pillar_of("GENSEC01-BP01") == "Security"
    assert pillar_of("MLCOST04-BP02") == "Cost Optimization"
    assert pillar_of("MLOPS01-BP01") == "Operational Excellence"
    assert pillar_of("GENPERF02-BP01") == "Performance Efficiency"
    assert pillar_of("SUS03-BP01") == "Sustainability"
    ctx, store, confirm = context()
    record(ctx, best_practice="GENSEC01-BP01")
    assert store.findings()[0].pillar == "Security"
    assert "Security" in confirm.calls[0]


def test_bp_pattern_accepts_all_corpus_ids():
    ids = best_practice_ids(load_chunks(Path("data/rag/chunks.jsonl")))
    assert len(ids) > 400
    assert all(BP_PATTERN.fullmatch(i) for i in ids)
    assert all(pillar_of(i) for i in ids)


def test_existing_row_not_confirmed_again():
    ctx, _, confirm = context()
    record(ctx)
    again = record(ctx)
    assert again.text.startswith("already open")
    assert len(confirm.calls) == 1


def test_resolved_finding_is_reopened():
    ctx, store, _ = context()
    record(ctx)
    store.resolve_finding(store.findings()[0].id, date(2026, 11, 25))
    again = record(ctx)
    assert again.text == "reopened (was resolved on 2026-11-25)"
    assert store.findings()[0].status == "open"


def test_blocked_source_refused():
    ctx, store, _ = context(blocked={"wa-framework-old"})
    outcome = record(ctx, source="[S3]")
    assert outcome.text == "NOT DONE: a finding must rest on a current document"
    assert store.findings() == []


def test_canonical_hash_ignores_updated_and_key_order():
    a = {"id": "x", "name": "X", "updated": "2026-11-01", "components": [1, 2]}
    b = {"components": [1, 2], "name": "X", "id": "x", "updated": "2026-11-20"}
    c = {"id": "x", "name": "Y", "components": [1, 2]}
    assert canonical_hash(a) == canonical_hash(b)
    assert canonical_hash(a) != canonical_hash(c)


@pytest.mark.parametrize("summary", ["", "x" * 301])
def test_summary_length_checked_in_code(summary):
    ctx, store, _ = context()
    outcome = record(ctx, summary=summary)
    assert outcome.is_error
    assert store.findings() == []
