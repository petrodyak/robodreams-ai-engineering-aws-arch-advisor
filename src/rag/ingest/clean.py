"""Cleaning of extracted text, adapted from the lesson-6 `normalize` (spec §4, §9).

The lesson's `normalize` did two jobs on one string with pages separated by "\\f". Here they are
split, because the PDF extractor cuts sections on page lines before the text is normalized:

- `strip_page_furniture(pages)` works per page: running headers, footers and page numbers;
- `normalize(text)` works on any text: characters, hyphenation, spacing, wrapped lines.
"""

import re
import unicodedata
from collections import Counter

# "Page 2 of 3" or "2/3" (lesson 6). A bare number is not matched here: table values often sit
# on their own line; a bare page number is caught by the numbering rule below instead.
PAGE_NUMBER = re.compile(r"^\s*(page\s+)?\d+\s*(of|/)\s*\d+\s*$", re.IGNORECASE)
# the last line of an AWS PDF page: "<section title> <printed page number>", or just "<n>"
TRAILING_NUMBER = re.compile(r"^(?:.*\S\s+)?(\d{1,4})$")
ZERO_WIDTH = re.compile(
    "[\u200b\u200c\u200d\u2060\ufeff]"
)  # zero-width chars, word joiner, BOM
# lines that must stay on their own line: markdown headings, numbered titles, bullets,
# table rows and Well-Architected best-practice IDs (REL09-BP01 ...)
KEEP_LINE = re.compile(r"^(?:#{1,6} |\d+\.\s|[•\-*] |\||[A-Z]{2,5}\d{2}-BP\d{2}\b)")


def _last_line_index(lines: list[str]) -> int | None:
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip():
            return i
    return None


def strip_page_furniture(pages: list[str]) -> list[str]:
    """Drop running headers and footers from the pages of one PDF.

    1. A line found on more than half of the pages is a header or footer.
    2. A "Page 2 of 3" line is dropped.
    3. AWS PDFs end each page with "<section title> <n>", where n is the printed page number.
       The most common offset between n and the page index is the numbering; the last line of
       a page is dropped only when its number fits that numbering, so a year or a quota value
       at the end of a page is kept.
    One page gives no evidence of what repeats, so a single page is returned unchanged.
    """
    if len(pages) <= 1:
        return list(pages)
    split = [page.split("\n") for page in pages]

    on_pages: Counter[str] = Counter()
    for lines in split:
        on_pages.update({line.strip() for line in lines if line.strip()})
    repeated = {line for line, n in on_pages.items() if n > len(pages) / 2}
    split = [
        [ln for ln in lines if ln.strip() not in repeated and not PAGE_NUMBER.match(ln)]
        for lines in split
    ]

    offsets: dict[int, int] = {}  # page index -> printed number minus index
    for i, lines in enumerate(split):
        last = _last_line_index(lines)
        if last is not None and (m := TRAILING_NUMBER.match(lines[last].strip())):
            offsets[i] = int(m.group(1)) - i
    if offsets:
        offset, count = Counter(offsets.values()).most_common(1)[0]
        if count >= len(pages) / 2:
            for i, value in offsets.items():
                if value == offset:
                    del split[i][_last_line_index(split[i])]
    return ["\n".join(lines) for lines in split]


def unwrap(text: str) -> str:
    """Join lines that a PDF broke inside a sentence (lesson 6).

    A line is joined to the previous one when the previous line is long (>= 60 characters, so
    it was wrapped, not a short title) and does not end a sentence, and neither line is a
    heading, a bullet, a table row or a best-practice ID.
    """
    out: list[str] = []
    for line in text.split("\n"):
        prev = out[-1] if out else ""
        joinable = (
            prev
            and line.strip()
            and len(prev) >= 60
            and not KEEP_LINE.match(line.lstrip())
            and not prev.lstrip().startswith("|")
            and not prev.rstrip().endswith((".", ":", "!", "?"))
        )
        if joinable:
            out[-1] = f"{prev.rstrip()} {line.lstrip()}"
        else:
            out.append(line)
    return "\n".join(out)


def normalize(text: str) -> str:
    """One canonical text form, so that hashing, dedup and chunking see the same thing.

    NFKC (not NFC: NFKC also turns ligatures like "ﬁ" into "fi"), LF line ends, no zero-width
    characters, words hyphenated across lines joined ("secur-\\nity" -> "security", but "e-mail"
    stays), single spaces, wrapped lines joined, at most one blank line between paragraphs.
    """
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = ZERO_WIDTH.sub("", text)
    text = re.sub(r"(\w)-\n([a-z])", r"\1\2", text)
    text = "\n".join(re.sub(r"[ \t]+", " ", ln).strip() for ln in text.split("\n"))
    text = unwrap(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
