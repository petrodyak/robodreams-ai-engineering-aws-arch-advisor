"""Narrow the manual check of the Golden Set (step 5) to the rows worth looking at.

For each data/gold/<name>.json, compares its Endpoint Rows with the hostnames printed in the
Target Service's chapter of data/raw/<name>.txt, and prints what a person should check in
the PDF: hostnames printed but missing from the file, hostnames in the file that the text
does not print, rows whose hostname lacks their region_code, and region_name values that
disagree with the name the drafts use for that Region code elsewhere. Quota Rows and
quota_table_format are not checked here: they are compared with the PDF by hand.

A hostname printed across several lines ("…us-east-1.am" / "azonaws.com") is rejoined by
reading the Endpoint column of each table (src/extract/grounding.py, shared with the
pipeline's grounding since step 11). Quota names are compared with the Name column of every
Standard Quota Table the same way. The readers are helpers for a person, not a judge:
anything they cannot read shows up as a difference to look at, never as a silent pass.

Usage:  python -m scripts.check_gold [--set raw|holdout] [name ...]   (default: every gold file)
"""

import json
import sys
from collections import Counter

from scripts.make_gold_drafts import DRAFT_RUN, gold_documents, gold_path
from src.extract import pipeline
from src.extract.grounding import (
    printed_hostnames,
    printed_quota_names,
    squash,
    target_chapter,
)
from src.extract.schema import ServiceDocument, stored_context

# The readers moved to src/extract/grounding.py in step 11 (ADR-0005): the pipeline now
# validates every answer with them, and this script keeps using the same ones.


def region_names() -> dict[str, Counter]:
    """region_code -> the region_name values the draft run uses for it, over all 30."""
    names: dict[str, Counter] = {}
    for line in (pipeline.RUNS_DIR / f"{DRAFT_RUN}.jsonl").read_text().splitlines():
        output = json.loads(line)["output"] or {"endpoints": []}
        for e in output["endpoints"]:
            names.setdefault(e["region_code"], Counter())[e["region_name"]] += 1
    return names


def check(
    doc: pipeline.Document,
    names: dict[str, Counter],
    doc_set: pipeline.DocumentSet = pipeline.WORKING_SET,
) -> list[str]:
    """What to look at in the PDF for one gold file; an empty list means nothing flagged."""
    path = gold_path(doc.file, doc_set.gold_dir)
    gold = ServiceDocument.model_validate_json(
        path.read_text(), context=stored_context(doc.service)
    )
    printed = printed_hostnames(target_chapter(doc.text(doc_set.dir), doc.service))
    in_gold = [e.endpoint for e in gold.endpoints]
    notes = []

    for host in dict.fromkeys(h for h in printed if h not in set(in_gold)):
        notes.append(f"printed, not in gold: {host}")
    for host in dict.fromkeys(h for h in in_gold if h not in set(printed)):
        notes.append(f"in gold, not found in the text: {host}")
    for host, n in Counter(in_gold).items():
        if n > 1:
            notes.append(f"{n} rows with the same hostname: {host}")
    printed_names = printed_quota_names(
        target_chapter(doc.text(doc_set.dir), doc.service)
    )
    gold_names = [q.name for q in gold.quotas]
    # the same two comparisons as grounding G2: whitespace collapsed, or none at all for a
    # name the PDF wrapped mid-word ("transacti ons")
    printed_keys = {squash(n) for n in printed_names}
    gold_keys = {squash(n) for n in gold_names}
    for name in dict.fromkeys(n for n in printed_names if squash(n) not in gold_keys):
        notes.append(f"quota printed in a Standard Quota Table, not in gold: {name}")
    for name in dict.fromkeys(n for n in gold_names if squash(n) not in printed_keys):
        notes.append(f"quota in gold, not found as printed: {name}")
    if printed_names and gold.quota_table_format.value != "standard":
        notes.append(
            f"quota_table_format is {gold.quota_table_format.value!r} but the chapter "
            f"prints {len(printed_names)} Standard Quota Table row(s)"
        )
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


def main(only: list[str], doc_set: pipeline.DocumentSet = pipeline.WORKING_SET) -> None:
    names = region_names()
    docs = gold_documents(doc_set)
    flagged = 0
    for file, doc in docs.items():
        if only and not any(file.startswith(o) for o in only):
            continue
        path = gold_path(file, doc_set.gold_dir)
        if not path.exists():
            print(f"\n{path.name}: missing, run python -m scripts.make_gold_drafts")
            continue
        notes = check(doc, names, doc_set)
        gold = json.loads(path.read_text())
        print(
            f"\n{path.name}: {len(gold['endpoints'])} endpoints, "
            f"{len(gold['quotas'])} quotas ({gold['quota_table_format']}) — "
            + (f"{len(notes)} to check" if notes else "endpoints match the text")
        )
        for note in notes:
            print(f"  - {note}")
        flagged += bool(notes)
    print(f"\n{flagged} file(s) with rows to check against the PDF")


if __name__ == "__main__":
    argv = sys.argv[1:]
    doc_set = pipeline.WORKING_SET
    if "--set" in argv:
        i = argv.index("--set")
        doc_set = pipeline.DOCUMENT_SETS[argv[i + 1]]
        argv = argv[:i] + argv[i + 2 :]
    main(argv, doc_set)
