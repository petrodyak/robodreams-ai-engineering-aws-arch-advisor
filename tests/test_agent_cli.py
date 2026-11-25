"""The chat CLI (spec §3; src/agent/cli.py)."""

import io

from src.agent.cli import LATER, console_confirm, format_labels, parse_command, run_chat
from src.agent.loop import LoopState, TurnResult


def test_cli_eof_at_confirm_is_no():
    class Eof(io.StringIO):
        def readline(self, *_args):
            raise EOFError

    out = io.StringIO()
    assert (
        console_confirm(Eof(), out)("Record [high · Reliability · REL09-BP01] x?", {})
        is False
    )
    assert "[y/N]" in out.getvalue()


def test_confirm_yes_and_default_no():
    out = io.StringIO()
    assert console_confirm(io.StringIO("y\n"), out)("Record?", {}) is True
    assert console_confirm(io.StringIO("\n"), out)("Record?", {}) is False
    assert console_confirm(io.StringIO("maybe\n"), out)("Record?", {}) is False


class FakeSession:
    session_id = 3
    team = "data-platform"

    def __init__(self):
        self.asked: list[str] = []
        self.closed = False
        self.renewed = 0
        self.forgotten: list[str] = []
        self.feedback: list[tuple] = []

    def ask(self, question: str) -> TurnResult:
        self.asked.append(question)
        return TurnResult(
            answer=f"answer to {question}",
            stop="answer",
            partial=False,
            state=LoopState(started=0.0, steps=1, usd=0.0004),
            last_text="",
        )

    def new(self):
        self.renewed += 1

    def forget(self, key: str) -> bool:
        self.forgotten.append(key)
        return True

    def feedback_up(self) -> str:
        self.feedback.append(("up",))
        return "noted"

    def feedback_down(self, comment: str) -> str:
        self.feedback.append(("down", comment))
        return "noted"

    def reject(self, bp: str, reason: str) -> str:
        self.feedback.append(("reject", bp, reason))
        return "noted"

    def close(self):
        self.closed = True


def test_cli_eof_closes_session_and_exits_0():
    s = FakeSession()
    out = io.StringIO()
    assert run_chat(s, io.StringIO("What can you do?\n"), out) == 0
    assert s.asked == ["What can you do?"]
    assert s.closed
    assert "answer to What can you do?" in out.getvalue()


def test_cli_commands_parsed():
    assert parse_command("/new") == ("new", "")
    assert parse_command("/quit") == ("quit", "")
    assert parse_command("/down shorter please") == ("down", "shorter please")
    assert parse_command("Review lakehouse-iceberg") is None
    s = FakeSession()
    out = io.StringIO()
    script = "/up\n/down x\n/reject REL01-BP01 raised\n/forget region\n/new\n/quit\n"
    assert run_chat(s, io.StringIO(script), out) == 0
    assert LATER not in out.getvalue()  # every command works since Task 24.4
    assert s.forgotten == ["region"]
    assert s.feedback == [("up",), ("down", "x"), ("reject", "REL01-BP01", "raised")]
    assert s.renewed == 1
    assert s.asked == []
    assert s.closed


def test_format_labels_collapses_runs():
    assert format_labels(["S1", "S2", "S3", "S4", "S5"]) == "[S1]–[S5]"
    assert (
        format_labels(["S21", "S22", "S23", "S17", "S24"])
        == "[S21]–[S23], [S17], [S24]"
    )
    assert format_labels(["S7"]) == "[S7]"


class RaisingSession(FakeSession):
    def __init__(self, error: BaseException):
        super().__init__()
        self.error = error

    def ask(self, question: str) -> TurnResult:
        self.asked.append(question)
        raise self.error


def test_cli_request_error_keeps_the_chat_alive():
    # final review, finding 2: a failed request (e.g. a 400 from the API) must not end the chat
    s = RaisingSession(RuntimeError("400 bad request"))
    out = io.StringIO()
    assert run_chat(s, io.StringIO("first\nsecond\n"), out) == 0
    assert s.asked == ["first", "second"]
    assert "error: RuntimeError: 400 bad request" in out.getvalue()
    assert s.closed


def test_cli_ctrl_c_during_request_ends_cleanly():
    s = RaisingSession(KeyboardInterrupt())
    out = io.StringIO()
    assert run_chat(s, io.StringIO("first\nsecond\n"), out) == 0
    assert s.asked == ["first"]
    assert s.closed


def test_ctrl_c_at_confirm_ends_the_chat():
    # step 22 review, minor 11: Ctrl-C at [y/N] writes nothing and ends the chat cleanly
    import pytest

    class Interrupt(io.StringIO):
        def readline(self, *_args):
            raise KeyboardInterrupt

    with pytest.raises(KeyboardInterrupt):
        console_confirm(Interrupt(), io.StringIO())("Record?", {})
