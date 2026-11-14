"""Deduplication helpers (src/rag/ingest/dedup.py): exact content hash and near-duplicates."""

from src.rag.ingest.dedup import content_hash, jaccard, near_duplicates, shingles


def test_hash_ignores_spacing():
    assert content_hash("a  b\r\nc") == content_hash("a b c")
    assert content_hash("a b c").startswith("sha256:")
    assert len(content_hash("x")) == len("sha256:") + 64
    assert content_hash("a b c") != content_hash("a b d")


def test_shingles_and_jaccard():
    assert shingles("A b c d e f") == {
        ("a", "b", "c", "d", "e"),
        ("b", "c", "d", "e", "f"),
    }
    assert jaccard({1, 2}, {2, 3}) == 1 / 3
    assert jaccard(set(), set()) == 0.0


def test_near_duplicates():
    words = [f"w{i}" for i in range(200)]
    a = " ".join(words)
    b = " ".join(words[:-1] + ["changed"])  # 1 word of 200 differs
    c = " ".join(f"other{i}" for i in range(200))
    pairs = near_duplicates({"doc-a": a, "doc-b": b, "doc-c": c})
    assert len(pairs) == 1
    (x, y, score) = pairs[0]
    assert (x, y) == ("doc-a", "doc-b")
    assert score >= 0.8
