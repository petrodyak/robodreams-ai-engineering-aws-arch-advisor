"""Rebuild the readable mirror of every run: results/runs/jsonl/*.jsonl -> results/runs/md/*.md.

A run keeps its own mirror current (src/extract/pipeline.py). This script is for the two
other cases: run files that predate the mirror, and a change to the Markdown layout in
src/extract/report_md.py, after which every mirror is stale at once.

Usage:  python -m scripts.render_runs_md      (make runs-md)
"""

from src.extract import pipeline
from src.extract.report_md import write_markdown


def main() -> None:
    paths = sorted(pipeline.RUNS_DIR.glob("*.jsonl"))
    for jsonl in paths:
        md = pipeline.RUNS_MD_DIR / f"{jsonl.stem}.md"
        write_markdown(jsonl, md)
        print(f"{jsonl.name} -> {md.relative_to(pipeline.ROOT)}")
    print(f"{len(paths)} run file(s) rendered")


if __name__ == "__main__":
    main()
