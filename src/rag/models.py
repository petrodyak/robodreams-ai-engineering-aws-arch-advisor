"""Shared types of the RAG stage (spec §4).

`ChunkRecord` is one line of data/rag/chunks.jsonl. Stage 3 (the agent) reads that file, so its
field names are part of the project's contract: renaming one is a breaking change (ADR-0007).
"""

from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict

DocType = Literal["framework", "pillar", "lens", "guide"]
Format = Literal["pdf", "html"]
Strategy = Literal["structure", "fixed"]


class Section(BaseModel):
    """One section of an extracted document, before chunking.

    `path` is the heading path inside the document, without the document title,
    e.g. ["Failure management", "Back up data", "REL09-BP01 Identify and back up all data"].
    `page_start` / `page_end` are 1-based PDF pages; None for HTML.
    """

    path: list[str]
    text: str
    page_start: int | None = None
    page_end: int | None = None


class DocMeta(BaseModel):
    """What the chunker copies into every chunk of one document (from data/rag/manifest.csv)."""

    doc_id: str
    title: str
    doc_type: DocType
    format: Format
    source_url: str
    published: date
    doc_hash: str


class ChunkRecord(BaseModel):
    """One chunk with its metadata: exactly the fields of spec §4, nothing else."""

    model_config = ConfigDict(extra="forbid")

    chunk_id: str
    doc_id: str
    title: str
    doc_type: DocType
    format: Format
    source_url: str
    published: date
    section_path: list[str]
    page_start: int | None
    page_end: int | None
    text: str
    n_tokens: int
    chunk_hash: str
    doc_hash: str
    strategy: Strategy
    pipeline_version: str
