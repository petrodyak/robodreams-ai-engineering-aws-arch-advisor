# Implementation steps — HW 1 (Structured Extraction Service)

Working plan and execution log for stage 1 up to the deadline **27.10 23:59**. What we build is in
[`stage1-data-contract.md`](stage1-data-contract.md) and the ADRs ([0001](adr/0001-standard-quota-tables-only.md),
[0002](adr/0002-model-extracts-code-derives.md), [0003](adr/0003-format-checks-are-validation-failures.md));
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
| `.env` with `ANTHROPIC_API_KEY` (template — `.env.example`) | Petro | 4 | ⬜ |
| Ollama installed, `ollama pull qwen2.5:7b` (≈4.7 GB) | Petro | 6 | ⬜ |
| Hardware: MacBook Pro M4 Pro, 48 GB — a 7B model fits with room to spare | — | 6 | ✅ |

## 3. Steps overview

| # | Step | Branch | Who / Petro's time | Points (HW criterion) | By | Status |
|---|---|---|---|---|---|---|
| 0 | Git rules and gates (`make check`) | `step-0-git-rules-and-gates` | — | repo quality | 15.10 | ✅ PR #1 (`8076640`) |
| 1 | Data contract, GLOSSARY, ADR-0001…0003 | `step-1-contract-amendments` | — | — | 16.10 | ✅ PR #2 (`4c046be`) |
| 1.1 | This plan | `patch-1.1-implementation-steps` | review 10 min | — | 16.10 | ✅ PR #3 (`f1636f2`) |
| 1.2 | Status row for step 1.1 | `patch-1.2-step-1.1-status-row` | — | — | 17.10 | 🔄 |
| 2 | Pydantic schema + tests | `step-2-schema` | plan + review ~30 min | step 1: schema (2) | 17.10 | ⬜ |
| 3 | Shared LLM interface + Claude | `step-3-llm-claude` | review ~30 min | step 1: structured output, retry/timeout (2) | 18.10 | ⬜ |
| 4 | Prompt v1, sampling config, pipeline, `make run`, run `claude__v1__t0` | `step-4-pipeline-v1` | "ok" on the cost | step 1: all texts run (2); step 3: validation (3), logging (2) | 19.10 | ⬜ |
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
- **Done:** —

### Step 3 — Shared LLM interface + Claude

- **Goal:** one function `extract(text, service, prompt, sampling)` for both providers; Claude —
  `claude-haiku-4-5` with structured output.
- **Files:** `src/extract/llm/` (interface + `claude.py`).
- **Done when:** timeout and transport retry (up to 3 attempts, contract item 15); returns the response +
  `usage` + `latency_ms`; a unit test without network (fake client).
- **Open:** `messages.parse()` or `messages.create()` with `output_config` — to be decided in the step's
  plan (the raw response text is needed for the repair call).
- **Done:** —

### Step 4 — Prompt v1, pipeline, first run

- **Goal:** one-command launch; the first Run over all 30 documents.
- **Files:** `prompts/extract_v1.txt`, `prompts/CHANGELOG.md`, `config/sampling.yaml` (`t0`, `t05`),
  `src/extract/pipeline.py` (repair loop, item 16), `main.py`, the `make run` target,
  `results/runs/claude__v1__t0.jsonl`.
- **Done when:** 30 Run Records with model, prompt version, sampling, `attempts`, `status`;
  finding F1 (`max_tokens`) closed.
- **Open:** —
- **Done:** —

### Step 5 — Golden set

- **Goal:** 10 verified Service Documents (`gold=1` in the manifest), the reference for the metrics.
- **Files:** `data/gold/<name>.json` ×10, `data/gold/README.md` (draft run id, date, procedure
  "model-assisted, human-verified"), a gold validity test.
- **Done when:** every file checked against the PDF (endpoints, quotas, `quota_table_format`); the test passes;
  the README states the advantage of the model that produced the draft.
- **Open:** checking order — start with `short` to calibrate the procedure.
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
| `claude__v1__t0` | 4 | yes (also the gold draft) | ≈$1 (confirm with `count_tokens`) | — |
| `claude__v1__t05` | 6 | yes | ≈$1 | — |
| `qwen2.5-7b__v1__t0` | 6 | yes | $0, ≈30–60 min | — |
| `qwen2.5-7b__v1__t05` | 6 | yes | $0, ≈30–60 min | — |
| `claude__v2__t0` | 8 | yes | ≈$1 | — |
| `qwen2.5-7b__v2__t0` | 8 | yes | $0 | — |
| `qwen2.5-7b__v2__t05` | 8 | desirable | $0 | — |
| `claude__v2__t05` | 8 | only if budget remains | ≈$1 | — |

**API budget:** $5 for the whole of HW 1 → 3 required Claude runs ≈ $3 + repair calls. Spent: **$0**.

**Petro's time:** ≈6 h until the deadline (3–4 h/week); the golden set is about half of it — reserve a block on
20–22.10.

## 6. Deferred findings

Things we noticed but close somewhere other than where we found them. A closed finding stays in the table with the step
and the PR that closed it.

| # | Finding | Found in | Closed in | Status |
|---|---|---|---|---|
| F1 | `max_tokens` ≈8k (contract item 14) may not be enough: S3 — 254 rows with `region_name` ≈ 9k tokens | step 1 | step 4 (`count_tokens` + a trial call on S3) | ⬜ |
| F2 | Ollama's default `num_ctx` may truncate long input. 17.10: value 32768 in `config/sampling.yaml` (`providers.ollama`), justified by S3/EMR token measurements; still to be passed in `ollama.py` | plan | step 6 (explicit `num_ctx`) | ⬜ |
| F3 | The README must name the known limits: Standard Quota Table only (ADR-0001), the AWS domain list (ADR-0003), Neighbour Tail | step 1 | step 8 | ⬜ |
| F4 | The local branch `backup/step-0-1-grill-me-1-local-snapshot` is needed only as the basis for the tests | step 1 | after step 2 is merged — delete | ⬜ |

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
