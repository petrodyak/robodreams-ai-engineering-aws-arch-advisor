"""Integration: the real MCP server over stdio, as the agent starts it (spec §9). No network."""

import sys
import time
from pathlib import Path

import pytest

from src.agent.mcp_client import McpTools
from src.agent.tools import execute

ROOT = Path(__file__).resolve().parents[1]


def test_stdio_roundtrip():
    started = time.monotonic()
    with McpTools("data-platform") as mcp:
        assert {s["name"] for s in mcp.specs()} == {
            "list_architectures",
            "get_architecture",
            "get_service_quota",
        }
        hashes: dict[str, str] = {}
        registry = mcp.entries([], arch_hashes=hashes)
        own = execute(
            "get_architecture",
            {"architecture_id": "lakehouse-iceberg"},
            registry,
            timeout=10,
        )
        other = execute(
            "get_architecture",
            {"architecture_id": "payments-core"},
            registry,
            timeout=10,
        )
        quota = execute(
            "get_service_quota",
            {"service": "AWS Glue", "quota_name": "task DPUs"},
            registry,
            timeout=10,
        )
    closed = time.monotonic()
    assert not own.is_error and "lakehouse-iceberg" in hashes
    assert other.is_error
    assert "access denied (403)" in other.text
    assert "Each of the other supported Regions: 500" in quota.text
    assert closed - started < 30


def test_server_process_has_no_secrets(monkeypatch, tmp_path: Path):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test")
    monkeypatch.setenv("LANGFUSE_SECRET_KEY", "sk-lf-test")
    monkeypatch.setenv("LANGFUSE_PUBLIC_KEY", "pk-lf-test")
    names_file = tmp_path / "env.txt"
    probe = [
        sys.executable,
        str(ROOT / "tests" / "helpers" / "env_probe.py"),
        str(names_file),
    ]
    with McpTools("data-platform", cmd=probe) as mcp:
        assert mcp.specs()
    names = names_file.read_text(encoding="utf-8").splitlines()
    assert "TEAM" in names
    assert not [n for n in names if n.startswith(("ANTHROPIC", "LANGFUSE"))]


def test_server_without_team_fails_with_one_line():
    with pytest.raises(RuntimeError) as error, McpTools("nobody"):
        pass
    assert str(error.value).startswith("MCP server did not start:")


def test_mcp_inspect_bad_team_is_one_line(capsys):
    # step 23 review minor 4: a bad TEAM gives one line, not a traceback
    import asyncio

    from scripts.mcp_inspect import inspect

    assert asyncio.run(inspect("nobody", None, {})) == 1
    err = capsys.readouterr().err
    assert err.startswith("MCP server did not start:")
    assert "Traceback" not in err
