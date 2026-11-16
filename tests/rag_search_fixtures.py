"""Shared fixtures for the index and search tests: six chunks and a fake embedder.

The fake embedder is a bag-of-letters vector (26 letter counts), so texts that share letters are
close in cosine. It needs no model download and no network (plan: Global Constraints).
"""

from datetime import date

from src.rag.ingest.dedup import content_hash
from src.rag.models import ChunkRecord


def fake_embed(texts: list[str]) -> list[list[float]]:
    out = []
    for t in texts:
        v = [0.0] * 26
        for ch in t.lower():
            if "a" <= ch <= "z":
                v[ord(ch) - 97] += 1.0
        v[0] += 0.001  # never an all-zero vector (cosine is undefined for it)
        out.append(v)
    return out


def chunk(
    chunk_id: str,
    text: str,
    *,
    doc_type: str = "pillar",
    published: date = date(2024, 11, 6),
    path: list[str] | None = None,
) -> ChunkRecord:
    doc_id = chunk_id.split("#")[0]
    return ChunkRecord(
        chunk_id=chunk_id,
        doc_id=doc_id,
        title=f"{doc_id} title",
        doc_type=doc_type,
        format="pdf",
        source_url=f"https://example.org/{doc_id}.pdf",
        published=published,
        section_path=path or ["Section"],
        page_start=1,
        page_end=1,
        text=text,
        n_tokens=len(text.split()),
        chunk_hash=content_hash(text),
        doc_hash="sha256:" + "0" * 64,
        strategy="structure",
        pipeline_version="ingest-v1",
    )


CHUNKS = [
    chunk(
        "wa-reliability#0000",
        "REL09-BP01 Identify and back up all data that needs to be backed up.",
        path=["Failure management", "REL09-BP01 Identify and back up all data"],
    ),
    chunk(
        "wa-reliability#0001",
        "REL10-BP01 Deploy the workload to multiple locations.",
        path=["Failure management", "REL10-BP01 Deploy to multiple locations"],
    ),
    chunk(
        "wa-security#0000",
        "SEC08-BP02 Enforce encryption at rest with AWS KMS keys.",
        path=["Data protection", "SEC08-BP02 Enforce encryption at rest"],
    ),
    chunk(
        "wa-lens-analytics#0000",
        "Use Apache Iceberg tables for the data lake and query them with Athena.",
        doc_type="lens",
        published=date(2023, 4, 1),
    ),
    chunk(
        "pg-iceberg#0000",
        "Iceberg compaction rewrites small files into larger ones.",
        doc_type="guide",
        published=date(2025, 2, 1),
    ),
    chunk(
        "wa-framework-2020#0000",
        "The reliability pillar of the 2020 framework edition.",
        doc_type="framework",
        published=date(2020, 7, 1),
    ),
]
