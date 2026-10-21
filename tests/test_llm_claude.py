"""ClaudeClient and the shared retry loop (src/extract/llm/), without network.

A fake SDK client records every request and plays back a script of responses and
exceptions, so these tests pin the request shape, the transport retry (contract item 15)
and what one call reports back (text, usage, latency, attempts) for the Run Record.
"""

import anthropic
import httpx2
import pytest
from anthropic.types import Message, MessageTokensCount

from src.extract.llm import ClaudeClient, LLMCallError, llm_schema
from src.extract.llm.claude import cost_usd
from src.extract.schema import Sampling

T0 = Sampling(name="t0", temperature=0.0, top_p=None)
SYSTEM = "Extract the endpoints and quotas of the target service."
MESSAGES = [{"role": "user", "content": "Target service: Amazon Aurora DSQL\n..."}]
REQUEST = httpx2.Request("POST", "https://api.anthropic.com/v1/messages")


def message(text='{"schema_version": "1"}', stop_reason="end_turn"):
    return Message.model_validate(
        {
            "id": "msg_test",
            "type": "message",
            "role": "assistant",
            "model": "claude-haiku-4-5",
            "content": [{"type": "text", "text": text}],
            "stop_reason": stop_reason,
            "stop_sequence": None,
            "usage": {"input_tokens": 1500, "output_tokens": 900},
        }
    )


def status_error(cls, code):
    response = httpx2.Response(code, request=REQUEST)
    return cls(f"HTTP {code}", response=response, body=None)


class FakeMessages:
    def __init__(self, script):
        self.script = list(script)
        self.requests = []
        self.count_requests = []

    def count_tokens(self, **kwargs):
        self.count_requests.append(kwargs)
        return MessageTokensCount(input_tokens=4321)

    def create(self, **kwargs):
        self.requests.append(kwargs)
        step = self.script.pop(0)
        if isinstance(step, Exception):
            raise step
        return step


class FakeAnthropic:
    def __init__(self, *script):
        self.messages = FakeMessages(script)


class FakeClock:
    """perf_counter that advances only when the code sleeps or a call is made."""

    def __init__(self):
        self.now = 0.0
        self.sleeps = []

    def __call__(self):
        return self.now

    def sleep(self, seconds):
        self.sleeps.append(seconds)
        self.now += seconds


def claude(*script, clock=None):
    clock = clock or FakeClock()
    fake = FakeAnthropic(*script)
    return ClaudeClient(client=fake, sleep=clock.sleep, clock=clock), fake


# ---------------------------------------------------------------- the request


def test_request_carries_model_schema_and_limits():
    client, fake = claude(message())
    client.complete(SYSTEM, MESSAGES, T0)
    request = fake.messages.requests[0]
    assert request["model"] == "claude-haiku-4-5"
    # finding F1: a complete S3 answer is ≈14.4k tokens, cut off at 16384 in the trial
    assert request["max_tokens"] == 32000
    assert request["timeout"] == 300
    assert request["system"] == SYSTEM
    assert request["messages"] == MESSAGES
    assert request["output_config"] == {
        "format": {"type": "json_schema", "schema": llm_schema()}
    }


def test_temperature_goes_through_extra_body_and_unset_top_p_is_not_sent():
    # anthropic 1.x removed temperature/top_p from the method signatures; the API still
    # accepts them for claude-haiku-4-5 (contract item 14).
    client, fake = claude(message())
    client.complete(SYSTEM, MESSAGES, Sampling(name="t05", temperature=0.5, top_p=None))
    assert fake.messages.requests[0]["extra_body"] == {"temperature": 0.5}


def test_top_p_is_sent_when_a_configuration_sets_it():
    client, fake = claude(message())
    client.complete(SYSTEM, MESSAGES, Sampling(name="x", temperature=0.0, top_p=0.9))
    assert fake.messages.requests[0]["extra_body"] == {"temperature": 0.0, "top_p": 0.9}


def test_model_facing_schema_has_no_computed_field():
    schema = llm_schema()
    assert "endpoint_type" not in str(schema)
    assert schema["additionalProperties"] is False


# ---------------------------------------------------------------- the reply


def test_reply_carries_text_usage_and_stop_reason():
    client, _ = claude(message(text='{"a": 1}', stop_reason="max_tokens"))
    reply = client.complete(SYSTEM, MESSAGES, T0)
    assert reply.text == '{"a": 1}'
    assert (reply.usage.input_tokens, reply.usage.output_tokens) == (1500, 900)
    assert reply.stop_reason == "max_tokens"
    assert reply.attempts == 1


# ---------------------------------------------------------------- transport retry


@pytest.mark.parametrize(
    "error",
    [
        anthropic.APITimeoutError(request=REQUEST),
        anthropic.APIConnectionError(request=REQUEST),
        status_error(anthropic.RateLimitError, 429),
        status_error(anthropic.InternalServerError, 500),
        status_error(anthropic.APIStatusError, 529),  # overloaded
    ],
)
def test_transient_error_is_retried(error):
    clock = FakeClock()
    client, fake = claude(error, message(), clock=clock)
    reply = client.complete(SYSTEM, MESSAGES, T0)
    assert reply.attempts == 2
    assert len(fake.messages.requests) == 2
    assert clock.sleeps == [1.0]


def test_three_transient_failures_raise_with_the_attempt_count():
    clock = FakeClock()
    timeout = anthropic.APITimeoutError(request=REQUEST)
    client, fake = claude(timeout, timeout, timeout, message(), clock=clock)
    with pytest.raises(LLMCallError) as raised:
        client.complete(SYSTEM, MESSAGES, T0)
    assert raised.value.attempts == 3
    assert len(fake.messages.requests) == 3  # the fourth answer is never asked for
    # exponential backoff, and no sleep after the last try
    assert clock.sleeps == [1.0, 2.0]
    assert isinstance(raised.value.__cause__, anthropic.APITimeoutError)


def test_client_error_is_not_retried():
    client, fake = claude(status_error(anthropic.BadRequestError, 400), message())
    with pytest.raises(LLMCallError) as raised:
        client.complete(SYSTEM, MESSAGES, T0)
    assert raised.value.attempts == 1
    assert len(fake.messages.requests) == 1


def test_latency_covers_every_attempt_and_the_backoff():
    clock = FakeClock()
    timeout = anthropic.APITimeoutError(request=REQUEST)
    client, _ = claude(timeout, message(), clock=clock)
    assert client.complete(SYSTEM, MESSAGES, T0).latency_ms == 1000


def test_failed_call_reports_its_latency():
    clock = FakeClock()
    timeout = anthropic.APITimeoutError(request=REQUEST)
    client, _ = claude(timeout, timeout, timeout, clock=clock)
    with pytest.raises(LLMCallError) as raised:
        client.complete(SYSTEM, MESSAGES, T0)
    assert raised.value.latency_ms == 3000


# ---------------------------------------------------------------- cost


def test_count_input_tokens_sends_the_same_schema_as_a_real_call():
    client, fake = claude()
    assert client.count_input_tokens(SYSTEM, MESSAGES) == 4321
    request = fake.messages.count_requests[0]
    assert request["model"] == "claude-haiku-4-5"
    assert request["system"] == SYSTEM
    assert request["output_config"] == {
        "format": {"type": "json_schema", "schema": llm_schema()}
    }
    assert fake.messages.requests == []  # nothing billable was sent


def test_cost_uses_haiku_4_5_list_prices():
    # $1 per million input tokens, $5 per million output tokens
    assert cost_usd(1_000_000, 0) == 1.0
    assert cost_usd(200_000, 100_000) == pytest.approx(0.7)
