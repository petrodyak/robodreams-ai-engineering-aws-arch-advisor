"""ClaudeJSON (src/rag/llm.py), without network.

A fake SDK client records each request and plays back one response, so these tests pin the
request shape of spec D4 (no sampling parameters, effort in output_config), how the answer text
is read past thinking blocks, a refusal, and the price.
"""

import pytest
from anthropic.types import Message, MessageTokensCount

from src.rag.llm import PRICES, ClaudeJSON, cost_usd

SCHEMA = {
    "type": "object",
    "properties": {"found": {"type": "boolean"}},
    "required": ["found"],
    "additionalProperties": False,
}


def message(content, stop_reason="end_turn", input_tokens=3000):
    return Message.model_validate(
        {
            "id": "msg_test",
            "type": "message",
            "role": "assistant",
            "model": "claude-haiku-5-5",
            "content": content,
            "stop_reason": stop_reason,
            "stop_sequence": None,
            "usage": {"input_tokens": input_tokens, "output_tokens": 700},
        }
    )


TEXT = {"type": "text", "text": '{"found": true}'}
THINKING = {"type": "thinking", "thinking": "", "signature": "sig"}


class FakeMessages:
    def __init__(self, response):
        self.response = response
        self.requests = []
        self.count_requests = []

    def create(self, **kwargs):
        self.requests.append(kwargs)
        return self.response

    def count_tokens(self, **kwargs):
        self.count_requests.append(kwargs)
        return MessageTokensCount(input_tokens=4321)


class FakeClient:
    def __init__(self, response):
        self.messages = FakeMessages(response)


def llm(response):
    return ClaudeJSON("claude-haiku-5-5", "medium", 4000, client=FakeClient(response))


def test_request_shape():
    client = llm(message([TEXT]))
    client.complete_json("system text", "user text", SCHEMA)

    request = client._client.messages.requests[0]
    assert request["model"] == "claude-haiku-5-5"
    assert request["max_tokens"] == 4000
    assert request["system"] == "system text"
    assert request["messages"] == [{"role": "user", "content": "user text"}]
    assert request["output_config"] == {
        "format": {"type": "json_schema", "schema": SCHEMA},
        "effort": "medium",
    }
    for banned in ("temperature", "top_p", "top_k", "extra_body", "thinking"):
        assert banned not in request


def test_reads_text_blocks_by_type():
    result = llm(message([THINKING, TEXT])).complete_json("s", "u", SCHEMA)

    assert result.text == '{"found": true}'
    assert result.stop_reason == "end_turn"
    assert (result.input_tokens, result.output_tokens) == (3000, 700)
    assert result.attempts == 1


def test_refusal_returns_none():
    result = llm(message([], stop_reason="refusal")).complete_json("s", "u", SCHEMA)

    assert result.text is None
    assert result.stop_reason == "refusal"


def test_cost():
    assert PRICES["claude-haiku-5-5"] == (0.10, 0.50)
    assert cost_usd("claude-haiku-5-5", 1_000_000, 1_000_000) == pytest.approx(0.60)
    assert cost_usd("claude-sonnet-5-5", 1_000_000, 1_000_000) == pytest.approx(12.00)


def test_haiku_price_stops_at_100k():
    # Above 100K input tokens Haiku 5.5 bills at a higher rate that PRICES does not hold.
    with pytest.raises(ValueError, match="100K"):
        llm(message([TEXT], input_tokens=100_001)).complete_json("s", "u", SCHEMA)


def test_count_input_tokens_sends_the_schema():
    client = llm(message([TEXT]))

    assert client.count_input_tokens("s", "u", SCHEMA) == 4321
    request = client._client.messages.count_requests[0]
    assert request["output_config"] == {
        "format": {"type": "json_schema", "schema": SCHEMA}
    }
    assert request["messages"] == [{"role": "user", "content": "u"}]
