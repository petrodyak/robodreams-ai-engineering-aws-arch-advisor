"""Contract of src/extract/schema.py (docs/stage1-data-contract.md, ADR-0001..0003).

These tests pin what the model sees (the JSON Schema), what the validators reject
(the input to the repair call, contract item 16) and the round trip of stored
gold/results JSON. Fixture values are taken from data/raw/006-amazon-aurora-dsql.txt.
"""

import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from src.extract.llm import SCHEMA_FILE, llm_schema_json
from src.extract.llm import llm_schema as sent_llm_schema
from src.extract.schema import (
    EndpointRow,
    EndpointType,
    QuotaRow,
    RunRecord,
    ServiceDocument,
    Status,
    answer_context,
    stored_context,
)

SERVICE = "Amazon Aurora DSQL"


def endpoint_row(**overrides):
    row = {
        "region_name": "US East (Ohio)",
        "region_code": "us-east-2",
        "endpoint": "dsql.us-east-2.api.aws",
        "protocol": "HTTPS",
    }
    return row | overrides


def quota_row(**overrides):
    row = {
        "name": "Cluster size",
        "default": "Each supported Region: 10,000 Gigabytes",
        "adjustable": True,
        "description": "The maximum capacity (in GB) for an Aurora DSQL cluster.",
    }
    return row | overrides


def document(**overrides):
    doc = {
        "schema_version": "1",
        "service": SERVICE,
        "quota_table_format": "standard",
        "endpoints": [
            endpoint_row(),
            endpoint_row(endpoint="dsql-fips.us-east-2.api.aws"),
        ],
        "quotas": [quota_row()],
    }
    return doc | overrides


def answer(doc, service=SERVICE):
    """Validate `doc` the way the pipeline validates a model answer."""
    return ServiceDocument.model_validate(doc, context=answer_context(service))


def load_record(record):
    """Validate a Run Record the way metrics load a results line."""
    return RunRecord.model_validate(record, context=stored_context(SERVICE))


# ---------------------------------------------------------------- what the model sees


def llm_schema():
    return ServiceDocument.model_json_schema()


def schema_objects(schema):
    objects = [schema, *schema.get("$defs", {}).values()]
    return [o for o in objects if o.get("type") == "object"]


def test_llm_schema_has_no_computed_field():
    # endpoint_type is derived by code (contract item 6), the model must not be asked for it.
    assert "endpoint_type" not in json.dumps(llm_schema())


def test_llm_schema_objects_forbid_extra_properties():
    # Claude structured outputs require additionalProperties: false on every object.
    objects = schema_objects(llm_schema())
    assert len(objects) == 3  # ServiceDocument, EndpointRow, QuotaRow
    assert all(o.get("additionalProperties") is False for o in objects)


def test_llm_schema_requires_every_field():
    # No defaults: the model states every field instead of silently skipping one.
    for obj in schema_objects(llm_schema()):
        assert set(obj["required"]) == set(obj["properties"])


def test_every_field_description_reaches_the_model():
    # The schema actually sent, not the Pydantic one: transform_schema drops a
    # description that sits next to a $ref, so an enum field's description has to live
    # on the enum class (its docstring), which survives in $defs.
    schema = sent_llm_schema()
    defs = schema["$defs"]
    for obj in schema_objects(schema):
        for name, prop in obj["properties"].items():
            target = defs[prop["$ref"].rsplit("/", 1)[-1]] if "$ref" in prop else prop
            assert target.get("description"), (
                f"{obj['title']}.{name} has no description"
            )


def test_quota_table_format_definition_reaches_the_model():
    # The definition of "standard" is what separates the three formats (ADR-0001).
    described = sent_llm_schema()["$defs"]["QuotaTableFormat"]["description"]
    assert "Name, Default, Adjustable, Description" in described


def test_schema_file_matches_the_sent_schema():
    # `make check` regenerates the file first; this catches a plain `pytest` run
    # after a schema.py change that left the documented schema stale.
    assert SCHEMA_FILE.read_text() == llm_schema_json(), (
        f"{SCHEMA_FILE} is stale, run `make schema`"
    )


def test_example_document_is_a_valid_model_answer():
    # docs/service-document.example.json is hand-made data, so it cannot be regenerated
    # like the schema file; this fails instead when schema.py stops accepting it.
    example = (
        Path(__file__).resolve().parents[1] / "docs" / "service-document.example.json"
    )
    text = example.read_text()
    doc = ServiceDocument.model_validate_json(text, context=answer_context(SERVICE))
    assert (len(doc.endpoints), len(doc.quotas)) == (25, 4)


# ---------------------------------------------------------------- normalisation (item 9)


def test_line_wraps_in_strings_are_collapsed():
    q = QuotaRow(**quota_row(name="Connections  per\n   cluster"))
    assert q.name == "Connections per cluster"


def test_region_name_wrapped_over_lines_is_collapsed():
    e = EndpointRow(**endpoint_row(region_name="US\nEast (N.\nVirginia)"))
    assert e.region_name == "US East (N. Virginia)"


def test_footnote_marker_in_description_is_kept():
    text = "The maximum number of active clusters.¹"
    assert QuotaRow(**quota_row(description=text)).description == text


def test_multi_region_default_is_kept_verbatim():
    # ADR-0002: the printed text, not a parsed number.
    default = "us-east-1: 20,000; us-east-2: 6,000"
    assert QuotaRow(**quota_row(default=default)).default == default


# ---------------------------------------------------------------- endpoint_type (item 6)


@pytest.mark.parametrize(
    ("region", "host", "expected"),
    [
        ("us-east-2", "sqs.us-east-2.amazonaws.com", EndpointType.IPV4),
        ("us-east-2", "sqs-fips.us-east-2.amazonaws.com", EndpointType.FIPS),
        ("us-east-2", "dsql.us-east-2.api.aws", EndpointType.DUAL_STACK),
        ("us-east-2", "dsql-fips.us-east-2.api.aws", EndpointType.FIPS_DUAL_STACK),
        ("us-east-1", "ecr-fips.us-east-1.on.aws", EndpointType.FIPS_DUAL_STACK),
        ("us-east-1", "s3.dualstack.us-east-1.amazonaws.com", EndpointType.DUAL_STACK),
        (
            "us-east-2",
            "s3-fips.dualstack.us-east-2.amazonaws.com",
            EndpointType.FIPS_DUAL_STACK,
        ),
        ("us-west-2", "s3-us-west-2.amazonaws.com", EndpointType.IPV4),
        ("us-west-2", "globalaccelerator.amazonaws.com", EndpointType.GLOBAL),
        ("us-east-1", "cloudfront.amazonaws.com", EndpointType.GLOBAL),
    ],
)
def test_endpoint_type_is_derived_from_hostname(region, host, expected):
    row = EndpointRow(**endpoint_row(region_code=region, endpoint=host))
    assert row.endpoint_type == expected


# ---------------------------------------------------------------- format checks (ADR-0003)


@pytest.mark.parametrize(
    "region",
    ["ca-centra\nl-1", "ap-southe ast-3", "US East (Ohio)", "useast1", "us-east", ""],
)
def test_broken_region_code_is_rejected(region):
    with pytest.raises(ValidationError, match="region_code"):
        EndpointRow(**endpoint_row(region_code=region))


@pytest.mark.parametrize("region", ["us-east-1", "us-gov-west-1", "cn-north-1"])
def test_real_region_codes_are_accepted(region):
    assert EndpointRow(**endpoint_row(region_code=region)).region_code == region


@pytest.mark.parametrize(
    "host",
    [
        "dsql-fips.us-east-2.api.a\nws",  # a line wrap left a space after normalisation
        "https://dsql.us-east-2.api.aws",  # the scheme is not part of the hostname
        "dsql.us-east-2.example.com",  # not an AWS domain
        "dsql.us-east-2.notamazonaws.com",  # look-alike, not a subdomain of amazonaws.com
        "api.aws",  # the bare domain is not an endpoint
        "dsql",
    ],
)
def test_broken_endpoint_is_rejected(host):
    with pytest.raises(ValidationError, match="endpoint"):
        EndpointRow(**endpoint_row(endpoint=host))


@pytest.mark.parametrize(
    "host",
    [
        "sqs.us-east-2.amazonaws.com",
        "sqs.cn-north-1.amazonaws.com.cn",
        "dsql.us-east-2.api.aws",
        "ecr-fips.us-east-2.on.aws",
    ],
)
def test_every_aws_domain_is_accepted(host):
    assert EndpointRow(**endpoint_row(endpoint=host)).endpoint == host


def test_protocol_is_the_printed_value():
    assert EndpointRow(**endpoint_row(protocol="HTTP and HTTPS")).protocol == (
        "HTTP and HTTPS"
    )
    with pytest.raises(ValidationError, match="protocol"):
        EndpointRow(**endpoint_row(protocol="https"))


@pytest.mark.parametrize("fmt", ["non_standard", "none"])
def test_quotas_outside_a_standard_table_are_rejected(fmt):
    # ADR-0001 + ADR-0003: only Standard Quota Table rows are extracted.
    with pytest.raises(ValidationError, match="quota_table_format"):
        answer(document(quota_table_format=fmt))


@pytest.mark.parametrize("fmt", ["standard", "non_standard", "none"])
def test_empty_quotas_are_valid_for_any_format(fmt):
    assert answer(document(quota_table_format=fmt, quotas=[])).quotas == []


# ---------------------------------------------------------------- service check (item 2)


def test_matching_service_is_accepted():
    assert answer(document()).service == SERVICE


def test_neighbour_tail_service_is_rejected():
    # 006-amazon-aurora-dsql starts with the tail of Amazon Aurora quotas.
    with pytest.raises(ValidationError, match=SERVICE):
        answer(document(service="Amazon Aurora"))


def test_service_check_ignores_whitespace_only():
    assert answer(document(service="Amazon  Aurora\nDSQL")).service == SERVICE
    with pytest.raises(ValidationError):
        answer(document(service="amazon aurora dsql"))


@pytest.mark.parametrize("context", [None, {}, {"stored": True}])
def test_validation_without_a_service_context_fails(context):
    # A caller that forgets the context must not lose the Neighbour Tail detector silently.
    with pytest.raises(ValidationError, match="context"):
        ServiceDocument.model_validate(document(), context=context)


def test_service_check_can_be_skipped_on_purpose():
    doc = document(service="Amazon Aurora")
    loaded = ServiceDocument.model_validate(doc, context=stored_context(None))
    assert loaded.service == "Amazon Aurora"


# ---------------------------------------------------------------- shape


@pytest.mark.parametrize("version", ["2", "1.0", 1])
def test_unknown_schema_version_is_rejected(version):
    # "1.0" is what qwen wrote on every v1 document (finding F15)
    with pytest.raises(ValidationError, match="schema_version"):
        answer(document(schema_version=version))


def test_sent_schema_constrains_schema_version_to_an_enum():
    # Finding F15: a Literal["1"] became a plain string after transform_schema; an enum
    # survives it, so both models are told the one allowed value
    schema = sent_llm_schema()
    ref = schema["properties"]["schema_version"]["$ref"].rsplit("/", 1)[1]
    assert schema["$defs"][ref]["enum"] == ["1"]


def test_model_cannot_invent_fields():
    with pytest.raises(ValidationError):
        EndpointRow(**endpoint_row(notes="FIPS endpoint"))


@pytest.mark.parametrize("value", ["Yes", "yes", "true", 1])
def test_adjustable_must_be_a_json_boolean(value):
    with pytest.raises(ValidationError, match="adjustable"):
        QuotaRow(**quota_row(adjustable=value))


def test_adjustable_is_required():
    row = quota_row()
    del row["adjustable"]
    with pytest.raises(ValidationError, match="adjustable"):
        QuotaRow(**row)


# ---------------------------------------------------------------- stored files


def test_gold_round_trip_keeps_endpoint_type():
    doc = answer(document())
    stored = json.loads(doc.model_dump_json())
    assert [e["endpoint_type"] for e in stored["endpoints"]] == [
        "dual_stack",
        "fips_dual_stack",
    ]
    # the stored computed field does not trip extra="forbid" when loading a file
    assert (
        ServiceDocument.model_validate(stored, context=stored_context(SERVICE)) == doc
    )


def test_endpoint_type_in_a_model_answer_is_rejected():
    # In an answer the key is a field the model invented: it goes to the repair call.
    row = endpoint_row(endpoint_type="dual_stack")
    with pytest.raises(ValidationError, match="endpoint_type"):
        answer(document(endpoints=[row]))


def run_record(**overrides):
    record = {
        "file": "006-amazon-aurora-dsql.pdf",
        "group": "short",
        "model": "claude-haiku-4-5",
        "prompt_version": "v1",
        "sampling": {"name": "t0", "temperature": 0.0, "top_p": None},
        "attempts": 1,
        "latency_ms": 1234,
        "usage": {"input_tokens": 1500, "output_tokens": 900},
        "status": "ok",
        "output": document(),
        "error": None,
    }
    return record | overrides


def test_ok_record_round_trips():
    record = load_record(run_record())
    line = record.model_dump_json()
    assert (
        RunRecord.model_validate_json(line, context=stored_context(SERVICE)) == record
    )


def test_record_built_from_a_validated_answer_still_needs_a_context():
    # Pydantic re-runs ServiceDocument's after-validator on an instance too, so the
    # pipeline builds its Run Record with the same answer context.
    fields = run_record(output=answer(document()))
    with pytest.raises(ValidationError, match="context"):
        RunRecord(**fields)
    record = RunRecord.model_validate(fields, context=answer_context(SERVICE))
    assert record.output.service == SERVICE


def test_float_latency_is_rounded_to_whole_milliseconds():
    assert load_record(run_record(latency_ms=1234.56)).latency_ms == 1235


@pytest.mark.parametrize(
    ("status", "output", "error"),
    [
        (Status.OK, None, None),  # ok without an output
        (Status.OK, document(), "1 validation error"),  # ok with an error
        (Status.REPAIRED, document(), None),  # repaired without the first error
        (Status.FAILED, document(), "1 validation error"),  # failed with an output
        (Status.FAILED, None, None),  # failed without an error
    ],
)
def test_record_status_must_match_output_and_error(status, output, error):
    with pytest.raises(ValidationError, match="status"):
        load_record(run_record(status=status, output=output, error=error))


@pytest.mark.parametrize(
    ("status", "output", "error"),
    [
        (Status.REPAIRED, document(), "1 validation error"),
        (Status.FAILED, None, "1 validation error"),
    ],
)
def test_repaired_and_failed_records_are_valid(status, output, error):
    record = load_record(run_record(status=status, output=output, error=error))
    assert record.status == status


def test_record_needs_at_least_one_attempt():
    with pytest.raises(ValidationError, match="attempts"):
        load_record(run_record(attempts=0))
