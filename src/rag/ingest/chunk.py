"""Chunking: structure-aware chunks and the fixed-size baseline (spec §4, ADR-0007).

Structure-aware:
1. Short sections are merged: while a chunk is below MIN_TOKENS, the next section joins it if it
   lies under the same parent (a sibling, or a subsection such as "Implementation guidance") and
   the result still fits. The merged chunk's path is the common prefix of the merged paths.
2. Each section is packed: whole paragraphs, lists and tables up to the limit. A block above the
   hard maximum is cut at lines, then sentences, then tokens (lesson 6 `split_block`).
3. The limit leaves room for the Contextual Header: header + text fit the 512 tokens the
   embedding model reads.

Fixed: windows of `size` tokens with `overlap` tokens of overlap over the whole document,
ignoring structure: the baseline the retrieval eval compares against.
"""

import re

import tiktoken

from src.rag.ingest.dedup import content_hash
from src.rag.models import ChunkRecord, DocMeta, Section

MIN_TOKENS = 250
MAX_TOKENS = 450
HARD_MAX = 480
EMBED_LIMIT = 512  # BAAI/bge-small-en-v1.5 reads at most 512 tokens
PIPELINE_VERSION = "ingest-v1"

ENC = tiktoken.get_encoding("cl100k_base")


def n_tokens(text: str) -> int:
    """Tokens as cl100k_base counts them: an approximation of the embedding tokenizer."""
    return len(ENC.encode(text))


def header(title: str, path: list[str]) -> str:
    """Contextual Header: "<document title> > <p1> > <p2>"."""
    return " > ".join([title, *path])


def _common_prefix(a: list[str], b: list[str]) -> list[str]:
    out = []
    for x, y in zip(a, b, strict=False):
        if x != y:
            break
        out.append(x)
    return out


def _merge_short(sections: list[Section]) -> list[Section]:
    merged: list[Section] = []
    parent: list[
        str
    ] = []  # the parent under which the last merged section may still grow
    for s in sections:
        last = merged[-1] if merged else None
        if (
            last is not None
            and n_tokens(last.text) < MIN_TOKENS
            and s.path[: len(parent)] == parent
            and n_tokens(last.text + "\n\n" + s.text) <= MAX_TOKENS
        ):
            pages = [
                p
                for p in (last.page_start, last.page_end, s.page_start, s.page_end)
                if p
            ]
            merged[-1] = Section(
                path=_common_prefix(last.path, s.path),
                text=last.text + "\n\n" + s.text,
                page_start=min(pages) if pages else None,
                page_end=max(pages) if pages else None,
            )
            parent = _common_prefix(parent, s.path)
        else:
            merged.append(s)
            parent = s.path[:-1]
    return merged


def _cut_tokens(text: str, size: int) -> list[str]:
    tokens = ENC.encode(text)
    return [ENC.decode(tokens[i : i + size]) for i in range(0, len(tokens), size)]


def split_block(block: str, max_tokens: int) -> list[str]:
    """Cut a block that does not fit at the safest place: lines -> sentences -> tokens."""
    if n_tokens(block) <= max_tokens:
        return [block]
    pieces: list[str] = []
    for line in block.split("\n"):
        if n_tokens(line) <= max_tokens:
            pieces.append(line)
            continue
        for sentence in re.split(r"(?<=[.!?])\s+", line):
            if n_tokens(sentence) <= max_tokens:
                pieces.append(sentence)
            else:
                pieces += _cut_tokens(sentence, max_tokens)
    return pieces


def _pack(text: str, limit: int, hard: int) -> list[str]:
    """Pack whole blocks up to limit; only a block above hard is split."""
    pieces: list[tuple[str, str]] = []  # (piece, separator before it)
    for block in (b.strip() for b in text.split("\n\n")):
        if not block:
            continue
        if n_tokens(block) <= hard:
            pieces.append((block, "\n\n"))
        else:
            parts = split_block(block, limit)
            pieces += [(p, "\n" if k else "\n\n") for k, p in enumerate(parts)]

    chunks: list[str] = []
    cur, cur_has_body = "", False
    for piece, sep in pieces:
        candidate = cur + sep + piece if cur else piece
        # a chunk that is only its heading line may take a block up to the hard maximum
        fits = n_tokens(candidate) <= (limit if cur_has_body else hard)
        if cur and not fits:
            chunks.append(cur)
            cur, cur_has_body = piece, False
        else:
            cur = candidate
        cur_has_body = cur_has_body or "\n" in cur or n_tokens(cur) > 40
    if cur:
        chunks.append(cur)
    return chunks


def _record(
    meta: DocMeta,
    chunk_id: str,
    strategy: str,
    section: Section,
    text: str,
    tokens: int,
):
    return ChunkRecord(
        chunk_id=chunk_id,
        doc_id=meta.doc_id,
        title=meta.title,
        doc_type=meta.doc_type,
        format=meta.format,
        source_url=meta.source_url,
        published=meta.published,
        section_path=section.path,
        page_start=section.page_start,
        page_end=section.page_end,
        text=text,
        n_tokens=tokens,
        chunk_hash=content_hash(text),
        doc_hash=meta.doc_hash,
        strategy=strategy,
        pipeline_version=PIPELINE_VERSION,
    )


def chunk_structure(sections: list[Section], meta: DocMeta) -> list[ChunkRecord]:
    """Structure-aware chunks of one document; ids "<doc_id>#0000", "<doc_id>#0001", ..."""
    records: list[ChunkRecord] = []
    for s in _merge_short(sections):
        room = (
            EMBED_LIMIT - n_tokens(header(meta.title, s.path)) - 1
        )  # "\n" after the header
        hard = min(HARD_MAX, room)
        limit = min(MAX_TOKENS, hard)
        for text in _pack(s.text, limit, hard):
            chunk_id = f"{meta.doc_id}#{len(records):04d}"
            records.append(
                _record(meta, chunk_id, "structure", s, text, n_tokens(text))
            )
    return records


def chunk_fixed(
    sections: list[Section], meta: DocMeta, size: int = 400, overlap: int = 60
) -> list[ChunkRecord]:
    """Fixed windows over the whole document; ids "<doc_id>#f0000", ...

    A window's section_path is the section it starts in; its pages run from that section's first
    page to the last page of the section it ends in.
    """
    sep = ENC.encode("\n\n")
    tokens: list[int] = []
    owner: list[int] = []  # section index of every token
    for i, s in enumerate(sections):
        if tokens:
            tokens += sep
            owner += [i] * len(sep)
        encoded = ENC.encode(s.text)
        tokens += encoded
        owner += [i] * len(encoded)

    records: list[ChunkRecord] = []
    start = 0
    while start < len(tokens):
        window = tokens[start : start + size]
        first, last = sections[owner[start]], sections[owner[start + len(window) - 1]]
        span = Section(
            path=first.path,
            text="",
            page_start=first.page_start,
            page_end=last.page_end,
        )
        chunk_id = f"{meta.doc_id}#f{len(records):04d}"
        records.append(
            _record(meta, chunk_id, "fixed", span, ENC.decode(window), len(window))
        )
        if start + size >= len(tokens):
            break
        start += size - overlap
    return records


def chunk_stats(chunks: list[ChunkRecord]) -> dict:
    """How often a chunk starts mid-sentence, and the chunk sizes (lesson 6).

    The lesson's "cut tables" count is not kept (F27): it counted any line with a "|" that is not
    a whole table row, and in this corpus those are link titles ("... | AWS Big Data Blog"), not
    tables. PDF tables reach the chunker as plain lines, so there is nothing to count them by.
    """
    mid = sum(1 for c in chunks if c.text[:1].islower())
    sizes = [c.n_tokens for c in chunks] or [0]
    return {
        "chunks": len(chunks),
        "starts_mid_sentence": mid,
        "avg_tokens": round(sum(sizes) / len(sizes)),
        "max_tokens": max(sizes),
    }
