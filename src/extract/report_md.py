"""Human-readable mirror of a run file: results/runs/jsonl/<run_id>.jsonl -> results/runs/md/<run_id>.md.

JSONL is the source of truth (contract item 12) and what metrics read; a line of 20k
characters of JSON is unreadable for a person. This module renders the same Run Records as
Markdown: a run header, one summary table over all documents, then one section per document
with its endpoint and quota tables and the error text, if any. Nothing in the repository
reads the Markdown back, so its layout can change freely; the Run Record cannot.

The file is regenerated from the whole JSONL after every record, so during a long run it
always shows what has been recorded so far, and a resumed run keeps it complete.
"""

from pathlib import Path

from src.extract.schema import RunRecord, stored_context

GENERATED_NOTE = (
    "Generated from the JSONL run file by `src/extract/report_md.py`; do not edit."
)


def load_records(path: Path) -> list[RunRecord]:
    """Every Run Record of a run file, in file order.

    `stored_context(None)` skips the service check on purpose: the records were validated
    against their Target Service when they were written, and this reader has no manifest.
    """
    if not path.exists():
        return []
    return [
        RunRecord.model_validate_json(line, context=stored_context(None))
        for line in path.read_text().split("\n")
        if line.strip()
    ]


def write_markdown(jsonl_path: Path, md_path: Path) -> None:
    """Render `jsonl_path` as Markdown into `md_path` (the run id is the file stem)."""
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(render_markdown(jsonl_path.stem, load_records(jsonl_path)))


# ---------------------------------------------------------------- rendering


def render_markdown(run_id: str, records: list[RunRecord]) -> str:
    lines = [f"# Run `{run_id}`", "", GENERATED_NOTE, ""]
    if not records:
        return "\n".join(lines + ["No Run Records yet.", ""])

    # model, prompt and sampling are the same for every record of a run
    first, sampling = records[0], records[0].sampling
    lines += [
        f"- Model: `{first.model}`",
        f"- Prompt version: `{first.prompt_version}` (file sha `{first.prompt_sha}`)",
        f"- Schema sha: `{first.schema_sha}`; validation version `{first.validation_version}`",
        f"- Sampling: `{sampling.name}` (temperature {sampling.temperature}, top_p {sampling.top_p})",
        f"- Documents: {len(records)}",
        "",
        "## Summary",
        "",
    ]
    lines += _summary_table(records)
    lines += ["", "## Documents", ""]
    for rec in records:
        lines += _document_section(rec)
    return "\n".join(lines)


def _summary_table(records: list[RunRecord]) -> list[str]:
    header = [
        "#",
        "Document",
        "Group",
        "Status",
        "Calls",
        "Latency, s",
        "In tokens",
        "Out tokens",
        "Quota table",
        "Endpoints",
        "Quotas",
    ]
    rows = []
    for i, rec in enumerate(records, 1):
        out = rec.output
        rows.append(
            [
                str(i),
                f"[{rec.file}](#{_anchor(rec.file)})",
                rec.group.value,
                rec.status.value,
                str(rec.attempts),
                f"{rec.latency_ms / 1000:.1f}",
                f"{rec.usage.input_tokens:,}",
                f"{rec.usage.output_tokens:,}",
                out.quota_table_format.value if out else "—",
                str(len(out.endpoints)) if out else "—",
                str(len(out.quotas)) if out else "—",
            ]
        )
    return _table(header, rows)


def _document_section(rec: RunRecord) -> list[str]:
    status = (
        f"- Status: **{rec.status.value}**, {rec.attempts} call(s), "
        f"{rec.latency_ms / 1000:.1f} s, "
        f"in {rec.usage.input_tokens:,} / out {rec.usage.output_tokens:,} tokens"
    )
    lines = [f"### {rec.file}", "", status]
    out = rec.output
    if out is not None:
        lines += [
            f"- Service: {out.service}; quota table format: `{out.quota_table_format.value}`",
            "",
            f"#### Endpoints ({len(out.endpoints)})",
            "",
        ]
        lines += _table(
            ["Region name", "Region", "Endpoint", "Protocol", "Type"],
            [
                [
                    e.region_name,
                    e.region_code,
                    e.endpoint,
                    e.protocol.value,
                    e.endpoint_type.value,
                ]
                for e in out.endpoints
            ],
        )
        lines += ["", f"#### Quotas ({len(out.quotas)})", ""]
        lines += _table(
            ["Name", "Default", "Adjustable", "Description"],
            [
                [q.name, q.default, "Yes" if q.adjustable else "No", q.description]
                for q in out.quotas
            ],
        )
    if rec.error is not None:
        # "repaired" keeps the first failure (schema.py); "failed" has both failures
        title = (
            "Error"
            if rec.status.value == "failed"
            else "First answer rejected (repaired)"
        )
        lines += ["", f"#### {title}", "", "```text", rec.error.rstrip(), "```"]
    return lines + [""]


def _table(header: list[str], rows: list[list[str]]) -> list[str]:
    if not rows:
        return ["_none_"]
    return [
        "| " + " | ".join(header) + " |",
        "|" + "---|" * len(header),
        *("| " + " | ".join(_cell(c) for c in row) + " |" for row in rows),
    ]


def _cell(text: str) -> str:
    # A pipe or a line break inside a cell would break the table row.
    return text.replace("|", "\\|").replace("\n", " ")


def _anchor(file: str) -> str:
    # GitHub-style heading anchor for "### <file>": lowercase, dots dropped, spaces to hyphens
    return file.lower().replace(".", "").replace(" ", "-")
