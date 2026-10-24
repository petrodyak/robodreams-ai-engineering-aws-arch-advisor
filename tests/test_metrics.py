"""The metrics (src/extract/metrics.py), on hand-made records and gold files.

Pins contract items 17-19: key matching as sets with precision / recall, per-field accuracy
on matched rows (description case-insensitive), the manifest as the denominator of validity
with a missing record counted as failed and "no answer" (finding F11), the __gold scope,
the percentiles, and the cost per 1,000 documents (Claude from usage, local model $0).
"""

import csv

import pytest

from src.extract import metrics
from src.extract.llm.claude import cost_usd
from src.extract.pipeline import Document
from src.extract.schema import (
    EndpointRow,
    Group,
    Protocol,
    QuotaRow,
    RunRecord,
    Sampling,
    ServiceDocument,
    Status,
    Usage,
    stored_context,
)

T0 = Sampling(name="t0", temperature=0.0, top_p=None)

DOCS = [
    Document("001-a.pdf", "Service A", Group.SHORT, gold=True),
    Document("002-b.pdf", "Service B", Group.SHORT, gold=False),
    Document("003-c.pdf", "Service C", Group.MEDIUM, gold=True),
    Document("004-d.pdf", "Service D", Group.EDGE, gold=False),
]


def ep(host, region="us-east-2", name="US East (Ohio)", protocol="HTTPS"):
    return EndpointRow(
        region_name=name, region_code=region, endpoint=host, protocol=Protocol(protocol)
    )


def quota(name, default="100", adjustable=True, description="Max things"):
    return QuotaRow(
        name=name, default=default, adjustable=adjustable, description=description
    )


def document(service, endpoints, quotas=(), fmt="standard"):
    if not quotas:
        fmt = "none"
    return ServiceDocument.model_validate(
        {
            "schema_version": "1",
            "service": service,
            "quota_table_format": fmt,
            "endpoints": [e.model_dump(exclude={"endpoint_type"}) for e in endpoints],
            "quotas": [q.model_dump() for q in quotas],
        },
        context=stored_context(service),
    )


def record(
    doc: Document,
    output,
    *,
    status=None,
    latency_ms=1000,
    usage=(100, 50),
    model="claude-haiku-4-5",
    prompt_sha="8a0da697aa92",
    schema_sha="d4010de95c65",
):
    status = status or (Status.OK if output is not None else Status.FAILED)
    return RunRecord.model_validate(
        {
            "file": doc.file,
            "group": doc.group,
            "model": model,
            "prompt_version": "v1",
            "prompt_sha": prompt_sha,
            "schema_sha": schema_sha,
            "sampling": T0,
            "attempts": 1 if status == Status.OK else 2,
            "latency_ms": latency_ms,
            "usage": Usage(input_tokens=usage[0], output_tokens=usage[1]),
            "status": status,
            "output": output,
            "error": None if status == Status.OK else "first answer invalid",
        },
        context=stored_context(doc.service),
    )


GOLD_A = document(
    "Service A",
    [
        ep("a.us-east-2.amazonaws.com"),
        ep("a-fips.us-east-2.amazonaws.com"),
        ep("a.eu-west-1.amazonaws.com", "eu-west-1", "Europe (Ireland)"),
    ],
    [quota("Max things"), quota("Max other", "5", False, "Other things")],
)
GOLD_C = document("Service C", [ep("c.us-east-2.amazonaws.com")])


@pytest.fixture
def gold_dir(tmp_path):
    d = tmp_path / "gold"
    d.mkdir()
    for file, doc in (("001-a.json", GOLD_A), ("003-c.json", GOLD_C)):
        (d / file).write_text(doc.model_dump_json(indent=2))
    return d


# ---------------------------------------------------------------- run id


@pytest.mark.parametrize(
    "run_id, model, prompt, sampling, gold",
    [
        ("claude__v1__t0", "claude", "v1", "t0", False),
        ("qwen2.5-7b__v2__t05", "qwen2.5-7b", "v2", "t05", False),
        ("claude__v1__t05__gold", "claude", "v1", "t05", True),
    ],
)
def test_parse_run_id(run_id, model, prompt, sampling, gold):
    run = metrics.parse_run_id(run_id)
    assert (run.model, run.prompt_version, run.sampling, run.gold) == (
        model,
        prompt,
        sampling,
        gold,
    )
    assert run.scope == ("gold" if gold else "full")


def test_parse_run_id_rejects_other_names():
    with pytest.raises(ValueError, match="not a run id"):
        metrics.parse_run_id("claude-v1-t0")


def test_gold_scope_is_the_gold_rows_of_the_manifest():
    assert metrics.run_scope(metrics.parse_run_id("claude__v1__t05__gold"), DOCS) == [
        DOCS[0],
        DOCS[2],
    ]
    assert metrics.run_scope(metrics.parse_run_id("claude__v1__t0"), DOCS) == DOCS


# ---------------------------------------------------------------- key matching and fields


def test_rows_matched_by_key_as_sets():
    predicted = [
        ep("a.us-east-2.amazonaws.com"),
        ep("a.us-east-2.amazonaws.com"),  # a duplicate is one key
        ep("a-fips.us-east-2.amazonaws.com"),
        ep("extra.us-east-2.amazonaws.com"),  # not in gold
        # a.eu-west-1 missing
    ]
    t = metrics.match_rows(
        GOLD_A.endpoints, predicted, "endpoint", metrics.ENDPOINT_FIELDS
    )
    assert (t.gold, t.predicted, t.matched) == (3, 3, 2)
    assert t.precision == pytest.approx(2 / 3)
    assert t.recall == pytest.approx(2 / 3)


def test_fields_scored_on_matched_rows_only():
    predicted = [
        ep("a.us-east-2.amazonaws.com", protocol="HTTP"),  # protocol wrong
        ep(
            "a-fips.us-east-2.amazonaws.com", name="US East (N. Virginia)"
        ),  # name wrong
        ep(
            "extra.us-east-2.amazonaws.com", region="eu-west-1"
        ),  # unmatched: not scored
    ]
    t = metrics.match_rows(
        GOLD_A.endpoints, predicted, "endpoint", metrics.ENDPOINT_FIELDS
    )
    assert t.field_total == {"region_name": 2, "region_code": 2, "protocol": 2}
    assert t.field_accuracy("region_name") == 0.5
    assert t.field_accuracy("region_code") == 1.0
    assert t.field_accuracy("protocol") == 0.5


def test_description_is_case_insensitive_other_fields_exact():
    predicted = [
        quota("Max things", description="MAX THINGS"),  # case only: correct
        quota("Max other", "5.0", False, "Other things"),  # default differs: wrong
    ]
    t = metrics.match_rows(GOLD_A.quotas, predicted, "name", metrics.QUOTA_FIELDS)
    assert t.matched == 2
    assert t.field_accuracy("description") == 1.0
    assert t.field_accuracy("default") == 0.5
    assert t.field_accuracy("adjustable") == 1.0


def test_no_matched_rows_means_undefined_field_accuracy():
    t = metrics.match_rows(GOLD_A.quotas, [], "name", metrics.QUOTA_FIELDS)
    assert t.precision is None  # nothing predicted
    assert t.recall == 0.0
    assert t.field_accuracy("default") is None


def test_missing_output_scores_as_empty_extraction():
    acc = metrics.score_document(GOLD_A, None)
    assert (acc.endpoints.gold, acc.endpoints.predicted, acc.endpoints.matched) == (
        3,
        0,
        0,
    )
    assert acc.quotas.recall == 0.0
    assert acc.format_correct is False


def test_quota_table_format_is_scored_per_document():
    same = document("Service A", GOLD_A.endpoints, GOLD_A.quotas)
    other = document("Service A", GOLD_A.endpoints, [], fmt="none")
    assert metrics.score_document(GOLD_A, same).format_correct
    assert not metrics.score_document(GOLD_A, other).format_correct


# ---------------------------------------------------------------- percentiles


@pytest.mark.parametrize(
    "values, p, expected",
    [
        ([10], 50, 10),
        ([10], 95, 10),
        ([10, 20], 50, 15),
        ([1, 2, 3, 4, 5], 50, 3),
        ([1, 2, 3, 4, 5], 95, 4.8),  # linear interpolation between ranks 4 and 5
        ([5, 1, 3], 50, 3),  # unsorted input
    ],
)
def test_percentile(values, p, expected):
    assert metrics.percentile(values, p) == pytest.approx(expected)


def test_percentile_of_nothing_raises():
    with pytest.raises(ValueError):
        metrics.percentile([], 50)


# ---------------------------------------------------------------- one run


def rows_by_group(rows):
    return {gm.group: gm.row() for gm in rows}


def test_denominator_is_the_manifest_and_a_missing_record_is_no_answer(gold_dir):
    # 4 documents in scope; only 2 recorded (one ok, one failed): F11 — the two others are
    # failed as well and reported as "no answer"
    records = [
        record(DOCS[0], GOLD_A),
        record(DOCS[1], None, status=Status.FAILED),
    ]
    rows = rows_by_group(metrics.run_metrics("claude__v1__t0", records, DOCS, gold_dir))
    total = rows["total"]
    assert (
        total["n_docs"],
        total["ok"],
        total["repaired"],
        total["failed"],
        total["no_answer"],
    ) == (4, 1, 0, 3, 2)
    assert total["pct_ok"] == 25.0
    assert total["pct_ok_or_repaired"] == 25.0
    # the edge group has one document and no record at all
    assert (
        rows["edge"]["n_docs"],
        rows["edge"]["no_answer"],
        rows["edge"]["failed"],
    ) == (1, 1, 1)
    assert rows["edge"]["latency_p50_ms"] is None
    assert rows["edge"]["cost_per_1000_usd"] is None


def test_gold_run_has_the_gold_rows_as_denominator(gold_dir):
    records = [record(DOCS[0], GOLD_A), record(DOCS[2], GOLD_C)]
    rows = rows_by_group(
        metrics.run_metrics("claude__v1__t05__gold", records, DOCS, gold_dir)
    )
    assert set(rows) == {
        "short",
        "medium",
        "total",
    }  # no edge document in the Golden Set
    assert rows["total"]["n_docs"] == 2
    assert rows["total"]["scope"] == "gold"
    assert rows["total"]["pct_ok"] == 100.0


def test_a_record_outside_the_scope_is_an_error(gold_dir):
    records = [record(DOCS[1], None, status=Status.FAILED)]  # 002-b is not gold
    with pytest.raises(ValueError, match="outside the run's scope"):
        metrics.run_metrics("claude__v1__t05__gold", records, DOCS, gold_dir)


def test_repaired_counts_in_ok_or_repaired_only(gold_dir):
    records = [record(DOCS[0], GOLD_A, status=Status.REPAIRED), record(DOCS[2], GOLD_C)]
    total = rows_by_group(
        metrics.run_metrics("claude__v1__t05__gold", records, DOCS, gold_dir)
    )["total"]
    assert (
        total["ok"],
        total["repaired"],
        total["pct_ok"],
        total["pct_ok_or_repaired"],
    ) == (1, 1, 50.0, 100.0)


def test_latency_and_cost_from_the_records(gold_dir):
    records = [
        record(DOCS[0], GOLD_A, latency_ms=1000, usage=(1000, 2000)),
        record(DOCS[2], GOLD_C, latency_ms=3000, usage=(3000, 4000)),
    ]
    total = rows_by_group(
        metrics.run_metrics("claude__v1__t05__gold", records, DOCS, gold_dir)
    )["total"]
    assert (total["latency_p50_ms"], total["latency_p95_ms"]) == (2000, 2900)
    assert total["wallclock_s"] == 4
    assert total["cost_per_1000_usd"] == pytest.approx(
        round(cost_usd(4000, 6000) / 2 * 1000, 2)
    )


def test_local_model_costs_nothing_but_reports_wall_clock(gold_dir):
    records = [
        record(
            DOCS[0], GOLD_A, latency_ms=60_000, usage=(1000, 2000), model="qwen2.5:7b"
        ),
        record(
            DOCS[2], GOLD_C, latency_ms=90_000, usage=(3000, 4000), model="qwen2.5:7b"
        ),
    ]
    total = rows_by_group(
        metrics.run_metrics("qwen2.5-7b__v1__t0__gold", records, DOCS, gold_dir)
    )["total"]
    assert total["cost_per_1000_usd"] == 0.0
    assert total["wallclock_s"] == 150


def test_accuracy_is_a_micro_average_over_gold_documents(gold_dir):
    # gold A: 3 endpoints, 2 quotas; gold C: 1 endpoint. The A output misses one endpoint
    # and the whole quotas table; C is failed and counts as an empty extraction.
    output_a = document("Service A", GOLD_A.endpoints[:2], [], fmt="none")
    records = [record(DOCS[0], output_a), record(DOCS[2], None, status=Status.FAILED)]
    rows = rows_by_group(
        metrics.run_metrics("claude__v1__t05__gold", records, DOCS, gold_dir)
    )
    total = rows["total"]
    assert (total["gold_docs"], total["gold_scored"]) == (2, 1)
    assert total["ep_precision"] == 100.0  # 2 of 2 predicted
    assert total["ep_recall"] == 50.0  # 2 of 4 gold rows (3 + 1)
    assert total["q_precision"] is None  # nothing predicted
    assert total["q_recall"] == 0.0
    assert total["quota_table_format_acc"] == 0.0  # A: none vs standard; C: no output
    assert total["ep_region_name_acc"] == 100.0
    # the medium group holds only the failed C
    assert rows["medium"]["ep_recall"] == 0.0
    assert rows["medium"]["ep_precision"] is None


def test_non_gold_documents_do_not_enter_accuracy(gold_dir):
    records = [
        record(DOCS[1], document("Service B", [ep("b.us-east-2.amazonaws.com")]))
    ]
    total = rows_by_group(
        metrics.run_metrics("claude__v1__t0", records, DOCS, gold_dir)
    )["total"]
    assert total["ok"] == 1
    # the two gold documents have no record: scored as empty extractions
    assert (total["gold_docs"], total["gold_scored"], total["ep_recall"]) == (2, 0, 0.0)


# ---------------------------------------------------------------- all runs -> CSV


def test_csv_has_one_row_per_run_and_group_plus_total(tmp_path, gold_dir):
    runs = tmp_path / "runs"
    runs.mkdir()
    full = [
        record(DOCS[0], GOLD_A),
        record(DOCS[1], None, status=Status.FAILED),
        record(DOCS[2], GOLD_C),
        # 004-d (edge) has no record at all: no answer
    ]
    gold = [record(DOCS[0], GOLD_A), record(DOCS[2], GOLD_C)]
    for run_id, recs in (("claude__v1__t0", full), ("claude__v1__t05__gold", gold)):
        (runs / f"{run_id}.jsonl").write_text(
            "".join(r.model_dump_json() + "\n" for r in recs)
        )

    rows = metrics.all_metrics(runs, DOCS, gold_dir)
    out = tmp_path / "metrics.csv"
    metrics.write_csv(rows, out)

    with open(out, newline="") as f:
        read = list(csv.DictReader(f))
    assert [r["run_id"] + "/" + r["group"] for r in read] == [
        "claude__v1__t0/short",
        "claude__v1__t0/medium",
        "claude__v1__t0/edge",
        "claude__v1__t0/total",
        "claude__v1__t05__gold/short",
        "claude__v1__t05__gold/medium",
        "claude__v1__t05__gold/total",
    ]
    assert list(read[0]) == metrics.COLUMNS
    assert read[3]["n_docs"] == "4" and read[-1]["n_docs"] == "2"
    assert read[2]["latency_p50_ms"] == ""  # undefined is an empty cell, not "None"
    assert "claude__v1__t0" in metrics.summary(rows)


def test_provenance_is_one_pair_per_run_and_reported(gold_dir):
    records = [record(DOCS[0], GOLD_A), record(DOCS[2], GOLD_C)]
    total = rows_by_group(
        metrics.run_metrics("claude__v1__t05__gold", records, DOCS, gold_dir)
    )["total"]
    assert (total["prompt_sha"], total["schema_sha"]) == (
        "8a0da697aa92",
        "d4010de95c65",
    )


def test_mixed_provenance_in_one_run_file_is_an_error(gold_dir):
    # Finding F17: a run resumed after a schema change would mix two configurations
    # under one run id; metrics refuse it instead of averaging them
    records = [
        record(DOCS[0], GOLD_A, schema_sha="e707d2e9616f"),
        record(DOCS[2], GOLD_C, schema_sha="d4010de95c65"),
    ]
    with pytest.raises(ValueError, match="different provenance"):
        metrics.run_metrics("claude__v1__t05__gold", records, DOCS, gold_dir)


def test_real_runs_carry_the_two_schemas_of_hw1():
    """The backfilled provenance (scripts/backfill_provenance.py): the Literal schema on
    the 21.10–23.10 runs, the enum schema after PR #16 — including the v1 prompt run of
    24.10, which is finding F17 made visible in the data."""
    rows = {gm.run_id: gm.row() for gm in metrics.all_metrics() if gm.group == "total"}
    literal, enum = "e707d2e9616f", "d4010de95c65"
    assert rows["claude__v1__t0"]["schema_sha"] == literal
    assert rows["qwen2.5-7b__v1__t0__gold"]["schema_sha"] == literal
    assert rows["claude__v2__t0"]["schema_sha"] == enum
    assert rows["qwen2.5-7b__v1__t0"]["schema_sha"] == enum  # F17
    assert (
        rows["qwen2.5-7b__v1__t0"]["prompt_sha"] == rows["claude__v1__t0"]["prompt_sha"]
    )
    assert rows["claude__v2__t0"]["prompt_sha"] != rows["claude__v1__t0"]["prompt_sha"]


def test_metrics_on_the_real_golden_set_and_runs():
    """The committed runs and gold files go through without error; the first Claude run
    is 30/30 ok (Implementation_steps, step 4) and every gold document gets scored."""
    rows = {(gm.run_id, gm.group): gm.row() for gm in metrics.all_metrics()}
    total = rows[("claude__v1__t0", "total")]
    assert total["n_docs"] == 30
    assert total["no_answer"] == 0
    assert (total["gold_docs"], total["gold_scored"]) == (10, 10)
    assert total["ep_recall"] is not None and total["q_recall"] is not None
