"""Source-grounded validation (src/extract/grounding.py, ADR-0005; lecturer's remark 1).

Small layout-mode samples pin the two readers (hostnames of the Endpoint column, names of
the Name column of a Standard Quota Table) and the three checks G1–G3; the last tests run
the checks over the committed Golden Set and run files, which is how the parsers were
calibrated: every gold file must pass, and every flagged model row was checked against
the raw text by hand (step 11 log).
"""

import json

import pytest

from src.extract import grounding, pipeline
from src.extract.schema import ServiceDocument, stored_context

CHAPTER = """Amazon Example endpoints and quotas

Service endpoints

 Region Name           Region          Endpoint                                     Protocol

 US East (Ohio)        us-east-2       example.us-east-2.amazonaws.com              HTTPS
                                       example-fips.us-east-2.amazon                HTTPS
                                       aws.com
 Canada West           ca-west-1       example.ca-west-1.api.aws                    HTTPS
 (Calgary)

In your AWS account.example-kvs.global.api.aws is printed in prose, not in a table.

Service quotas

 Name                                              Default                  Adjustabl Description
                                                                            e

 Concurrent compute capacity for                   Each supported           No       The maximum number
 Ray worker instances per account.                 Region: 50                        of data processing units

 Data API maximum concurrent cluster-s             Each supported           No       The maximum number
 ecret pairs                                       Region: 30                        of unique pairs



Service quotas                                                                   Version 1.0 2698

AWS General Reference                                                             Reference guide

 Name                                              Default                  Adjustabl Description
                                                                            e

 cationToReplica API requests                      second                            PutSecretValue,

 Topics per account                                Each supported           Yes      The maximum number
                                                   Region: 100,000                   of topics.

Amazon Next endpoints and quotas
"""

RESOURCE_CHAPTER = """Amazon Other endpoints and quotas

Service endpoints

 Region Name           Region          Endpoint                                     Protocol

 US East (Ohio)        us-east-2       other.us-east-2.amazonaws.com                HTTPS

Service quotas

 Resource                                                 Quota                  Adjustable

 Maximum number of tasks you can create                   100                    Yes
"""


def doc(service="Amazon Example", endpoints=(), quotas=(), fmt="none"):
    return ServiceDocument.model_validate(
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
        },
        context=stored_context(service),
    )


# ---------------------------------------------------------------- the readers


def test_printed_hostnames_rejoin_wraps_and_skip_prose():
    chapter = grounding.target_chapter(CHAPTER, "Amazon Example")
    assert grounding.printed_hostnames(chapter) == [
        "example.us-east-2.amazonaws.com",
        "example-fips.us-east-2.amazonaws.com",
        "example.ca-west-1.api.aws",
    ]


def test_printed_quota_names_join_wrapped_rows_and_page_breaks():
    chapter = grounding.target_chapter(CHAPTER, "Amazon Example")
    assert grounding.printed_quota_names(chapter) == [
        "Concurrent compute capacity for Ray worker instances per account.",
        # a page break with a repeated header cut this row: rejoined by the lower-case
        # tail; the wrap inside "cluster-s / ecret" stays as the PDF printed it
        "Data API maximum concurrent cluster-s ecret pairs cationToReplica API requests",
        "Topics per account",
    ]


def test_standard_table_detection():
    assert grounding.has_standard_quota_table(CHAPTER)
    assert not grounding.has_standard_quota_table(RESOURCE_CHAPTER)
    assert grounding.printed_quota_names(RESOURCE_CHAPTER) == []


# ---------------------------------------------------------------- G1–G3


@pytest.fixture
def g():
    return grounding.Grounding.of(CHAPTER, "Amazon Example")


def test_g1_every_endpoint_must_be_printed_in_a_table(g):
    ok = doc(
        endpoints=["example.us-east-2.amazonaws.com", "example.ca-west-1.api.aws"],
        fmt="standard",
    )
    assert g.errors(ok) == []
    # a well-formed hostname taken from the prose (the schema's format check cannot see
    # the difference), a pattern-completed hostname (044 RDS: a dual-stack twin the table
    # does not print), a neighbouring chapter's hostname (Neighbour Tail)
    bad = doc(
        endpoints=[
            "example-kvs.global.api.aws",
            "example.us-west-2.api.aws",
            "next.us-east-2.amazonaws.com",
        ],
        fmt="standard",
    )
    errors = g.errors(bad)
    assert len(errors) == 3
    assert errors[0].startswith("endpoints.0.endpoint: not printed")
    assert "example.us-west-2.api.aws" in errors[1]


def test_g2_quota_names_as_printed_or_without_whitespace(g):
    ok = doc(
        fmt="standard",
        quotas=[
            "Concurrent compute capacity for Ray worker instances per account.",
            "Data API maximum concurrent cluster-secret pairs cationToReplica API requests",
            "topics per account",  # case does not matter
        ],
    )
    assert g.errors(ok) == []
    invented = doc(fmt="standard", quotas=["Maximum number of tasks you can create"])
    assert [e for e in g.errors(invented) if e.startswith("quotas.0.name")]
    # a dropped trailing period is not "as printed" (qwen, 075)
    trimmed = doc(fmt="standard", quotas=["Topics per account."])
    assert [e for e in g.errors(trimmed) if e.startswith("quotas.0.name")]


def test_g3_quota_table_format_follows_the_printed_header(g):
    assert [e for e in g.errors(doc(fmt="none")) if e.startswith("quota_table_format")]
    assert g.errors(doc(fmt="standard")) == []
    other = grounding.Grounding.of(RESOURCE_CHAPTER, "Amazon Other")
    assert other.errors(doc(service="Amazon Other", fmt="non_standard")) == []
    assert [
        e
        for e in other.errors(doc(service="Amazon Other", fmt="standard"))
        if e.startswith("quota_table_format")
    ]


def test_grounding_is_scoped_to_the_target_chapter():
    nxt = grounding.Grounding.of(CHAPTER, "Amazon Next")
    assert nxt.hostnames == set()
    assert not nxt.standard_table


# ---------------------------------------------------------------- the real data


def real_grounding():
    return {
        d.file: (d, grounding.Grounding.of(d.text(), d.service))
        for d in pipeline.load_manifest()
    }


def test_every_gold_file_is_grounded_in_its_chapter():
    """The Golden Set was checked against the PDF by hand (step 5); the readers must
    find every one of its rows in the text. The one exception is 038 until its gold is
    re-checked (finding F18): the chapter prints Standard Quota Tables."""
    exceptions = {"038-amazon-opensearch-service.pdf": ["quota_table_format"]}
    for file, (d, g) in real_grounding().items():
        if not d.gold:
            continue
        gold = ServiceDocument.model_validate_json(
            (pipeline.ROOT / "data" / "gold" / file).with_suffix(".json").read_text(),
            context=stored_context(None),
        )
        kinds = sorted({e.split(":")[0].split(".")[0] for e in g.errors(gold)})
        assert kinds == exceptions.get(file, []), (file, g.errors(gold)[:3])


def test_grounding_catches_the_known_model_errors_and_nothing_more_for_claude():
    """claude__v2__t0: exactly five documents, one row each, every one confirmed against
    the raw text by hand (step 11 log) — the calibration of the readers."""
    runs = {d: g for d, g in real_grounding().items()}
    flagged = {}
    for line in (pipeline.RUNS_DIR / "claude__v2__t0.jsonl").read_text().splitlines():
        rec = json.loads(line)
        if not rec["output"]:
            continue
        out = ServiceDocument.model_validate(
            rec["output"], context=stored_context(None)
        )
        errors = runs[rec["file"]][1].errors(out)
        if errors:
            flagged[rec["file"][:3]] = len(errors)
    assert flagged == {"091": 1, "044": 1, "038": 1, "025": 1, "010": 1}
