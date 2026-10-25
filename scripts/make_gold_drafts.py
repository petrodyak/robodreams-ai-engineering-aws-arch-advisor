"""Copy the Golden Set drafts from a run into the set's gold folder (contract item 10).

For every manifest row with gold=1, the `output` of its Run Record in
results/runs/jsonl/<run_id>.jsonl becomes <gold_dir>/<name>.json, which is then corrected by
hand against the PDF. The computed `endpoint_type` is left out: it is derived from the
hostname, would go stale while a hostname is being corrected, and loading a gold file
recomputes it. An existing gold file is never overwritten, so hand corrections are safe to
re-run over.

Working Set (step 5): data/gold/ from `claude__v1__t0`. Held-out Set (step 12):
data/holdout/gold/ from `claude__v2__t0__holdout__gold__val2` — a draft whose every row is
grounded in the chapter (ADR-0005), unlike the step 5 drafts.

Usage:  python -m scripts.make_gold_drafts [--set raw|holdout] [--run <run_id>]
"""

import argparse
import json
from pathlib import Path

from src.extract import pipeline
from src.extract.schema import RunRecord, stored_context

GOLD_DIR = pipeline.WORKING_SET.gold_dir
DRAFT_RUN = "claude__v1__t0"  # contract item 10
DRAFT_RUNS = {
    "raw": DRAFT_RUN,
    "holdout": "claude__v2__t0__holdout__gold__val2",
}


def gold_documents(
    doc_set: pipeline.DocumentSet = pipeline.WORKING_SET,
) -> dict[str, pipeline.Document]:
    """Manifest rows with gold=1, by file name."""
    return {d.file: d for d in pipeline.load_manifest(doc_set.manifest) if d.gold}


def gold_path(file: str, gold_dir: Path = GOLD_DIR) -> Path:
    """<set>/<name>.pdf -> <gold_dir>/<name>.json (contract item 1)."""
    return gold_dir / Path(file).with_suffix(".json").name


def draft_json(record: RunRecord) -> str:
    data = record.output.model_dump(
        mode="json", exclude={"endpoints": {"__all__": {"endpoint_type"}}}
    )
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def main(
    doc_set: pipeline.DocumentSet = pipeline.WORKING_SET, run_id: str | None = None
) -> None:
    run_id = run_id or DRAFT_RUNS[doc_set.name]
    gold = gold_documents(doc_set)
    gold_dir = doc_set.gold_dir
    run_file = pipeline.RUNS_DIR / f"{run_id}.jsonl"
    records = {}
    for line in run_file.read_text().splitlines():
        file = json.loads(line)["file"]
        if file in gold:
            records[file] = RunRecord.model_validate_json(
                line, context=stored_context(gold[file].service)
            )

    gold_dir.mkdir(parents=True, exist_ok=True)
    for file in gold:
        path = gold_path(file, gold_dir)
        record = records.get(file)
        if path.exists():
            print(f"{path.name}: exists, kept")
        elif record is None or record.output is None:
            print(f"{path.name}: no valid answer in {run_id}, write it by hand")
        else:
            path.write_text(draft_json(record))
            print(f"{path.name}: draft from {run_id} ({record.status.value})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--set", choices=sorted(pipeline.DOCUMENT_SETS), default="raw")
    parser.add_argument(
        "--run", help="run id to draft from (default: the set's draft run)"
    )
    args = parser.parse_args()
    main(pipeline.DOCUMENT_SETS[args.set], args.run)
