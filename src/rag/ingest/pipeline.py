"""Ingestion pipeline: data/rag/manifest.csv + data/rag/raw/ -> chunk files + ingest manifest.

Per document: extract (with structure) -> clean -> dedup -> chunk (both strategies) -> metadata.

- chunks.jsonl: the structure-aware chunks, the product that search, answers and the stage-3
  agent read;
- chunks_fixed.jsonl: the fixed-size baseline, only for the retrieval comparison (step 17);
- ingest_manifest.json: duplicates, empty documents and statistics of both.

All outputs are deterministic, so they are committed, and a re-run on the same corpus gives
byte-identical files.

Usage:  python -m src.rag.ingest.pipeline      (make ingest)
"""

import csv
import hashlib
import json
from datetime import date
from pathlib import Path

from src.rag.ingest.chunk import (
    PIPELINE_VERSION,
    chunk_fixed,
    chunk_stats,
    chunk_structure,
    n_tokens,
)
from src.rag.ingest.dedup import content_hash, near_duplicates
from src.rag.ingest.extract_html import extract_html
from src.rag.ingest.extract_pdf import extract_pdf
from src.rag.models import ChunkRecord, DocMeta, Section

ROOT = Path("data/rag")
# Which copy of a duplicate survives: the most specific document. The current Well-Architected
# Framework PDF repeats every pillar's best practices in its appendix; a citation should name the
# Reliability Pillar for REL09-BP01, not the 1,000-page Framework.
DEDUP_PRIORITY = {"pillar": 0, "lens": 1, "guide": 2, "framework": 3}


def extract(path: Path, fmt: str) -> list[Section]:
    """Sections of one raw document, by format."""
    if fmt == "pdf":
        return extract_pdf(path)
    if fmt == "html":
        return extract_html(path.read_text(encoding="utf-8"))
    raise ValueError(f"unsupported format: {fmt}")


def document_text(sections: list[Section]) -> str:
    return "\n\n".join(s.text for s in sections)


def document_hash(sections: list[Section]) -> str:
    """The Document hash: content_hash of the document's cleaned text ("sha256:<hex>").

    It changes only when the text changes, not when AWS rebuilds the file around it (F21), so
    data/rag/manifest.csv records it (without the "sha256:" prefix) as the version of the corpus.
    """
    return content_hash(document_text(sections))


def _write_jsonl(path: Path, records: list[ChunkRecord]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for c in sorted(records, key=lambda c: c.chunk_id):
            f.write(c.model_dump_json() + "\n")


def run(
    manifest: Path, raw_dir: Path, chunks_out: Path, fixed_out: Path, report_out: Path
) -> dict:
    with manifest.open(newline="") as f:
        rows = list(csv.DictReader(f))

    documents, empty, texts = [], [], {}
    seen_docs: dict[str, str] = {}
    seen_chunks: set[tuple[str, str]] = set()
    dropped = {"documents": 0, "chunks": 0}
    by_strategy: dict[str, list[ChunkRecord]] = {"structure": [], "fixed": []}

    order = sorted(
        range(len(rows)), key=lambda i: (DEDUP_PRIORITY[rows[i]["doc_type"]], i)
    )
    for row in (rows[i] for i in order):
        sections = extract(raw_dir / f"{row['doc_id']}.{row['format']}", row["format"])
        text = document_text(sections)
        if not text.strip():
            empty.append(row["doc_id"])
            continue
        doc_hash = content_hash(text)
        if doc_hash in seen_docs:
            dropped["documents"] += 1
            continue
        seen_docs[doc_hash] = row["doc_id"]
        texts[row["doc_id"]] = text

        meta = DocMeta(
            doc_id=row["doc_id"],
            title=row["title"],
            doc_type=row["doc_type"],
            format=row["format"],
            source_url=row["url"],
            published=date.fromisoformat(row["published"]),
            doc_hash=doc_hash,
        )
        counts, duplicates = {}, 0
        for strategy, chunks in (
            ("structure", chunk_structure(sections, meta)),
            ("fixed", chunk_fixed(sections, meta)),
        ):
            kept = []
            for c in chunks:
                key = (strategy, c.chunk_hash)
                if key in seen_chunks:
                    dropped["chunks"] += 1
                    duplicates += 1
                    continue
                seen_chunks.add(key)
                kept.append(c)
            counts[strategy] = len(kept)
            by_strategy[strategy] += kept
        documents.append(
            {
                "doc_id": row["doc_id"],
                "sections": len(sections),
                "chunks_structure": counts["structure"],
                "chunks_fixed": counts["fixed"],
                "tokens": n_tokens(text),
                "duplicate_chunks_dropped": duplicates,
            }
        )

    position = {row["doc_id"]: i for i, row in enumerate(rows)}
    documents.sort(
        key=lambda d: position[d["doc_id"]]
    )  # the report follows the manifest order
    empty.sort(key=position.__getitem__)
    _write_jsonl(chunks_out, by_strategy["structure"])
    _write_jsonl(fixed_out, by_strategy["fixed"])

    version = hashlib.sha256(
        ("\n".join(sorted(seen_docs)) + "\n" + PIPELINE_VERSION).encode()
    ).hexdigest()
    report = {
        "dataset_version": version,
        "pipeline_version": PIPELINE_VERSION,
        "documents": documents,
        "exact_duplicates_dropped": dropped,
        "near_duplicates": [list(p) for p in near_duplicates(texts)],
        "empty_documents": empty,
        "stats": {s: chunk_stats(chunks) for s, chunks in by_strategy.items()},
    }
    report_out.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return report


def main() -> None:
    report = run(
        ROOT / "manifest.csv",
        ROOT / "raw",
        ROOT / "chunks.jsonl",
        ROOT / "chunks_fixed.jsonl",
        ROOT / "ingest_manifest.json",
    )
    print(
        f"dataset_version {report['dataset_version'][:16]}  documents {len(report['documents'])}"
    )
    for strategy, stats in report["stats"].items():
        print(f"{strategy:9} {stats}")
    print(f"exact duplicates dropped {report['exact_duplicates_dropped']}")
    print(
        f"near duplicates {report['near_duplicates']}  empty {report['empty_documents']}"
    )


if __name__ == "__main__":
    main()
