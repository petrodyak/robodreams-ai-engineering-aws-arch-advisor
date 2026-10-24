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
| 3.2 | README: "Why this is not just table parsing" | `patch-3.2-readme-not-table-parsing` | review 5 min | repo quality | 21.10 | ✅ PR #9 (`d9f8116`) |
| 4 | Prompt v1, sampling config, pipeline, `make run`, run `claude__v1__t0` | `step-4-pipeline-v1` | "ok" on the cost | step 1: all texts run (2); step 3: validation (3), logging (2) | 19.10 | ✅ PR #10 (`15e8d1a`) |
| 4.1 | Status rows for steps 4 and 3.2 | `patch-4.1-step-4-status-row` | — | — | 21.10 | ✅ PR #11 (`462e69c`) |
| 5 | Golden set: drafts → manual check against the PDF | `step-5-golden-set` | **~2–3 h** | step 2: correct measurements (part of 3) | 22.10 | ✅ PR #12 (`7d0d50a`) |
| 6 | Ollama implementation + v1 runs | `step-6-llm-ollama` | review ~20 min | step 2: shared interface (3), ≥2 configurations (2) | 22.10 | ✅ PR #13 (`a7df1d4`) |
| 7 | Metrics → `results/metrics.csv` | `step-7-metrics` | review ~20 min | step 2: correct measurements (3) | **24.10 checkpoint** | 🔄 branch `step-7-metrics` |
| 8 | Prompt v2 + CHANGELOG, v2 runs, README | `step-8-prompt-v2` | choosing changes ~30 min | step 3: ≥2 versions + changelog (3); repo quality (2) | 26.10 | ✅ PR #16 (`df1a8cd`); Claude v2 run PR #17 (`ea70c6e`); qwen runs 🔄 branch `patch-8.2-qwen-runs` |
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
  `results/runs/jsonl/claude__v1__t0.jsonl`.
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
- **Open:** — (decisions of 21.10–22.10 are in `data/gold/README.md` and contract item 6).
- **Done:**
  - 21.10, commit `3a80f0d`: `make gold-drafts` (drafts from `claude__v1__t0`, never overwrites),
    `make gold-check` (printed hostnames of every endpoints table vs the gold rows, wraps
    rejoined), `tests/test_gold.py`, `data/gold/README.md`; contract item 6 amended (every
    endpoints table, one row per hostname, templated hostnames as printed). 133 tests.
  - 22.10: all 10 files checked against the PDF by Petro (✅ in `data/gold/README.md`).
    Corrections to the Claude draft: `048` +20 rows of the "Legacy endpoints" table that the
    draft missed (a real Claude error, material for the error analysis); 5 rows removed by the
    reviewer as not in the PDF or outside items 6/7 (`033`, `085`, `007` one endpoint each;
    `048`, `076` one quota each) — `make gold-check` keeps listing those three hostnames
    because the `.txt` prints them. Net: endpoints +20 / −3, quotas −2. The README states the
    drafting model's advantage. F6 closed; F14 closed for the gold documents. 133 tests.

### Step 6 — Ollama + v1 runs

- **Goal:** qwen2.5:7b through the same interface; the second sampling configurations.
- **Files:** `src/extract/llm/ollama.py`; runs `qwen2.5-7b__v1__t0`, `qwen2.5-7b__v1__t05`,
  `claude__v1__t05__gold`.
- **Done when:** the pipeline is unchanged (only a new provider); qwen runs in the background, latency
  recorded; finding F2 (`num_ctx`) closed.
- **Open:** run order, each only after Petro's ok — (1) `qwen2.5-7b__v1__t0` (S3 again,
  now at `num_predict` 18432) and (2) `qwen2.5-7b__v1__t05` in the background; F15 makes every
  qwen answer go through a repair call, so expect ≈2–3 h per run; (3) `claude__v1__t05__gold`
  (≈ $0.27: input $0.06 + ≈42k output tokens).
- **Done:**
  - 22.10, code: `OllamaClient` behind the same `LLMClient` interface — the identical schema
    through `format`, `num_ctx` from the config (F2), `num_predict` (now 18432), a reply that hits
    `num_predict` or fills `num_ctx` is cut off (`stop_reason = max_tokens`), transport retry
    as for Claude. `main.py --model qwen2.5-7b`, `--gold` (run id suffix `__gold`; `make run
    GOLD=1`); `Document.gold` from the manifest. Contract items 11, 14, 18 amended. The
    pipeline is unchanged.
  - 22.10, readable run files: `results/runs/jsonl/` (the JSONL, source of truth, existing
    files moved with `git mv`) and `results/runs/md/` (a Markdown mirror per run — summary
    table, then endpoints, quotas and the error text per document), rewritten from the whole
    JSONL after every record, so a long qwen run can be read while it runs. `src/extract/
    report_md.py`, `make runs-md` rebuilds every mirror; contract item 12 amended. The Run
    Record format is unchanged; only the JSONL path moved.
  - 23.10, trials, $0: qwen t0 on S3 was cut off at `num_predict` 16384 (13,714 in / 16,384
    out, 505 s ≈ 32 tokens/s; `num_ctx` held: 30,098 of 32,768) — kept in `results/trials/`. A
    direct call on `006` (scratchpad, not a run) showed why: qwen writes indented JSON (1.32×
    the characters) but about as many tokens as Claude (1,493 vs 1,454), so S3 needs ≈17.1k →
    `num_predict` 18432 (contract item 14). The same call found F15.
  - 23.10–24.10, the three Golden Set runs (`patch-6.1-v1-runs`; checkpoint scope, see the
    plan change log): `claude__v1__t05__gold` 10/10 `ok`, 306 s, $0.27 — identical row counts
    and accuracy to `t0` (temperature 0.5 changes nothing for Haiku 4.5 here);
    `qwen2.5-7b__v1__t0__gold` 9 `repaired` + 1 `failed` (`048` cut off at `num_predict`
    after a repetition loop, 18,432 output tokens for a 4.8k-token input), 40 min wall;
    `qwen2.5-7b__v1__t05__gold` 7 `repaired` + 3 `failed` (`075`, `048`: four hostnames of a
    Region merged into one `endpoint` cell, caught by ADR-0003 and not repaired; `038` cut
    off), 37 min wall. Every qwen first answer failed on `schema_version: "1.0"` (F15), so
    qwen `% ok` is 0 and `% ok + repaired` is 90 / 70. Accuracy on gold (endpoints P / R):
    Claude 99.6 / 97.3, qwen t0 96.8 / 75.8, qwen t05 93.0 / 46.3; `quota_table_format`
    10/10 vs 7/10 vs 6/10 — `066` and `038` taken for `standard` with invented Quota Rows
    (ADR-0001). `region_name` on matched rows: Claude 100 %, qwen 65 % (t0) — the Region
    code written into `region_name` on some rows, and "Canada West (Calgary)" shortened to
    "Canada (Calgary)". All of it in `results/metrics.csv` (16 rows) and `prompts/CHANGELOG.md`
    v2; the error analysis itself is step 9. F2 closed (`num_ctx` held on every document).

### Step 7 — Metrics

- **Goal:** all numbers for REPORT from one script (contract items 17–19).
- **Files:** `src/extract/metrics.py`, `results/metrics.csv`, tests for key-based row matching.
- **Done when:** key precision/recall + per-field accuracy on gold; `% ok`, `% ok + repaired`;
  latency p50/p95; cost per 1,000 documents — by group and in total. **Checkpoint 24.10:** link in
  `#ai-engineering-2-flood`.
- **Open:** —
- **Done:**
  - 23.10, code: `src/extract/metrics.py` (`make metrics`: every `results/runs/jsonl/*.jsonl`
    → `results/metrics.csv`, one row per run × group + total, and a one-line-per-run summary
    table in the terminal), `tests/test_metrics.py` (28 tests, hand-made records and gold
    files, plus one on the committed run and gold). Decisions: rows are matched as key
    *sets* (`endpoint` / `name`), so a hostname a model prints twice is one row (contract
    item 6); per-field accuracy only on matched rows, `description` case-insensitive; a gold
    document without an output (`failed` or no answer) is scored as an empty extraction
    (every gold row missing, format wrong), so a model is not rewarded for failing on the
    hard documents; group and total accuracy are micro-averages over rows. Validity's
    denominator is the run's scope from the manifest — 30, or the `gold=1` rows for a `__gold`
    run — and a document without a record is `failed` + `no_answer` (F11; tested). Percentile
    with linear interpolation (numpy's default). Cost per 1,000 from the recorded documents
    only (tokens lost before a `NoAnswer` are in the run log, F10); local model $0 and the
    summed per-document wall clock as `wallclock_s` (item 19). 180 tests.
  - 23.10, `claude__v1__t0` (30 documents): 100 % ok, p50 35.6 s / p95 86.2 s, $40.2 per
    1,000; on the Golden Set endpoints precision 99.6 % / recall 97.3 %, quotas 98.0 % /
    100 %, every scored field ≥ 99 %, `quota_table_format` 10/10. The recall gap is the
    20-row "Legacy endpoints" table of `048` that the draft missed (step 5), the precision gap
    the 3 rows the reviewer removed from gold — the numbers agree with the step 5 log.

### Step 8 — Prompt v2, README

- **Goal:** the second prompt version, justified by the v1 errors.
- **Files:** `prompts/extract_v2.txt`, an entry in `prompts/CHANGELOG.md` (what changed and why), v2 runs,
  `README.md` (problem, how to install and run, how to reproduce the data, known limits).
- **Done when:** every change in v2 is tied to a specific v1 error; the README passes "clean
  clone → `make install` → `make run`"; finding F3 (known limits in the README) closed.
- **Open:**
  - the v2 runs — `claude__v2__t0` (30, ≈ $1.3, budget $3.20 left) after the qwen t05 gold run
    has finished (no concurrent runs: latency); `qwen2.5-7b__v2__t0` (30, ≈ 2–3 h) and the
    moved `qwen2.5-7b__v1__t0` (30) in the background on 24.10.
  - **No real values as examples in v2** (Petro, 24.10). A weak model copies concrete example
    values from the prompt into its answers: in another HW 1 project qwen2.5:3b wrote the
    prompt's example address into texts that had none. v2 rules describe a format in words or
    with placeholders (`<quota name>`, `<default value>`) and never quote a real quota, endpoint
    or service name. A copied row shows up as a precision drop on gold; check qwen v2 output
    for prompt strings. Applied 24.10: the AgentCore hostname example in rule 2 replaced by a
    placeholder description; the v1 examples kept by v2 (`"Each supported Region: 10,000"`,
    `"us-east-1: 20,000; us-east-2: 6,000"`, `"ap-" / "southeast-4"`) are format patterns,
    not values of any Working Set document — left as is so that v1 → v2 changes only what the
    error table names.
- **Done:**
  - 23.10, code: `prompts/extract_v2.txt` + the v2 entry in `prompts/CHANGELOG.md`, a table of
    four v1 errors → four changes (F15 `schema_version`; `066` Resource / Quota layout taken
    for `standard`; `007` templated hostnames dropped and `076` a row from outside the table;
    rows lost on long tables, `048` whole "Legacy endpoints" table by Claude). Only the system
    section changed; user and repair sections are v1's. Schema: `schema_version` is the enum
    `SchemaVersion` ("1"), which `transform_schema` keeps as `"enum": ["1"]` (tested) — records
    and gold files unchanged. Deliberately unchanged: the full-object repair message (a
    patch-style repair would change the pipeline for both providers, contract item 16).
    README: a "run the extraction" section (`make install` … `make metrics`) and "Known
    limits" (F3 closed). 184 tests.
  - 24.10, `claude__v2__t0` (`patch-8.1-v2-runs`; 30 documents, 29 `ok` + 1 `repaired`,
    $1.28, p50 44 s / p95 89 s, $42.7 per 1,000): endpoints recall on gold 97.3 → **100 %**
    (`048` took the "Legacy endpoints" table: 84 → 104 rows); precision 99.6, quotas 98.0 /
    100, format 10/10, `default` 99.0 (one gold row). Outside gold, rule 2 closed F14's
    "fewer" cases: `078` 78 → 234, `017` 94 → 248, `044` 78 → 166 rows. The one `repaired`:
    `010` CloudFront, a prose line taken as a row (`region_code` empty, "AWS
    account.cloudfront-kvs.global.api.aws"), caught by ADR-0003 and fixed by the repair — the
    side effect of a wider rule 2, material for the error analysis. Cost +$2.5 per 1,000 and
    +8 s p50 from the extra rows. Two concurrent `make run` processes wrote `092` and `023`
    twice (two paid calls each, ≈ $0.05): the duplicates were removed by hand before the
    commit (first record kept) → finding F16.
  - 24.10, the three qwen runs overnight (`patch-8.2-qwen-runs`; 30 documents each, one
    after another under `caffeinate`): `qwen2.5-7b__v1__t0` 21 `ok` + 4 `repaired` + 5
    `failed`, 110 min; `qwen2.5-7b__v2__t0` 26 `ok` + 4 `failed`, **no repair call**, 99 min;
    `qwen2.5-7b__v2__t05` 21 `ok` + 1 `repaired` + 8 `failed`, 113 min. v1 → v2 at t0:
    validity 70 → 86.7 %, endpoints recall on gold 78.6 → 91.0, quotas recall 76 → 93,
    `quota_table_format` 7 → 8 of 10; `048` SQS `failed` → `ok` (80 rows, 23 quotas), `038`
    173 → 184 rows. Not fixed by v2: `066` and `038` still `standard` with invented Quota
    Rows (quota precision 69.9), `region_name` 63 → 70 % (Region code written as the name).
    The four v2 failures are the largest documents: `017`, `049`, `025` cut off at
    `num_predict`, `074` a hostname outside the AWS domains (ADR-0003). t05 again only
    hurts qwen: −17 pp validity, 8 `failed`. **F17:** the overnight `qwen2.5-7b__v1__t0` ran on
    `main` after PR #16, i.e. with the `SchemaVersion` enum — it is "prompt v1 text + the
    fixed schema", not the v1 the Golden Set runs saw. The 30-document v1 → v2 comparison
    therefore isolates the rule text; the F15 effect (0 % ok, every document repaired) is
    read from the `__gold` v1 runs. The report says so next to the table. 32 metric rows.

### Step 9 — REPORT.md

- **Goal:** a "model × prompt × sampling" table, 3–5 analysed errors, the production choice
  + under which conditions the decision would change.
- **Done when:** all numbers come from `results/metrics.csv`; the Q&A feedback of 26.10 is taken into account. The report is a **dated
  snapshot**: it states at the top the commit and run ids the numbers were taken from; later code changes do not
  retroactively edit the report.
- **Structure** (adapted from another HW 1 report):
  1. **Header line** — commit and run ids; `make metrics` rebuilds every number.
  2. **Summary** — 4–5 sentences: the headline numbers and the recommendation.
  3. **What was compared** — task, data (30 documents, 10 gold), models, prompts, sampling; one
     line per metric definition (contract items 17–19): key precision/recall, per-field accuracy
     on matched rows, a failed gold document scored as an empty extraction, validity denominator.
  4. **Results** — the table from `results/metrics.csv`, one row per run (% ok / % ok + repaired,
     precision/recall, field accuracy, p50/p95, $ per 1,000), then 3–4 "what the table says" bullets.
  5. **Error analysis** — 3–5 errors, each: what → how often (n of N) → one document, expected vs
     got → why → what v2 changed → effect in numbers. Candidates: Neighbour Tail, non-standard
     layout (empty list expected), multi-region default cells, placeholders, `048` legacy endpoints.
  6. **Choice for production and when to change it** — with the scale arithmetic: the cost of
     100,000 documents, and the days one laptop needs at the measured p50.
  7. **Limitations** — at least: gold drafted from `claude__v1__t0` (an advantage to Claude);
     `claude__v1__t05` on gold only (budget decision 21.10); one run per configuration and 10 gold
     documents, so 1–2 rows can be noise; qwen context limits (S3).
  8. **Reproduce** — the metrics command and a link to the README run section.
- **Not taken:** a held-out test set — no time before 27.10; named under Limitations instead.
- **Done:** —

## 5. Run matrix and budget

| Run id | Step | Required | Cost estimate | Actual |
|---|---|---|---|---|
| `claude__v1__t0` | 4 | yes (also the gold draft) | ≈$1.9 (input measured: 262,867 tokens ≈ $0.26; output from the S3 trial) | **$1.21** — in 264,757 / out 188,292; 30/30 `ok`, 30 calls |
| `claude__v1__t05__gold` | 6 | yes — **the 10 Golden Set documents only** (budget decision 21.10; run id suffix decided 22.10) | ≈$0.27 | **$0.27** — in 60,968 / out 42,366; 10/10 `ok`, 10 calls, 306 s (23.10) |
| `qwen2.5-7b__v1__t0__gold` | 6 | yes (checkpoint scope, 23.10) | $0, ≈40–60 min (F15: every document repaired) | **$0**, 40 min — 9 `repaired`, 1 `failed` (23.10) |
| `qwen2.5-7b__v1__t0` | 8 | yes (moved from 6, 23.10) | $0, ≈2–3 h | **$0**, 110 min — 21 `ok`, 4 `repaired`, 5 `failed` (24.10; enum schema, F17) |
| `qwen2.5-7b__v1__t05__gold` | 6 | yes (checkpoint scope, 23.10) | $0, ≈40–60 min | **$0**, 37 min — 7 `repaired`, 3 `failed` (24.10) |
| `claude__v2__t0` | 8 | yes | ≈$1.8 (≈$1.3 after the v1 actual) | **$1.28** — in 285,494 / out 199,197; 29 `ok` + 1 `repaired`, 31 calls (24.10); ≈ $0.05 more paid for the duplicate calls (F16) |
| `qwen2.5-7b__v2__t0` | 8 | yes | $0 | **$0**, 99 min — 26 `ok`, 4 `failed`, no repair call (24.10) |
| `qwen2.5-7b__v2__t05` | 8 | desirable | $0 | **$0**, 113 min — 21 `ok`, 1 `repaired`, 8 `failed` (24.10) |
| `claude__v2__t05` | 8 | no (budget decision 21.10) | ≈$1.8 | — |

**API budget:** $5 for the whole of HW 1. Spent before the full `claude__v1__t0` run: **$0.42** — three
S3 calls: at 16384, cut off ($0.22, `results/trials/…max-tokens-16384`); at 32000 before the enum
descriptions reached the model ($0.10, `results/trials/…before-enum-descriptions`); at 32000 with the
fixed schema ($0.10, the record in `claude__v1__t0`).

**Spent after `claude__v1__t0`: $1.53** — the run $1.21 (its S3 record included) + the two S3 trials kept in
`results/trials/` ($0.22 + $0.10). With the actual run cost, the plan below is ≈ $1.53 + $0.3
(`claude__v1__t05`, gold) + ≈ $1.3 (`claude__v2__t0`) ≈ **$3.1**.

**Spent after `claude__v1__t05__gold` (23.10): $1.80** — $1.53 + $0.27. Remaining for `claude__v2__t0`:
$3.20 against an estimate of ≈ $1.3.

**Spent after `claude__v2__t0` (24.10): ≈ $3.13** — $1.80 + $1.28 + ≈ $0.05 (F16). ≈ $1.87 reserve; no
further Claude run is planned (`claude__v2__t05` stays dropped).

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
| F2 | Ollama's default `num_ctx` may truncate long input. 17.10: value 32768 in `config/sampling.yaml` (`providers.ollama`), justified by S3/EMR token measurements; still to be passed in `ollama.py`. 21.10: the S3 answer is ≈16.6k Claude tokens, so S3 needs ≈13.1k + ≈17k ≈ 30k of 32768 — check S3 first in step 6 | plan | step 6 (explicit `num_ctx`) | ✅ step 6 (`patch-6.1-v1-runs`): `num_ctx` 32768 held on every Golden Set document; the cap that bites is `num_predict` (`048`, `038`) |
| F3 | The README must name the known limits: Standard Quota Table only (ADR-0001), the AWS domain list (ADR-0003), Neighbour Tail | step 1 | step 8 | ✅ step 8 (`step-8-prompt-v2`): README "Known limits" |
| F4 | The local branch `backup/step-0-1-grill-me-1-local-snapshot` is needed only as the basis for the tests | step 1 | after step 2 is merged — delete | ✅ deleted 17.10 after PR #5 (was `e2f27cf`) |
| F5 | `Field(description=...)` texts in `schema.py` are model instructions outside `prompts/`, not covered by `prompt_version` | step 2 review | step 4 (state in `prompts/CHANGELOG.md` that schema descriptions are part of a prompt version) | ✅ step 4 (`step-4-pipeline-v1`); 21.10: the enum descriptions were not sent at all, fixed in the same step |
| F6 | `endpoint_rows` in `data/raw/manifest.csv` undercounts: it matched hostnames on one line, but wrapped hostnames are split (S3: 254 in the manifest, 290 rows extracted, all 36 extra are rejoined wraps). S3 also has several endpoint sub-tables (`s3`, `s3tables`, `s3-accesspoint`, `s3-control`); contract item 6 says "the endpoints table" | step 4 | step 5 (gold check counts rows in the PDF, not from the manifest; state "all endpoint tables of the chapter" in item 6) | ✅ step 5 (`step-5-golden-set`): contract item 6 names every endpoints table; gold rows are counted against the printed text and the PDF. The manifest column is left as is and is not used by metrics |
| F7 | A transport failure (a non-retryable 4xx such as "credit balance is too low", or a 429/529 still failing after 3 attempts) is written as a permanent `failed` Run Record, and resume skips it: after a top-up the documents stay `failed` and count against validity. The backoff (1 s, 2 s) also ignores `retry-after` | step 4 review | step 4, before the full run | ✅ step 4 (`step-4-pipeline-v1`) |
| F8 | `done_files` parses every line, so one half-written last line (killed process, full disk) makes every later resume crash with `JSONDecodeError` | step 4 review | step 4 | ✅ step 4 (`step-4-pipeline-v1`) |
| F9 | `SCHEMA_FILE` and the example path in `tests/test_schema.py` are relative to the current directory: `cd tests && pytest` fails; `pipeline.py` already uses `ROOT / ...` | step 4 review | step 4 | ✅ step 4 (`step-4-pipeline-v1`) |
| F10 | Tokens paid before a `NoAnswer` (the first call when the repair call has no answer) appear only in the run log, not in the `main.py` cost summary or any record-based cost metric, so spending against the $5 budget is under-reported | review of the F7 fix | step 4 | ✅ step 4 (`step-4-pipeline-v1`) |
| F11 | Every non-retryable error becomes `NoAnswer`, also a permanent one (400 "prompt is too long", a rejected schema): such a document never gets a record, `main.py` exits non-zero on every run, and step 7 waits for 30 records forever. Contract item 15 considers only temporary causes | review of the F7 fix | step 4 (contract items 15, 18: counted as failed in metrics; no error classification) | ✅ step 4 (`step-4-pipeline-v1`); metrics side ✅ step 7 (`step-7-metrics`: no record → `failed` + `no_answer`, tested) |
| F12 | Results-file edge cases: a line that is JSON but not an object raises a bare `TypeError` without its line number; `{"file": null}` counts as done; a complete record whose final `\n` was stripped by hand is dropped as a cut-off line (recoverable from Git) | review of the F8 fix | Petro's call | ⬜ |
| F13 | No test pins `main.py`'s non-zero exit (contract item 15) or `NoAnswer.__cause__` | review of the F7 fix | Petro's call | ⬜ |
| F14 | `claude__v1__t0` is 30/30 valid, but endpoint row counts differ from the manifest in both directions. Fewer: `078` IAM Identity Center 78 of 234, `017` DynamoDB 94 of 203, `044` RDS 78 of 165, `092` Secrets Manager 44 of 62, `048` SQS 84 of 104 (gold). More: `007` AgentCore 39 vs 22 (templated `gatewayId`, gold), `055` App Mesh 120 vs 77, `042` Redshift 253 vs 201, `038` OpenSearch 183 vs 170 (Neighbour Tail of Network Security Manager? gold), `085` Lake Formation 88 vs 75 (gold). Also `042` Redshift has `quota_table_format: none` (ADR-0001 expects `non_standard`?) and `010` CloudFront has 97 Quota Rows. Expected or manifest-side: `005` Aurora 36 of 72 (decided: one row per hostname), `074` Global Accelerator 2 of 105 (the text has 5 hostnames — manifest, F6). The manifest undercounts wrapped hostnames (F6), so these are signals, not verdicts | step 4 (full run) | step 5 (gold `048`, `007`, `038`, `085`: count against the PDF); steps 8–9 (non-gold: error analysis and v2 changes) | ◐ gold part ✅ step 5 (`step-5-golden-set`): `085`, `007`, `038` match the printed hostnames (the manifest undercounts, F6; no Neighbour Tail); `048` missed the 20-row "Legacy endpoints" table, added to gold. Non-gold ✅ step 8 (`patch-8.1-v2-runs`): v2 rule 2 took the missing tables — `078` 234, `017` 248, `044` 166 rows (the manifest undercounts, F6); `092` 44 unchanged, `055`, `042`, `010` unchanged — the "more" cases are rejoined wraps (F6), not errors; `042` `none` and `010`'s 97 Quota Rows stay as v1 printed them → step 9 if the error analysis needs them |
| F15 | `anthropic.transform_schema` turns `schema_version: Literal["1"]` into a plain string with `{const: 1}` in its description, so the schema constrains neither model. Claude writes `"1"`; qwen wrote `"1.0"` (direct call on `006`, 23.10), which fails validation, so every qwen v1 answer needs a repair call — longer runs, and on the largest documents the repair (document + previous answer) may not fit `num_ctx`. Not fixed in v1: Claude v1 already ran with this schema, and both models must see the same one | step 6 (direct call) | step 8 (prompt v2: an enum `["1"]` the schema keeps, a CHANGELOG entry tied to this error) | ✅ step 8: enum `SchemaVersion` (PR #16); `qwen2.5-7b__v2__t0` has no repair call at all, `qwen2.5-7b__v1__t0` with the enum 21/30 `ok` vs 0/10 before (`patch-8.2-qwen-runs`) |
| F16 | Nothing stops two `make run` processes from appending to the same run file: both skip the documents already done and then extract the same next ones (`claude__v2__t0`: `092`, `023` twice, two paid calls each). Cheap fix: a lock file next to the JSONL, or `main.py` refusing when one exists | step 8 (v2 run) | Petro's call | ⬜ |
| F17 | The schema is part of a prompt version (`prompts/CHANGELOG.md`), but `schema.py` is not versioned per prompt: once PR #16 merged, every later run — v1 included — used the `SchemaVersion` enum. `qwen2.5-7b__v1__t0` (30) is therefore "v1 text + fixed schema" and differs from the `__gold` v1 runs on exactly F15. Not a bug to fix now (one schema for all runs is the contract, item 1); the report states which runs saw which schema | step 8 (overnight runs) | step 9 (stated in REPORT; a `schema_version`-per-prompt mechanism is out of scope) | ◐ |

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
| 21.10 | Golden Set re-selected to 6 `short` / 3 `medium` / 1 `edge` to cut the manual check (step 5); the limits it sets on the metrics — `edge` on one document, no global service in gold — are in `data-notes.md` |
| 22.10 | Correction: the Golden Set does contain `non_standard` documents (`066`, `038`), so `quota_table_format` accuracy covers all three values; `data-notes.md` fixed |
| 22.10 | The Golden-Set-only Claude run is `claude__v1__t05__gold`: the scope is in the run id (contract items 11, 18), so a full run never resumes into its file and metrics use the gold rows as its denominator |
| 21.10 | Budget variant A: `claude__v1__t05` on the 10 Golden Set documents only, `claude__v2__t05` dropped (section 5); step 6 needs a `--gold` option in `main.py` |
| 23.10 | Checkpoint scope: all three step 6 runs today on the Golden Set only (`qwen2.5-7b__v1__t0__gold`, `qwen2.5-7b__v1__t05__gold`, `claude__v1__t05__gold`), because F15 makes a full qwen run ≈ 2–3 h; the full `qwen2.5-7b__v1__t0` moves to step 8 (error analysis), its validity and latency on 30 documents follow then |
| 24.10 | From another HW 1 report: the REPORT structure in step 9 and the "no real values as examples" rule for prompt v2 in step 8 |
| 24.10 | `qwen2.5-7b__v2__t05` (desirable) run overnight together with the two required qwen runs; F17 recorded: runs after PR #16 use the enum schema whatever the prompt version |
