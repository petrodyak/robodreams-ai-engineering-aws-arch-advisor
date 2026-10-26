"""Long documents in parts (src/extract/parts.py, step 13; lecturer's remark 3).

The splitter is pinned on small chapters that reproduce the real layouts (one pair of
sections, no quotas block, two pairs as in 091, custom endpoint headings as in 046, a
page footer and the intro sentence that must not count as headings), then on all 40 real
chapters: the endpoints part must print every hostname of the chapter and no Standard
Quota Table, the quotas part the reverse. The pipeline tests drive a fake provider through
the two calls, the per-part repair, the merge and the status rules; the run id, the Run
Record and the metrics checks come last.
"""

import json

import pytest

from src.extract import grounding, metrics, parts, pipeline
from src.extract.llm import LLMReply
from src.extract.schema import (
    Group,
    PartRecord,
    RunRecord,
    Status,
    Usage,
    stored_context,
    worst_status,
)

SERVICE = "Amazon Example"
CHAPTER = """Amazon Example endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint.

Service quotas, also referred to as limits, are the maximum number of service resources or
operations for your AWS account.

Service endpoints

 Region Name           Region          Endpoint                                     Protocol

 US East (Ohio)        us-east-2       example.us-east-2.amazonaws.com              HTTPS

Service endpoints                                                                   Version 1.0 2698

AWS General Reference                                                             Reference guide

 Canada West           ca-west-1       example.ca-west-1.api.aws                    HTTPS
 (Calgary)

Service quotas

 Name                                              Default                  Adjustabl Description
                                                                            e

 Topics per account                                Each supported           Yes      The maximum number
                                                   Region: 100,000                   of topics.

Amazon Next endpoints and quotas

Service endpoints

 Region Name           Region          Endpoint                                     Protocol

 US East (Ohio)        us-east-2       next.us-east-2.amazonaws.com                 HTTPS
"""

# 091: two pairs of sections, with " for …" tails; 046: endpoints under custom headings
TWO_PAIRS = """Amazon Pairs endpoints and quotas

AWS Resource Groups

Service endpoints

 Region Name           Region          Endpoint                                     Protocol

 US East (Ohio)        us-east-2       groups.us-east-2.amazonaws.com               HTTPS

Service quotas for Resource Groups

 Name                                              Default                  Adjustabl Description
                                                                            e

 Groups per account                                Each supported           Yes      The maximum number
                                                   Region: 100                       of groups.

Tagging

Service endpoints for AWS Resource Groups Tagging API

 Region Name           Region          Endpoint                                     Protocol

 US East (Ohio)        us-east-2       tagging.us-east-2.amazonaws.com              HTTPS

Service quotas for Tagging (Tag Editor and Resource Groups Tagging API)

 Name                                              Default                  Adjustabl Description
                                                                            e

 Tags per resource                                 Each supported           No       The maximum number
                                                   Region: 50                        of tags.
"""

CUSTOM_HEADINGS = """Amazon Custom endpoints and quotas

Service API endpoints

 Region Name           Region          Endpoint                                     Protocol

 US East (Ohio)        us-east-2       custom.us-east-2.amazonaws.com               HTTPS

SMTP endpoints

 Region Name           Region          Endpoint                                     Protocol

 US East (Ohio)        us-east-2       smtp.us-east-2.amazonaws.com                 HTTPS

DKIM domains

 Region Name           Region          Endpoint                                     Protocol

 US East (Ohio)        us-east-2       dkim.us-east-2.amazonaws.com                 HTTPS

Service quotas

 Name                                              Default                  Adjustabl Description
                                                                            e

 Sending quota                                     200                      Yes      Emails per day.

OpenSearch Serverless

 Name                                              Default                  Adjustabl Notes
                                                                            e

 Collections                                       100                      Yes      Not standard.
"""

NO_QUOTAS = """Amazon Bare endpoints and quotas

Service endpoints

 Region Name           Region          Endpoint                                     Protocol

 US East (Ohio)        us-east-2       bare.us-east-2.amazonaws.com                 HTTPS
"""


# ---------------------------------------------------------------- the splitter


@pytest.mark.parametrize(
    "line, kind",
    [
        ("Service endpoints", "endpoints"),
        ("Service quotas", "quotas"),
        ("Service quotas for Resource Groups", "quotas"),
        ("Service endpoints for AWS Resource Groups Tagging API", "endpoints"),
        ("Service endpoint (global)", "endpoints"),
        ("SMTP endpoints", "endpoints"),
        ("AWS Global Networks for Transit Gateways Quotas (Network", "quotas"),
        ("DKIM domains", "other"),
        ("OpenSearch Serverless", "other"),
        ("", None),
        (" Region Name           Region          Endpoint", None),  # indented: a table
        ("Service endpoints                                 Version 1.0 2698", None),
        ("Service quotas, also referred to as limits, are the maximum number", None),
        (
            "The following are the service endpoints and service quotas for this service.",
            None,
        ),
    ],
)
def test_heading_kind(line, kind):
    assert parts.heading_kind(line) == kind


def test_split_one_pair_keeps_the_title_and_cuts_the_neighbour():
    p = parts.split_chapter(CHAPTER, SERVICE)
    assert p.title == "Amazon Example endpoints and quotas"
    assert p.endpoints.startswith("Amazon Example endpoints and quotas\n\n")
    assert p.quotas.startswith("Amazon Example endpoints and quotas\n\n")
    # the intro prose and both endpoints tables (the page footer between them) go with
    # the endpoints; the quotas table with the quotas; the next chapter with neither
    assert "example.ca-west-1.api.aws" in p.endpoints
    assert "Topics per account" not in p.endpoints
    assert "Topics per account" in p.quotas
    assert "example.us-east-2" not in p.quotas
    assert "next.us-east-2" not in p.endpoints + p.quotas
    assert grounding.printed_hostnames(p.endpoints) == [
        "example.us-east-2.amazonaws.com",
        "example.ca-west-1.api.aws",
    ]
    assert grounding.printed_quota_names(p.quotas) == ["Topics per account"]


def test_split_two_pairs_collects_both_of_each_kind():
    p = parts.split_chapter(TWO_PAIRS, "Amazon Pairs")
    assert grounding.printed_hostnames(p.endpoints) == [
        "groups.us-east-2.amazonaws.com",
        "tagging.us-east-2.amazonaws.com",
    ]
    assert grounding.printed_quota_names(p.quotas) == [
        "Groups per account",
        "Tags per resource",
    ]
    # an "other" heading continues the current block: "Tagging" follows a quotas block
    assert "\nTagging\n" in p.quotas and "Tagging\n" not in p.endpoints
    assert (
        "\nAWS Resource Groups\n" in p.endpoints
    )  # … and the first block is endpoints


def test_split_custom_endpoint_headings_and_a_quota_subheading():
    p = parts.split_chapter(CUSTOM_HEADINGS, "Amazon Custom")
    assert len(grounding.printed_hostnames(p.endpoints)) == 3
    assert "OpenSearch Serverless" in p.quotas  # stays in the quotas block
    assert "Collections" in p.quotas and "Collections" not in p.endpoints


def test_split_without_a_quotas_block_gives_an_empty_quotas_part():
    p = parts.split_chapter(NO_QUOTAS, "Amazon Bare")
    assert p.quotas == ""
    assert grounding.printed_hostnames(p.endpoints) == ["bare.us-east-2.amazonaws.com"]


def test_every_real_chapter_splits_cleanly():
    """The property the run relies on: every printed hostname is in the endpoints part,
    every Standard Quota Table in the quotas part, and nothing of either in the other."""
    for doc_set in (pipeline.WORKING_SET, pipeline.HOLDOUT_SET):
        for d in pipeline.load_manifest(doc_set.manifest):
            text = d.text(doc_set.dir)
            chapter = grounding.target_chapter(text, d.service)
            p = parts.split_chapter(text, d.service)
            assert set(grounding.printed_hostnames(p.endpoints)) == set(
                grounding.printed_hostnames(chapter)
            ), d.file
            assert grounding.printed_hostnames(p.quotas) == [], d.file
            assert set(grounding.printed_quota_names(p.quotas)) == set(
                grounding.printed_quota_names(chapter)
            ), d.file
            assert grounding.printed_quota_names(p.endpoints) == [], d.file
            assert grounding.has_standard_quota_table(
                p.quotas
            ) == grounding.has_standard_quota_table(chapter), d.file
            assert not grounding.has_standard_quota_table(p.endpoints), d.file


def test_chapters_without_a_quotas_block_are_the_two_known_ones():
    bare = sorted(
        d.file[:3]
        for d in pipeline.load_manifest()
        if parts.split_chapter(d.text(), d.service).quotas == ""
    )
    assert bare == ["007", "085"]


# ---------------------------------------------------------------- the merge


def answer(endpoints=(), quotas=(), fmt=None, service=SERVICE):
    fmt = fmt or ("standard" if quotas else "none")
    return json.dumps(
        {
            "schema_version": "1",
            "service": service,
            "quota_table_format": fmt,
            "endpoints": [
                {
                    "region_name": "US East (Ohio)",
                    "region_code": "us-east-2",
                    "endpoint": h,
                    "protocol": "HTTPS",
                }
                for h in endpoints
            ],
            "quotas": [
                {"name": n, "default": "1", "adjustable": True, "description": "d"}
                for n in quotas
            ],
        }
    )


def doc_of(text, service=SERVICE):
    from src.extract.schema import ServiceDocument, answer_context

    return ServiceDocument.model_validate_json(text, context=answer_context(service))


def test_merge_takes_each_kind_from_its_part_and_ignores_spill():
    ep = doc_of(answer(["example.us-east-2.amazonaws.com"], ["spilled quota"]))
    q = doc_of(answer(["spilled.us-east-2.amazonaws.com"], ["Topics per account"]))
    merged = parts.merge(SERVICE, ep, q)
    assert [e.endpoint for e in merged.endpoints] == ["example.us-east-2.amazonaws.com"]
    assert [x.name for x in merged.quotas] == ["Topics per account"]
    assert merged.quota_table_format.value == "standard"
    assert parts.spill("endpoints", ep) == 1 and parts.spill("quotas", q) == 1
    assert parts.part_rows("endpoints", ep) == 1 and parts.part_rows("quotas", q) == 1


def test_merge_without_a_quotas_part_says_none():
    ep = doc_of(answer(["example.us-east-2.amazonaws.com"]))
    merged = parts.merge(SERVICE, ep, None)
    assert merged.quota_table_format.value == "none" and merged.quotas == []


# ---------------------------------------------------------------- the pipeline

T0 = pipeline.load_sampling("t0")
PROMPT = pipeline.load_prompt("v2")
DOC = pipeline.Document(file="001-example.pdf", service=SERVICE, group=Group.SHORT)
EP = "example.us-east-2.amazonaws.com"
CA = "example.ca-west-1.api.aws"


def reply(text, *, tokens=(1000, 200), latency_ms=500, stop_reason="end_turn"):
    return LLMReply(
        text=text,
        usage=Usage(input_tokens=tokens[0], output_tokens=tokens[1]),
        latency_ms=latency_ms,
        attempts=1,
        stop_reason=stop_reason,
    )


class FakeLLM:
    model = "fake-model"

    def __init__(self, *script):
        self.script = list(script)
        self.requests = []

    def complete(self, system, messages, sampling):
        self.requests.append(messages)
        return self.script.pop(0)


def extract(*script, text=CHAPTER, doc=DOC):
    llm = FakeLLM(*script)
    rec = pipeline.extract_document(llm, doc, text, PROMPT, T0, parts=True)
    return rec, llm


def test_two_calls_each_with_its_part_merged_into_one_record():
    rec, llm = extract(
        reply(answer([EP, CA]), tokens=(700, 300), latency_ms=400),
        reply(answer(quotas=["Topics per account"]), tokens=(500, 100), latency_ms=300),
    )
    assert len(llm.requests) == 2
    first, second = (r[0]["content"] for r in llm.requests)
    assert EP in first and "Topics per account" not in first
    assert "Topics per account" in second and EP not in second
    assert "Amazon Example endpoints and quotas" in first and "…" not in second
    assert rec.status == Status.OK and rec.error is None
    assert [e.endpoint for e in rec.output.endpoints] == [EP, CA]
    assert [q.name for q in rec.output.quotas] == ["Topics per account"]
    # sums over both parts (contract items 12, 19)
    assert rec.attempts == 2 and rec.latency_ms == 700
    assert rec.usage == Usage(input_tokens=1200, output_tokens=400)
    assert [p.name for p in rec.parts] == ["endpoints", "quotas"]
    assert [(p.status, p.rows, p.spill) for p in rec.parts] == [
        (Status.OK, 2, 0),
        (Status.OK, 1, 0),
    ]


def test_each_part_is_judged_on_its_own_rows_only():
    # the endpoints part answers `none` for the format (it sees no quotas table) and the
    # quotas part returns no endpoints: neither is an error for that part
    rec, _ = extract(
        reply(answer([EP, CA], fmt="none")),
        reply(answer(quotas=["Topics per account"])),
    )
    assert rec.status == Status.OK


def test_a_part_gets_its_own_repair_and_the_record_is_repaired():
    rec, llm = extract(
        reply(answer([EP, "invented.us-east-2.amazonaws.com"])),  # G1 on the part
        reply(answer([EP, CA])),  # the repair of the endpoints part
        reply(answer(quotas=["Topics per account"])),
    )
    assert len(llm.requests) == 3
    assert "invented.us-east-2" in llm.requests[1][-1]["content"]  # the repair message
    assert rec.status == Status.REPAIRED
    assert rec.parts[0].status == Status.REPAIRED and rec.parts[0].attempts == 2
    assert rec.parts[1].status == Status.OK
    assert rec.error.startswith("[endpoints]\n") and "invented" in rec.error
    assert [e.endpoint for e in rec.output.endpoints] == [EP, CA]


def test_a_failed_part_fails_the_document_but_the_other_part_is_still_called():
    rec, llm = extract(
        reply(answer([EP])[:-20], stop_reason="max_tokens"),  # cut off: no repair call
        reply(answer(quotas=["Topics per account"])),
    )
    assert len(llm.requests) == 2
    assert rec.status == Status.FAILED and rec.output is None
    assert rec.parts[0].status == Status.FAILED and rec.parts[0].rows is None
    assert rec.parts[1].status == Status.OK and rec.parts[1].rows == 1
    assert "cut off" in rec.error


def test_a_chapter_without_a_quotas_block_makes_one_call():
    doc = pipeline.Document(
        file="002-bare.pdf", service="Amazon Bare", group=Group.SHORT
    )
    rec, llm = extract(
        reply(answer(["bare.us-east-2.amazonaws.com"], service="Amazon Bare")),
        text=NO_QUOTAS,
        doc=doc,
    )
    assert len(llm.requests) == 1
    assert [p.name for p in rec.parts] == ["endpoints"]
    assert rec.output.quota_table_format.value == "none" and rec.output.quotas == []


def test_spill_is_counted_and_ignored():
    rec, _ = extract(
        reply(answer([EP, CA], ["Topics per account"])),  # quotas in the endpoints part
        reply(answer([EP], ["Topics per account"])),  # an endpoint in the quotas part
    )
    assert rec.status == Status.OK
    assert [p.spill for p in rec.parts] == [1, 1]
    assert len(rec.output.endpoints) == 2 and len(rec.output.quotas) == 1


def test_whole_document_path_is_unchanged():
    llm = FakeLLM(reply(answer([EP, CA], ["Topics per account"])))
    rec = pipeline.extract_document(llm, DOC, CHAPTER, PROMPT, T0)
    assert rec.parts is None and rec.status == Status.OK and len(llm.requests) == 1


# ---------------------------------------------------------------- run id and records


@pytest.mark.parametrize(
    "kwargs, expected",
    [
        ({}, "claude__v2__t0__parts__val2"),
        ({"gold": True}, "claude__v2__t0__parts__gold__val2"),
        (
            {"doc_set": pipeline.HOLDOUT_SET, "gold": True},
            "claude__v2__t0__parts__holdout__gold__val2",
        ),
    ],
)
def test_parts_run_id_and_its_parse(kwargs, expected):
    assert pipeline.make_run_id("claude", "v2", "t0", parts=True, **kwargs) == expected
    run = metrics.parse_run_id(expected)
    assert run.parts and run.validation == "2" and run.sampling == "t0"
    assert run.gold == kwargs.get("gold", False)


def test_run_ids_without_parts_are_unchanged():
    assert not metrics.parse_run_id("claude__v2__t0__val2").parts
    assert not metrics.parse_run_id("qwen2.5-7b__v1__t05__gold").parts


def test_worst_status():
    assert worst_status([Status.OK, Status.OK]) == Status.OK
    assert worst_status([Status.OK, Status.REPAIRED]) == Status.REPAIRED
    assert worst_status([Status.REPAIRED, Status.FAILED]) == Status.FAILED


def part(name, status=Status.OK, rows=1):
    failed = status == Status.FAILED
    return PartRecord(
        name=name,
        words=10,
        attempts=1 if status == Status.OK else 2,
        latency_ms=100,
        usage=Usage(input_tokens=10, output_tokens=5),
        status=status,
        rows=None if failed else rows,
        spill=None if failed else 0,
        error=None if status == Status.OK else "e",
    )


def record(status, parts_, output):
    return RunRecord.model_validate(
        {
            "file": DOC.file,
            "group": DOC.group,
            "model": "fake",
            "prompt_version": "v2",
            "prompt_sha": "a3adf0379524",
            "schema_sha": "d4010de95c65",
            "validation_version": "2",
            "sampling": T0,
            "attempts": 2,
            "latency_ms": 200,
            "usage": Usage(input_tokens=20, output_tokens=10),
            "status": status,
            "output": output,
            "error": None if status == Status.OK else "e",
            "parts": parts_,
        },
        context=stored_context(SERVICE),
    )


def test_record_status_must_be_the_worst_of_its_parts():
    out = doc_of(answer([EP]))
    record(Status.OK, [part("endpoints"), part("quotas")], out)
    record(Status.REPAIRED, [part("endpoints", Status.REPAIRED), part("quotas")], out)
    with pytest.raises(ValueError, match="worst of the parts"):
        record(Status.OK, [part("endpoints", Status.REPAIRED), part("quotas")], out)
    with pytest.raises(ValueError, match="parts must be"):
        record(Status.OK, [part("quotas")], out)


def test_old_records_without_parts_still_load():
    line = (pipeline.RUNS_DIR / "claude__v2__t0__val2.jsonl").read_text().split("\n")[0]
    rec = RunRecord.model_validate_json(line, context=stored_context(None))
    assert rec.parts is None


def test_metrics_refuse_a_parts_run_id_over_whole_document_records():
    out = doc_of(answer([EP]))
    whole = record(Status.OK, None, out)
    docs = [DOC]
    with pytest.raises(ValueError, match="parts"):
        metrics.run_metrics("claude__v2__t0__parts__val2", [whole], docs, pipeline.ROOT)
    in_parts = record(Status.OK, [part("endpoints")], out)
    with pytest.raises(ValueError, match="whole documents"):
        metrics.run_metrics("claude__v2__t0__val2", [in_parts], docs, pipeline.ROOT)
    rows = metrics.run_metrics(
        "claude__v2__t0__parts__val2", [in_parts], docs, pipeline.ROOT
    )
    assert rows[-1].row()["pct_ok"] == 100.0


def test_markdown_mirror_shows_the_parts():
    from src.extract.report_md import render_markdown

    out = doc_of(answer([EP]))
    rec = record(
        Status.REPAIRED, [part("endpoints", Status.REPAIRED, 1), part("quotas")], out
    )
    md = render_markdown("claude__v2__t0__parts__val2", [rec])
    assert "- In parts:" in md
    assert "- Part `endpoints` (10 words): **repaired**, 2 call(s)" in md
    assert "- Part `quotas` (10 words): **ok**, 1 call(s)" in md
