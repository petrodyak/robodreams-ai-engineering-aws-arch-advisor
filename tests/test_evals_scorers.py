"""Deterministic scorers (evals/scorers.py, spec §7), on hand-built items and answer records."""

import pytest

from evals.scorers import (
    abstain_correct,
    aggregate,
    citations_valid,
    context_share,
    in_context,
    key_facts,
    retrieved,
    source_hit,
)
from evals.testset import TestItem
from src.rag.answer import NOT_FOUND, AnswerRecord, SourceRef, ValidClaim


def item(id_="one01", kind="single", facts=("RPO", "4 hours"), section="REL09-BP01 X"):
    answerable = kind != "no_answer"
    return TestItem(
        id=id_,
        question=f"question {id_}",
        kind=kind,
        expected_answer="x",
        key_facts=list(facts) if answerable else [],
        expected_sources=(
            [{"doc_id": "wa-reliability", "section": section}] if answerable else []
        ),
        relevant_chunk_ids=["wa-reliability#0188"] if answerable else [],
        answerable=answerable,
        verified_by="Petro",
        verified_on="2026-11-17",
    )


def ref(doc_id="wa-reliability", path=("Failure management", "REL09-BP01 X")):
    return SourceRef(
        label="S1",
        chunk_id=f"{doc_id}#0188",
        doc_id=doc_id,
        title="t",
        section_path=list(path),
        page_start=1,
    )


def record(
    question="question one01",
    found=True,
    text="Set an rpo of 4  Hours. [S1]",
    refs=None,
    retrieved_ids=("wa-reliability#0188",),
    context_ids=("wa-reliability#0188",),
    dropped=(),
    uncited=0,
):
    claims = (
        [ValidClaim(text=text, citations=["S1"], refs=refs or [ref()])] if found else []
    )
    return AnswerRecord(
        question=question,
        found=found,
        answer=text if found else NOT_FOUND,
        claims=claims,
        sources={"S1": "wa-reliability#0188"},
        retrieved=list(retrieved_ids),
        in_context=list(context_ids),
        dropped_labels=list(dropped),
        uncited_claims=uncited,
        context_tokens=300,
        stop_reason="end_turn",
        model="claude-haiku-5-5",
        effort="medium",
        prompt_version="v1",
        prompt_sha="abc",
        input_tokens=1000,
        output_tokens=100,
        cost_usd=0.0002,
        latency_ms=10,
    )


def test_not_found_on_no_answer_item():
    it, rec = item("none01", kind="no_answer"), record("question none01", found=False)

    assert abstain_correct(it, rec) is True
    assert source_hit(it, rec) is None
    assert key_facts(it, rec) is None
    assert retrieved(it, rec) is None and in_context(it, rec) is None
    assert citations_valid(rec) is True  # vacuously: no claims


def test_answer_on_no_answer_item_is_wrong():
    assert abstain_correct(item("none01", kind="no_answer"), record()) is False


def test_key_facts_normalized():
    assert key_facts(item(), record()) == 1.0
    assert key_facts(item(facts=("RPO", "8 hours")), record()) == 0.5


def test_key_facts_match_whole_words_only():
    """ "ALL" (the distribution style) is not found inside "small"; "six" not inside "sixty"."""
    it = item(facts=("ALL", "six"))

    assert (
        key_facts(it, record(text="Use it for small tables, sixty of them. [S1]"))
        == 0.0
    )
    assert (
        key_facts(it, record(text="Use ALL for small tables; six pillars. [S1]")) == 1.0
    )
    assert (
        key_facts(
            item(facts=("push_down_predicate",)),
            record(text="Set push_down_predicate. [S1]"),
        )
        == 1.0
    )


def test_source_hit_needs_doc_and_section():
    assert source_hit(item(), record()) is True
    assert source_hit(item(), record(refs=[ref(doc_id="wa-framework")])) is False
    assert source_hit(item(), record(refs=[ref(path=("Failure management",))])) is False
    # matching ignores case and spacing; an empty expected section matches the document
    assert source_hit(item(section="rel09-bp01  x"), record()) is True
    assert source_hit(item(section=""), record(refs=[ref(path=())])) is True


def test_citations_valid():
    assert citations_valid(record()) is True
    assert citations_valid(record(dropped=["S9"])) is False
    assert citations_valid(record(uncited=1)) is False


def test_retrieved_and_in_context():
    rec = record(context_ids=())
    assert retrieved(item(), rec) is True
    assert in_context(item(), rec) is False
    assert retrieved(item(), record(retrieved_ids=())) is False


def test_aggregate():
    items = [item("one01"), item("one02"), item("none01", kind="no_answer")]
    recs = [
        record("question one01"),
        record("question one02", found=False),
        record("question none01", found=False),
    ]

    m = aggregate(items, recs)

    assert m["abstain_accuracy"] == 1.0
    assert m["false_abstain_rate"] == pytest.approx(0.5)
    assert m["source_hit"] == pytest.approx(0.5)
    assert m["key_facts"] == pytest.approx(0.5)
    assert m["citations_valid"] == 1.0
    assert m["retrieved"] == 1.0 and m["in_context"] == 1.0
    assert m["failed"] == ["one02"]


def test_aggregate_rejects_misaligned_records():
    with pytest.raises(ValueError, match="one01"):
        aggregate([item("one01")], [record("another question")])


def test_context_share_counts_every_relevant_chunk():
    """`in_context` is true with one relevant chunk; `context_share` shows the part that is missing
    (a two-part question that loses its second chunk, F23)."""
    it = item("many03", kind="multi")
    it.relevant_chunk_ids = ["a#0001", "b#0002", "c#0003", "d#0004"]
    rec = record("question many03", context_ids=("a#0001", "x#0009", "c#0003"))

    assert in_context(it, rec) is True
    assert context_share(it, rec) == pytest.approx(0.5)
    assert context_share(item("none01", kind="no_answer"), rec) is None
    assert aggregate([it], [rec])["context_share"] == pytest.approx(0.5)
