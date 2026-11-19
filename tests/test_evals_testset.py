"""The testset file (evals/testset.jsonl) and its item model (evals/testset.py, spec §7)."""

import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from evals.testset import TestItem, load_testset
from src.rag.index import load_chunks

TESTSET = Path("evals/testset.jsonl")
CHUNKS = Path("data/rag/chunks.jsonl")
HELDOUT = Path("evals/testset_heldout.jsonl")


def test_testset_items_valid():
    items = load_testset(TESTSET)
    assert items
    assert len({it.id for it in items}) == len(items)
    for it in items:
        assert it.answerable == (it.kind != "no_answer")


def test_testset_sources_and_labels_exist():
    """Every expected source names a real document; every labelled chunk id exists."""
    chunks = load_chunks(CHUNKS)
    doc_ids = {c.doc_id for c in chunks}
    chunk_ids = {c.chunk_id for c in chunks}
    for it in load_testset(TESTSET):
        assert {s.doc_id for s in it.expected_sources} <= doc_ids, it.id
        assert set(it.relevant_chunk_ids) <= chunk_ids, it.id


def test_answerable_must_match_kind():
    row = {
        "id": "x",
        "question": "q",
        "kind": "no_answer",
        "expected_answer": "",
        "key_facts": [],
        "expected_sources": [],
        "relevant_chunk_ids": [],
        "answerable": True,
        "verified_by": None,
        "verified_on": None,
    }
    with pytest.raises(ValidationError, match="answerable"):
        TestItem.model_validate(row)
    with pytest.raises(ValidationError):
        TestItem.model_validate({**row, "answerable": False, "extra": 1})
    assert TestItem.model_validate_json(json.dumps({**row, "answerable": False}))


MIN_PER_KIND = {"single": 10, "multi": 4, "no_answer": 4, "similar": 3, "outdated": 3}


def test_testset_composition():
    """Spec §7: ≥ 24 items in the five kinds, every answerable item labelled and sourced,
    every item checked by hand (verified_by / verified_on)."""
    items = load_testset(TESTSET)
    chunk_ids = {c.chunk_id for c in load_chunks(CHUNKS)}

    assert len(items) >= 24
    for kind, minimum in MIN_PER_KIND.items():
        assert sum(it.kind == kind for it in items) >= minimum, kind
    for it in items:
        if it.answerable:
            assert it.relevant_chunk_ids, it.id
            assert set(it.relevant_chunk_ids) <= chunk_ids, it.id
            assert it.expected_sources, it.id
        assert it.verified_by and it.verified_on, it.id


def test_heldout_items_are_no_answer_and_new():
    """The held-out set (F32): no-answer questions only, none of them shared with the testset."""
    held = load_testset(HELDOUT)
    main = load_testset(TESTSET)
    assert len(held) == 10
    assert all(it.kind == "no_answer" and not it.relevant_chunk_ids for it in held)
    assert all(it.verified_by for it in held)
    assert not {it.id for it in held} & {it.id for it in main}
    assert not {it.question for it in held} & {it.question for it in main}
