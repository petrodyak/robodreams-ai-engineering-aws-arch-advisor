"""Retrieval metrics (evals/retrieval.py): recall@k, reciprocal rank, fixed-chunk relevance."""

import pytest

from evals.retrieval import (
    evaluate_retrieval,
    recall_at,
    reciprocal_rank,
    relevant_fixed_ids,
)
from evals.testset import TestItem
from tests.rag_search_fixtures import chunk

BACKUP = (
    "REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data "
    "from sources. Amazon S3 can be used as a backup destination for multiple data sources. "
    "AWS Backup centralizes and automates data protection across AWS services."
)


def test_recall_and_mrr():
    ranked, relevant = ["a", "b", "c"], {"b"}
    assert recall_at(ranked, relevant, 1) == 0
    assert recall_at(ranked, relevant, 2) == 1
    assert reciprocal_rank(ranked, relevant) == 0.5
    assert reciprocal_rank(ranked, {"z"}) == 0.0


def _fixed(chunk_id: str, text: str):
    return chunk(chunk_id, text).model_copy(update={"strategy": "fixed"})


def test_relevant_fixed_ids_overlap():
    """Petro's option B: overlap counts across documents; unrelated text does not."""
    structure = {"wa-reliability#0188": chunk("wa-reliability#0188", BACKUP)}
    words = BACKUP.split()
    inside = " ".join(words[: int(len(words) * 0.7)])  # 70 % of the structure chunk
    fixed = [
        _fixed(
            "wa-reliability#f0164", inside + " Next section starts here with new words."
        ),
        _fixed("wa-framework#f0617", "Some framework preamble. " + inside),
        _fixed(
            "wa-security#f0001",
            "SEC08-BP02 Enforce encryption at rest with AWS KMS keys.",
        ),
    ]
    got = relevant_fixed_ids(fixed, structure, {"wa-reliability#0188"})
    assert got == {"wa-reliability#f0164", "wa-framework#f0617"}


def _item(item_id: str, relevant: list[str]) -> TestItem:
    return TestItem(
        id=item_id,
        question="q",
        kind="single",
        expected_answer="a",
        key_facts=[],
        expected_sources=[],
        relevant_chunk_ids=relevant,
        answerable=True,
        verified_by=None,
        verified_on=None,
    )


def test_evaluate_retrieval():
    rankings = {"q1": ["x", "a"], "q2": ["y"] * 5 + ["b"], "q3": ["z"]}
    items = [_item("q1", ["a"]), _item("q2", ["b"]), _item("q3", ["c"])]
    r = evaluate_retrieval(
        lambda q: rankings[q], items, lambda it: set(it.relevant_chunk_ids),
        query_of=lambda it: it.id,
    )  # fmt: skip
    assert r["recall@5"] == pytest.approx(1 / 3)  # only q1 within 5
    assert r["recall@10"] == pytest.approx(2 / 3)  # q2 at rank 6
    assert r["mrr"] == pytest.approx((1 / 2 + 1 / 6 + 0) / 3)
    assert r["misses"] == ["q3"]
    assert r["questions"] == 3
    assert r["ms"] >= 0


def test_evaluate_retrieval_rejects_an_unlabelled_item():
    with pytest.raises(ValueError, match="q1"):
        evaluate_retrieval(lambda q: [], [_item("q1", [])], lambda it: set())
