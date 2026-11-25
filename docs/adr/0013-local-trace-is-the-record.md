---
status: accepted
date: 2026-11-24
---

# The local JSONL trace is the record; Langfuse mirrors it

The HW 3 brief requires the stop reason of every request in the trace, fault errors visible in the trace
instead of a silent `None`, and run results "with traces" in `evals/`. The eval checks must read the
trace deterministically, in CI and on a clean clone, with no account and no network. Petro wants the
traces in Langfuse too, and made it a mandatory deliverable on 25.11 (spec D16).

## Decision

- **Local trace, the record:** one JSON line per request with the question, the session, the model calls
  (tokens, $, latency), the tool calls (arguments, result truncated to 500 characters, error, attempts,
  faults), the critic verdicts, the retrieved chunk ids, the stop reason and the totals. Eval runs write
  it next to their results; the checks read only this file.
- **Langfuse, the mirror** (cloud, Python SDK 5.2 — the spec planned v4, the calls are the same; keys `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`,
  `LANGFUSE_BASE_URL` in `.env`): one trace per request grouped by session id, a generation per Claude
  call, a span per tool call (MCP ones included), stop reason, faults, prompt version and run id as
  metadata and tags, `/up` / `/down` and each eval task's pass / fail as scores.
- **Never fails a request.** Missing keys or an unreachable Langfuse degrade to the local trace with one
  warning. This fallback is for tests, CI, a clean clone and an outage, not a way to skip the deliverable:
  the three final runs are traced in Langfuse and `REPORT-hw3.md` links the traces of its three failures.
- `make langfuse-check` verifies the keys and region with one test trace and no Claude call ($0).

## Considered options

- **Langfuse only** — the UI is better for reading a trace, but the evals would need the network and an
  account, and an outage would lose the record.
- **Local trace only** — enough for the checks, but no shared view of a trace to link from the report.
- **LangSmith** — the other option the brief names; Langfuse was chosen (D16) because it is open
  source and can be self-hosted, which keeps the stage-4 monitoring options open.

## Consequences

- Only public data is sent to Langfuse (the AWS corpus and invented architectures).
- Unit tests use a fake Langfuse client (no network) to check the mapping and that a Langfuse failure
  never fails a request.
- **Stage 4:** the trace JSONL is the base for monitoring and cost tracking (spec §19).
