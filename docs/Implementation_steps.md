# Implementation steps — HW 1 (Structured Extraction Service)

Working plan and execution log for stage 1 up to the deadline **27.10 23:59**. What we build is in
[`stage1-data-contract.md`](stage1-data-contract.md) and the ADRs ([0001](adr/0001-standard-quota-tables-only.md),
[0002](adr/0002-model-extracts-code-derives.md), [0003](adr/0003-format-checks-are-validation-failures.md),
[0004](adr/0004-openrouter-for-course-exercises-only.md));
how we work with Git is in [`GIT_RULES.md`](GIT_RULES.md). This file answers "in what order, who,
by when, how do we know a step is done" (the plan) and "what was done, what we decided and why" (the log).

> **Maintenance rule:** a step's entry in this file (status + the "Done" subsection) is updated
> **in the same PR** as the step's code, not afterwards. A step is not finished until its entry exists here.

> **Status comes from git, not from prose.** A finished step is marked `✅ PR #N (merge commit sha)`; if
> a row here and `git log --oneline origin/main` disagree, git is right.

Statuses: ✅ merged (PR, sha) · 🔄 in progress (branch exists) · ⬜ not started · ⏸ blocked

## 1. Standing rules

Apply to every step and are not repeated in the steps:

- **The contract is the source of truth.** Code is checked against `stage1-data-contract.md`; a decision
  that changes it is first a contract amendment (and an ADR if a principle changes), then code.
- **Money before the run.** Before every Claude run — an estimate via `count_tokens`, stated
  and agreed; actual spend goes into section 5 after the run. The limit is $5 for the whole of HW 1.
- **Keys only in `.env`**, only `.env.example` in Git.
- **Nothing in `data/` is deleted** — only moved.
- **One branch = one step = one PR**; before a PR, `make check` is green; commit/push only on
  Petro's command.
- **A finding is not fixed inside someone else's step.** It is recorded under "Deferred findings" with the
  step where it will be closed, and closed separately.
- **Entries are short:** the "Done" subsection is at most 10 lines.

## 2. Prerequisites

| What | Who | Needed before step | Status |
|---|---|---|---|
| `.env` with `ANTHROPIC_API_KEY` (template — `.env.example`) | Petro | 4 | ✅ 21.10 (new key; `count_tokens` answers) |
| `OPENROUTER_API_KEY` in `.env` — course exercises only, no HW 1 step needs it (ADR-0004) | Petro | — | ✅ |
| Ollama installed, `ollama pull qwen2.5:7b` (≈4.7 GB) | Petro | 6 | ✅ (`ollama list` shows `qwen2.5:7b`) |
| Hardware: MacBook Pro M4 Pro, 48 GB — a 7B model fits with room to spare | — | 6 | ✅ |

## 3. Steps overview

| # | Step | Branch | Who / Petro's time | Points (HW criterion) | By | Status |
|---|---|---|---|---|---|---|
| 0 | Git rules and gates (`make check`) | `step-0-git-rules-and-gates` | — | repo quality | 15.10 | ✅ PR #1 (`8076640`) |
| 1 | Data contract, GLOSSARY, ADR-0001…0003 | `step-1-contract-amendments` | — | — | 16.10 | ✅ PR #2 (`4c046be`) |
| 1.1 | This plan | `patch-1.1-implementation-steps` | review 10 min | — | 16.10 | ✅ PR #3 (`f1636f2`) |
| 1.2 | Status row for step 1.1 | `patch-1.2-step-1.1-status-row` | — | — | 17.10 | ✅ PR #4 (`4cfa1a5`) |
| 2 | Pydantic schema + tests | `step-2-schema` | plan + review ~30 min | step 1: schema (2) | 17.10 | ✅ PR #5 (`a2852bb`) |
| 2.1 | Split `CLAUDE.md`: core rules stay, stage details move to `docs/` | `patch-2.1-claude-md-split` | review 10 min | — | 17.10 | ✅ PR #6 (`8eb97d8`) |
| 3 | Shared LLM interface + Claude | `step-3-llm-claude` | review ~30 min | step 1: structured output, retry/timeout (2) | 18.10 | ✅ PR #7 (`277e1de`) |
| 3.1 | Status row for step 3 | `patch-3.1-step-3-status-row` | — | — | 21.10 | ✅ PR #8 (`e4bfad3`) |
| 3.2 | README: "Why this is not just table parsing" | `patch-3.2-readme-not-table-parsing` | review 5 min | repo quality | 21.10 | 🔄 PR #9 |
| 4 | Prompt v1, sampling config, pipeline, `make run`, run `claude__v1__t0` | `step-4-pipeline-v1` | "ok" on the cost | step 1: all texts run (2); step 3: validation (3), logging (2) | 19.10 | 🔄 branch `step-4-pipeline-v1` |
| 5 | Golden set: drafts → manual check against the PDF | `step-5-golden-set` | **~2–3 h** | step 2: correct measurements (part of 3) | 22.10 | ⬜ |
| 6 | Ollama implementation + v1 runs | `step-6-llm-ollama` | review ~20 min | step 2: shared interface (3), ≥2 configurations (2) | 22.10 | ⬜ |
| 7 | Metrics → `results/metrics.csv` | `step-7-metrics` | review ~20 min | step 2: correct measurements (3) | **24.10 checkpoint** | ⬜ |
| 8 | Prompt v2 + CHANGELOG, v2 runs, README | `step-8-prompt-v2` | choosing changes ~30 min | step 3: ≥2 versions + changelog (3); repo quality (2) | 26.10 | ⬜ |
| 9 | `REPORT.md` (after the Q&A on 26.10) | `step-9-report` | ~1 h together | step 4 (6) | **27.10** | ⬜ |

## 4. Steps

For every step: **goal · files · done when · open** (the plan) and **done** (the log, after the
merge). "Done when" is what we check before the PR, plus `make check` green and the entry here updated.

"Done" template: *files and test count · decisions and why · deviations from the plan · findings
(→ section 6)*.

### Step 0 — Git rules and gates

- **Done:** `docs/GIT_RULES.md` (branches, commits, PRs, review), `make check` = `ruff check` +
  `ruff format --check` + `pytest`. The type checker is deliberately deferred to keep the toolchain minimal.

### Step 1 — Data contract

- **Done:** `GLOSSARY.md`, `docs/stage1-data-contract.md` (19 items), ADR-0001 (Standard
  Quota Table only), ADR-0002 (the model extracts what is printed, code derives the rest). Amendments on 16.10 after
  reconciling with the grill branch (not merged, its commit is in `backup/step-0-1-grill-me-1-local-snapshot`):
  `protocol` + `HTTP and HTTPS` (present in 7 files), `endpoint_type` + `fips_dual_stack`, ADR-0003
  (format/consistency checks → repair, because otherwise the repair loop hardly ever fires), Claude =
  `claude-haiku-4-5` (newer models do not accept `temperature`, and we need `t0`/`t05`).

### Step 1.1 — This plan

- **Done:** plan for steps 2–9; second version on 16.10 — carried over from the Silpo project's
  `implementation-steps.md`: the maintenance rule, status from git, standing rules, the "Done" log, deferred findings, the report as a
  snapshot. Not carried over: mutation testing, multiple reviewer agents, large entries.

### Step 2 — Pydantic schema

- **Goal:** `ServiceDocument` / `EndpointRow` / `QuotaRow` exactly per the contract (items 3–9), Run Record (item 12).
- **Files:** `src/extract/schema.py`, `tests/test_schema.py` (based on the tests from
  `backup/step-0-1-grill-me-1-local-snapshot`, rewritten for the contract).
- **Done when:** whitespace normalisation on every `str`; `endpoint_type` (5 values) is computed
  from the hostname; the ADR-0003 format/consistency checks fail with `ValidationError`; the JSON Schema for the model
  has no `endpoint_type` and has `additionalProperties: false`; a gold file survives a round trip.
- **Open:** —
- **Done:** `src/extract/schema.py` (315 lines), `tests/test_schema.py` (32 tests, 69 cases);
  `pyproject.toml` gets the pytest `pythonpath`. Decisions: one `NormStr` type collapses whitespace
  on every extracted `str`; validation requires a context (`answer_context(service)` /
  `stored_context(service | None)`), so a forgotten context fails instead of skipping the
  Neighbour Tail check; stored `endpoint_type` is dropped only in `stored_context`, so in a model
  answer it is an invented field; `adjustable` is strict JSON boolean; float `latency_ms` is
  rounded; Run Record `sampling` = `{name, temperature, top_p}`. Format checks stay in validators
  (ADR-0003). Found: Pydantic re-runs the after-validator on an already validated instance, so a
  Run Record needs the context too. Review findings 5–7 (unversioned Field descriptions,
  substring region match, tuple rebuild) left as is.

### Step 2.1 — Split `CLAUDE.md`

- **Done:** `CLAUDE.md` 172 → ~110 lines: it keeps only what every session needs (who, stages,
  constraints, how to work, git hard rules, a "read before you work on…" table, repo map). Moved, not
  dropped: the HW 1 assignment → `docs/hw1-brief.md`; dataset, text extraction and data quirks →
  `docs/data-notes.md`; the "current state / next step" list is superseded by this file; the schema
  summary was already in the contract. Found: the `@docs/GIT_RULES.md` import sat inside backticks, so
  it never loaded; replaced by a 6-line summary + "read before any git operation" rather than a real
  import (+207 lines in every session).

### Step 3 — Shared LLM interface + Claude

- **Goal:** one function `extract(text, service, prompt, sampling)` for both providers; Claude —
  `claude-haiku-4-5` with structured output.
- **Files:** `src/extract/llm/` (interface + `claude.py`).
- **Done when:** timeout and transport retry (up to 3 attempts, contract item 15); returns the response +
  `usage` + `latency_ms`; a unit test without network (fake client).
- **Open:** —
- **Done:** `src/extract/llm/` (`base.py` 86, `claude.py` 110 lines), `tests/test_llm_claude.py`
  (10 tests, 14 cases, fake SDK client, no network, $0). Decisions: providers only `complete(system,
  messages, sampling) -> LLMReply`; validation + repair are written once in the step 4 pipeline (the
  `extract(...)` of the plan moves there); `messages.create()` + `output_config`, not `parse()`
  (parse validates without the service context and hides the raw text); own retry loop, 3 attempts,
  backoff 1 s / 2 s, SDK `max_retries=0`, because the SDK does not report attempts; timeout 120 s per
  attempt. Found: `anthropic` 1.x dropped `temperature`/`top_p` from the signatures, so they go in
  `extra_body` (Haiku 4.5 still accepts them); both providers get `anthropic.transform_schema(...)`.
  Not verified against the live API yet (no smoke call): first real request is in step 4.
- **Also in this PR (not step 3 scope):** `openai` added via `uv add` as the OpenRouter client for
  course exercises, `OPENROUTER_API_KEY` in `.env.example`, ADR-0004 records the boundary: not an
  HW 1 provider.

### Step 3.2 — README: why this is not just table parsing

- **Done:** `README.md` gets a section explaining why the quota and endpoint tables are a
  structured-extraction task rather than table parsing: layout-mode text, Neighbour Tails,
  non-standard layouts (ADR-0001), irregular cells (ADR-0002), and why an objective golden set
  makes the model comparison measurable. Written now so `REPORT.md` (step 9) can refer to it
  instead of repeating it. Finding F3 (known limits in the README) stays with step 8 — this
  section motivates the task, it does not list the limits.

### Step 4 — Prompt v1, pipeline, first run

- **Goal:** one-command launch; the first Run over all 30 documents.
- **Files:** `prompts/extract_v1.txt`, `prompts/CHANGELOG.md`, `config/sampling.yaml` (`t0`, `t05`),
  `src/extract/pipeline.py` (repair loop, item 16), `main.py`, the `make run` target,
  `results/runs/claude__v1__t0.jsonl`.
- **Done when:** 30 Run Records with model, prompt version, sampling, `attempts`, `status`;
  finding F1 (`max_tokens`) closed.
- **Open:** — (S3 re-run under the fixed schema, decided 21.10; the earlier record is in
  `results/trials/`).
- **Done:** —
  - 21.10, commit `078a766`: pipeline, prompt v1, `make run` / `make estimate`, the S3 trial
    (F1 closed: `MAX_TOKENS` 32000, `TIMEOUT_S` 300, contract items 14/16 amended); Golden Set
    membership rebalanced in the manifest. 105 tests.
  - 21.10: the enum field descriptions (`quota_table_format`, `protocol`) were dropped by
    `anthropic.transform_schema` and never reached the model → moved to the enum docstrings; a
    test walks the schema actually sent. `docs/service-document.schema.json` (the sent schema,
    regenerated by `make schema`, run first by `make check`; a test fails on a stale copy) and
    `docs/service-document.example.json` (Aurora DSQL, 25 endpoints, 4 quotas, kept valid by a
    test). 109 tests.
  - 21.10: review findings F7–F9 fixed before the full run. A transport failure raises
    `NoAnswer` and gets no Run Record (contract item 15 amended), so the next run retries the
    document; `retry-after` is obeyed up to 60 s; a cut-off last line is dropped before
    resuming and a broken line elsewhere raises; `main.py` exits non-zero while documents
    lack a record. Two tests that pinned the old `failed`-on-no-answer behaviour were replaced
    by tests of the new contract. 117 tests.
  - 21.10: review findings F10–F11 fixed. A document that keeps getting no answer stays without
    a record and metrics count it as failed, reported as "no answer" (contract items 15, 18) —
    no classification of API errors. `run()` returns `RunResult(records, lost)`, and the cost
    summary of `main.py` includes the tokens paid for documents that ended without a record.
    118 tests.
  - 21.10: the full run `claude__v1__t0` — **30/30 `ok` on the first call**, no repair, no
    transport retry (30 calls). Input 264,757 / output 188,292 tokens ≈ **$1.21** (≈ $40 per
    1,000 documents); latency ≈ 33 s p50 / ≈ 87 s p95 (rough; step 7 computes the metric).
    The estimate was ≈ $1.9: output per Endpoint Row is lower outside S3. Valid is not correct:
    endpoint row counts differ from the manifest in both directions → finding F14.

### Step 5 — Golden set

- **Goal:** 10 verified Service Documents (`gold=1` in the manifest), the reference for the metrics.
- **Files:** `data/gold/<name>.json` ×10, `data/gold/README.md` (draft run id, date, procedure
  "model-assisted, human-verified"), a gold validity test.
- **Done when:** every file checked against the PDF (endpoints, quotas, `quota_table_format`); the test passes;
  the README states the advantage of the model that produced the draft.
- **Open:** checking order — start with `short` to calibrate the procedure. Endpoints are checked by
  a script against the target section of the `.txt` (hostnames, wraps, `region_code`, `protocol`);
  `region_name`, quotas and rows the script cannot parse are checked by hand against the PDF.
  Decided 21.10: `005-amazon-aurora` prints the same 36 hostnames twice (MySQL- and
  PostgreSQL-Compatible tables) → the gold file holds one row per hostname (36) and metrics
  compare key sets; amend contract item 6 in this step. Open: how to write the templated
  `gatewayId` endpoints of `007-amazon-bedrock-agentcore` (22 rows) — decide against the PDF.
- **Done:** —

### Step 6 — Ollama + v1 runs

- **Goal:** qwen2.5:7b through the same interface; the second sampling configurations.
- **Files:** `src/extract/llm/ollama.py`; runs `qwen2.5-7b__v1__t0`, `qwen2.5-7b__v1__t05`,
  `claude__v1__t05`.
- **Done when:** the pipeline is unchanged (only a new provider); qwen runs in the background, latency
  recorded; finding F2 (`num_ctx`) closed.
- **Open:** —
- **Done:** —

### Step 7 — Metrics

- **Goal:** all numbers for REPORT from one script (contract items 17–19).
- **Files:** `src/extract/metrics.py`, `results/metrics.csv`, tests for key-based row matching.
- **Done when:** key precision/recall + per-field accuracy on gold; `% ok`, `% ok + repaired`;
  latency p50/p95; cost per 1,000 documents — by group and in total. **Checkpoint 24.10:** link in
  `#ai-engineering-2-flood`.
- **Open:** the denominator of validity is the 30 documents of the manifest, not the lines of the
  run file: a document without a record counts as failed and is reported as "no answer"
  (contract item 18, finding F11) — needs its own test here.
- **Done:** —

### Step 8 — Prompt v2, README

- **Goal:** the second prompt version, justified by the v1 errors.
- **Files:** `prompts/extract_v2.txt`, an entry in `prompts/CHANGELOG.md` (what changed and why), v2 runs,
  `README.md` (problem, how to install and run, how to reproduce the data, known limits).
- **Done when:** every change in v2 is tied to a specific v1 error; the README passes "clean
  clone → `make install` → `make run`"; finding F3 (known limits in the README) closed.
- **Done:** —

### Step 9 — REPORT.md

- **Goal:** a "model × prompt × sampling" table, 3–5 analysed errors, the production choice
  + under which conditions the decision would change.
- **Done when:** all numbers come from `results/metrics.csv`; the Q&A feedback of 26.10 is taken into account. The report is a **dated
  snapshot**: it states at the top the commit and run ids the numbers were taken from; later code changes do not
  retroactively edit the report.
- **Done:** —

## 5. Run matrix and budget

| Run id | Step | Required | Cost estimate | Actual |
|---|---|---|---|---|
| `claude__v1__t0` | 4 | yes (also the gold draft) | ≈$1.9 (input measured: 262,867 tokens ≈ $0.26; output from the S3 trial) | **$1.21** — in 264,757 / out 188,292; 30/30 `ok`, 30 calls |
| `claude__v1__t05` | 6 | yes — **the 10 Golden Set documents only** (budget decision 21.10) | ≈$0.3 | — |
| `qwen2.5-7b__v1__t0` | 6 | yes | $0, ≈30–60 min | — |
| `qwen2.5-7b__v1__t05` | 6 | yes | $0, ≈30–60 min | — |
| `claude__v2__t0` | 8 | yes | ≈$1.8 | — |
| `qwen2.5-7b__v2__t0` | 8 | yes | $0 | — |
| `qwen2.5-7b__v2__t05` | 8 | desirable | $0 | — |
| `claude__v2__t05` | 8 | no (budget decision 21.10) | ≈$1.8 | — |

**API budget:** $5 for the whole of HW 1. Spent before the full `claude__v1__t0` run: **$0.42** — three
S3 calls: at 16384, cut off ($0.22, `results/trials/…max-tokens-16384`); at 32000 before the enum
descriptions reached the model ($0.10, `results/trials/…before-enum-descriptions`); at 32000 with the
fixed schema ($0.10, the record in `claude__v1__t0`).

**Spent after `claude__v1__t0`: $1.53** — the run $1.21 (its S3 record included) + the two S3 trials kept in
`results/trials/` ($0.22 + $0.10). With the actual run cost, the plan below is ≈ $1.53 + $0.3
(`claude__v1__t05`, gold) + ≈ $1.3 (`claude__v2__t0`) ≈ **$3.1**.

**Budget decision (21.10, variant A).** Three full Claude runs would cost ≈ $5.2, over the limit. Per-field
accuracy — the main comparison — is computed on the Golden Set only (contract item 17), so
`claude__v1__t05` runs on the 10 Golden Set documents (≈ $0.3): the model × sampling table stays complete,
and only its validity and latency for Claude t05 rest on 10 documents instead of 30 — the report says so.
Planned total ≈ $0.42 + $1.55 + $0.3 + $1.8 ≈ **$4.1**, ≈ $0.9 reserve. Rejected: B (no Claude t05 — a gap
in the sampling comparison), the Batch API (no meaningful latency), raising the limit. Revisit before
`claude__v2__t0` if the actual cost of `claude__v1__t0` is well above $1.9.

**Petro's time:** ≈6 h until the deadline (3–4 h/week); the golden set is about half of it — reserve a block on
20–22.10.

## 6. Deferred findings

Things we noticed but close somewhere other than where we found them. A closed finding stays in the table with the step
and the PR that closed it.

| # | Finding | Found in | Closed in | Status |
|---|---|---|---|---|
| F1 | `max_tokens` ≈8k (contract item 14) may not be enough: S3 — 254 rows with `region_name` ≈ 9k tokens. 21.10 trial: a complete S3 answer is 16,589 tokens (290 rows, ≈57 tokens/row), cut off at 16384 → `MAX_TOKENS` 32000, `TIMEOUT_S` 300, contract items 14/16 amended (no repair for a cut-off answer) | step 1 | step 4 (`count_tokens` + a trial call on S3) | ✅ step 4 (`step-4-pipeline-v1`) |
| F2 | Ollama's default `num_ctx` may truncate long input. 17.10: value 32768 in `config/sampling.yaml` (`providers.ollama`), justified by S3/EMR token measurements; still to be passed in `ollama.py`. 21.10: the S3 answer is ≈16.6k Claude tokens, so S3 needs ≈13.1k + ≈17k ≈ 30k of 32768 — check S3 first in step 6 | plan | step 6 (explicit `num_ctx`) | ⬜ |
| F3 | The README must name the known limits: Standard Quota Table only (ADR-0001), the AWS domain list (ADR-0003), Neighbour Tail | step 1 | step 8 | ⬜ |
| F4 | The local branch `backup/step-0-1-grill-me-1-local-snapshot` is needed only as the basis for the tests | step 1 | after step 2 is merged — delete | ✅ deleted 17.10 after PR #5 (was `e2f27cf`) |
| F5 | `Field(description=...)` texts in `schema.py` are model instructions outside `prompts/`, not covered by `prompt_version` | step 2 review | step 4 (state in `prompts/CHANGELOG.md` that schema descriptions are part of a prompt version) | ✅ step 4 (`step-4-pipeline-v1`); 21.10: the enum descriptions were not sent at all, fixed in the same step |
| F6 | `endpoint_rows` in `data/raw/manifest.csv` undercounts: it matched hostnames on one line, but wrapped hostnames are split (S3: 254 in the manifest, 290 rows extracted, all 36 extra are rejoined wraps). S3 also has several endpoint sub-tables (`s3`, `s3tables`, `s3-accesspoint`, `s3-control`); contract item 6 says "the endpoints table" | step 4 | step 5 (gold check counts rows in the PDF, not from the manifest; state "all endpoint tables of the chapter" in item 6) | ⬜ |
| F7 | A transport failure (a non-retryable 4xx such as "credit balance is too low", or a 429/529 still failing after 3 attempts) is written as a permanent `failed` Run Record, and resume skips it: after a top-up the documents stay `failed` and count against validity. The backoff (1 s, 2 s) also ignores `retry-after` | step 4 review | step 4, before the full run | ✅ step 4 (`step-4-pipeline-v1`) |
| F8 | `done_files` parses every line, so one half-written last line (killed process, full disk) makes every later resume crash with `JSONDecodeError` | step 4 review | step 4 | ✅ step 4 (`step-4-pipeline-v1`) |
| F9 | `SCHEMA_FILE` and the example path in `tests/test_schema.py` are relative to the current directory: `cd tests && pytest` fails; `pipeline.py` already uses `ROOT / ...` | step 4 review | step 4 | ✅ step 4 (`step-4-pipeline-v1`) |
| F10 | Tokens paid before a `NoAnswer` (the first call when the repair call has no answer) appear only in the run log, not in the `main.py` cost summary or any record-based cost metric, so spending against the $5 budget is under-reported | review of the F7 fix | step 4 | ✅ step 4 (`step-4-pipeline-v1`) |
| F11 | Every non-retryable error becomes `NoAnswer`, also a permanent one (400 "prompt is too long", a rejected schema): such a document never gets a record, `main.py` exits non-zero on every run, and step 7 waits for 30 records forever. Contract item 15 considers only temporary causes | review of the F7 fix | step 4 (contract items 15, 18: counted as failed in metrics; no error classification) | ✅ step 4 (`step-4-pipeline-v1`); metrics side in step 7 |
| F12 | Results-file edge cases: a line that is JSON but not an object raises a bare `TypeError` without its line number; `{"file": null}` counts as done; a complete record whose final `\n` was stripped by hand is dropped as a cut-off line (recoverable from Git) | review of the F8 fix | Petro's call | ⬜ |
| F13 | No test pins `main.py`'s non-zero exit (contract item 15) or `NoAnswer.__cause__` | review of the F7 fix | Petro's call | ⬜ |
| F14 | `claude__v1__t0` is 30/30 valid, but endpoint row counts differ from the manifest in both directions. Fewer: `078` IAM Identity Center 78 of 234, `017` DynamoDB 94 of 203, `044` RDS 78 of 165, `092` Secrets Manager 44 of 62, `048` SQS 84 of 104 (gold). More: `007` AgentCore 39 vs 22 (templated `gatewayId`, gold), `055` App Mesh 120 vs 77, `042` Redshift 253 vs 201, `038` OpenSearch 183 vs 170 (Neighbour Tail of Network Security Manager? gold), `085` Lake Formation 88 vs 75 (gold). Also `042` Redshift has `quota_table_format: none` (ADR-0001 expects `non_standard`?) and `010` CloudFront has 97 Quota Rows. Expected or manifest-side: `005` Aurora 36 of 72 (decided: one row per hostname), `074` Global Accelerator 2 of 105 (the text has 5 hostnames — manifest, F6). The manifest undercounts wrapped hostnames (F6), so these are signals, not verdicts | step 4 (full run) | step 5 (gold `048`, `007`, `038`, `085`: count against the PDF); steps 8–9 (non-gold: error analysis and v2 changes) | ⬜ |

## 7. Risks

| Risk | Impact | What we do |
|---|---|---|
| The Claude budget runs out | fewer runs in the table | estimate before every run; cut runs, not schema fields |
| qwen truncates long output / drops rows | low recall in `edge` | not a bug but material for the error analysis |
| The golden set is not checked in time | no per-field accuracy | step 5 starts right after step 4 |

## 8. Plan change log

| Date | What changed |
|---|---|
| 16.10 | First version of the plan |
| 16.10 | Practices from Silpo: maintenance rule, status from git, standing rules, per-step "Done", deferred findings (F1–F4; `max_tokens` and `num_ctx` moved here from the risks), REPORT as a snapshot; "Actual" column in the run matrix |
| 17.10 | All `.md` files translated to English; repository docs are written in English from now on |
| 17.10 | Step 2.1 added: `CLAUDE.md` split; this file is now the only place for status and next step |
| 21.10 | Step 3.2 added: README section "Why this is not just table parsing" (answers the question whether a structured source is a fair structured-extraction task) |
| 21.10 | Golden Set re-selected to 6 `short` / 3 `medium` / 1 `edge` to cut the manual check (step 5); the limits it sets on the metrics — `edge` on one document, no `non_standard` and no global service in gold — are in `data-notes.md` |
| 21.10 | Budget variant A: `claude__v1__t05` on the 10 Golden Set documents only, `claude__v2__t05` dropped (section 5); step 6 needs a `--gold` option in `main.py` |
