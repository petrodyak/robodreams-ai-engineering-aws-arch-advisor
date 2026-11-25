"""The MCP server of the architecture registry and the service quotas (spec §5, §9, D12, D15, ADR-0009).

Three read-only tools over stdio; the team comes from the `TEAM` environment variable that the
launcher sets, never from a tool argument. The server never prints to stdout (it belongs to the
protocol); errors at start-up and logs go to stderr. Tool descriptions are read from the same
versioned file as the agent's own tools (`prompts/agent_tools_v1.json`), so they are versioned once.

    TEAM=data-platform python -m src.mcp_server     (make mcp-inspect)
"""

import json
import logging
import os
import sys
from pathlib import Path
from typing import Annotated, Literal

from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
from mcp_types import ToolAnnotations
from pydantic import Field

from src.mcp_server.quotas import GOLD_SERVICES, quotas
from src.mcp_server.registry import (
    ARCH_ID,
    REGISTRY,
    InvalidArchitecture,
    list_team,
    load_architecture,
    owner_of,
    resolve_path,
    team_dir,
)

log = logging.getLogger("mcp_server")

TOOLS_VERSION = (
    "v1"  # the agent's config/agent.yaml `tools_version`; one file for all six tools
)
PROMPTS = (
    Path(__file__).resolve().parents[2]
    / "prompts"
    / f"agent_tools_{TOOLS_VERSION}.json"
)
TEXT = json.loads(PROMPTS.read_text(encoding="utf-8"))
READ_ONLY = ToolAnnotations(read_only_hint=True)

# WARNING: at the default INFO the server logs every tool error ("Tool 'x' failed") to stderr,
# which the agent's terminal shows; the error already reaches the model as the tool result
server = MCPServer("aws-arch-registry", log_level="WARNING")


def _team() -> str:
    return os.environ["TEAM"]


def check_startup() -> int:
    """0 when `TEAM` names a team folder; otherwise one line on stderr and 1 (spec §9)."""
    team = os.environ.get("TEAM")
    if not team:
        sys.stderr.write("MCP server: TEAM is not set\n")
        return 1
    try:
        folder = team_dir(REGISTRY, team)
    except ValueError:
        folder = None
    if folder is None or not folder.is_dir():
        sys.stderr.write(f"MCP server: unknown team '{team}'\n")
        return 1
    return 0


@server.tool(
    description=TEXT["list_architectures"]["description"], annotations=READ_ONLY
)
def list_architectures() -> dict:
    rows, broken = list_team(REGISTRY, _team())
    return {"architectures": rows, "unreadable_files": broken}


@server.tool(description=TEXT["get_architecture"]["description"], annotations=READ_ONLY)
def get_architecture(
    architecture_id: Annotated[
        str,
        Field(
            pattern=ARCH_ID,
            description=TEXT["get_architecture"]["params"]["architecture_id"],
        ),
    ],
) -> dict:
    team = _team()
    try:
        path = resolve_path(REGISTRY, team, architecture_id)
    except ValueError as error:
        raise ToolError(str(error)) from error
    if not path.is_file():
        owner = owner_of(REGISTRY, architecture_id)
        if owner is not None and owner != team:
            # the brief's "no access (403)": the id exists, its content is never read (spec §9)
            raise ToolError(
                f"access denied (403): architecture '{architecture_id}' is not available to team '{team}'"
            )
        raise ToolError(
            f"architecture '{architecture_id}' not found in the registry of team '{team}'"
        )
    try:
        return load_architecture(path).model_dump(mode="json")
    except InvalidArchitecture as error:
        raise ToolError(str(error)) from error


@server.tool(
    description=TEXT["get_service_quota"]["description"], annotations=READ_ONLY
)
def get_service_quota(
    service: Annotated[
        Literal[GOLD_SERVICES],  # type: ignore[valid-type]
        Field(description=TEXT["get_service_quota"]["params"]["service"]),
    ],
    quota_name: Annotated[
        str | None,
        Field(
            max_length=100,
            description=TEXT["get_service_quota"]["params"]["quota_name"],
        ),
    ] = None,
) -> dict:
    try:
        return quotas(service, quota_name)
    except ValueError as error:
        raise ToolError(str(error)) from error


def main() -> None:
    logging.basicConfig(stream=sys.stderr, level=logging.WARNING)
    code = check_startup()
    if code:
        sys.exit(code)
    server.run("stdio")
