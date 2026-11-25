---
status: accepted
date: 2026-11-24
---

# Data that teams own goes through an MCP server; the public corpus search stays function calling

The HW 3 brief requires at least one tool that the agent gets through its own MCP server, and asks the
README to explain why that tool is behind MCP and not ordinary function calling. The agent has two kinds
of data. The architecture registry (`architectures/<team>/<id>.json`) belongs to teams, and who may see
which architecture is a rule. The HW 1 quota tables (`data/gold/`) are read-only reference data. The
Well-Architected corpus of HW 2 is public, and only this agent searches it. Petro decided the split
after the builder check (spec D12, 24.11).

## Decision

- One MCP server (`src/mcp_server/`, package `mcp` 2.x, stdio transport, D15) with three read-only
  tools: `list_architectures` (ids and names of the caller's team only), `get_architecture` (registry,
  access by team) and `get_service_quota` (HW 1 gold data).
- The server enforces access in one place: `TEAM` comes from the process environment set by the
  launcher, never from a tool argument; the path is built by code and checked to lie inside
  `architectures/<TEAM>/`; the service is in an allow-list; no SQL, no shell, no generic file read, no
  write tool. An architecture of another team is a `403` that names the id but never its content.
- The server process gets only `TEAM` and `PATH`: no Anthropic or Langfuse key reaches it.
- `search_corpus` stays function calling inside the agent: the corpus is public, only this agent uses
  it, and the citation check works on in-process chunk objects (session labels, the label map in
  SQLite).

## Considered options

- **Everything as function calling** — simplest, but the access rule would live in the agent and in
  every later client, and the brief's MCP item would be missing.
- **Everything behind MCP, search included** — one protocol for all tools, but search results would have
  to carry the label map across the process boundary, and the citation check would read text instead of
  chunk objects. Kept as a stretch goal after the deadline (spec §18).
- **Only `get_service_quota` behind MCP** — meets the letter of the brief with public data, so there is
  no access rule worth a server and no real 403 to test.

## Consequences

- The same server plugs into Claude Code or Claude Desktop while Petro designs, and into the stage-4
  API; in stage 4 `TEAM` comes from the caller's token and the transport becomes HTTP, the tools do not
  change.
- The server is versioned and tested on its own (path traversal, bad id, another team, unknown service,
  broken JSON, no `TEAM`), plus one integration test that starts it over stdio and checks its
  environment.
- The agent needs an MCP client with its own asyncio loop in a background thread, because the agent loop
  is synchronous (spec §9 "Threads").
- README "Why MCP" is written from this ADR.
