"""ToolUseLLM (src/agent/llm.py), without network.

A fake SDK client records each request and plays back scripted responses, so these tests pin the
request shape of D19 (no sampling parameters, effort in output_config), prompt caching on the stable
prefix, how a turn's blocks are kept for the history (spec §6), a refusal, the price and the retry.
"""

import anthropic
import httpx
import pytest
from anthropic.types import Message

from src.agent.llm import ToolUseLLM, turn_cost

SYSTEM = [{"type": "text", "text": "You review AWS architectures."}]
TOOLS = [
    {
        "name": "search_corpus",
        "description": "Search.",
        "input_schema": {"type": "object"},
    },
    {
        "name": "record_finding",
        "description": "Record.",
        "input_schema": {"type": "object"},
    },
]
MESSAGES = [{"role": "user", "content": "Review lakehouse-iceberg"}]

THINKING = {"type": "thinking", "thinking": "", "signature": "sig"}
TEXT = {"type": "text", "text": "I will search the corpus."}
TOOL_USE = {
    "type": "tool_use",
    "id": "toolu_1",
    "name": "search_corpus",
    "input": {"query": "data lake backup", "doc_types": None, "published_from": None},
}


def message(content, stop_reason="end_turn", usage=None):
    return Message.model_validate(
        {
            "id": "msg_test",
            "type": "message",
            "role": "assistant",
            "model": "claude-haiku-5-5",
            "content": content,
            "stop_reason": stop_reason,
            "stop_sequence": None,
            "usage": usage or {"input_tokens": 3000, "output_tokens": 700},
        }
    )


class FakeMessages:
    def __init__(self, responses):
        self.responses = list(responses)
        self.requests = []

    def create(self, **kwargs):
        self.requests.append(kwargs)
        item = self.responses.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


class FakeClient:
    def __init__(self, responses):
        self.messages = FakeMessages(responses)


def llm(*responses):
    return ToolUseLLM(
        "claude-haiku-5-5",
        "medium",
        4000,
        client=FakeClient(responses),
        sleep=lambda _: None,
    )


def test_request_has_no_sampling_params():
    client = llm(message([TEXT]))
    client.call(SYSTEM, TOOLS, MESSAGES)
    request = client._client.messages.requests[0]
    assert request["model"] == "claude-haiku-5-5"
    assert request["max_tokens"] == 4000
    assert request["output_config"] == {"effort": "medium"}
    for banned in ("temperature", "top_p", "top_k", "thinking", "tool_choice"):
        assert banned not in request


def test_cache_control_on_last_tool_and_system():
    client = llm(message([TEXT]))
    client.call(SYSTEM, TOOLS, MESSAGES)
    request = client._client.messages.requests[0]
    # Tools render before system, so these two breakpoints cover the whole stable prefix.
    assert request["tools"][-1]["cache_control"] == {"type": "ephemeral"}
    assert "cache_control" not in request["tools"][0]
    assert request["system"][-1]["cache_control"] == {"type": "ephemeral"}
    # The caller's lists are not edited: the next request of the loop sends them again unchanged.
    assert "cache_control" not in TOOLS[-1]
    assert "cache_control" not in SYSTEM[-1]


def test_thinking_blocks_kept_in_content():
    turn = llm(message([THINKING, TEXT, TOOL_USE], stop_reason="tool_use")).call(
        SYSTEM, TOOLS, MESSAGES
    )
    assert [b.type for b in turn.content] == ["thinking", "text", "tool_use"]
    assert turn.content[0].signature == "sig"
    assert turn.text == "I will search the corpus."
    assert len(turn.tool_uses) == 1
    assert turn.tool_uses[0].id == "toolu_1"
    assert turn.tool_uses[0].name == "search_corpus"
    assert turn.tool_uses[0].input["query"] == "data lake backup"
    assert turn.stop_reason == "tool_use"


def test_refusal_has_no_tool_uses():
    turn = llm(message([], stop_reason="refusal")).call(SYSTEM, TOOLS, MESSAGES)
    assert turn.stop_reason == "refusal"
    assert turn.tool_uses == []
    assert turn.text == ""


def test_truncated_response_is_not_parsed_for_tools():
    # A response cut at max_tokens may carry a half-built tool call: it is never run (spec §6).
    turn = llm(message([TEXT, TOOL_USE], stop_reason="max_tokens")).call(
        SYSTEM, TOOLS, MESSAGES
    )
    assert turn.stop_reason == "max_tokens"
    assert turn.tool_uses == []


def test_turn_cost_with_cache():
    # Haiku 5.5: $0.10 / $0.50 per MTok. Prompt caching docs: a cache read costs 0.1x the base
    # input price, a 5-minute cache write 1.25x.
    assert turn_cost("claude-haiku-5-5", 1_000_000, 0, 0, 0) == pytest.approx(0.10)
    assert turn_cost("claude-haiku-5-5", 0, 1_000_000, 0, 0) == pytest.approx(0.50)
    assert turn_cost("claude-haiku-5-5", 0, 0, 1_000_000, 0) == pytest.approx(0.010)
    assert turn_cost("claude-haiku-5-5", 0, 0, 0, 1_000_000) == pytest.approx(0.125)


def test_turn_reports_cache_tokens_and_cost():
    usage = {
        "input_tokens": 1000,
        "output_tokens": 500,
        "cache_read_input_tokens": 2000,
        "cache_creation_input_tokens": 0,
    }
    turn = llm(message([TEXT], usage=usage)).call(SYSTEM, TOOLS, MESSAGES)
    assert turn.input_tokens == 1000
    assert turn.cache_read_tokens == 2000
    assert turn.cache_write_tokens == 0
    assert turn.cost_usd == pytest.approx(
        (1000 * 0.10 + 500 * 0.50 + 2000 * 0.010) / 1e6
    )


def test_transient_error_retried():
    overloaded = anthropic.APIStatusError(
        "overloaded",
        response=httpx.Response(
            529, request=httpx.Request("POST", "https://api.anthropic.com")
        ),
        body=None,
    )
    turn = llm(overloaded, message([TEXT])).call(SYSTEM, TOOLS, MESSAGES)
    assert turn.attempts == 2
    assert turn.text == "I will search the corpus."


def test_prompt_above_price_limit_fails_loudly():
    usage = {
        "input_tokens": 60_000,
        "output_tokens": 10,
        "cache_read_input_tokens": 50_000,
    }
    with pytest.raises(ValueError, match="100K"):
        llm(message([TEXT], usage=usage)).call(SYSTEM, TOOLS, MESSAGES)
