"""The ingestion pipeline (src/rag/ingest/pipeline.py) on a fixture corpus of tiny documents."""

import csv
import json

from src.rag.ingest.pipeline import document_hash, extract, run
from tests.rag_fixtures import AWS_PAGE, EMPTY_PAGE, make_pdf

COLUMNS = ["doc_id", "title", "format", "url", "doc_type", "published", "sha256"]


def _corpus(tmp_path):
    raw = tmp_path / "raw"
    raw.mkdir(parents=True)
    (raw / "pg-keys.html").write_text(AWS_PAGE)
    (raw / "pg-keys-copy.html").write_text(
        AWS_PAGE
    )  # the same page under a second doc_id
    (raw / "pg-empty.html").write_text(EMPTY_PAGE)
    header = "Test Pillar AWS Well-Architected Framework"
    pages = [
        [
            header,
            "Failure management",
            "Failure management keeps the workload running.",
            "x 1",
        ],
        [header, "REL09-BP01 Identify data", "Identify all data to back up.", "x 2"],
    ]
    outline = [(0, "Failure management", 0), (1, "REL09-BP01 Identify data", 1)]
    make_pdf(raw / "wa-test.pdf", pages, outline)
    rows = [
        ("wa-test", "Test Pillar", "pdf", "pillar"),
        ("pg-keys", "Guide: Choose keys", "html", "guide"),
        ("pg-keys-copy", "Guide: Choose keys (copy)", "html", "guide"),
        ("pg-empty", "Guide: Empty", "html", "guide"),
    ]
    manifest = tmp_path / "manifest.csv"
    with manifest.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)
        for doc_id, title, fmt, doc_type in rows:
            writer.writerow(
                [doc_id, title, fmt, f"https://x/{doc_id}", doc_type, "2024-11-06", ""]
            )
    return manifest, raw


def _run(tmp_path, name):
    manifest, raw = _corpus(tmp_path / name)
    out = tmp_path / name
    report = run(
        manifest,
        raw,
        out / "chunks.jsonl",
        out / "chunks_fixed.jsonl",
        out / "ingest_manifest.json",
    )
    return report, out


def _lines(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


def test_run_is_deterministic(tmp_path):
    _, a = _run(tmp_path, "a")
    _, b = _run(tmp_path, "b")
    for name in ("chunks.jsonl", "chunks_fixed.jsonl", "ingest_manifest.json"):
        assert (a / name).read_bytes() == (b / name).read_bytes(), name
    for name in ("chunks.jsonl", "chunks_fixed.jsonl"):
        ids = [c["chunk_id"] for c in _lines(a / name)]
        assert ids == sorted(ids)


def test_strategies_in_separate_files(tmp_path):
    # chunks.jsonl is the product stage 3 reads; the fixed baseline lives next to it
    _, out = _run(tmp_path, "s")
    assert {c["strategy"] for c in _lines(out / "chunks.jsonl")} == {"structure"}
    assert {c["strategy"] for c in _lines(out / "chunks_fixed.jsonl")} == {"fixed"}


def test_exact_duplicate_dropped(tmp_path):
    report, out = _run(tmp_path, "d")
    assert report["exact_duplicates_dropped"]["documents"] == 1
    doc_ids = {
        json.loads(line)["doc_id"]
        for line in (out / "chunks.jsonl").read_text().splitlines()
    }
    assert "pg-keys-copy" not in doc_ids
    assert {"wa-test", "pg-keys"} <= doc_ids


def test_empty_document_listed(tmp_path):
    report, _ = _run(tmp_path, "e")
    assert report["empty_documents"] == ["pg-empty"]
    by_id = {d["doc_id"]: d for d in report["documents"]}
    assert by_id["wa-test"]["chunks_structure"] >= 1
    assert by_id["pg-keys"]["chunks_structure"] >= 1
    assert report["dataset_version"]
    assert set(report["stats"]) == {"structure", "fixed"}


def test_document_hash_ignores_bytes_outside_the_text(tmp_path):
    # F21: AWS rebuilds its pages and PDFs; the hash must follow the content, not the bytes
    page = tmp_path / "a.html"
    page.write_text(AWS_PAGE)
    rebuilt = tmp_path / "b.html"
    rebuilt.write_text(
        AWS_PAGE.replace("<h6>Topics</h6>", "<h2>Topics</h2>").replace(
            "var x = 1;", "var x = 2;"
        )
    )
    assert document_hash(extract(page, "html")) == document_hash(
        extract(rebuilt, "html")
    )
    changed = tmp_path / "c.html"
    changed.write_text(
        AWS_PAGE.replace("Sort keys order the data.", "Sort keys order rows.")
    )
    assert document_hash(extract(page, "html")) != document_hash(
        extract(changed, "html")
    )


def test_duplicate_chunk_kept_in_the_most_specific_document(tmp_path):
    # the Framework repeats the pillars' best practices; the pillar keeps them, even when the
    # Framework comes first in the manifest
    manifest, raw = _corpus(tmp_path / "p")
    # the same page plus a long section of its own: one chunk is shared, one is not
    extra = "<h2>Appendix</h2><p>" + " ".join(["appendix"] * 470) + ".</p>"
    (raw / "wa-framework.html").write_text(
        AWS_PAGE.replace("<awsdocs-copyright>", extra + "<awsdocs-copyright>")
    )
    rows = manifest.read_text().splitlines()
    framework = "wa-framework,Framework,html,https://x/f,framework,2024-11-06,"
    manifest.write_text("\n".join([rows[0], framework, *rows[1:]]) + "\n")
    out = tmp_path / "p"
    report = run(
        manifest,
        raw,
        out / "chunks.jsonl",
        out / "chunks_fixed.jsonl",
        out / "ingest_manifest.json",
    )
    by_id = {d["doc_id"]: d for d in report["documents"]}
    assert by_id["pg-keys"]["duplicate_chunks_dropped"] == 0
    assert by_id["wa-framework"]["duplicate_chunks_dropped"] > 0
    # the report keeps the manifest order
    assert report["documents"][0]["doc_id"] == "wa-framework"
