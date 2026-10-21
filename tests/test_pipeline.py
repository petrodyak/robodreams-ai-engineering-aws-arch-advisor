"""The pipeline (src/extract/pipeline.py), without network.

A fake provider plays back a script of answers and call errors and records every request,
so these tests pin the repair loop (contract item 16), the Run Record sums (items 12, 19),
the prompt and config loading, and the resumable JSONL output.
"""

import json

import pytest

from src.extract import pipeline
from src.extract.llm import LLMCallError, LLMReply
from src.extract.schema import Group, RunRecord, Status, Usage, stored_context

T0 = pipeline.load_sampling("t0")
PROMPT = pipeline.load_prompt("v1")
DOC = pipeline.Document(
    file="006-amazon-aurora-dsql.pdf", service="Amazon Aurora DSQL", group=Group.SHORT
)
TEXT = "Amazon Aurora DSQL endpoints and quotas\n..."


def answer(service="Amazon Aurora DSQL", region_code="us-east-2"):
    return json.dumps(
        {
            "schema_version": "1",
            "service": service,
            "quota_table_format": "none",
            "endpoints": [
                {
                    "region_name": "US East (Ohio)",
                    "region_code": region_code,
                    "endpoint": "dsql.us-east-2.api.aws",
                    "protocol": "HTTPS",
                }
            ],
            "quotas": [],
        }
    )


def reply(
    text, *, tokens=(1000, 200), latency_ms=500, attempts=1, stop_reason="end_turn"
):
    return LLMReply(
        text=text,
        usage=Usage(input_tokens=tokens[0], output_tokens=tokens[1]),
        latency_ms=latency_ms,
        attempts=attempts,
        stop_reason=stop_reason,
    )


class FakeLLM:
    model = "fake-model"

    def __init__(self, *script):
        self.script = list(script)
        self.requests = []

    def complete(self, system, messages, sampling):
        self.requests.append(
            {"system": system, "messages": messages, "sampling": sampling}
        )
        step = self.script.pop(0)
        if isinstance(step, Exception):
            raise step
        return step


def extract(*script):
    llm = FakeLLM(*script)
    return pipeline.extract_document(llm, DOC, TEXT, PROMPT, T0), llm


# ---------------------------------------------------------------- inputs


def test_prompt_v1_has_its_three_sections():
    assert PROMPT.version == "v1"
    assert "Target service" in PROMPT.user and "{document}" in PROMPT.user
    assert "{error}" in PROMPT.repair
    assert (
        "{" not in PROMPT.system
    )  # no placeholders: the same system text for every document


def test_user_message_leaves_braces_in_the_document_alone():
    text = 'a JSON example {"a": 1} and a literal {service}'
    message = PROMPT.user_message("Amazon Athena", text)
    assert "Target service: Amazon Athena" in message
    assert text in message


@pytest.mark.parametrize(
    "content, problem",
    [
        ("=== system ===\nx\n=== user ===\n{service} {document}\n", "sections"),
        (
            "=== system ===\nx\n=== user ===\n{service}\n=== repair ===\n{error}\n",
            "placeholders",
        ),
    ],
)
def test_broken_prompt_file_is_rejected(tmp_path, content, problem):
    (tmp_path / "extract_vx.txt").write_text(content)
    with pytest.raises(ValueError, match=problem):
        pipeline.load_prompt("vx", tmp_path)


def test_sampling_configurations_come_from_the_config():
    assert (T0.name, T0.temperature, T0.top_p) == ("t0", 0.0, None)
    assert pipeline.load_sampling("t05").temperature == 0.5
    with pytest.raises(ValueError, match="unknown sampling"):
        pipeline.load_sampling("t1")


def test_manifest_gives_30_documents_with_their_text():
    docs = pipeline.load_manifest()
    assert len(docs) == 30
    assert docs[0] == DOC
    assert "Aurora DSQL" in docs[0].text()


def test_run_id_follows_the_contract():
    assert pipeline.make_run_id("claude", "v1", "t0") == "claude__v1__t0"


# ---------------------------------------------------------------- one document


def test_valid_first_answer_is_ok():
    record, llm = extract(reply(answer()))
    assert record.status == Status.OK
    assert record.output.endpoints[0].endpoint == "dsql.us-east-2.api.aws"
    assert record.error is None
    assert (record.model, record.prompt_version, record.sampling) == (
        "fake-model",
        "v1",
        T0,
    )
    request = llm.requests[0]
    assert request["system"] == PROMPT.system
    assert request["messages"] == [
        {"role": "user", "content": PROMPT.user_message(DOC.service, TEXT)}
    ]


def test_invalid_answer_gets_one_repair_call_with_the_error():
    record, llm = extract(
        reply(answer(region_code="ap-"), tokens=(1000, 200), latency_ms=500),
        reply(answer(), tokens=(1300, 210), latency_ms=700, attempts=2),
    )
    assert record.status == Status.REPAIRED
    assert record.output is not None
    # the first failure is kept for the error analysis
    assert "endpoints.0.region_code" in record.error
    # sums over both calls (contract items 12, 19)
    assert record.usage == Usage(input_tokens=2300, output_tokens=410)
    assert record.latency_ms == 1200
    assert record.attempts == 3
    first, repair = llm.requests[0]["messages"], llm.requests[1]["messages"]
    assert repair[:1] == first
    assert repair[1] == {"role": "assistant", "content": answer(region_code="ap-")}
    assert repair[2]["role"] == "user"
    assert "endpoints.0.region_code" in repair[2]["content"]


def test_wrong_service_is_repaired_not_accepted():
    # the Neighbour Tail detector (contract item 2)
    record, _ = extract(reply(answer(service="Amazon Aurora")), reply(answer()))
    assert record.status == Status.REPAIRED
    assert "expected the target service" in record.error


def test_second_failure_is_failed_and_there_is_no_third_call():
    record, llm = extract(reply("not json"), reply(answer(region_code="nowhere")))
    assert record.status == Status.FAILED
    assert record.output is None
    assert "after repair" in record.error and "region_code" in record.error
    assert len(llm.requests) == 2


def test_no_answer_is_failed_without_a_repair_call():
    error = LLMCallError("APITimeoutError: timed out", attempts=3, latency_ms=900_000)
    record, llm = extract(error)
    assert record.status == Status.FAILED
    assert record.attempts == 3
    assert record.latency_ms == 900_000
    assert record.usage == Usage(input_tokens=0, output_tokens=0)
    assert "no answer" in record.error
    assert len(llm.requests) == 1


def test_repair_call_without_an_answer_keeps_the_first_usage():
    error = LLMCallError("APITimeoutError: timed out", attempts=3, latency_ms=3000)
    record, _ = extract(reply("not json", latency_ms=500), error)
    assert record.status == Status.FAILED
    assert record.usage == Usage(input_tokens=1000, output_tokens=200)
    assert (record.attempts, record.latency_ms) == (4, 3500)
    assert "repair call: no answer" in record.error


def test_truncated_answer_is_failed_without_a_repair_call():
    # contract item 16, exception: a repair would be as long as the cut answer
    record, llm = extract(
        reply(
            '{"schema_version": "1", "end',
            tokens=(19_900, 32_000),
            stop_reason="max_tokens",
        ),
        reply(answer()),
    )
    assert record.status == Status.FAILED
    assert "cut off at the max_tokens limit" in record.error
    assert "no repair call" in record.error
    assert len(llm.requests) == 1
    assert record.usage == Usage(input_tokens=19_900, output_tokens=32_000)


def test_empty_answer_is_sent_back_as_a_placeholder():
    # the API rejects an empty assistant turn; the repair call must still go out
    _, llm = extract(reply(""), reply(answer()))
    assert llm.requests[1]["messages"][1]["content"] == pipeline.EMPTY_ANSWER


# ---------------------------------------------------------------- one run


def test_run_writes_one_loadable_record_per_document_and_resumes(tmp_path):
    raw = tmp_path / "raw"
    raw.mkdir()
    athena = pipeline.Document(
        file="004-amazon-athena.pdf", service="Amazon Athena", group=Group.EDGE
    )
    for doc in (DOC, athena):
        (raw / doc.file).with_suffix(".txt").write_text(TEXT)
    out = tmp_path / "runs" / "fake__v1__t0.jsonl"

    # first run: Athena fails twice, DSQL is fine
    llm = FakeLLM(reply(answer()), reply("not json"), reply("not json"))
    new = pipeline.run(
        llm, [DOC, athena], PROMPT, T0, out, raw_dir=raw, log=lambda _: None
    )
    assert [r.status for r in new] == [Status.OK, Status.FAILED]

    lines = out.read_text().splitlines()
    assert len(lines) == 2
    first = RunRecord.model_validate_json(lines[0], context=stored_context(DOC.service))
    assert first.output.endpoints[0].endpoint_type.value == "dual_stack"

    # second run with the same command: nothing is asked again
    again = FakeLLM()
    assert (
        pipeline.run(
            again, [DOC, athena], PROMPT, T0, out, raw_dir=raw, log=lambda _: None
        )
        == []
    )
    assert again.requests == []
    assert len(out.read_text().splitlines()) == 2
