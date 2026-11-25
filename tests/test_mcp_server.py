"""The MCP server: three read-only tools, team access and the 403 (spec §5, §9; src/mcp_server/)."""

import asyncio
import json
from pathlib import Path

import pytest
from mcp import Client
from mcp.server.mcpserver.exceptions import ToolError

from src.mcp_server import server as srv
from src.mcp_server.quotas import GOLD_AS_OF, GOLD_SERVICES, quotas

DESCRIPTIONS = json.loads(
    Path("prompts/agent_tools_v1.json").read_text(encoding="utf-8")
)


@pytest.fixture(autouse=True)
def team(monkeypatch):
    monkeypatch.setenv("TEAM", "data-platform")


def test_list_only_own_team():
    result = srv.list_architectures()
    ids = {r["architecture_id"] for r in result["architectures"]}
    assert ids == {"lakehouse-iceberg", "streaming-ingest"}
    assert result["unreadable_files"] == []


def test_get_own_architecture():
    doc = srv.get_architecture("lakehouse-iceberg")
    assert doc["id"] == "lakehouse-iceberg"
    assert doc["team"] == "data-platform"


def test_other_team_is_403():
    with pytest.raises(ToolError) as error:
        srv.get_architecture("payments-core")
    assert str(error.value) == (
        "access denied (403): architecture 'payments-core' is not available to team 'data-platform'"
    )


def test_missing_is_not_found():
    with pytest.raises(ToolError, match="not found"):
        srv.get_architecture("no-such-arch")


def test_bad_id_rejected(monkeypatch):
    def spy(*_args, **_kwargs):
        raise AssertionError("no file may be read for a bad id")

    monkeypatch.setattr(Path, "read_text", spy)
    with pytest.raises(ToolError, match="invalid architecture id"):
        srv.get_architecture("../x")


def test_quota_value_matches_gold():
    gold = json.loads(Path("data/gold/075-aws-glue.json").read_text(encoding="utf-8"))
    by_name = {q["name"]: q["default"] for q in gold["quotas"]}
    result = srv.get_service_quota("AWS Glue", "task DPUs")
    assert result["service"] == "AWS Glue"
    assert result["as_of"] == GOLD_AS_OF.isoformat() == "2026-10-22"
    assert result["quotas"]
    for row in result["quotas"]:
        assert row["default"] == by_name[row["name"]]
    names = [r["name"] for r in result["quotas"]]
    assert "Max task DPUs per account" in names


def test_quota_no_table_service():
    result = srv.get_service_quota("AWS DataSync")
    assert result["quotas"] == []
    assert "ADR-0001" in result["note"]


def test_quota_rows_capped():
    result = quotas("AWS Glue", None)
    assert len(result["quotas"]) == 10
    assert result["more"] == 36
    assert "narrow quota_name" in result["note"]


def test_unknown_service_rejected():
    with pytest.raises(ToolError) as error:
        srv.get_service_quota("Amazon S3")
    assert "AWS Glue" in str(error.value)


def test_gold_services_are_the_ten_of_the_spec():
    assert len(GOLD_SERVICES) == 10
    assert "Amazon Kinesis Data Streams" in GOLD_SERVICES
    assert "AWS Lake Formation" in GOLD_SERVICES


def test_unknown_team_exits(monkeypatch, capsys):
    monkeypatch.setenv("TEAM", "nobody")
    assert srv.check_startup() == 1
    assert "unknown team 'nobody'" in capsys.readouterr().err
    monkeypatch.delenv("TEAM")
    assert srv.check_startup() == 1
    assert "TEAM is not set" in capsys.readouterr().err


def test_server_runs_from_another_cwd(monkeypatch, tmp_path: Path):
    monkeypatch.chdir(tmp_path)
    assert srv.check_startup() == 0
    assert {
        r["architecture_id"] for r in srv.list_architectures()["architectures"]
    } == {
        "lakehouse-iceberg",
        "streaming-ingest",
    }
    assert srv.get_service_quota("AWS Glue", "task DPUs")["quotas"]


def test_server_never_prints():
    for path in Path("src/mcp_server").rglob("*.py"):
        assert "print(" not in path.read_text(encoding="utf-8"), path


def test_descriptions_from_json():
    async def tools():
        async with Client(srv.server) as client:
            return (await client.list_tools()).tools

    listed = {t.name: t for t in asyncio.run(tools())}
    assert set(listed) == {
        "list_architectures",
        "get_architecture",
        "get_service_quota",
    }
    for name, tool in listed.items():
        assert tool.description == DESCRIPTIONS[name]["description"]
        assert tool.annotations.read_only_hint is True
    arch_props = listed["get_architecture"].input_schema["properties"]
    assert (
        arch_props["architecture_id"]["description"]
        == DESCRIPTIONS["get_architecture"]["params"]["architecture_id"]
    )
    assert set(
        listed["get_service_quota"].input_schema["properties"]["service"]["enum"]
    ) == set(GOLD_SERVICES)


def test_protocol_call_returns_403_as_error():
    async def call():
        async with Client(srv.server) as client:
            return await client.call_tool(
                "get_architecture", {"architecture_id": "payments-core"}
            )

    result = asyncio.run(call())
    assert result.is_error
    assert "access denied (403)" in result.content[0].text
