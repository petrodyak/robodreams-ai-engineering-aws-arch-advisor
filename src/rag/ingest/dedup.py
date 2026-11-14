"""Deduplication, adapted from lesson 6 (spec §4, §9).

- exact: `content_hash` of the text, so whitespace and line endings do not change it;
- near: Jaccard similarity of word 5-shingles between documents.
"""

import hashlib
import re
import unicodedata
from itertools import combinations

from src.rag.ingest.clean import ZERO_WIDTH

NEAR_DUP_JACCARD = 0.8


def content_hash(text: str) -> str:
    """Hash the content, not the bytes: "sha256:" + hex of the whitespace-collapsed NFKC text."""
    canonical = " ".join(
        ZERO_WIDTH.sub("", unicodedata.normalize("NFKC", text)).split()
    )
    return "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def shingles(text: str, k: int = 5) -> set[tuple[str, ...]]:
    """All runs of k consecutive lower-cased words: the near-duplicate fingerprint."""
    words = re.findall(r"\w+", text.casefold())
    return {tuple(words[i : i + k]) for i in range(max(1, len(words) - k + 1))}


def jaccard(a: set, b: set) -> float:
    """Shared items / all items; 0.0 for two empty sets."""
    return len(a & b) / len(a | b) if a | b else 0.0


def near_duplicates(
    texts: dict[str, str], threshold: float = NEAR_DUP_JACCARD
) -> list[tuple[str, str, float]]:
    """Pairs of documents whose shingles overlap at or above threshold.

    Each pair is reported once, in the order of `texts`, with the score rounded to 3 digits.
    O(n²) over documents is fine for a corpus of 34.
    """
    sets = {doc_id: shingles(text) for doc_id, text in texts.items()}
    pairs = []
    for a, b in combinations(sets, 2):
        score = jaccard(sets[a], sets[b])
        if score >= threshold:
            pairs.append((a, b, round(score, 3)))
    return pairs
