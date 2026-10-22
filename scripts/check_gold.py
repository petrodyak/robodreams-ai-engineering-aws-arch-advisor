"""Narrow the manual check of the Golden Set (step 5) to the rows worth looking at.

For each data/gold/<name>.json, compares its Endpoint Rows with the hostnames printed in the
Target Service's chapter of data/raw/<name>.txt, and prints what a person should check in
the PDF: hostnames printed but missing from the file, hostnames in the file that the text
does not print, rows whose hostname lacks their region_code, and region_name values that
disagree with the name the drafts use for that Region code elsewhere. Quota Rows and
quota_table_format are not checked here: they are compared with the PDF by hand.

A hostname printed across several lines ("…us-east-1.am" / "azonaws.com") is rejoined by
reading the Endpoint column of each table: the column's position comes from the table
header, and fragments are concatenated until they form a hostname on an AWS domain. The
parser is a helper for a person, not a judge: anything it cannot read shows up as a
difference to look at, never as a silent pass.

Usage:  python -m scripts.check_gold [name ...]   (default: every gold file)
"""

import json
import re
import sys
from collections import Counter

from scripts.make_gold_drafts import DRAFT_RUN, gold_documents, gold_path
from src.extract import pipeline
from src.extract.schema import AWS_DOMAINS, ServiceDocument, stored_context

_HEADER_RE = re.compile(r"\bEndpoint\b.*\bProtocol\b")
# a run of words separated by single spaces: one table cell (cells are 2+ spaces apart)
_CELL_RE = re.compile(r"\S+(?: \S+)*")
_FRAGMENT_RE = re.compile(r"[A-Za-z0-9.-]+")
_DOMAIN_RE = "|".join(re.escape(d) for d in AWS_DOMAINS)
_HOSTNAME_RE = re.compile(rf"[A-Za-z0-9][A-Za-z0-9.-]*\.(?:{_DOMAIN_RE})")
# page furniture inside tables: "AWS General Reference … Reference guide", "… Version 1.0 337"
_FURNITURE_RE = re.compile(r"AWS General Reference|Version \d+\.\d+ \d+\s*$")
# prose between tables: six or more words separated by single spaces
_PROSE_RE = re.compile(r"\S+(?: \S+){5,}")
_CHAPTER_RE = re.compile(r"^\S.* endpoints and(?: quotas)?\s*$", re.MULTILINE)
SLACK = 4  # columns: layout-mode text shifts a cell by a few characters between lines


def target_chapter(text: str, service: str) -> str:
    """The Target Service's chapter: from its title to the next chapter's title."""
    start = text.find(f"{service} endpoints and")
    if start < 0:
        raise ValueError(f"no chapter title for {service!r}")
    later = [m.start() for m in _CHAPTER_RE.finditer(text) if m.start() > start]
    return text[start : later[0] if later else len(text)]


def printed_hostnames(chapter: str) -> list[str]:
    """Hostnames of the Endpoint column of every table, in print order, wraps rejoined."""
    hosts: list[str] = []
    column: tuple[int, int] | None = (
        None  # (Endpoint start, Protocol start) of the table
    )
    current = ""
    for line in chapter.splitlines():
        header = _HEADER_RE.search(line)
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


def region_names() -> dict[str, Counter]:
    """region_code -> the region_name values the draft run uses for it, over all 30."""
    names: dict[str, Counter] = {}
    for line in (pipeline.RUNS_DIR / f"{DRAFT_RUN}.jsonl").read_text().splitlines():
        output = json.loads(line)["output"] or {"endpoints": []}
        for e in output["endpoints"]:
            names.setdefault(e["region_code"], Counter())[e["region_name"]] += 1
    return names


def check(doc: pipeline.Document, names: dict[str, Counter]) -> list[str]:
    """What to look at in the PDF for one gold file; an empty list means nothing flagged."""
    path = gold_path(doc.file)
    gold = ServiceDocument.model_validate_json(
        path.read_text(), context=stored_context(doc.service)
    )
    printed = printed_hostnames(target_chapter(doc.text(), doc.service))
    in_gold = [e.endpoint for e in gold.endpoints]
    notes = []

    for host in dict.fromkeys(h for h in printed if h not in set(in_gold)):
        notes.append(f"printed, not in gold: {host}")
    for host in dict.fromkeys(h for h in in_gold if h not in set(printed)):
        notes.append(f"in gold, not found in the text: {host}")
    for host, n in Counter(in_gold).items():
        if n > 1:
            notes.append(f"{n} rows with the same hostname: {host}")
    for e in gold.endpoints:
        if e.region_code not in e.endpoint:
            notes.append(
                f"hostname without its region_code {e.region_code}: {e.endpoint}"
            )
        usual, _ = names.get(e.region_code, Counter({e.region_name: 1})).most_common(1)[
            0
        ]
        if e.region_name != usual:
            notes.append(
                f"region_name {e.region_name!r} for {e.region_code}, "
                f"elsewhere {usual!r}: {e.endpoint}"
            )
    return notes


def main(only: list[str]) -> None:
    names = region_names()
    docs = gold_documents()
    flagged = 0
    for file, doc in docs.items():
        if only and not any(file.startswith(o) for o in only):
            continue
        path = gold_path(file)
        if not path.exists():
            print(f"\n{path.name}: missing, run python -m scripts.make_gold_drafts")
            continue
        notes = check(doc, names)
        gold = json.loads(path.read_text())
        print(
            f"\n{path.name}: {len(gold['endpoints'])} endpoints, "
            f"{len(gold['quotas'])} quotas ({gold['quota_table_format']}) — "
            + (f"{len(notes)} to check" if notes else "endpoints match the text")
        )
        for note in notes:
            print(f"  - {note}")
        flagged += bool(notes)
    print(
        f"\n{flagged} file(s) with endpoints to check; quotas and quota_table_format: "
        "by hand against the PDF"
    )


if __name__ == "__main__":
    main(sys.argv[1:])
