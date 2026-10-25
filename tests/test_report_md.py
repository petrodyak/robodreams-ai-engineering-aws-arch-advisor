"""The Markdown mirror of a run file (src/extract/report_md.py)."""

from src.extract import report_md
from src.extract.schema import Group, RunRecord, Sampling, Status, Usage, stored_context

T0 = Sampling(name="t0", temperature=0.0, top_p=None)


def record(file, status, output, error, **usage):
    return RunRecord.model_validate(
        {
            "file": file,
            "group": Group.SHORT,
            "model": "fake-model",
            "prompt_version": "v1",
            "prompt_sha": "8a0da697aa92",
            "schema_sha": "d4010de95c65",
            "validation_version": "2",
            "sampling": T0,
            "attempts": 2 if status == Status.REPAIRED else 1,
            "latency_ms": 1234,
            "usage": Usage(input_tokens=1000, output_tokens=200),
            "status": status,
            "output": output,
            "error": error,
        },
        context=stored_context(None),
    )


OK = record(
    "006-amazon-aurora-dsql.pdf",
    Status.OK,
    {
        "schema_version": "1",
        "service": "Amazon Aurora DSQL",
        "quota_table_format": "standard",
        "endpoints": [
            {
                "region_name": "US East (Ohio)",
                "region_code": "us-east-2",
                "endpoint": "dsql.us-east-2.api.aws",
                "protocol": "HTTPS",
            }
        ],
        "quotas": [
            {
                "name": "Clusters | per Region",
                "default": "Each supported Region: 100",
                "adjustable": True,
                "description": "The maximum number of clusters.",
            }
        ],
    },
    None,
)
FAILED = record(
    "049-amazon-simple-storage-service.pdf",
    Status.FAILED,
    None,
    "- the answer was cut off at the max_tokens limit\n--- no repair call",
)


def test_header_and_summary_row_per_document():
    md = report_md.render_markdown("fake__v1__t0", [OK, FAILED])
    assert md.startswith("# Run `fake__v1__t0`")
    assert "- Model: `fake-model`" in md
    assert "- Documents: 2" in md
    summary = md.split("## Summary")[1].split("## Documents")[0]
    rows = [line for line in summary.splitlines() if line.startswith("| ")]
    assert len(rows) == 3  # header + 2 documents
    assert "| ok | 1 | 1.2 | 1,000 | 200 | standard | 1 | 1 |" in rows[1]
    assert "| failed | 1 | 1.2 | 1,000 | 200 | — | — | — |" in rows[2]


def test_document_section_has_its_tables_with_the_derived_endpoint_type():
    md = report_md.render_markdown("fake__v1__t0", [OK])
    assert "### 006-amazon-aurora-dsql.pdf" in md
    assert "#### Endpoints (1)" in md
    assert (
        "| US East (Ohio) | us-east-2 | dsql.us-east-2.api.aws | HTTPS | dual_stack |"
        in md
    )
    assert "#### Quotas (1)" in md
    # a pipe inside a cell is escaped, otherwise it would split the table row
    assert "| Clusters \\| per Region | Each supported Region: 100 | Yes |" in md
    assert "#### Error" not in md


def test_failed_document_shows_the_error_and_no_tables():
    md = report_md.render_markdown("fake__v1__t0", [FAILED])
    section = md.split("### 049-amazon-simple-storage-service.pdf")[1]
    assert "#### Endpoints" not in section
    assert "#### Error" in section
    assert (
        "```text\n- the answer was cut off at the max_tokens limit\n--- no repair call\n```"
        in section
    )


def test_empty_run_renders_a_placeholder():
    md = report_md.render_markdown("fake__v1__t0", [])
    assert "No Run Records yet." in md


def test_write_markdown_round_trips_through_the_jsonl(tmp_path):
    jsonl = tmp_path / "jsonl" / "fake__v1__t0.jsonl"
    jsonl.parent.mkdir()
    jsonl.write_text(OK.model_dump_json() + "\n" + FAILED.model_dump_json() + "\n")
    md = tmp_path / "md" / "fake__v1__t0.md"
    report_md.write_markdown(jsonl, md)
    assert [r.file for r in report_md.load_records(jsonl)] == [OK.file, FAILED.file]
    text = md.read_text()
    assert "# Run `fake__v1__t0`" in text and "- Documents: 2" in text
