"""The HW 2 corpus manifest (data/rag/manifest.csv) and its download script.

The manifest is tracked in Git; the documents it lists are not (data/rag/raw/ is
gitignored). These tests check the manifest itself and the hash check of the
downloader with a fake fetch, so they pass on a clean clone with no network.
"""

import csv
import hashlib
import re
from datetime import date
from pathlib import Path

import pytest

from scripts.download_rag_corpus import download

MANIFEST = Path(__file__).resolve().parent.parent / "data" / "rag" / "manifest.csv"
COLUMNS = ["doc_id", "title", "format", "url", "doc_type", "published", "sha256"]


@pytest.fixture(scope="module")
def rows():
    with open(MANIFEST, newline="") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == COLUMNS
        return list(reader)


def test_manifest_size_and_formats(rows):
    assert len(rows) >= 30
    assert {r["format"] for r in rows} >= {"pdf", "html"}
    types = [r["doc_type"] for r in rows]
    assert types.count("framework") >= 1
    assert types.count("pillar") == 6
    assert 3 <= types.count("lens") <= 4


def test_manifest_fields(rows):
    ids = [r["doc_id"] for r in rows]
    assert len(ids) == len(set(ids)), "doc_id must be unique"
    for r in rows:
        assert re.fullmatch(r"[a-z0-9-]+", r["doc_id"]), r["doc_id"]
        assert r["title"].strip(), r["doc_id"]
        assert r["format"] in {"pdf", "html"}, r["doc_id"]
        assert r["url"].startswith("https://"), r["doc_id"]
        assert r["doc_type"] in {"framework", "pillar", "lens", "guide"}, r["doc_id"]
        date.fromisoformat(r["published"])
        assert re.fullmatch(r"[0-9a-f]{64}", r["sha256"]), r["doc_id"]


def test_download_checks_hash(tmp_path):
    good = {"doc_id": "x", "format": "html", "url": "https://example.org/x"}
    good["sha256"] = hashlib.sha256(b"abc").hexdigest()
    path = download(good, tmp_path, fetch=lambda url: b"abc")
    assert path == tmp_path / "x.html"
    assert path.read_bytes() == b"abc"

    bad = dict(good, doc_id="y", sha256="0" * 64)
    with pytest.raises(ValueError, match="sha256"):
        download(bad, tmp_path, fetch=lambda url: b"abc")
    assert not (tmp_path / "y.html").exists()
