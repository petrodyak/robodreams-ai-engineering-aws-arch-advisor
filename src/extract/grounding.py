"""Source-grounded validation (ADR-0005): every extracted row must be printed in the chapter.

The schema and the format checks (ADR-0003) say whether an answer *looks* right. They are
satisfied by a value the model copied from the prompt or the schema — the Target Service
name, a well-formed hostname taken from the prose, a plausible quota name. This module
checks the answer against the document itself, with the same reader a person used to
verify the Golden Set (`scripts/check_gold.py`, step 5):

- G1 — every `endpoint` is a hostname printed in the Endpoint column of an endpoints table of
  the Target Service's chapter (line wraps rejoined). Not grounded by a substring search:
  the prose prints hostnames too, and "AWS account.cloudfront-kvs…" (`010`) is exactly the
  row that must fail.
- G2 — every quota `name` is the Name cell of a row of a Standard Quota Table of the chapter,
  compared with whitespace collapsed, or — for a name the PDF wrapped mid-word
  ("cluster-s" / "ecret pairs") — with all whitespace removed on both sides.
- G3 — `quota_table_format` is `standard` if and only if the chapter prints at least one
  Standard Quota Table header (`Name | Default | Adjustable | Description`, "Adjustable"
  possibly wrapped as "Adjustabl" / "e").

What is deliberately not grounded: `region_name` and `region_code` (the Region columns sit
next to the Endpoint column and a row's cells cannot be paired reliably without a full table
parser), `default` and `description` (free text, wrapped and broken by page furniture), and
completeness — grounding is about nothing invented, recall is measured against the Golden
Set. A violation is a validation failure in the same format as the schema's, so it goes
into the one repair call (contract item 16).
"""

import re
from dataclasses import dataclass, field

from src.extract.schema import AWS_DOMAINS, ServiceDocument, collapse_whitespace

VALIDATION_VERSION = (
    "2"  # "1": schema + ADR-0003 only (runs before step 11); "2": + G1–G3
)

# ---------------------------------------------------------------- the chapter

_CHAPTER_RE = re.compile(r"^\S.* endpoints and(?: quotas)?\s*$", re.MULTILINE)
# page furniture inside tables: "AWS General Reference … Reference guide", "… Version 1.0 337"
_FURNITURE_RE = re.compile(r"AWS General Reference|Version \d+\.\d+ \d+\s*$")
# prose between tables: six or more words separated by single spaces
_PROSE_RE = re.compile(r"\S+(?: \S+){5,}")
# a run of words separated by single spaces: one table cell (cells are 2+ spaces apart)
_CELL_RE = re.compile(r"\S+(?: \S+)*")
SLACK = 4  # columns: layout-mode text shifts a cell by a few characters between lines


def target_chapter(text: str, service: str) -> str:
    """The Target Service's chapter: from its title to the next chapter's title."""
    start = text.find(f"{service} endpoints and")
    if start < 0:
        raise ValueError(f"no chapter title for {service!r}")
    later = [m.start() for m in _CHAPTER_RE.finditer(text) if m.start() > start]
    return text[start : later[0] if later else len(text)]


# ---------------------------------------------------------------- endpoints tables

_ENDPOINT_HEADER_RE = re.compile(r"\bEndpoint\b.*\bProtocol\b")
_FRAGMENT_RE = re.compile(r"[A-Za-z0-9.-]+")
_DOMAIN_RE = "|".join(re.escape(d) for d in AWS_DOMAINS)
_HOSTNAME_RE = re.compile(rf"[A-Za-z0-9][A-Za-z0-9.-]*\.(?:{_DOMAIN_RE})")


def printed_hostnames(chapter: str) -> list[str]:
    """Hostnames of the Endpoint column of every table, in print order, wraps rejoined."""
    hosts: list[str] = []
    column: tuple[int, int] | None = None  # (Endpoint start, Protocol start)
    current = ""
    for line in chapter.splitlines():
        header = _ENDPOINT_HEADER_RE.search(line)
        if header:
            column = (line.index("Endpoint"), line.index("Protocol"))
            current = ""
            continue
        if column is None or _FURNITURE_RE.search(line) or not line.strip():
            continue
        if _PROSE_RE.search(line):  # the table has ended
            column, current = None, ""
            continue
        start, end = column
        cells = [
            m.group()
            for m in _CELL_RE.finditer(line)
            if start - SLACK <= m.start() < end - SLACK
        ]
        # "control. ap-" and "gatewayId      .gateway…": no hostname has a space in it
        fragment = "".join(cells).replace(" ", "")
        if not fragment:
            continue
        if not _FRAGMENT_RE.fullmatch(fragment):
            current = ""
            continue
        current += fragment
        if _HOSTNAME_RE.fullmatch(current):
            hosts.append(current)
            current = ""
    return hosts


# ---------------------------------------------------------------- quota tables

# "Name   Default   Adjustabl(e)   Description" on one line; the "e" of a wrapped
# "Adjustable" sits on the next line and is not needed to recognise the header. All four
# columns are required (GLOSSARY, Standard Quota Table): `038` prints ten tables with
# "Name | Default | Adjustable" or "… | Notes" — those are non_standard (ADR-0001).
_QUOTA_HEADER_RE = re.compile(
    r"\bName\b.{2,}\bDefault\b.{2,}\bAdjustabl.*\bDescription\b"
)


def printed_quota_names(chapter: str) -> list[str]:
    """The Name cell of every row of every Standard Quota Table of the chapter.

    Table lines are indented; a heading or a prose line starts in column 0 and ends the
    table. Inside a table a row's name may wrap over several lines: the lines of one row
    are contiguous and rows are separated by a blank line, so the Name-column text of a
    block of non-blank lines is one name. Page furniture is skipped.
    """
    names: list[str] = []
    name_end: int | None = (
        None  # the Default column's start: the Name column ends there
    )
    block: list[str] = []
    after_header = False

    def flush() -> None:
        if block:
            names.append(collapse_whitespace(" ".join(block)))
            block.clear()

    for line in chapter.splitlines():
        if _QUOTA_HEADER_RE.search(line):
            flush()
            name_end = line.index("Default")
            after_header = True
            continue
        if name_end is None or _FURNITURE_RE.search(line):
            continue
        if not line.strip():
            flush()
            continue
        if not line.startswith(
            " "
        ):  # column 0: a heading or prose, the table has ended
            flush()
            name_end = None
            continue
        cell = line[: max(name_end - SLACK, 0)].strip()
        if not cell or cell.lower() == "e":  # other columns only, or the "e" of a
            continue  # wrapped "Adjustable" under the header
        if after_header and cell[0].islower() and names:
            # A page break cut a row and the header was repeated: a name never starts
            # with a lower-case letter, so this is the tail of the previous row
            block.append(names.pop())
        block.append(cell)
        after_header = False
    flush()
    return [n for n in names if n]


def has_standard_quota_table(chapter: str) -> bool:
    return _QUOTA_HEADER_RE.search(chapter) is not None


def squash(s: str) -> str:
    return re.sub(r"\s+", "", s).lower()


# ---------------------------------------------------------------- the check


@dataclass
class Grounding:
    """What the chapter prints, computed once per document and reused by the repair call."""

    chapter: str
    hostnames: set[str] = field(init=False)
    quota_names: set[str] = field(init=False)  # lower-cased, whitespace collapsed
    quota_names_squashed: set[str] = field(init=False)  # no whitespace at all
    standard_table: bool = field(init=False)

    def __post_init__(self) -> None:
        self.hostnames = set(printed_hostnames(self.chapter))
        names = printed_quota_names(self.chapter)
        self.quota_names = {n.lower() for n in names}
        self.quota_names_squashed = {squash(n) for n in names}
        self.standard_table = has_standard_quota_table(self.chapter)

    @classmethod
    def of(cls, text: str, service: str) -> "Grounding":
        return cls(target_chapter(text, service))

    def errors(self, doc: ServiceDocument) -> list[str]:
        """Violations of G1–G3 as `path: message` lines, like the schema's errors."""
        out: list[str] = []
        for i, e in enumerate(doc.endpoints):
            if e.endpoint not in self.hostnames:
                out.append(
                    f"endpoints.{i}.endpoint: not printed in an endpoints table of the "
                    f"{doc.service!r} chapter: {e.endpoint!r}"
                )
        for i, q in enumerate(doc.quotas):
            if (
                q.name.lower() not in self.quota_names
                and squash(q.name) not in self.quota_names_squashed
            ):
                out.append(
                    f"quotas.{i}.name: not printed in a Standard Quota Table of the "
                    f"chapter: {q.name!r}"
                )
        is_standard = doc.quota_table_format.value == "standard"
        if is_standard and not self.standard_table:
            out.append(
                "quota_table_format: 'standard', but the chapter prints no table with the "
                "columns Name, Default, Adjustable, Description"
            )
        if not is_standard and self.standard_table:
            out.append(
                f"quota_table_format: {doc.quota_table_format.value!r}, but the chapter "
                "prints a table with the columns Name, Default, Adjustable, Description: "
                "that is a Standard Quota Table, return its rows with 'standard'"
            )
        return out
