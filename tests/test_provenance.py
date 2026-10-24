"""Lecturer's remark 2 (24.10), end to end: every run is tied to the exact prompt and schema.

These tests replay finding F17 — a run started under one prompt / schema and resumed after
one of them changed — and assert that the system makes the drift visible in the records and
refuses to mix two configurations under one run id. `tests/test_metrics.py` and
`tests/test_schema.py` cover the pieces; this file covers the property.
"""

import json

import pytest

from src.extract import metrics, pipeline
from src.extract.llm import LLMReply, llm_schema_sha
from src.extract.report_md import load_records
from src.extract.schema import Group, Usage
from tests.test_pipeline import ATHENA, DOC, TEXT, answer

T0 = pipeline.load_sampling("t0")
PROMPT = pipeline.load_prompt("v1")
DOCS = [
    pipeline.Document(DOC.file, DOC.service, DOC.group, gold=False),
    pipeline.Document(ATHENA.file, ATHENA.service, Group.EDGE, gold=False),
]


class OneAnswer:
    """A provider that answers every request with a valid document for the service asked."""

    model = "fake-model"

    def __init__(self):
        self.requests = 0

    def complete(self, system, messages, sampling):
        self.requests += 1
        service = messages[0]["content"].split("Target service: ")[1].split("\n")[0]
        return LLMReply(
            text=answer(service=service),
            usage=Usage(input_tokens=1000, output_tokens=200),
            latency_ms=500,
            attempts=1,
            stop_reason="end_turn",
        )


@pytest.fixture
def raw(tmp_path):
    raw = tmp_path / "raw"
    raw.mkdir()
    for doc in DOCS:
        (raw / doc.file).with_suffix(".txt").write_text(TEXT)
    return raw


def run(docs, out, raw, prompt=PROMPT):
    llm = OneAnswer()
    result = pipeline.run(llm, docs, prompt, T0, out, raw_dir=raw, log=lambda _: None)
    return result, llm


def test_every_record_names_the_prompt_and_schema_the_model_saw(tmp_path, raw):
    out = tmp_path / "runs" / "fake__v1__t0.jsonl"
    run(DOCS, out, raw)
    for rec in load_records(out):
        assert rec.prompt_sha == PROMPT.sha
        assert rec.schema_sha == llm_schema_sha()
    # the shas are of the bytes the pipeline read, not of names: recomputable by anyone
    stored = json.loads(out.read_text().split("\n")[0])
    assert stored["prompt_sha"] == pipeline.short_sha(
        (pipeline.PROMPTS_DIR / "extract_v1.txt").read_bytes()
    )


def test_f17_cannot_recur_a_schema_change_under_a_run_is_refused(
    tmp_path, raw, monkeypatch
):
    """The 24.10 case: a v1 run, the schema changed (PR #16), the same command resumed.
    Before step 10 the second half silently joined the first under the same run id."""
    out = tmp_path / "runs" / "fake__v1__t0.jsonl"
    run(DOCS[:1], out, raw)  # one document under the current schema
    before = out.read_text()

    monkeypatch.setattr(pipeline, "llm_schema_sha", lambda: "ffffffffffff")
    with pytest.raises(pipeline.ProvenanceMismatch, match="schema ffffffffffff"):
        run(DOCS, out, raw)  # the same run id, resumed with the second document

    assert out.read_text() == before  # nothing appended, nothing paid for


def test_a_prompt_edit_under_a_run_is_refused_too(tmp_path, raw):
    out = tmp_path / "runs" / "fake__v1__t0.jsonl"
    run(DOCS[:1], out, raw)

    # the same version name, one character changed inside a rule
    src = (pipeline.PROMPTS_DIR / "extract_v1.txt").read_bytes()
    (tmp_path / "extract_v1.txt").write_bytes(src.replace(b"Rules:", b"Rules :"))
    edited = pipeline.load_prompt("v1", tmp_path)
    assert edited.version == PROMPT.version and edited.sha != PROMPT.sha

    with pytest.raises(pipeline.ProvenanceMismatch, match=f"prompt {PROMPT.sha}"):
        run(DOCS, out, raw, prompt=edited)
    assert len(load_records(out)) == 1


def test_an_unchanged_configuration_still_resumes(tmp_path, raw):
    out = tmp_path / "runs" / "fake__v1__t0.jsonl"
    run(DOCS[:1], out, raw)
    result, llm = run(DOCS, out, raw)
    assert [r.file for r in result.records] == [ATHENA.file]  # only the missing one
    assert llm.requests == 1


def test_metrics_refuse_a_file_that_already_mixes_two_configurations(tmp_path, raw):
    """A file written before the guard (or edited by hand) with two provenance pairs is
    not averaged: the second line of defence, in case the first one is bypassed."""
    out = tmp_path / "runs" / "fake__v1__t0.jsonl"
    run(DOCS, out, raw)
    lines = out.read_text().rstrip("\n").split("\n")
    second = json.loads(lines[1])
    second["schema_sha"] = "ffffffffffff"
    out.write_text(lines[0] + "\n" + json.dumps(second) + "\n")

    with pytest.raises(ValueError, match="different provenance"):
        metrics.run_metrics("fake__v1__t0", load_records(out), DOCS, tmp_path)
