"""`make mcp-inspect`: start the MCP server alone over stdio and look at it (spec D15).

Lists the server's tools with their descriptions and annotations; with a tool name and JSON arguments
it calls that tool once and prints the result, error flag included. It uses the same stdio client and
the same environment as the agent (only TEAM and PATH), so what you see is what the agent gets.
The MCP Inspector (`npx @modelcontextprotocol/inspector`) needs Node.js, which this setup does not have.

    make mcp-inspect
    make mcp-inspect TOOL=get_architecture ARGS='{"architecture_id": "payments-core"}'
    make mcp-inspect TEAM=payments TOOL=list_architectures
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

from mcp import Client

from src.agent.mcp_client import _describe, server_params

ROOT = Path(__file__).resolve().parents[1]


async def inspect(team: str, tool: str | None, args: dict) -> int:
    # the agent's own launch parameters (TEAM and PATH only), so what you see is what the agent gets
    try:
        async with Client(server_params(team)) as client:
            return await _show(client, tool, args)
    except Exception as error:  # noqa: BLE001 - one line for a server that did not start (Review Focus 2)
        sys.stderr.write(f"MCP server did not start: {_describe(error)}\n")
        return 1


async def _show(client, tool: str | None, args: dict) -> int:
    if tool is None:
        for t in (await client.list_tools()).tools:
            read_only = t.annotations.read_only_hint if t.annotations else None
            print(f"{t.name}  (read_only_hint={read_only})")
            print(f"  {t.description}")
            print(f"  input: {json.dumps(t.input_schema.get('properties', {}))}\n")
        return 0
    result = await client.call_tool(tool, args)
    print(f"is_error: {result.is_error}")
    for item in result.content:
        print(getattr(item, "text", item))
    return 0  # an is_error result is a normal answer of the tool, shown above


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--team", default="data-platform")
    p.add_argument("--tool")
    p.add_argument("--args", default="{}", help="JSON object of tool arguments")
    a = p.parse_args()
    return asyncio.run(inspect(a.team, a.tool, json.loads(a.args)))


if __name__ == "__main__":
    sys.exit(main())
