# Implementation steps — HW 3 (Agent System)

Working plan and execution log for stage 3 up to the deadline **02.12 23:59**. What we build is in the
spec [`superpowers/specs/2026-11-24-hw3-agent-design.md`](superpowers/specs/2026-11-24-hw3-agent-design.md)
and the ADRs ([0009](adr/0009-mcp-for-owned-data.md), [0010](adr/0010-side-effects-gated-in-code.md),
[0011](adr/0011-retrieved-text-is-data.md), [0012](adr/0012-agent-state-in-sqlite.md),
[0013](adr/0013-local-trace-is-the-record.md)); the task-level plan is
[`superpowers/plans/2026-11-24-hw3-agent.md`](superpowers/plans/2026-11-24-hw3-agent.md); the assignment
is [`hw3-brief.md`](hw3-brief.md); how we work with Git is in [`GIT_RULES.md`](GIT_RULES.md). HW 2 is
tracked, frozen, in [`hw2-implementation-steps.md`](hw2-implementation-steps.md); step numbers and
finding numbers continue from it.

> **Maintenance rule:** a step's entry in this file (status + the "Done" subsection) is updated
> **in the same PR** as the step's code, not afterwards. A step is not finished until its entry exists here.

> **Status comes from git, not from prose.** If a row here and `git log --oneline origin/main` disagree,
> git is right.

Statuses: ✅ merged (PR, sha) · 🔄 in progress (branch or open PR) · ⬜ not started · ⏸ blocked

## 1. Standing rules

Apply to every step and are not repeated in the steps:

- **The spec is the source of truth.** Code is checked against the spec; a decision that changes it is
  first a spec amendment (and an ADR if a principle changes), then code.
- **Money before the run.** Before every paid Claude run, an estimate via `count_tokens`, stated; a run
  under $1 goes without asking, anything above waits for Petro's "ok". Actual spend goes into section 5
  after the run. The limit is **$10** for the whole of HW 3 (D19).
- **Keys only in `.env`**, only `.env.example` in Git; CI reads the `ANTHROPIC_API_KEY` repository secret.
- **Nothing in `data/` is deleted** — only moved. The HW 2 corpus and `src/rag/` behaviour do not change
  (D22).
- **One branch = one step = one PR**; before a PR, `make check` is green; commit, push, PR and merge
  only on Petro's word.
- **Temporary: stacked branches until HW 2 is checked** (Petro, 25.11; the plan's Global Constraints).
  HW 2 is under the lecturer's review, expected to end in 1–3 days (by about 28.11), and nothing is
  merged into `main` until then. A step branch started inside that window is cut from the previous step
  branch, and its PR has that branch as its base. When Petro says HW 2 is checked, the open PRs are
  merged in order, each one's base switched to `main` first, and no step branch is deleted before the
  stack is merged. After that, every new step branch is cut from an up-to-date `main` again.
- **Status rows (D21, as D9).** A step's own PR sets its row to `🔄 PR #N` (a `docs:` commit after
  `gh pr create`). The next step's PR flips it to `✅ PR #N (merge sha)`; a row closed inside the stacked
  window has no merge sha yet, and the first PR after the window adds the shas. Step 26's row is closed
  by the pre-submission check against the brief.
- **A finding is not fixed inside someone else's step.** It is recorded under "Deferred findings" (from
  F33) with the step where it will be closed, and closed separately.
- **AI-first log.** Every step adds 1–2 lines to section 9 whenever something generated had to be
  corrected, with the commit; `REFLECTION.md` is written from it (spec §14).
- **English only** for every repository artefact, prompt, tool description, eval request and agent
  answer (D17).
- **Entries are short:** the "Done" subsection is at most 10 lines.
- **Terms:** "Well-Architected" for the AWS Well-Architected Framework — never "WA", never "AWS WAF"
  (that is the Web Application Firewall).

## 2. Prerequisites

| What | Who | Needed before step | Status |
|---|---|---|---|
| `.env` with `ANTHROPIC_API_KEY` (same key as HW 1 and HW 2) | Petro | 22 | ✅ (HW 1) |
| Langfuse account, project and keys (`LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_BASE_URL`) in `.env`, ~10 min; verified with `make langfuse-check` in Task 22.9 | Petro | 22 | ✅ 25.11 (keys in `.env`; `make langfuse-check` accepted them, EU region) |
| Read the checkpoint feedback of lesson 14 (26.11) against the spec | Petro | 23 | ⬜ |
| Check the architectures in the registry are realistic, ~30 min | Petro | 23 | ⬜ |
| Check the task set, ~1 h; "ok" on the estimate of the final runs | Petro | 25 | ⬜ |
| Write the conclusions of `REFLECTION.md`, ~1 h | Petro | 26 | ⬜ |

## 3. Steps overview

| # | Step | Branch | Who / Petro's time | Points (HW criterion) | By | Status |
|---|---|---|---|---|---|---|
| 21 | Housekeeping: brief, this file, spec + plan in Git, ADR-0009–0013, CLAUDE.md, GLOSSARY, `.env.example`, `.gitignore`, `docs/coding-agent-memory.md` | `step-21-hw3-setup` | review ~20 min; Langfuse keys ~10 min | 4: instructions in the repo (part of 3 + 3) | 25.11 | ✅ PR #48 |
| 22 | Agent core: loop, limits, local trace, `search_corpus`, `record_finding` with guard and idempotency, SQLite store, faults wrapper, minimal eval runner, first fault run, Langfuse sink | `step-22-agent-core` | review ~1 h | 1: tools (3), control (4), faults (4) | 27.11 | 🔄 PR #49 |
| 23 | MCP server: registry, quotas, client, 403; first fault run of the MCP faults | `step-23-mcp` | review ~30 min; architectures ~30 min | 2: MCP server (4), permissions (3), why MCP (1) | 28.11 | ⬜ |
| 24 | Critic, overlay (injection, editions), memory, feedback, history summary | `step-24-rag-memory` | review ~45 min | 3: retrieval as a decision, injection, versions (5), memory (3), feedback (3) | 29.11 | ⬜ |
| 25 | Task set, checks, runner metrics, `lint`, ablations | `step-25-tasks` | check the tasks ~1 h; "ok" on the estimate | task set and report (2, part) | 30.11 | ⬜ |
| 26 | 3 final runs, `REPORT-hw3.md`, `REPORT.md` pointer, README, `REFLECTION.md`, pre-submission check | `step-26-report` | `REFLECTION.md` conclusions ~1 h | task set and report (2), reflection (3 + 3), repository (2) | 01.12 | ⬜ |

02.12 is the buffer. If time runs short, the cut order of spec §16 applies; never cut: Langfuse (D16), the
six-pillar coverage of a review (D25), the limits, the confirmation gate, the 403 tasks.

## 4. Steps

For every step: **goal · files · done when · open** (the plan) and **done** (the log, after the
merge). The task-level detail (interfaces, tests) is in the plan file.

### Step 21 — Housekeeping

- **Goal:** everything a later step reads exists in the repository: the brief, this file, the terms,
  the five ADRs, the approved spec and plan, the coding agent's standing rules.
- **Files:** `docs/hw3-brief.md`, this file, `CLAUDE.md`, `GLOSSARY.md`, ADR-0009–0013,
  `docs/coding-agent-memory.md`, `.gitignore`, `.env.example`, `docs/superpowers/`, one line at the top
  of `docs/hw2-implementation-steps.md`.
- **Done when:** `make check` green (393 tests, as on `main`); `CLAUDE.md` points every HW 3 question to
  the right file.
- **Open:** Langfuse keys in `.env` (Petro), before step 22.
- **Done:** `docs/hw3-brief.md` (the brief translated almost verbatim; HW 3 command `make agent`), this
  file, ADR-0009–0013, `docs/coding-agent-memory.md` (6 auto-memory rules), GLOSSARY "Agent (stage 3)"
  (26 terms), `CLAUDE.md` → stage 3 (budget, model, three "Read before…" rows, the temporary
  stacked-branch line), `.env.example` (Langfuse keys), `.gitignore` (`var/`), the frozen line of the HW 2
  file, the spec and the plan in Git. An independent review found 1 important and 13 minor wording
  issues, all fixed before the commit. `make check`: 393 passed.

### Step 22 — Agent core

- **Goal:** a working agent loop on `claude-haiku-5-5` with two tools of its own (`search_corpus`,
  `record_finding`), every limit of spec §6, the faults wrapper of §7, the confirmation gate and
  idempotency of §8, state in SQLite, a local trace and its Langfuse mirror.
- **Files:** `src/agent/` (config, store, llm, tools, faults, search_tool, findings, loop, tracing,
  session, cli), `config/agent.yaml`, `prompts/agent_system_v1.txt`, `prompts/agent_tools_v1.json`,
  `evals/agent/` (minimal runner), `Makefile`, tests.
- **Done when:** `make check` green; the first fault run shows retries only for read-only tools and an
  honest "unavailable"; Petro sees a request's trace in Langfuse.
- **Open:** limits re-measured after the first run (spec §6).
- **Relevance band (Task 22.4, 25.11; `uv run python -m evals.agent.relevance_band`, local, $0).** Top-1
  reranker score (`hybrid_rerank`, uncalibrated logit) of the 20 answerable questions of
  `evals/testset.jsonl` against the 14 `no_answer` ones (4 there + 10 held-out):
  - answerable: −1.10 (sim03), 1.88 (old01), then 3.81–9.13, median 5.41;
  - no_answer: −5.10 to 0.58 for 9 of them, then 2.45 (held09), 2.59 (none01), 3.48 (none04),
    4.52 (held10), 7.89 (held05).

  The best cut, 3.64, leaves 4 of 34 on the wrong side (sim03 and old01 below it, held10 and held05
  above it). `relevance_threshold: 3.6` is set: the band is a hint in the tool result, not a gate, and
  the description says only that all-`low` results *probably* mean no answer. The cut is fitted on the
  same 34 questions, so its 88 % is optimistic; the report says so (F32 asked for a second signal).
- **First fault run (Task 22.8, 25.11; `evals/agent/results/2026-11-25-v1-run1/`, estimate $0.008,
  actual $0.0022):** the run scored 3 / 3, but only t10 (no tool) and t22a (`503` on `search_corpus`)
  are real passes. t22a: each search took 3 attempts (2 retries) and the answer says the search is
  unavailable, with no recommendation from memory. t19 (`read_only`) "passed" without reaching the gate:
  `record_finding` refused earlier, with "read the architecture with get_architecture first", because
  `get_architecture` arrives in step 23. The final review caught it; t19 now has a precondition (the
  result says "recording is switched off"), so it scores `invalid` until step 23, and its first real
  run is there, together with t16–t18 (which write a finding). The run directory is kept as it is.
- **Prompt cache (measured):** the tools + system prefix is 2,636 tokens; the first call of a run writes
  it (`cache_write_tokens` 2,636) and every later call reads it (`cache_read_tokens` 2,636), so it is
  above Haiku 5.5's 512-token minimum.
- **One full review (Task 22.8 Step 5b, 25.11):** a described data-lake architecture (no MCP yet):
  3 model calls; the six pillar searches came in **one step**, then two more searches; 46.5 k input,
  4.4 k output, 7.9 k cache-read tokens; **$0.0069**; 27 s (the three calls 3.5 s, 7.5 s, 10.3 s; each
  search ≈ 0.7 s). Six findings, every pillar cited, `Pillars covered: 6 of 6`. The limits of §6 stay:
  the review used 29 % of `max_tokens`, 14 % of `max_usd`, 3 of 12 steps and 11 % of `max_seconds`;
  they are the ceiling for a model that searches one call at a time. The history inside a request is
  not cached (no breakpoint on `messages`): calls 2 and 3 re-send 19.6 k and 26.7 k uncached tokens; a
  third breakpoint would cut that, at $0.007 per review it is not worth a change now.
- **Done:** `src/agent/` config, store (all §11 tables), llm (strict tools, prompt cache, no sampling
  parameters), tools + faults (`FAULTS=`, retries for read-only tools only), `search_corpus` (session
  labels, `<document>` tags, relevance band 3.6), `record_finding` (checks in the §8 order, the gate in
  code, idempotency), loop (limits, wrap-up, partial result from the trace), tracing (local JSONL +
  Langfuse 5.2 sink), session, CLI; `prompts/agent_system_v1.txt`, `agent_tools_v1.json`; `evals/agent/`
  runner, checks, 3 tasks; make targets `agent`, `agent-ask`, `agent-eval`, `agent-estimate`,
  `findings`, `findings-resolve`, `langfuse-check`. First fault run: t10 and t22a pass (t19 invalid until step 23), one review $0.0069, Langfuse
  traces read back from its API. `make check`: 516 passed (393 before the step).

### Step 23 — MCP server

- **Goal:** an MCP server over stdio with three read-only tools (`list_architectures`,
  `get_architecture`, `get_service_quota`), team access and the 403, used by the agent as an MCP client.
- **Files:** `src/mcp_server/`, `architectures/`, `src/agent/mcp_client.py`, `Makefile` (`mcp-inspect`),
  tests.
- **Done when:** `make check` green; a review task reads its architecture over MCP; a 403 task ends with
  an explanation and no workaround.
- **Open:** —
- **Done:** —

### Step 24 — Agentic RAG, memory, feedback

- **Goal:** the critic, the adversarial overlay (an injection chunk and two editions of one rule),
  long-term memory and the history window with its summary, and feedback (`/up`, `/down`, `/reject`)
  that changes the next answer.
- **Files:** `src/agent/critic.py`, `context.py`, `search_tool.py` (overlay), `store.py`, `session.py`,
  `cli.py`, `findings.py`, `data/agent/`, tests (the plan's file map is the authority).
- **Done when:** `make check` green; the feedback test shows the next answer change.
- **Open:** one live call to check the critic's `system` message (spec §17).
- **Done:** —

### Step 25 — Task set, runner, lint, ablations

- **Goal:** ~30 tasks with deterministic checks, faults included; run metrics and stability; `lint` of
  prompts and tool descriptions in `make check`; the ablations.
- **Files:** `evals/agent/`, `Makefile` (`agent-ablations`), tests.
- **Done when:** `make check` green; Petro has checked the tasks and said "ok" to the estimate.
- **Open:** —
- **Done:** —

### Step 26 — Runs and reports

- **Goal:** three final runs with Langfuse on; `REPORT-hw3.md` with metrics, 3 failures and the fault
  table; the pointer block in `REPORT.md`; README; `REFLECTION.md`; the pre-submission check.
- **Files:** `evals/agent/results/`, `REPORT-hw3.md`, `REPORT.md`, `README.md`, `REFLECTION.md`,
  `docs/coding-agent-memory.md` (refreshed), this file.
- **Done when:** every row of section 10 has evidence; the Langfuse links of `REPORT-hw3.md` open.
- **Open:** —
- **Done:** —

## 5. Run matrix and budget

| Run id | Step | Required | Cost estimate | Actual |
|---|---|---|---|---|
| first fault run (`t10,t19,t22a`; t16–t18 moved to 23) | 22 | yes | $0.0082 (`make agent-estimate`) | $0.0022 |
| one full review measured (Task 22.8 Step 5b) | 22 | yes | ≈ $0.01–0.02 | $0.0069 |
| two `make agent-ask` questions with Langfuse on (Task 22.9) | 22 | yes | ≈ $0.002 | $0.0013 |
| first fault run of the MCP faults | 23 | yes | < $0.1 | |
| critic `system` message check (one call) | 24 | yes | < $0.01 | |
| 3 final runs of the full task set | 26 | yes | ≈ $0.15 each at the upper end | |
| 2 ablations (`--fixed-rag`, `--no-memory`) | 25–26 | yes (`--no-memory` may be cut) | ≈ $0.15 each | |
| development and manual checks | 22–26 | as needed | ≈ $1.5 | |

**API budget:** $10 for the whole of HW 3 (D19); the spec estimates **$2.5–3** in total (§16, re-measured
with `count_tokens` before step 25). Per 1,000 requests ≈ $3 for questions and ≈ $7–15 for full reviews,
capped at $50 by `max_usd = 0.05`. Spent so far: $0.0104 (step 22).

## 6. Deferred findings

Numbering continues from HW 2 (F21–F32 are in `hw2-implementation-steps.md`). F32 is taken up by the
spec (§10, the relevance band); F23 (a two-part question loses its second part) is met by the two-part
tasks of §13, where the agent may search once per part; F28 and F30 stay out of scope (§18); F24 (the
HW 2 judge) is not touched by HW 3.

| # | Finding | Found in | Closed in | Status |
|---|---|---|---|---|

## 7. Risks

From spec §17:

| Risk | What we do |
|---|---|
| Haiku 5.5 is weak at multi-step tool use | prompt versions with a changelog; `effort` is a config value; the report says what failed; Sonnet 5.5 would be a D19 amendment, its cost stated first |
| The search does not retrieve the injection chunk or both editions | the task is `invalid`, not `passed`; the overlay chunk is written on a searched topic; the task's query is tuned once and recorded |
| MCP stdio subprocess misbehaves (stdout pollution, hang on exit) | no `print` in the server; a start-up handshake test; the client closes the session in `finally` |
| Langfuse unavailable or the SDK API differs from the docs | the v4 calls are checked in the docs before code; the sink is the last task of step 22; an outage falls back to the local trace, and the final runs are repeated with Langfuse on before submission |
| Haiku refuses a benign request | `stop = refusal` in the trace, scored as a failure, never retried silently |
| A six-pillar review does not fit the limits, or Haiku skips a pillar | the limits are re-measured after the first run of step 22; critic check 5 and the review tasks check the coverage |
| The API refuses the critic's `system` message | one live call in step 24; fallback to a `user` message |
| Step 22 is too large for two days | its order gives a working loop and the first fault run before the Langfuse sink, which may finish at the start of step 23 but is never dropped |
| Time | one step = one PR; cuts in the order of spec §16 |

## 8. Plan change log

| Date | What changed |
|---|---|
| 24.11 | First version: steps 21–26 from the approved spec and plan; D10–D11 decided on 23.11, D12–D22 on 24.11 |
| 25.11 | Spec amended after a critical review: D13 and D16 amended (Langfuse mandatory), D23–D25 added; the Langfuse sink is its own Task 22.9, the last task of step 22 |
| 25.11 | `make langfuse-check` added to Task 22.9: one test trace, no Claude call, $0, to verify the keys and the region before the first traced request (Petro) |
| 25.11 | Temporary stacked branches while HW 2 is under the lecturer's review (Petro): nothing is merged into `main` for 1–3 days; afterwards the open PRs are merged in order and the normal rules apply again |
| 25.11 | Plan executed inline in one session (Petro: "Native"), with one independent code review per step before its commit |
| 25.11 | Task 22.9: `uv add langfuse` resolved 5.2.0, not the v4 of the spec; the calls are the same (spec §12 amended). The client exports only its own spans: the Anthropic SDK's OpenTelemetry span doubled every generation |
| 25.11 | Task 22.8: the first fault run of step 22 is t10, t19 and t22a; t16–t18 need `get_architecture` (the architecture hash of a finding) and run first in step 23. The §6 limits stay after the measured review (3 calls, $0.0069) |

## 9. AI-first log

What the coding agent generated and what had to be corrected; the source of `REFLECTION.md`.

| Date | Step | What was generated | What had to be corrected | Commit |
|---|---|---|---|---|
| 25.11 | 21 | GLOSSARY entry "Stop Reason" | named the API's `end_turn` as a trace value; the spec's trace values are `answer`, `truncated`, `refusal`, `error` and the limit names. Found by the independent review before the commit | PR #48 (b0c57fc) |
| 25.11 | 22 | Task 22.5 `execute` (tools.py) | the tool's own `faults` were overwritten by the wrapper's empty list, so a `duplicate` fault applied by `record_finding` was missing from the trace; caught by `test_duplicate_fault_one_row`, fixed by merging the two lists | PR #49 (f8566f6) |
| 25.11 | 22 | Task 22.9 Langfuse client setup | each Claude call appeared twice in Langfuse (our generation plus the Anthropic SDK's own OpenTelemetry span), doubling the cost shown; seen in the first traced request, fixed with `should_export_span=is_langfuse_span` and a test | PR #49 (f8566f6) |
| 25.11 | 22 | the plan's first fault run (t16–t19, t22a) | t16–t18 cannot pass before step 23: `record_finding` needs the architecture hash from `get_architecture`; the run was cut to t10, t19, t22a and the rest moved to step 23 | PR #49 (f8566f6) |
| 25.11 | 22 | the whole step, independent review before the commit | 6 Important findings fixed with a failing test each: t19 passed without reaching the gate (precondition added); a failed request or Ctrl-C crashed the chat; one failing task lost the eval summary; the frozen `today` was used as a wall clock (purge, finding dates); architecture reads survived `/new`; a failed request lost its cost; plus unvalidated task overrides | PR #49 (f8566f6) |
| 25.11 | 22 | CLI tool line `[S21]–[S17]` | a range "first–last" is wrong when a search re-uses an earlier label; `format_labels` collapses runs (written before its test, a TDD slip) | PR #49 (f8566f6) |

## 10. Pre-submission check (step 26)

`docs/hw3-brief.md`, line by line. The evidence is a path in this repository; the planned evidence below
is from spec §1 and is replaced by the real path when the step is done.

### Criteria (40 points)

| HW step | Item | Points | Evidence |
|---|---|---|---|
| 1 | ≥ 2 tools with clear descriptions and argument schemas | 3 | 6 narrow tools (spec §5), descriptions in `prompts/agent_tools_v1.json`, Pydantic schemas, `lint` in `make check` |
| 1 | Execution control: step limit, timeout, budget | 4 | `config/agent.yaml` limits, stop reason in every trace, the budget task returns a partial result (§6) |
| 1 | Argument validation, tool errors and faults: timeout / 503, format change, duplicate action | 4 | `FAULTS=` wrapper, retries for read-only tools only, schema check of tool output, idempotency key (§7, §8) |
| 2 | A working MCP server, ≥ 1 tool used by the agent | 4 | `src/mcp_server/`, 3 read-only tools over stdio, required in the review, listing and quota tasks (§9) |
| 2 | Server permissions, validation, security; access denial without a workaround | 3 | read-only, folder and service allow-lists, `TEAM` from the launcher, 403 tasks with workaround checks (§9) |
| 2 | Why MCP and not function calling | 1 | README section + ADR-0009 |
| 3 | Retrieval as the agent's decision; injection in a document; conflicting versions | 5 | `search_corpus` tool, two-part and no-search tasks, `--fixed-rag` ablation, adversarial overlay, five vs six pillars (§10) |
| 3 | Memory (short- or long-term) | 3 | both, in SQLite, with a stated retention policy (§11) |
| 3 | User feedback | 3 | `/down`, `/reject` change the next answer: a test and a before / after dialogue in README (§11) |
| — | ≥ 15 tasks with deterministic checks incl. faults; REPORT with metrics, 3 failures, fault table | 2 | ~30 tasks (§13), `REPORT-hw3.md` (§14) |
| 4 | Concrete reflection: what the coding agent did well, what had to be rewritten | 3 | `REFLECTION.md`, fed by section 9 of this file (§14) |
| 4 | Signs of review of generated code: tests, fixes, rationale | 3 | PR history, tests, section 9 entries with commit links |
| — | README, one-command launch, keys not in code | 2 | `make agent`, `.env.example` |

### What must be in the repository

| Item | Evidence |
|---|---|
| code of the agent, the tools and the MCP server | `src/agent/`, `src/mcp_server/` |
| `prompts/`: system prompt and tool descriptions with versions and changelog | `prompts/agent_system_v1.txt`, `prompts/agent_tools_v1.json`, `prompts/CHANGELOG.md` |
| `evals/`: task set incl. fault tasks, checks, run results with traces | `evals/agent/` |
| report: metrics, 3 failures, fault table | `REPORT-hw3.md`, pointer block in `REPORT.md` (D20) |
| `REFLECTION.md` | `REFLECTION.md` |
| coding agent's instructions in the repository | `CLAUDE.md`, `docs/GIT_RULES.md`, `docs/coding-agent-memory.md` |
| README: the agent, its tools, how to run the agent and the MCP server, why MCP, memory and feedback | `README.md` "Stage 3: Agent (HW 3)" |
| technical: Python 3.12, one command, keys in `.env`, cost per 1,000 requests | `pyproject.toml`, `make agent`, `.env.example`, `REPORT-hw3.md` |
