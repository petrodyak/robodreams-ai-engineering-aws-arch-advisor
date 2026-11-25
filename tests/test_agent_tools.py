"""Tool specs, the strict schema subset and execute() (spec §5, §6; src/agent/tools.py)."""

import threading
import time
from typing import Literal

import pytest
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from src.agent.tools import (
    ToolEntry,
    ToolOutcome,
    execute,
    load_descriptions,
    strict_schema,
    tool_spec,
)

# Strict tool use, "JSON Schema Limitations" (claude-api skill, shared/tool-use-concepts.md,
# checked 25.11): numeric bounds, minLength / maxLength and complex array constraints are not
# supported; every object needs additionalProperties: false. `pattern` is not in the supported list.
UNSUPPORTED = {
    "minimum",
    "maximum",
    "exclusiveMinimum",
    "exclusiveMaximum",
    "multipleOf",
    "minLength",
    "maxLength",
    "minItems",
    "maxItems",
    "uniqueItems",
    "pattern",
    "default",
}


class DemoArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(min_length=3, max_length=200)
    doc_types: list[Literal["guide", "pillar"]] | None = None
    k: int = Field(default=5, ge=1, le=8)


DESCRIPTIONS = {
    "demo": {
        "description": "Search the demo corpus.",
        "params": {
            "query": "What to look for.",
            "doc_types": "Optional filter.",
            "k": "Hits.",
        },
    }
}


def _keys(node) -> set[str]:
    if isinstance(node, dict):
        return set(node) | set().union(*(_keys(v) for v in node.values()))
    if isinstance(node, list):
        return set().union(*(_keys(v) for v in node)) if node else set()
    return set()


def test_tool_spec_strict():
    spec = tool_spec("demo", DemoArgs, DESCRIPTIONS)
    assert spec["name"] == "demo"
    assert spec["strict"] is True
    assert spec["description"] == "Search the demo corpus."
    schema = spec["input_schema"]
    assert schema["additionalProperties"] is False
    assert schema["properties"]["query"]["description"] == "What to look for."
    assert not (_keys(schema) & UNSUPPORTED)
    assert "title" not in schema


def test_strict_schema_drops_length_keywords():
    schema = strict_schema(DemoArgs.model_json_schema())
    assert "minLength" not in schema["properties"]["query"]
    assert "maxLength" not in schema["properties"]["query"]
    with pytest.raises(ValidationError):
        DemoArgs(query="ab")  # the model still checks what the API no longer sees


def test_optional_is_required_nullable():
    schema = strict_schema(DemoArgs.model_json_schema())
    assert set(schema["required"]) == {"query", "doc_types", "k"}
    types = [
        branch.get("type") for branch in schema["properties"]["doc_types"]["anyOf"]
    ]
    assert "null" in types


def test_load_descriptions_v1_covers_local_tools():
    descriptions = load_descriptions("v1")
    for name in ("search_corpus", "record_finding", "remember"):
        assert descriptions[name]["description"]
        assert descriptions[name]["params"]


def _echo(args: DemoArgs) -> str:
    return f"found {args.query}"


def test_execute_ok():
    registry = {"demo": ToolEntry(fn=_echo, args_model=DemoArgs, read_only=True)}
    outcome = execute(
        "demo", {"query": "backup", "doc_types": None, "k": 5}, registry, timeout=1.0
    )
    assert outcome == ToolOutcome(text="found backup", is_error=False)


def test_execute_unknown_tool():
    outcome = execute("drop_table", {}, {}, timeout=1.0)
    assert outcome.is_error
    assert outcome.text.startswith("ERROR: unknown tool 'drop_table'")


def test_execute_bad_args_returns_error():
    registry = {"demo": ToolEntry(fn=_echo, args_model=DemoArgs, read_only=True)}
    outcome = execute("demo", {"doc_types": None, "k": 5}, registry, timeout=1.0)
    assert outcome.is_error
    assert outcome.text.startswith("ERROR:")
    assert "query" in outcome.text


def test_execute_exception_returns_error():
    def broken(_args):
        raise RuntimeError("index not loaded")

    registry = {"demo": ToolEntry(fn=broken, args_model=DemoArgs, read_only=True)}
    outcome = execute(
        "demo", {"query": "backup", "doc_types": None, "k": 5}, registry, timeout=1.0
    )
    assert outcome.is_error
    assert "index not loaded" in outcome.text


def test_execute_timeout():
    def slow(_args):
        time.sleep(0.5)
        return "late"

    registry = {"demo": ToolEntry(fn=slow, args_model=DemoArgs, read_only=True)}
    outcome = execute(
        "demo", {"query": "backup", "doc_types": None, "k": 5}, registry, timeout=0.05
    )
    assert outcome.is_error
    assert "timeout" in outcome.text


def test_write_tool_runs_on_calling_thread():
    seen: dict[str, int] = {}

    def write_tool(_args):
        seen["write"] = threading.get_ident()
        return "ok"

    def read_tool(_args):
        seen["read"] = threading.get_ident()
        return "ok"

    registry = {
        "write": ToolEntry(fn=write_tool, args_model=DemoArgs, read_only=False),
        "read": ToolEntry(fn=read_tool, args_model=DemoArgs, read_only=True),
    }
    args = {"query": "backup", "doc_types": None, "k": 5}
    execute("write", args, registry, timeout=1.0)
    execute("read", args, registry, timeout=1.0)
    assert seen["write"] == threading.get_ident()
    assert seen["read"] != threading.get_ident()


def test_finish_runs_on_calling_thread():
    seen: dict[str, int] = {}

    def finish(raw: str) -> ToolOutcome:
        seen["finish"] = threading.get_ident()
        return ToolOutcome(text=raw.upper(), is_error=False)

    registry = {
        "demo": ToolEntry(fn=_echo, args_model=DemoArgs, read_only=True, finish=finish)
    }
    outcome = execute(
        "demo", {"query": "backup", "doc_types": None, "k": 5}, registry, timeout=1.0
    )
    assert outcome.text == "FOUND BACKUP"
    assert seen["finish"] == threading.get_ident()
