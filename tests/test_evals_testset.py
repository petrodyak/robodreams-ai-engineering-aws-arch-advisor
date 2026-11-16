"""The testset file (evals/testset.jsonl) and its item model (evals/testset.py, spec §7)."""

import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from evals.testset import TestItem, load_testset
from src.rag.index import load_chunks

TESTSET = Path("evals/testset.jsonl")
CHUNKS = Path("data/rag/chunks.jsonl")


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
