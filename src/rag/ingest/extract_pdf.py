"""PDF -> sections, following the PDF outline (spec §4).

The outline (bookmarks) gives the section titles and their nesting. Its page numbers are not
trusted blindly: in the Well-Architected PDFs, deep entries such as "Implementation guidance" or
"Resources" point to the same early page for every best practice. So each title is looked for as
a line of text: from the entry's page when that page is ahead of the current position, otherwise
forward from the current position, within a few pages. An entry whose title cannot be found
there is skipped, and its text stays in the parent section.

With no outline, sections start at heading-like lines: best-practice IDs (`REL09-BP01 ...`) and
numbered titles (`2.1 Design principles`).
"""

import re
import unicodedata
from bisect import bisect_left
from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO

from pypdf import PdfReader

from src.rag.ingest.clean import normalize, strip_page_furniture
from src.rag.models import Section

SEARCH_PAGES = 3  # how far past the current page a misplaced title is looked for
SKIP_TITLES = {"table of contents", "contents"}
COVER_PAGES = 15  # an outline entry named like the document only marks the front matter this early
TOC_LINE = re.compile(r"^.*\S\s*\.{5,}\s*\d+\s*$")  # "Introduction ........ 1"
HEADING_LINE = re.compile(r"^(?:[A-Z]{2,5}\d{2}-BP\d{2}\b|\d+(?:\.\d+)*\s+[A-Z])")


@dataclass
class _Cut:
    line: int  # index into the flat line list where the section starts
    title_lines: int  # how many lines the title occupies (0: cut at a page start)
    path: list[str]
    keep: bool = True
    cover: bool = False  # the cover page entry (title, copyright and trademark notice)


def _collapse(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).split())


def _outline(reader: PdfReader) -> list[tuple[int, str, int]]:
    """(level, title, 0-based page) for every outline entry, in outline order."""
    out: list[tuple[int, str, int]] = []

    def walk(items: list, level: int) -> None:
        for item in items:
            if isinstance(item, list):
                walk(item, level + 1)
                continue
            page = reader.get_destination_page_number(item)
            if page is not None and page >= 0:
                out.append((level, _collapse(item.title), page))

    walk(reader.outline, 0)
    return out


def _find_title(lines: list[tuple[int, str]], title: str, start: int, end: int):
    """First line in [start, end) that is the title, possibly wrapped over up to 3 lines."""
    for k in range(start, min(end, len(lines))):
        text = _collapse(lines[k][1])
        if not text or not title.startswith(text):
            continue
        for extra in range(3):
            if text == title:
                return k, extra + 1
            if k + extra + 1 >= len(lines):
                break
            text = _collapse(text + " " + lines[k + extra + 1][1])
            if not title.startswith(text):
                break
    return None


def _cuts_from_outline(lines, page_first, entries, doc_title) -> list[_Cut]:
    # the outline names the document as in its metadata ("Reliability Pillar - AWS Well-Architected
    # Framework"), or as the part before " - " ("AWS Well-Architected Framework" for the metadata
    # title "AWS Well-Architected Framework - Framework"); neither belongs in a section path
    names = {doc_title, doc_title.split(" - ")[0]} - {""}
    title_cuts: list[int] = []
    cuts: list[_Cut] = []
    stack: list[tuple[int, str]] = []
    pos = 0
    n_pages = len(page_first) - 1
    for level, title, page in entries:
        pos_page = lines[pos][0] if pos < len(lines) else n_pages - 1
        start = page_first[page] if page > pos_page else pos
        # the abstract page named like the document can sit after a long table of contents
        window = COVER_PAGES if title in names else SEARCH_PAGES
        end = (
            page_first[min(lines[start][0] + window + 1, n_pages)]
            if start < len(lines)
            else start
        )
        hit = _find_title(lines, title, start, end)
        if hit is None:
            if page <= pos_page:
                continue  # the title is not where the outline says, and not ahead either
            hit = (page_first[page], 0)
        line, title_lines = hit
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, title))
        path = [t for _, t in stack if t not in names]
        keep = not any(t.casefold() in SKIP_TITLES for _, t in stack)
        cover = title in names and lines[line][0] == 0
        if level == 0 and title in names and page < COVER_PAGES:
            title_cuts.append(len(cuts))
        cuts.append(_Cut(line, title_lines, path, keep and not cover, cover))
        pos = line + title_lines
    # the cover and the table of contents come before the last entry named like the document
    # (the pillars name their cover "Reliability Pillar" and their abstract page by the full title)
    if title_cuts:
        for cut in cuts[: title_cuts[-1]]:
            cut.keep = False
    return cuts


def _cuts_from_patterns(lines) -> list[_Cut]:
    cuts = []
    for k, (_, text) in enumerate(lines):
        title = _collapse(text)
        if HEADING_LINE.match(title) and len(title) <= 120 and not title.endswith("."):
            cuts.append(_Cut(k, 1, [title]))
    return cuts


def extract_pdf(path: Path | BinaryIO) -> list[Section]:
    """Sections of one PDF (a path or an open binary file); each section's text starts with its
    title line."""
    reader = PdfReader(path)
    pages = strip_page_furniture([page.extract_text() or "" for page in reader.pages])
    lines = [
        (i, line)
        for i, page in enumerate(pages)
        for line in page.split("\n")
        if not TOC_LINE.match(line)
    ]
    page_of = [p for p, _ in lines]
    page_first = [bisect_left(page_of, p) for p in range(len(pages) + 1)]
    doc_title = _collapse(str((reader.metadata or {}).get("/Title") or ""))

    entries = _outline(reader)
    cuts = _cuts_from_outline(lines, page_first, entries, doc_title) if entries else []
    if not cuts:
        cuts = _cuts_from_patterns(lines)
    if not cuts or cuts[0].line > 0:
        # text before the first heading: kept unless it is the rest of the cover page. In the
        # archived 2020 Framework edition (whose cover entry is lost with the running header) it
        # is the page that says "This paper has been archived. The latest version is at: ..."
        cuts.insert(0, _Cut(0, 0, [], keep=not (cuts and cuts[0].cover)))

    sections: list[Section] = []
    for i, cut in enumerate(cuts):
        if not cut.keep:
            continue
        stop = cuts[i + 1].line if i + 1 < len(cuts) else len(lines)
        body_lines = lines[cut.line + cut.title_lines : stop]
        body = normalize("\n".join(text for _, text in body_lines))
        if not body:
            continue  # a heading with nothing under it lives on in its children's paths
        text = f"{cut.path[-1]}\n\n{body}" if cut.path else body
        used = [p for p, t in body_lines if t.strip()]
        sections.append(
            Section(
                path=cut.path,
                text=text,
                page_start=lines[cut.line][0] + 1,
                page_end=(used[-1] if used else lines[cut.line][0]) + 1,
            )
        )
    return sections
