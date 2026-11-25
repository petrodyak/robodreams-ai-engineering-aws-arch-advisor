"""The FAULTS= wrapper (spec §7; src/agent/faults.py)."""

import pytest
from pydantic import BaseModel

from src.agent.faults import (
    Fault,
    ToolUnavailable,
    apply_faults,
    faults_for,
    inject,
    parse_faults,
    with_retries,
)
from src.agent.tools import ToolEntry, execute


class NoArgs(BaseModel):
    pass


class Spy:
    """A tool that counts its calls and fails with a 503 the first `failures` times."""

    def __init__(self, failures: int = 0):
        self.calls = 0
        self.failures = failures

    def __call__(self, _args):
        self.calls += 1
        if self.calls <= self.failures:
            raise ToolUnavailable("503")
        return "quota rows"


def test_parse_faults():
    assert parse_faults("503:search_corpus,duplicate") == [
        Fault(kind="503", tool="search_corpus"),
        Fault(kind="duplicate", tool=None),
    ]
    assert parse_faults("") == []
    with pytest.raises(ValueError):
        parse_faults("explode")


def test_fault_applies_to_named_tool_only():
    faults = parse_faults("503:search_corpus")
    assert faults_for("search_corpus", faults) == [
        Fault(kind="503", tool="search_corpus")
    ]
    assert faults_for("get_service_quota", faults) == []


def test_retry_read_only_only():
    sleeps: list[float] = []
    spy = Spy(failures=99)
    entry = with_retries(
        ToolEntry(fn=spy, args_model=NoArgs, read_only=True), [], sleep=sleeps.append
    )
    outcome = execute("q", {}, {"q": entry}, timeout=1.0)
    assert spy.calls == 3
    assert sleeps == [0.5, 1.0]
    assert outcome.attempts == 3
    assert outcome.is_error
    assert outcome.text == (
        "ERROR: service unavailable (503) after 3 attempts; tell the user, do not guess"
    )

    write_spy = Spy(failures=99)
    write_entry = with_retries(
        ToolEntry(fn=write_spy, args_model=NoArgs, read_only=False),
        [],
        sleep=sleeps.append,
    )
    outcome = execute("w", {}, {"w": write_entry}, timeout=1.0)
    assert write_spy.calls == 1
    assert outcome.is_error
    assert outcome.attempts == 1


def test_retry_recovers_after_one_failure():
    sleeps: list[float] = []
    spy = Spy(failures=1)
    entry = with_retries(
        ToolEntry(fn=spy, args_model=NoArgs, read_only=True), [], sleep=sleeps.append
    )
    outcome = execute("q", {}, {"q": entry}, timeout=1.0)
    assert outcome.text == "quota rows"
    assert not outcome.is_error
    assert outcome.attempts == 2
    assert sleeps == [0.5]


@pytest.mark.parametrize("kind", ["timeout", "503", "429"])
def test_injected_fault_never_reaches_the_tool(kind):
    sleeps: list[float] = []
    spy = Spy()
    entry = inject(kind, ToolEntry(fn=spy, args_model=NoArgs, read_only=True))
    entry = with_retries(entry, [Fault(kind=kind, tool=None)], sleep=sleeps.append)
    outcome = execute("q", {}, {"q": entry}, timeout=1.0)
    assert spy.calls == 0
    assert outcome.attempts == 3
    assert f"service unavailable ({kind})" in outcome.text
    assert outcome.faults == [kind]
    assert sleeps == [0.5, 1.0]  # injected sleep: no real wait


def test_apply_faults_wraps_only_matching_tools():
    sleeps: list[float] = []
    search, quota = Spy(), Spy()
    registry = {
        "search_corpus": ToolEntry(fn=search, args_model=NoArgs, read_only=True),
        "get_service_quota": ToolEntry(fn=quota, args_model=NoArgs, read_only=True),
    }
    wrapped = apply_faults(
        registry, parse_faults("503:search_corpus"), sleep=sleeps.append
    )
    assert execute("search_corpus", {}, wrapped, timeout=1.0).is_error
    ok = execute("get_service_quota", {}, wrapped, timeout=1.0)
    assert ok.text == "quota rows"
    assert ok.faults == []
    assert search.calls == 0
    assert quota.calls == 1
