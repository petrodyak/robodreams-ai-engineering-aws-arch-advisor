"""One-off: add `prompt_sha` / `schema_sha` to the eight HW 1 run files made before step 10.

Contract item 12 (24.10) requires every Run Record to pin the exact prompt file and the exact
JSON Schema the model saw. The runs of 21.10–24.10 predate the fields; their provenance is
recovered from git — the commit `main` was at when each run was made (the step log in
docs/Implementation_steps.md) — by hashing the files as they were at that commit, with the
same `short_sha` the pipeline uses now. The mapping below is the evidence for finding F17:
`qwen2.5-7b__v1__t0` carries the v1 prompt with the enum schema.

Usage, from the repo root, once: `uv run python -m scripts.backfill_provenance`
Idempotent: a record that already has both fields is left as is.
"""

import json
import subprocess

from src.extract.llm import short_sha
from src.extract.pipeline import ROOT, RUNS_DIR, RUNS_MD_DIR
from src.extract.report_md import write_markdown

SCHEMA_PATH = (
    "docs/service-document.schema.json"  # the sent schema, kept in Git by make schema
)

# run id -> (commit main was at, prompt file). Dates: Implementation_steps.md, steps 4, 6, 8.
RUNS = {
    "claude__v1__t0": ("15e8d1a", "prompts/extract_v1.txt"),  # 21.10, PR #10
    "claude__v1__t05__gold": (
        "a7df1d4",
        "prompts/extract_v1.txt",
    ),  # 23.10, after PR #13
    "qwen2.5-7b__v1__t0__gold": ("a7df1d4", "prompts/extract_v1.txt"),  # 23.10
    "qwen2.5-7b__v1__t05__gold": ("a7df1d4", "prompts/extract_v1.txt"),  # 23.10–24.10
    "claude__v2__t0": ("df1a8cd", "prompts/extract_v2.txt"),  # 24.10, after PR #16
    "qwen2.5-7b__v2__t0": (
        "ea70c6e",
        "prompts/extract_v2.txt",
    ),  # 24.10 night, after PR #17
    "qwen2.5-7b__v2__t05": ("ea70c6e", "prompts/extract_v2.txt"),  # 24.10 night
    "qwen2.5-7b__v1__t0": ("ea70c6e", "prompts/extract_v1.txt"),  # 24.10 night: F17
}


def file_at(commit: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{commit}:{path}"], cwd=ROOT, check=True, capture_output=True
    ).stdout


def backfill(run_id: str, commit: str, prompt_path: str) -> tuple[str, str, int]:
    prompt_sha = short_sha(file_at(commit, prompt_path))
    schema_sha = short_sha(file_at(commit, SCHEMA_PATH))
    path = RUNS_DIR / f"{run_id}.jsonl"
    out, changed = [], 0
    for line in path.read_text().split("\n"):
        if not line.strip():
            continue
        rec = json.loads(line)
        if "prompt_sha" not in rec or "schema_sha" not in rec:
            # insert after prompt_version so the stored key order matches RunRecord
            items = list(rec.items())
            i = [k for k, _ in items].index("prompt_version") + 1
            items[i:i] = [("prompt_sha", prompt_sha), ("schema_sha", schema_sha)]
            rec = dict(items)
            changed += 1
        out.append(json.dumps(rec, ensure_ascii=False))
    path.write_text("\n".join(out) + "\n")
    write_markdown(path, RUNS_MD_DIR / f"{run_id}.md")
    return prompt_sha, schema_sha, changed


def main() -> None:
    for run_id, (commit, prompt_path) in RUNS.items():
        p, s, n = backfill(run_id, commit, prompt_path)
        print(f"{run_id:28} prompt {p}  schema {s}  ({n} record(s) updated)")
    missing = {f.stem for f in RUNS_DIR.glob("*.jsonl")} - set(RUNS)
    if missing:
        raise SystemExit(f"run files without a mapping: {sorted(missing)}")


if __name__ == "__main__":
    main()
