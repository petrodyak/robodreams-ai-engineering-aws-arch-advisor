"""The agent's MCP client: tool specs, response schemas, MCP faults (spec §7, §9; src/agent/mcp_client.py).

Unit tests use a fake MCP client (no subprocess); tests/test_mcp_stdio.py starts the real server.
"""

import asyncio
from pathlib import Path

import pytest
from mcp_types import CallToolResult, TextContent, Tool, ToolAnnotations
from pydantic import BaseModel

from src.agent.faults import parse_faults
from src.agent.findings import canonical_hash
from src.agent.mcp_client import McpTools, server_params
from src.agent.tools import execute
from src.mcp_server.registry import REGISTRY, load_architecture, resolve_path


class NoArgs(BaseModel):
    pass


LAKEHOUSE = load_architecture(
    resolve_path(REGISTRY, "data-platform", "lakehouse-iceberg")
).model_dump(mode="json")
QUOTA = {
    "service": "AWS Glue",
    "as_of": "2026-10-22",
    "quotas": [
        {
            "name": "Max task DPUs per account",
            "default": "Each of the other supported Regions: 500",
            "adjustable": True,
            "description": "The maximum compute capacity in DPUs.",
        }
    ],
    "more": 0,
    "source": "AWS General Reference",
}
TOOLS = [
    Tool(
        name="list_architectures",
        description="List.",
        input_schema={"type": "object", "properties": {}},
        annotations=ToolAnnotations(read_only_hint=True),
    ),
    Tool(
        name="get_architecture",
        description="Read one.",
        input_schema={
            "type": "object",
            "properties": {
                "architecture_id": {
                    "type": "string",
                    "pattern": "^[a-z0-9][a-z0-9-]{2,39}$",
                    "title": "Architecture Id",
                }
            },
            "required": ["architecture_id"],
        },
        annotations=ToolAnnotations(read_only_hint=True),
    ),
    Tool(
        name="get_service_quota",
        description="Quotas.",
        input_schema={
            "type": "object",
            "properties": {
                "service": {"type": "string", "enum": ["AWS Glue"]},
                "quota_name": {
                    "anyOf": [{"type": "string", "maxLength": 100}, {"type": "null"}],
                    "default": None,
                },
            },
            "required": ["service"],
        },
        annotations=ToolAnnotations(read_only_hint=True),
    ),
]


class FakeClient:
    """Plays the mcp Client: list_tools and call_tool, recording calls; may die mid-session."""

    def __init__(self, *, die_after: int | None = None, fail_start: bool = False):
        self.calls: list[tuple[str, dict]] = []
        self.die_after = die_after
        self.fail_start = fail_start
        self.closed = False

    async def __aenter__(self):
        if self.fail_start:
            raise ConnectionError(
                "server process exited with code 1: MCP server: TEAM is not set"
            )
        return self

    async def __aexit__(self, *exc):
        self.closed = True
        return False

    async def list_tools(self):
        class Listed:
            tools = TOOLS

        return Listed()

    async def call_tool(self, name, arguments=None, read_timeout_seconds=None):
        self.calls.append((name, arguments))
        if self.die_after is not None and len(self.calls) > self.die_after:
            import anyio

            raise anyio.ClosedResourceError
        if (
            name == "get_architecture"
            and arguments["architecture_id"] == "payments-core"
        ):
            text = "Error executing tool get_architecture: access denied (403): architecture 'payments-core' is not available to team 'data-platform'"
            return CallToolResult(
                content=[TextContent(type="text", text=text)], is_error=True
            )
        data = {"get_architecture": LAKEHOUSE, "get_service_quota": QUOTA}.get(
            name, {"architectures": [], "unreadable_files": []}
        )
        return CallToolResult(
            content=[TextContent(type="text", text="{}")],
            structured_content=data,
            is_error=False,
        )


def tools(fake: FakeClient, **kwargs) -> McpTools:
    return McpTools("data-platform", client_factory=lambda _params: fake, **kwargs)


def test_mcp_spec_strict():
    with tools(FakeClient()) as mcp:
        specs = {s["name"]: s for s in mcp.specs()}
    assert set(specs) == {"list_architectures", "get_architecture", "get_service_quota"}
    arch = specs["get_architecture"]
    assert arch["description"] == "Read one."
    assert arch["strict"] is True
    schema = arch["input_schema"]
    assert schema["additionalProperties"] is False
    assert "pattern" not in schema["properties"]["architecture_id"]
    quota = specs["get_service_quota"]["input_schema"]
    assert set(quota["required"]) == {"service", "quota_name"}
    assert "default" not in quota["properties"]["quota_name"]


def test_server_env_only_team_and_path(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test")
    monkeypatch.setenv("LANGFUSE_SECRET_KEY", "sk-lf-test")
    params = server_params("data-platform")
    assert set(params.env) == {"TEAM", "PATH"}
    assert params.env["TEAM"] == "data-platform"
    assert Path(params.cwd) == Path(__file__).resolve().parents[1]


def test_get_architecture_fills_hash():
    hashes: dict[str, str] = {}
    with tools(FakeClient()) as mcp:
        registry = mcp.entries([], arch_hashes=hashes)
        outcome = execute(
            "get_architecture",
            {"architecture_id": "lakehouse-iceberg"},
            registry,
            timeout=5,
        )
    assert not outcome.is_error
    assert '"id": "lakehouse-iceberg"' in outcome.text
    assert hashes == {"lakehouse-iceberg": canonical_hash(LAKEHOUSE)}


def test_403_is_error_text_without_prefix():
    with tools(FakeClient()) as mcp:
        registry = mcp.entries([], arch_hashes={})
        outcome = execute(
            "get_architecture",
            {"architecture_id": "payments-core"},
            registry,
            timeout=5,
        )
    assert outcome.is_error
    assert outcome.text == (
        "ERROR: access denied (403): architecture 'payments-core' is not available to team 'data-platform'"
    )


def test_schema_fault_is_error():
    with tools(FakeClient()) as mcp:
        registry = mcp.entries(parse_faults("schema"), arch_hashes={})
        outcome = execute(
            "get_service_quota",
            {"service": "AWS Glue", "quota_name": "task DPUs"},
            registry,
            timeout=5,
        )
    assert outcome.is_error
    assert "default" in outcome.text
    assert outcome.text.startswith(
        "ERROR: the quota service returned an unexpected format"
    )
    assert "500" not in outcome.text
    assert outcome.faults == ["schema"]


def test_quota_response_validated_and_passed_through():
    with tools(FakeClient()) as mcp:
        registry = mcp.entries([], arch_hashes={})
        outcome = execute(
            "get_service_quota",
            {"service": "AWS Glue", "quota_name": None},
            registry,
            timeout=5,
        )
    assert not outcome.is_error
    assert "Each of the other supported Regions: 500" in outcome.text


def test_bad_arguments_never_reach_the_server():
    fake = FakeClient()
    with tools(fake) as mcp:
        registry = mcp.entries([], arch_hashes={})
        outcome = execute(
            "get_architecture",
            {"architecture_id": "../payments/payments-core"},
            registry,
            timeout=5,
        )
    assert outcome.is_error
    assert fake.calls == []


def test_server_dies_mid_session():
    from src.agent.tools import ToolEntry

    fake = FakeClient(die_after=1)
    with tools(fake) as mcp:
        registry = mcp.entries([], arch_hashes={})
        registry["echo"] = ToolEntry(
            fn=lambda _a: "local tool still works", args_model=NoArgs, read_only=True
        )
        first = execute("list_architectures", {}, registry, timeout=5)
        dead = execute("list_architectures", {}, registry, timeout=5)
        local = execute("echo", {}, registry, timeout=5)
    assert not first.is_error
    assert dead.is_error
    assert dead.text == "ERROR: MCP server unavailable"
    assert local.text == "local tool still works"


def test_startup_failure_message():
    with pytest.raises(RuntimeError) as error, tools(FakeClient(fail_start=True)):
        pass
    assert str(error.value).startswith("MCP server did not start:")
    assert "TEAM is not set" in str(error.value)


def test_session_closed_on_exit():
    fake = FakeClient()
    with tools(fake):
        pass
    assert fake.closed


def test_args_models_match_the_server():
    # the agent validates arguments with its own models before a call; they must match the server's
    from src.mcp_server import server as srv

    async def listed():
        from mcp import Client

        async with Client(srv.server) as client:
            return {t.name: t.input_schema for t in (await client.list_tools()).tools}

    import os

    os.environ.setdefault("TEAM", "data-platform")
    server_schemas = asyncio.run(listed())
    with tools(FakeClient()) as mcp:
        registry = mcp.entries([], arch_hashes={})
    for name, schema in server_schemas.items():
        assert set(registry[name].args_model.model_fields) == set(
            schema.get("properties", {})
        ), name


class TextOnlyClient(FakeClient):
    """mcp 2.3 returns a `-> dict` tool result as JSON text only, with no structured_content."""

    async def call_tool(self, name, arguments=None, read_timeout_seconds=None):
        import json

        result = await super().call_tool(name, arguments, read_timeout_seconds)
        if result.is_error:
            return result
        text = json.dumps(result.structured_content)
        return CallToolResult(
            content=[TextContent(type="text", text=text)], is_error=False
        )


def test_json_text_result_is_parsed_and_validated():
    hashes: dict[str, str] = {}
    with tools(TextOnlyClient()) as mcp:
        registry = mcp.entries(parse_faults("schema"), arch_hashes=hashes)
        arch = execute(
            "get_architecture",
            {"architecture_id": "lakehouse-iceberg"},
            registry,
            timeout=5,
        )
        quota = execute(
            "get_service_quota",
            {"service": "AWS Glue", "quota_name": None},
            registry,
            timeout=5,
        )
    assert not arch.is_error
    assert hashes["lakehouse-iceberg"] == canonical_hash(LAKEHOUSE)
    assert quota.is_error and "default" in quota.text


def test_non_json_text_is_unexpected_format():
    class Garbage(FakeClient):
        async def call_tool(self, name, arguments=None, read_timeout_seconds=None):
            return CallToolResult(
                content=[TextContent(type="text", text="<html>502</html>")],
                is_error=False,
            )

    with tools(Garbage()) as mcp:
        registry = mcp.entries([], arch_hashes={})
        outcome = execute("list_architectures", {}, registry, timeout=5)
    assert outcome.is_error
    assert outcome.text.startswith(
        "ERROR: the registry service returned an unexpected format"
    )


def test_hash_only_for_the_id_that_was_asked():
    # review Important 2: a response for another id must not open the record_finding gate for it
    class WrongId(FakeClient):
        async def call_tool(self, name, arguments=None, read_timeout_seconds=None):
            result = await super().call_tool(name, arguments, read_timeout_seconds)
            if name == "get_architecture":
                result.structured_content = {
                    **LAKEHOUSE,
                    "id": "payments-core",
                    "team": "payments",
                }
            return result

    hashes: dict[str, str] = {}
    with tools(WrongId()) as mcp:
        registry = mcp.entries([], arch_hashes=hashes)
        outcome = execute(
            "get_architecture",
            {"architecture_id": "lakehouse-iceberg"},
            registry,
            timeout=5,
        )
    assert outcome.is_error
    assert "unexpected" in outcome.text
    assert hashes == {}


def test_specs_only_for_registered_tools():
    # review minor 3: a tool the agent does not register must not be offered to Claude
    extra = Tool(
        name="drop_all",
        description="x",
        input_schema={"type": "object", "properties": {}},
    )

    class More(FakeClient):
        async def list_tools(self):
            listed = type("Listed", (), {})()
            listed.tools = [*TOOLS, extra]
            return listed

    with tools(More()) as mcp:
        names = {s["name"] for s in mcp.specs()}
        registered = set(mcp.entries([], arch_hashes={}))
    assert (
        names
        == registered
        == {"list_architectures", "get_architecture", "get_service_quota"}
    )
