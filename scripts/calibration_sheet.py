"""`make calibration-sheet`: ≥ 12 answers of a run for Petro to label by hand (spec §7, step 19).

The answers are the answerable items of the run, the deterministic failures first (then the lowest
key-fact share), so the v1 failures are among the labelled ones. Writes:
- `evals/labels/calibration_sheet.md`: per answer the question, the reference answer, every claim with
  the text of the sources it cites, and two boxes to tick (pass / fail, claim not in its source yes / no);
- `evals/labels/calibration.jsonl`: one row per answer with the human fields null; the ticks of the
  sheet are copied into it after labelling.

It refuses to overwrite a calibration.jsonl that already holds a label. With `--append` it keeps the
labelled rows and adds `--rows` answers of another run (`--run`) to the end of both files, skipping
items already labelled for that run; the judges then read each label from its own run.
"""

import argparse
import json
import sys
from pathlib import Path

from evals.answers import load_run
from evals.calibration import CalibrationRow, load_calibration
from evals.scorers import key_facts, passed
from evals.testset import TestItem, load_testset
from src.rag.answer import AnswerRecord
from src.rag.config import load_config

TESTSET = Path("evals/testset.jsonl")
CHUNKS = Path("data/rag/chunks.jsonl")
SHEET = Path("evals/labels/calibration_sheet.md")
LABELS = Path("evals/labels/calibration.jsonl")
MIN_ROWS = 12

HEADER = [
    "Label each answer by hand; the judges are checked against these labels (spec §7).",
    "",
    "- **Correct?** Pass when the answer states the facts of the reference answer and does not",
    "  contradict it. Wording, order and extra detail do not matter.",
    "- **Claim not in its source?** Yes when at least one claim cannot be found in the source it cites",
    "  (shown under the claim), even if the claim is true.",
    "",
    "Tick one box on each line. The answers that the deterministic scorers failed come first.",
    "",
]


def pick(
    items: list[TestItem], recs: list[AnswerRecord], n: int, skip: set[str]
) -> list[tuple[bool, float, TestItem, AnswerRecord]]:
    """The n answerable answers not in `skip`: deterministic failures first, then fewest key facts."""
    answered = [
        (passed(it, rec), key_facts(it, rec) or 0.0, it, rec)
        for it, rec in zip(items, recs)
        if it.answerable and it.id not in skip
    ]
    answered.sort(key=lambda t: (t[0], t[1], t[2].id))
    return answered[:n]


def _run_note(run: str) -> str:
    """Heading note for an appended answer: which run, and how many sources its model saw."""
    k = run.rsplit("__k", 1)[-1]
    return f" — answer of run k={k} (only the top {k} sources in context) `{run}`"


def render(chosen, run: str | None, chunks: dict) -> list[str]:
    out = []
    for ok, share, it, rec in chosen:
        out += [
            f"## {it.id} ({it.kind})" + ("" if run is None else _run_note(run)),
            "",
            "- Correct?          [ ] pass   [ ] fail",
            "- Claim not in its source? [ ] yes    [ ] no",
            "",
            f"**Q:** {it.question}",
            "",
            f"**Reference answer:** {it.expected_answer}",
            "",
            f"*Deterministic scorers: {'pass' if ok else 'fail'}, key facts {share:.2f}.*",
            "",
            "**Answer, claim by claim:**",
            "",
        ]
        cited = {}
        for n, claim in enumerate(rec.claims, 1):
            out += [f"{n}. {claim.text} {''.join(f'[{c}]' for c in claim.citations)}"]
            cited.update({ref.label: ref for ref in claim.refs})
        out += ["", "**Cited sources, full text:**", ""]
        for label in sorted(cited, key=lambda s: int(s[1:])):
            ref = cited[label]
            text = " ".join(chunks[ref.chunk_id]["text"].split())
            path = " > ".join(ref.section_path) or "(no section)"
            out += [
                f"> **[{label}]** `{ref.chunk_id}` {ref.title} > {path}",
                ">",
                f"> {text}",
                "",
            ]
        out += ["**Note (optional):** ", "", "---", ""]
    return out


def main() -> None:
    cfg = load_config()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--run",
        default=f"{cfg.answer_model}__{cfg.prompt_version}__{cfg.answer_effort}__k{cfg.k}",
    )
    parser.add_argument("--rows", type=int, default=MIN_ROWS)
    parser.add_argument("--append", action="store_true")
    args = parser.parse_args()

    existing = load_calibration(LABELS)
    if not args.append and any(r.human_pass is not None for r in existing):
        sys.exit(f"{LABELS} already holds labels: move it aside first, or use --append")
    if args.append and not SHEET.exists():
        sys.exit(f"{SHEET}: no sheet to append to; run without --append first")

    testset = load_testset(TESTSET)
    chunks = {
        c["chunk_id"]: c
        for c in map(json.loads, CHUNKS.read_text(encoding="utf-8").splitlines())
    }
    run_file = Path(f"evals/results/{args.run}.jsonl")
    rows = {r["id"]: r for r in load_run(run_file, testset)}
    recs = [
        AnswerRecord.model_validate({k: v for k, v in rows[it.id].items() if k != "id"})
        for it in testset
    ]
    skip = (
        {r.item_id for r in existing if r.run_id == args.run} if args.append else set()
    )
    chosen = pick(testset, recs, args.rows, skip)

    new_rows = [
        CalibrationRow(
            item_id=it.id,
            run_id=args.run,
            human_pass=None,
            human_unsupported=None,
            labelled_on=None,
        )
        for _, _, it, _ in chosen
    ]
    if args.append:
        SHEET.write_text(
            SHEET.read_text(encoding="utf-8").rstrip("\n")
            + "\n\n"
            + "\n".join(render(chosen, args.run, chunks)),
            encoding="utf-8",
        )
        all_rows = existing + new_rows
    else:
        title = [f"# Calibration sheet — run `{args.run}`", ""]
        SHEET.write_text(
            "\n".join(title + HEADER + render(chosen, None, chunks)), encoding="utf-8"
        )
        all_rows = new_rows
    LABELS.write_text(
        "".join(r.model_dump_json() + "\n" for r in all_rows), encoding="utf-8"
    )
    print(f"{len(chosen)} answers of {args.run} → {SHEET}, rows → {LABELS}")


if __name__ == "__main__":
    main()
