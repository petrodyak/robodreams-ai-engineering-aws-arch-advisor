"""Chunking (src/rag/ingest/chunk.py): structure-aware chunks and the fixed-size baseline."""

from datetime import date

from src.rag.ingest.chunk import (
    ENC,
    HARD_MAX,
    PIPELINE_VERSION,
    chunk_fixed,
    chunk_stats,
    chunk_structure,
    header,
    n_tokens,
)
from src.rag.models import ChunkRecord, DocMeta, Section

META = DocMeta(
    doc_id="wa-test",
    title="Test Pillar - AWS Well-Architected Framework",
    doc_type="pillar",
    format="pdf",
    source_url="https://example.org/test.pdf",
    published=date(2024, 11, 6),
    doc_hash="sha256:" + "0" * 64,
)


def words(n: int, word: str = "data") -> str:
    """A sentence of about n tokens ("data" is one cl100k token, so is " data")."""
    return " ".join([word.capitalize()] + [word] * (n - 2)) + "."


def section(path: list[str], *paragraphs: str, page: int | None = 1) -> Section:
    text = "\n\n".join([path[-1], *paragraphs]) if path else "\n\n".join(paragraphs)
    return Section(path=path, text=text, page_start=page, page_end=page)


def test_structure_respects_sizes():
    long_path = [
        "Failure management",
        "Back up data",
        "REL09-BP01 Identify and back up all data",
    ]
    sections = [
        section(["Intro"], words(120), words(90)),
        section(long_path, *[words(150) for _ in range(6)]),
        section(long_path + ["Implementation guidance"], words(470)),
    ]
    chunks = chunk_structure(sections, META)
    assert chunks
    for c in chunks:
        assert c.n_tokens == n_tokens(c.text)
        assert c.n_tokens <= HARD_MAX
        assert n_tokens(header(META.title, c.section_path) + "\n" + c.text) <= 512
        assert c.strategy == "structure"
    assert [c.chunk_id for c in chunks] == [
        f"wa-test#{i:04d}" for i in range(len(chunks))
    ]


def test_short_sections_merge_under_parent():
    sections = [
        section(["Failure management", "REL09-BP01 Identify data"], words(100)),
        section(["Failure management", "REL09-BP02 Secure backups"], words(100)),
    ]
    chunks = chunk_structure(sections, META)
    assert len(chunks) == 1
    assert chunks[0].section_path == ["Failure management"]
    assert "REL09-BP01 Identify data" in chunks[0].text
    assert "REL09-BP02 Secure backups" in chunks[0].text


def test_subsection_merges_into_its_best_practice():
    bp = ["Failure management", "REL09-BP01 Identify data"]
    sections = [
        section(bp, words(80)),
        section(bp + ["Implementation guidance"], words(80)),
        section(bp + ["Resources"], words(40)),
    ]
    chunks = chunk_structure(sections, META)
    assert len(chunks) == 1
    assert chunks[0].section_path == bp


def test_no_merge_across_parents():
    sections = [
        section(["Failure management", "REL09-BP01 Identify data"], words(100)),
        section(["Change management", "REL06-BP01 Monitor"], words(100)),
    ]
    chunks = chunk_structure(sections, META)
    assert [c.section_path for c in chunks] == [
        ["Failure management", "REL09-BP01 Identify data"],
        ["Change management", "REL06-BP01 Monitor"],
    ]


def test_no_merge_beyond_max():
    sections = [
        section(["Failure management", "REL09-BP01 Identify data"], words(240)),
        section(["Failure management", "REL09-BP02 Secure backups"], words(240)),
    ]
    assert len(chunk_structure(sections, META)) == 2


def test_oversize_block_split():
    rows = [f"| row {i} | {words(12)} |" for i in range(100)]
    table = "\n".join(rows)
    assert n_tokens(table) > 1500
    chunks = chunk_structure([section(["Quotas"], table)], META)
    assert len(chunks) >= 4
    seen = []
    for c in chunks:
        assert c.n_tokens <= HARD_MAX
        for line in c.text.split("\n"):
            if line.startswith("|"):
                assert line.endswith("|"), line
                seen.append(line)
    assert seen == rows  # every row exactly once, in order, never cut


def test_fixed_windows():
    text = " ".join(["alpha", "beta", "gamma", "delta"] * 250)  # 1,000 one-token words
    tokens = ENC.encode(text)
    assert len(tokens) == 1000
    chunks = chunk_fixed(
        [Section(path=["Body"], text=text)], META, size=400, overlap=60
    )
    assert [c.n_tokens for c in chunks] == [400, 400, 320]
    assert chunks[0].text == ENC.decode(tokens[:400])
    assert chunks[1].text == ENC.decode(tokens[340:740])
    assert all(c.strategy == "fixed" for c in chunks)
    assert [c.chunk_id for c in chunks] == [
        "wa-test#f0000",
        "wa-test#f0001",
        "wa-test#f0002",
    ]


def test_fixed_chunk_knows_its_starting_section():
    sections = [
        Section(path=["A"], text=" ".join(["alpha"] * 300), page_start=1, page_end=2),
        Section(path=["B"], text=" ".join(["beta"] * 300), page_start=3, page_end=4),
    ]
    chunks = chunk_fixed(sections, META, size=400, overlap=60)
    assert chunks[0].section_path == ["A"]
    assert (chunks[0].page_start, chunks[0].page_end) == (1, 4)
    assert chunks[1].section_path == ["B"]


def test_record_fields():
    chunks = chunk_structure([section(["Intro"], words(300))], META)
    chunks += chunk_fixed([section(["Intro"], words(300))], META)
    for c in chunks:
        ChunkRecord.model_validate(c.model_dump())
        assert c.chunk_hash.startswith("sha256:")
        assert c.doc_hash == META.doc_hash
        assert c.pipeline_version == PIPELINE_VERSION == "ingest-v1"


def test_stats_count_mid_sentence():
    chunks = chunk_fixed([section(["Intro"], words(300))], META, size=100, overlap=0)
    chunks[1] = chunks[1].model_copy(update={"text": "continues the sentence."})
    stats = chunk_stats(chunks)
    assert stats["chunks"] == len(chunks)
    assert stats["starts_mid_sentence"] >= 1
    assert stats["max_tokens"] <= 100
    # F27: the "|" count was link titles, not tables, so no table figure is reported
    assert set(stats) == {
        "chunks",
        "starts_mid_sentence",
        "avg_tokens",
        "max_tokens",
    }
