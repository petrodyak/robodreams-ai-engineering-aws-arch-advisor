"""OllamaClient (src/extract/llm/ollama.py), without a running Ollama server.

A fake client records every request and plays back a script of responses and exceptions,
so these tests pin what the local model receives (the same schema as Claude, the sampling
and the provider constants), how a reply becomes an LLMReply, when a reply counts as cut
off, and which failures are retried (contract item 15).
"""

import httpx
import ollama
import pytest

from src.extract.llm import LLMCallError, OllamaClient, llm_schema
from src.extract.llm.ollama import num_ctx
from src.extract.schema import Sampling

T0 = Sampling(name="t0", temperature=0.0, top_p=None)
SYSTEM = "Extract the endpoints and quotas of the target service."
MESSAGES = [{"role": "user", "content": "Target service: Amazon Aurora DSQL\n..."}]


def response(text='{"schema_version": "1"}', *, done_reason="stop", tokens=(3000, 900)):
    return ollama.ChatResponse(
        model="qwen2.5:7b",
        message=ollama.Message(role="assistant", content=text),
        done=True,
        done_reason=done_reason,
        prompt_eval_count=tokens[0],
        eval_count=tokens[1],
    )


class FakeOllama:
    def __init__(self, *script):
        self.script = list(script)
        self.requests = []

    def chat(self, **kwargs):
        self.requests.append(kwargs)
        step = self.script.pop(0)
        if isinstance(step, Exception):
            raise step
        return step


def local(*script, window=32768):
    fake = FakeOllama(*script)
    sleeps = []
    client = OllamaClient(
        client=fake, window=window, sleep=sleeps.append, clock=lambda: 0.0
    )
    return client, fake, sleeps


# ---------------------------------------------------------------- the request


def test_request_carries_the_same_schema_as_claude_and_the_provider_constants():
    client, fake, _ = local(response())
    client.complete(SYSTEM, MESSAGES, T0)
    request = fake.requests[0]
    assert request["model"] == "qwen2.5:7b"
    assert request["format"] == llm_schema()  # identical schema for both models
    assert request["messages"] == [{"role": "system", "content": SYSTEM}, *MESSAGES]
    assert request["options"] == {
        "temperature": 0.0,
        "num_ctx": 32768,
        "num_predict": 18432,  # S3 trial at 16384 was cut off (23.10)
    }  # top_p unset is not sent (contract item 14)


def test_top_p_is_sent_when_a_configuration_sets_it():
    client, fake, _ = local(response())
    client.complete(SYSTEM, MESSAGES, Sampling(name="x", temperature=0.5, top_p=0.9))
    assert fake.requests[0]["options"]["top_p"] == 0.9


def test_num_ctx_comes_from_the_config():
    # finding F2: set explicitly, never Ollama's memory-dependent default
    assert num_ctx() == 32768


# ---------------------------------------------------------------- the reply


def test_reply_carries_text_usage_and_stop_reason():
    client, _, _ = local(response(text='{"a": 1}', tokens=(3000, 900)))
    reply = client.complete(SYSTEM, MESSAGES, T0)
    assert reply.text == '{"a": 1}'
    assert (reply.usage.input_tokens, reply.usage.output_tokens) == (3000, 900)
    assert reply.stop_reason == "stop"
    assert reply.attempts == 1


def test_hitting_num_predict_counts_as_cut_off():
    client, _, _ = local(response(done_reason="length"))
    assert client.complete(SYSTEM, MESSAGES, T0).stop_reason == "max_tokens"


def test_filling_the_context_window_counts_as_cut_off():
    # Ollama drops tokens silently when input + output reach num_ctx
    client, _, _ = local(response(tokens=(20000, 12768)), window=32768)
    assert client.complete(SYSTEM, MESSAGES, T0).stop_reason == "max_tokens"


# ---------------------------------------------------------------- transport retry


@pytest.mark.parametrize(
    "error",
    [
        ConnectionError("Failed to connect to Ollama"),
        httpx.ReadTimeout("timed out"),
        ollama.ResponseError("server error", status_code=500),
        ollama.ResponseError("busy", status_code=429),
    ],
)
def test_transient_error_is_retried(error):
    client, fake, sleeps = local(error, response())
    assert client.complete(SYSTEM, MESSAGES, T0).attempts == 2
    assert len(fake.requests) == 2
    assert sleeps == [1.0]


def test_unknown_model_is_not_retried():
    error = ollama.ResponseError("model 'qwen2.5:7b' not found", status_code=404)
    client, fake, _ = local(error, response())
    with pytest.raises(LLMCallError) as raised:
        client.complete(SYSTEM, MESSAGES, T0)
    assert raised.value.attempts == 1
    assert len(fake.requests) == 1
