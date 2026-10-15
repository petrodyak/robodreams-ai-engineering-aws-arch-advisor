"""Integrity of the 30-document working set in data/raw/.

data/raw/manifest.csv and data/raw/*.txt are tracked in Git and feed later stages
(extraction, RAG, agent), so these checks must pass on a clean clone. The PDFs
are gitignored and deliberately not touched here.
"""

import csv
from pathlib import Path

import pytest

RAW = Path(__file__).resolve().parent.parent / "data" / "raw"
MANIFEST = RAW / "manifest.csv"
GROUPS = {"short", "medium", "edge"}


@pytest.fixture(scope="module")
def rows():
    with open(MANIFEST, newline="") as f:
        return list(csv.DictReader(f))


def txt_path(row):
    return (RAW / row["file"]).with_suffix(".txt")


def test_manifest_has_30_rows(rows):
    assert len(rows) == 30, f"expected 30 rows in {MANIFEST}, got {len(rows)}"


def test_groups_are_known(rows):
    bad = {r["file"]: r["group"] for r in rows if r["group"] not in GROUPS}
    assert not bad, f"unknown group (allowed: {sorted(GROUPS)}): {bad}"


def test_every_file_has_txt(rows):
    missing = [txt_path(r).name for r in rows if not txt_path(r).is_file()]
    assert not missing, f"missing .txt, run scripts/extract_text.py: {missing}"


def test_every_txt_is_non_empty(rows):
    empty = [
        txt_path(r).name
        for r in rows
        if txt_path(r).is_file() and txt_path(r).stat().st_size == 0
    ]
    assert not empty, f"empty .txt (text extraction failed?): {empty}"
