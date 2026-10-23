"""Copy the Golden Set drafts from a run into data/gold/ (contract item 10, step 5).

For every manifest row with gold=1, the `output` of its Run Record in
results/runs/<run_id>.jsonl becomes data/gold/<name>.json, which is then corrected by hand
against the PDF. The computed `endpoint_type` is left out: it is derived from the hostname,
would go stale while a hostname is being corrected, and loading a gold file recomputes it.

An existing gold file is never overwritten, so hand corrections are safe to re-run over.

Usage:  python -m scripts.make_gold_drafts [run_id]   (default: claude__v1__t0)
"""

import json
import sys
from pathlib import Path

from src.extract import pipeline
from src.extract.schema import RunRecord, stored_context

GOLD_DIR = pipeline.ROOT / "data" / "gold"
DRAFT_RUN = "claude__v1__t0"  # contract item 10


def gold_documents() -> dict[str, pipeline.Document]:
    """Manifest rows with gold=1, by file name."""
    return {d.file: d for d in pipeline.load_manifest() if d.gold}


def gold_path(file: str, gold_dir: Path = GOLD_DIR) -> Path:
    """data/raw/<name>.pdf -> data/gold/<name>.json (contract item 1)."""
    return gold_dir / Path(file).with_suffix(".json").name


def draft_json(record: RunRecord) -> str:
    data = record.output.model_dump(
        mode="json", exclude={"endpoints": {"__all__": {"endpoint_type"}}}
    )
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def main(run_id: str = DRAFT_RUN) -> None:
    gold = gold_documents()
    run_file = pipeline.RUNS_DIR / f"{run_id}.jsonl"
    records = {}
    for line in run_file.read_text().splitlines():
        file = json.loads(line)["file"]
        if file in gold:
            records[file] = RunRecord.model_validate_json(
                line, context=stored_context(gold[file].service)
            )

    GOLD_DIR.mkdir(parents=True, exist_ok=True)
    for file in gold:
        path = gold_path(file)
        record = records.get(file)
        if path.exists():
            print(f"{path.name}: exists, kept")
        elif record is None or record.output is None:
            print(f"{path.name}: no valid answer in {run_id}, write it by hand")
        else:
            path.write_text(draft_json(record))
            print(f"{path.name}: draft from {run_id} ({record.status.value})")


if __name__ == "__main__":
    main(*sys.argv[1:])
