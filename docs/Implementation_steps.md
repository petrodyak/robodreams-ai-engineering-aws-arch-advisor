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
  and agreed; actual spend goes into section 5 after the run. The limit is $10 for the whole of HW 1
  ($5 until 25.10; raised for the held-out runs, see section 5).
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
| 7 | Metrics → `results/metrics.csv` | `step-7-metrics` | review ~20 min | step 2: correct measurements (3) | **24.10 checkpoint** | ✅ PR #14 (`1744709`); gold v1 runs PR #15 (`7c9342d`) |
| 8 | Prompt v2 + CHANGELOG, v2 runs, README | `step-8-prompt-v2` | choosing changes ~30 min | step 3: ≥2 versions + changelog (3); repo quality (2) | 26.10 | ✅ PR #16 (`df1a8cd`); Claude v2 run PR #17 (`ea70c6e`); qwen runs PR #18 (`8dd84e7`) |
| 9 | `REPORT.md` (after the Q&A on 26.10) | `step-9-report` | ~1 h together | step 4 (6) | **27.10** | ✅ PR #19 (`0869fda`); README results PR #20 (`c4b6139`); second edition after the lecturer's remarks PR #27 (`f27ef5c`); remarks table PR #28 (`2cc86f0`) |
| 10 | Run provenance: `prompt_sha` / `schema_sha` in every record (Q&A feedback, remark 2) | `step-10-run-provenance` | review ~15 min | step 3: logging (2); repo quality | 25.10 | ✅ PR #21 (`095b560`); guard PR #22 (`721ab6b`) |
| 11 | Source-grounded validation G1–G3, `validation_version`, gold `038` re-check (remark 1) | `step-11-grounded-validation` | review ~30 min + gold `038` ~30 min | step 3: validation (3); repo quality | 25.10 | ✅ PR #23 (`f51ebce`); gold `038` PR #24 (`7675345`); `__val2` re-runs PR #27 (`f27ef5c`) |
| 12 | Held-out Set: 10 unseen documents, gold for 5, runs with the `__holdout` scope (remark 4) | `step-12-holdout` | review ~15 min + gold ×5 ~1.5 h | step 3 (3); repo quality | 26.10 | ✅ PR #25 (`57a1a11`); gold PR #26 (`900b1d9`); runs PR #27 (`f27ef5c`) |
| 13 | Long documents in parts: endpoints part + quotas part, same prompt, merged by code; `__parts` runs (remark 3) | `step-13-parts` | review ~30 min; "ok" on ≈ $1.6 | step 3 (3); repo quality | 27.10 | ✅ PR #29 (`702643a`, code + F20 fix); runs + REPORT third edition PR #30 (`06f21de`) |

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
- **Done:**
  - 24.10, first draft (`step-9-report`, before the Q&A of 26.10): `REPORT.md` in the eight
    sections above, snapshot at `55892ec` (the eight run files). Five analysed errors: (1) a
    second endpoints table skipped — Claude v1, fixed by v2 rule 2; (2) a non-standard quota
    table reported as `standard` with invented rows — qwen, both prompts, v2 rule 3 did not
    land; (3) the Region code written as `region_name` — qwen, 205 of 686 matched rows, a
    model limit; (4) the output cap — 14 of qwen's 17 failures, six documents, two causes
    (size, repetition loop); (5) a prose line taken as a row — Claude v2, the side effect of
    (1)'s fix, caught by ADR-0003. Production choice: Claude v2 t0; the scale arithmetic
    (100k documents ≈ $4,300 vs ≈ 157 laptop-days) and four conditions under which it flips.
    Limitations name the gold bias, the 10-document / one-run noise floor, the gold-only
    Claude t05, F17 and the in-sample nature of v2. Q&A feedback goes into a `patch-9.1`.

### Step 10 — Run provenance (lecturer's remark 2 of 24.10)

- **Remark:** "tie every run to the exact prompt and schema version" — finding F17 showed a
  run id (`v1`) naming a prompt while the schema under it had changed.
- **Goal:** every Run Record pins the bytes the model saw; two configurations can never sit
  under one run id unnoticed.
- **Files:** `src/extract/schema.py` (`RunRecord.prompt_sha`, `schema_sha`),
  `src/extract/llm/base.py` (`short_sha`, `llm_schema_sha`), `src/extract/pipeline.py`
  (`Prompt.sha`), `src/extract/metrics.py` (two columns, the mixed-provenance guard),
  `src/extract/report_md.py` (header), `scripts/backfill_provenance.py`, the eight run files
  and their mirrors, `results/metrics.csv`; contract item 12, `prompts/CHANGELOG.md` table.
- **Done when:** the fields are required and validated; a run file with two provenance pairs
  fails metrics; the eight existing runs carry the shas recovered from git; F17 closed.
- **Not done on purpose:** a schema file per prompt version. The remark asks for a binding,
  not an isolation; one `schema.py` for every run is contract item 1, and the sha makes the
  drift visible instead of impossible — enough for a one-person project.
- **Done:**
  - 24.10, code: `prompt_sha` = sha256 of the prompt file bytes, `schema_sha` = sha256 of
    `llm_schema_json()` (the text of `docs/service-document.schema.json`), both 12 hex chars,
    required, pattern-validated. `metrics.py` refuses a run file whose records carry more
    than one pair (a resume after a prompt or schema edit). `scripts/backfill_provenance.py`
    hashes the files as they were at the commit each run was made (`git show`), run once:
    8 files, 180 records. Result, now in the data: two schemas (`e707…` Literal on the
    21.10–23.10 runs, `d401…` enum after PR #16) and two prompts (`8a0d…` v1, `a3ad…` v2);
    `qwen2.5-7b__v1__t0` = `8a0d…` + `d401…`, F17 visible in the CSV and tested. 199 tests.
  - 24.10, `patch-10.1-provenance-guard` — the remark as a property test. `run()` now
    refuses to resume a run file whose records were made with another prompt or schema
    (`ProvenanceMismatch`, raised before any call; `main.py` exits with "refusing to resume
    … start a new run id"), so the F17 situation is stopped at the source, not only at
    metrics. `tests/test_provenance.py` replays it end to end: a run, the schema changes
    under it, the same command resumes → refused, nothing appended; the same for a one-
    character prompt edit under the same version name; an unchanged configuration still
    resumes; a file that already mixes two pairs is refused by metrics (second line of
    defence). 204 tests.

### Step 11 — Source-grounded validation (lecturer's remark 1 of 24.10)

- **Remark:** "validation should check the data against the source, not what the model
  copied from the prompt." Our checks compared the `service` echo, the `schema_version`
  echo and the *shape* of hostnames and Region codes; none asked whether a row is printed.
- **Goal:** every answer judged against the chapter by code, the same way for both models;
  nothing invented passes as `ok`.
- **Files:** `src/extract/grounding.py` (the chapter readers, moved from
  `scripts/check_gold.py` and extended to Standard Quota Table rows; the checks G1–G3),
  `src/extract/pipeline.py` (grounding after the schema, before the repair; run id
  `__val2`), `src/extract/schema.py` (`validation_version`), `src/extract/metrics.py`
  (column, provenance triple, run id ↔ records check), `scripts/check_gold.py` (quota names
  and format now checked too), `tests/test_grounding.py`, ADR-0005, contract items 7, 9,
  11, 12, 16, the eight run files (`validation_version: "1"` backfilled).
- **Done when:** every Golden Set file passes grounding (except `038` until re-checked);
  every row grounding flags in `claude__v2__t0` is a real error confirmed against the raw
  text; the v2 runs re-done under validation "2" and the report updated.
- **Open:** nothing — F19 (the typographic apostrophe, below) is deferred.
- **Done:**
  - 24.10, code: `Grounding.of(text, service)` reads the chapter once per document —
    hostnames of the Endpoint column of every endpoints table (wraps rejoined), Name cells
    of every Standard Quota Table (rows wrapped over lines, rows cut by a page break with the
    header repeated), and whether a Standard Quota Table header is printed — and
    `errors(doc)` returns G1–G3 violations in the schema's `- path: message` form, so the
    repair call carries them unchanged. **Calibration on the real data** (the method, not
    just the result): every gold file passes with zero errors except `038`'s
    `quota_table_format` (F18); on `claude__v2__t0` grounding flags exactly five documents,
    one row each, every one confirmed against the raw text — `091` a Standard Quota Table
    called `non_standard`, `044` `rds.ap-southeast-5.api.aws` completed by pattern (the
    chapter prints only the `.amazonaws.com` twin), `038` (F18), `025` a quota name
    paraphrased from neighbouring rows' pattern ("The maximum number of SetVisibleToAllUsers
    API requests…" for the printed "Replenishment rate of SetVisibleToAllUsers calls"),
    `010` the prose row (now caught by G1 as well as by the format check). On
    `qwen2.5-7b__v2__t0` it flags 11 documents, 125 endpoint rows and 37 quota rows: FIPS
    and dual-stack twins the tables do not print (`092` 38 rows, `042` 65), `us-gov` rows
    (`095`), a Resource / Quota table reported as `standard` (`047`, `066`), a trailing
    period dropped from a name (`075`), `038`'s rows that *are* printed (right, see F18).
    Three reader faults found and fixed during calibration: a 7-word name tripped the
    prose-ends-the-table rule (now a table ends at a column-0 line); the mid-word fallback
    compared against whole lines, where other columns interleave (now per Name cell); a
    row cut by a page break was split in two (now rejoined by its lower-case tail).
    `validation_version` in every record, `__val2` in the run id, the provenance triple on
    resume and in metrics. 217 tests.
  - 25.10, `patch-11.1-gold-038`: the one-document run `claude__v2__t0__val2 --only 038`
    ($0.08): first answer `non_standard` → G3 error → the repair call returned `standard`
    with exactly the five rows of the domain table, 183 endpoints, 0 grounding errors —
    the pipeline doing what ADR-0005 says. While drafting, the G3 header regex was found
    to accept `Name / Default / Adjustable / Notes` and three-column headers (`038` has
    ten of those); it now requires `Description`, F18 recounted (one standard table, not
    eleven). Gold `038` re-drafted from that answer and checked against the PDF by Petro;
    every gold file passes grounding with zero errors; `make gold-check` clean. The run
    file stays as the start of `claude__v2__t0__val2` (the full re-run resumes into it).
    217 tests.
  - 25–26.10, `patch-12.2-val2-and-holdout-runs`: the two re-runs under validation "2".
    `claude__v2__t0__val2` — 25 `ok`, 4 `repaired`, 1 `failed`, 35 calls, $1.52, 27 min:
    the four repairs are exactly the four true flags of the calibration (`038`, `091` G3;
    `044` G1; `025` G2), each fixed by the repair call carrying the grounding error; gold
    accuracy quotas P/R 98.1 / 100, format 10/10. The `failed` one is `010`: the repair fixed
    the prose row (error 5) but wrote `doesn't` in a quota name where the PDF prints `doesn’t`
    — G2 compares characters, so a correct answer was rejected (**F19**, deferred).
    `qwen2.5-7b__v2__t0__val2` — 15 `ok`, 2 `repaired`, 13 `failed`, 143 min: 15 first
    answers rejected (7 G1, 3 G2, 1 G3, 3 cut off, 1 malformed hostname), the repair fixed
    the two Resource / Quota tables (`066`, `047` → no rows); precision on the finished
    documents 99.5 / 96.4, recall 54.5 / 50.5 because a `failed` document counts as empty.
    REPORT second edition: §3.3 validation 1 vs 2 on the same documents, §3.4 held-out,
    error 2 and error 5 rewritten for `038` and `010`, §5 and §6 updated. 224 tests.

### Step 12 — Held-out Set (lecturer's remark 4 of 24.10)

- **Remark:** "check prompt improvements on data you had not seen when writing them" — v2 was
  written from the v1 errors on the same 30 documents it is measured on (REPORT, Limitations).
- **Goal:** the v1 → v2 difference measured on documents the prompt author never saw.
- **Files:** `data/holdout/` (manifest, 10 texts; PDFs ignored), `data/holdout/gold/` (5),
  `scripts/select_docs.py` / `extract_text.py` (`--set`), `src/extract/pipeline.py`
  (`DocumentSet`, `__holdout` in the run id), `main.py` (`--set`), `src/extract/metrics.py`
  (set-aware), `scripts/make_gold_drafts.py` / `check_gold.py` (`--set`), `Makefile`
  (`SET=`), `tests/test_holdout.py`, contract item 20, `data-notes.md`.
- **Done when:** the set is disjoint from the Working Set and documented; the five gold files
  are checked; v1 and v2 run on it for both models within the budget; REPORT has an
  out-of-sample table.
- **Open:** nothing.
- **Done:**
  - 25.10, selection and code: 10 documents by a fixed rule (seed 20261025) — the pool had no
    `short` document left, so 6 `medium` + 4 `edge`; copied and extracted on the laptop,
    word counts equal to the pool profile for all ten. `DocumentSet` names a folder, its
    manifest, its gold folder and its run id scope; `WORKING_SET` and `HOLDOUT_SET`;
    everything that read `data/raw` or `data/gold` takes the set (`main.py --set`,
    metrics by the run id, the two gold scripts, `make … SET=holdout`). 223 tests.
  - 25.10, `patch-12.1-holdout-gold`: `claude__v2__t0__holdout__gold__val2` — 5/5 `ok` on the
    first answer, $0.17 — drafted into `data/holdout/gold/`; every row grounded; `make
    gold-check SET=holdout` clean (two mid-word wraps it flagged were the script's
    exact-match comparison, now the same squash comparison as G2); checked by Petro against
    the PDF with no corrections. `data/holdout/gold/README.md`; a test that the five files
    load, match the manifest and are grounded. 224 tests.
  - 25–26.10, `patch-12.2-val2-and-holdout-runs`: the four held-out runs, chained on the
    laptop overnight (`claude__v1` then the two qwen runs, after the Working Set qwen
    re-run). Budget decision 25.10 (variant B): both Claude prompt versions on the held-out
    gold, ≈ $0.4; Petro raised the HW 1 limit to $10 for this. Results on the five gold
    documents (390 endpoint rows, 105 quota rows): `claude__v1` 5/5 `ok`, endpoints P/R
    100 / 91.8 — `068` Elastic Beanstalk 76 of 108 rows, the second endpoints table missed,
    the same mechanism as `048` in the Working Set — quotas 100 / 100, $0.16;
    `claude__v2` 5/5 `ok`, 100 / 100 on both, $0.17: the v2 gain is out of sample. qwen on
    all ten: v1 3 `ok` / 2 `repaired` / 5 `failed`, endpoints 100 / 42.1, quotas 100 / 16.2,
    format 2/5, 46 min; v2 5 `ok` / 5 `failed`, 100 / 55.4, 100 / 42.9, format 3/5, 42 min;
    four documents fail under both prompts (`016`, `051`, `059`, `073`). REPORT §3.4.

### Step 13 — Long documents in parts (lecturer's remark 3 of 24.10)

- **Remark:** "process long documents in parts". Asked how (Q&A 26.10): the prompt stays
  the same; code splits the document first (the endpoints table and the quotas table apart,
  or by pages) and calls once per part with only that part's text, so nothing is read
  twice; code merges the results, drops duplicates, validates; approaches are tried and
  each one measured. Our cut-offs: `017`, `049`, `025` for qwen (18,432 output tokens, error
  4), S3 for Claude until `max_tokens` was raised.
- **Goal:** the same documents, the same prompt and schema, two calls per chapter instead
  of one; measured against the whole-document `__val2` runs on validity (did the cut-offs
  go away), recall (nothing lost at the seam), cost and latency.
- **Decision (option A of three, Petro 26.10):** two parts by section kind — the quotas
  part (the "Service quotas…" blocks) and the endpoints part (everything else of the
  chapter) — not by pages: the cut is semantic, no row is cut in half, no overlap, nothing to
  de-duplicate. Pages are the second step if a part is still too long (ADR-0006). The
  splitter cuts at headings (column 0, no sentence punctuation, ≤ 12 words; "quota" →
  quotas block, "endpoint" → endpoints block, any other heading continues the block):
  needed because the chapters are not uniform — `091` prints two pairs of sections with
  " for …" tails, `046` names its endpoints sections "Service API endpoints", "SMTP
  endpoints", `074` "Service endpoint (global)", `007` and `085` have no quotas section,
  and `038` has sub-headings inside its quotas section.
- **Files:** `src/extract/parts.py` (new: `heading_kind`, `split_chapter`, `merge`,
  `spill`, `part_rows`), `src/extract/pipeline.py` (`ask()` — the ask → validate → one
  repair loop, now shared by a whole document and a part; `extract_document(parts=True)`;
  `make_run_id(parts=)`, `run(parts=)`), `src/extract/grounding.py`
  (`Grounding.errors(doc, checks)`, `is_page_furniture`), `src/extract/schema.py`
  (`PartRecord`, `RunRecord.parts`, `worst_status`), `src/extract/metrics.py` (`__parts`
  in the run id, run id ↔ records check), `src/extract/report_md.py` (parts in the mirror),
  `main.py --parts`, `Makefile PARTS=1`, `tests/test_parts.py` (38), contract items 11, 12,
  21, ADR-0006, GLOSSARY "Part", README.
- **Done when:** `tests/test_parts.py` proves on all 40 chapters that the endpoints part
  prints every hostname and no Standard Quota Table and the quotas part the reverse; the
  pipeline tests pin two calls, per-part repair, merge, status rules, spill; `make check`
  green; `claude__v2__t0__parts__val2` and `qwen2.5-7b__v2__t0__parts__val2` run on the
  Working Set; REPORT §3.5 compares them with the `__val2` whole-document rows.
- **Open:** nothing for HW 1. Next experiments, each with its own run id, in the order the
  data suggests: a de-duplication of identical endpoint rows in `merge` (`005`); a note
  inside a part that it prints no table of the other kind, or a per-part schema (F20); a
  loop detector for the local model. Pages are not next: the new cut-offs are on small parts.
- **Done:**
  - 26.10, code: `split_chapter` checked on all 40 chapters before any pipeline code — the
    first version cut at the exact headings "Service endpoints" / "Service quotas" and
    missed `046` (custom headings, 0 of 148 hostnames in the endpoints part) and `074`
    ("Service endpoint (global)", 6 of 8); the heading-kind rule above gives 40/40. Each
    part is sent as "<title>\n\n<blocks>", so prompt rule 1 finds its chapter title.
    Per-part grounding: G1 only for endpoints, G2 + G3 for quotas — the endpoints part
    rightly says `none` for the format it cannot see, and that is not an error. The merged
    document is re-validated G1–G3 against the whole chapter by code (a violation there
    would be a bug in the splitter, so it raises). `ask()` carries the tokens already
    spent on the first part into a `NoAnswer` of the second (F10 accounting). 262 tests.
  - 26.10, `claude__v2__t0__parts__val2` (30, $1.43, 22 min): 25 `ok`, 5 `repaired`, 0
    `failed` — against the whole-document `__val2` run's 25 / 4 / 1 on the same documents.
    Rows identical on 28 of 30; `044` needs no repair any more (the pattern-completed
    hostname does not appear on the endpoints part), `010` goes from `failed` to
    `repaired` (the repaired quotas part wrote the typographic apostrophe this time — F19
    stands), `023` the other way (the quotas part first said `non_standard`). Input +4 %
    (the second copy of the instructions), output −9 % (fewer repairs), $1.52 → $1.43,
    latency sum 1,632 → 1,348 s. Spill 0 on all 30: Claude never writes the other kind.
    `005` Aurora: 72 endpoint rows, every hostname twice — the chapter prints two
    identical tables (MySQL- and PostgreSQL-Compatible Edition) and the parts answer is
    literal where the whole-document answer had merged them; the metrics match by
    hostname set, so recall is the same; a de-duplication in `merge` is the open item.
  - 26.10, **F20 found and fixed** on the first `qwen2.5-7b__v2__t0__parts__val2` (18 of 30
    before Petro stopped it; kept as `results/trials/qwen2.5-7b__v2__t0__parts__val2--before-F20.jsonl`):
    on a quotas part qwen invents an endpoints table (`047` 80 rows, `018` 20, `091` 16)
    and on `037`, `005`, `044` keeps inventing until the output cap; the invented rows
    carry schemes, `<Region>` placeholders and quota values as hostnames, and the schema's
    format checks rejected the part on them — fields the merge never reads, against item
    21 as written. Fix: `validate_answer(part=)` drops the other kind's fields from the raw
    answer before the schema (`parts.strip_other_kind`), counting them as `spill`. The
    Claude run is unaffected (spill 0, no part rejected on other-kind fields — checked);
    the qwen run is re-done from scratch under the fixed code, same run id (prompt, schema
    and validation unchanged, so the provenance guard cannot tell — this line is the
    record). 264 tests.
  - 27.10, `patch-13.1-parts-runs-and-report`: `qwen2.5-7b__v2__t0__parts__val2` (30, 174
    min) — 13 `ok`, 5 `repaired`, 12 `failed`; the whole-document run had 15 / 2 / 13. A
    wash on validity, worse underneath: cut-offs 3 → 7 (`017`, `049`, `025` stay — `025`'s
    endpoints part is 78 rows and still 18,432 tokens, a runaway; `037`, `005`, `038` on
    quotas parts, `044` on the endpoints part — new), output tokens +32 %, spill on every
    accepted quotas part (1–80 rows). `qwen2.5-7b__v2__t0__parts__holdout__val2` (10, 49
    min): 3 / 0 / 7 against 5 / 0 / 5 — `079` runs to the cap on its quotas part, `028`
    invents a `ca-west-1` pair. Gains: `007`, `095` `ok` (G1 failures as whole documents),
    `074` `repaired`; `region_name` accuracy on matched rows 79 → 95 %. REPORT third
    edition: §3.5 with both tables, remarks row 3 closed, error 4 and §§5–6 updated —
    production choice is now Claude in parts; qwen's numbers of record stay the
    whole-document ones. README results table. Budget ≈ $6.5 of $10.

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
| `claude__v2__t0__val2` | 11 | yes (remark 1: v2 under grounded validation) | ≈$1.3 + repairs | **$1.52** — 35 calls; 25 `ok`, 4 `repaired`, 1 `failed` (F19), 27 min (25.10) |
| `qwen2.5-7b__v2__t0__val2` | 11 | yes | $0, ≈100 min | **$0**, 143 min — 15 `ok`, 2 `repaired`, 13 `failed` (25.10) |
| `claude__v2__t0__holdout__gold__val2` | 12 | yes (also the held-out gold draft) | ≈$0.2 | **$0.17** — 5/5 `ok`, 5 calls (25.10) |
| `claude__v1__t0__holdout__gold__val2` | 12 | yes (variant B, budget raised to $10) | ≈$0.2 | **$0.16** — 5/5 `ok`, 5 calls (25.10) |
| `qwen2.5-7b__v1__t0__holdout__val2` | 12 | yes | $0, ≈45 min | **$0**, 46 min — 3 `ok`, 2 `repaired`, 5 `failed` (26.10) |
| `qwen2.5-7b__v2__t0__holdout__val2` | 12 | yes | $0, ≈45 min | **$0**, 42 min — 5 `ok`, 5 `failed` (26.10) |
| `claude__v2__t0__parts__val2` | 13 | yes (remark 3) | ≈$1.6 — the same input plus one more copy of the prompt per document, repairs | **$1.43** — in 376,314 / out 211,348; 25 `ok`, 5 `repaired`, 0 `failed`, 65 calls, 22 min (26.10) |
| `qwen2.5-7b__v2__t0__parts__val2` | 13 | yes | $0, ≈2.5 h | **$0**, 174 min — 13 `ok`, 5 `repaired`, 12 `failed`, 7 cut-offs (26–27.10, after the F20 fix; the first 18 records before it in `results/trials/`) |
| `qwen2.5-7b__v2__t0__parts__holdout__val2` | 13 | desirable ($0) | $0, ≈1 h | **$0**, 49 min — 3 `ok`, 7 `failed` (27.10) |

**API budget:** $5 for the whole of HW 1 until 25.10, **$10** since (raised by Petro for the
held-out runs after the lecturer's feedback; the $5 plan below is the history). Spent before the full `claude__v1__t0` run: **$0.42** — three
S3 calls: at 16384, cut off ($0.22, `results/trials/…max-tokens-16384`); at 32000 before the enum
descriptions reached the model ($0.10, `results/trials/…before-enum-descriptions`); at 32000 with the
fixed schema ($0.10, the record in `claude__v1__t0`).

**Spent after `claude__v1__t0`: $1.53** — the run $1.21 (its S3 record included) + the two S3 trials kept in
`results/trials/` ($0.22 + $0.10). With the actual run cost, the plan below is ≈ $1.53 + $0.3
(`claude__v1__t05`, gold) + ≈ $1.3 (`claude__v2__t0`) ≈ **$3.1**.

**Spent after `claude__v1__t05__gold` (23.10): $1.80** — $1.53 + $0.27. Remaining for `claude__v2__t0`:
$3.20 against an estimate of ≈ $1.3.

**Spent after `claude__v2__t0` (24.10): ≈ $3.13** — $1.80 + $1.28 + ≈ $0.05 (F16). ≈ $1.87 reserve; no
further Claude run was planned (`claude__v2__t05` stays dropped).

**Spent after `claude__v2__t0__val2` (25.10): ≈ $4.73** — $3.13 + $0.08 (the `038` document) + $1.52
(the re-run under validation "2": 35 calls, more output than `claude__v2__t0`). The held-out runs
(step 12, ≈ $0.4) take it to ≈ $5.13: limit raised to $10 on 25.10 (variant B).

**Spent after the held-out runs (26.10): ≈ $5.06** — $4.73 + $0.17 (`claude__v2` held-out) + $0.16
(`claude__v1` held-out). ≈ $4.9 of the $10 limit left.

**Spent after the step 13 Claude run (26.10): ≈ $6.49** — $5.06 + $1.43. ≈ $3.5 of the $10
limit left; no further Claude run is planned for HW 1.

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
| F16 | Nothing stops two `make run` processes from appending to the same run file: both skip the documents already done and then extract the same next ones (`claude__v2__t0`: `092`, `023` twice, two paid calls each). Cheap fix: a lock file next to the JSONL, or `main.py` refusing when one exists | step 8 (v2 run) | Petro's call | ⬜ accepted, not fixed (24.10): one user, one terminal; a lock file is the fix if stage 2–4 runs hit it again |
| F17 | The schema is part of a prompt version (`prompts/CHANGELOG.md`), but `schema.py` is not versioned per prompt: once PR #16 merged, every later run — v1 included — used the `SchemaVersion` enum. `qwen2.5-7b__v1__t0` (30) is therefore "v1 text + fixed schema" and differs from the `__gold` v1 runs on exactly F15. Not a bug to fix now (one schema for all runs is the contract, item 1); the report states which runs saw which schema | step 8 (overnight runs) | step 9 (stated in REPORT; a `schema_version`-per-prompt mechanism is out of scope) | ✅ step 10 (`step-10-run-provenance`): `prompt_sha` / `schema_sha` in every record, backfilled from git; metrics refuse mixed provenance |
| F18 | **Gold `038` was wrong on `quota_table_format`.** The chapter prints one Standard Quota Table (domain and instance quotas, `Name / Default / Adjustable / Description`, 5 rows) and ten other quota tables with `Notes` instead of `Description` or three columns — `non_standard` by definition. The Claude v1 draft saw the ten and called the document `non_standard`; the hand check confirmed the draft. Found by G3 on the gold file. First read as "eleven standard tables" (PR #23): the G3 header regex did not require the `Description` column; it does now, and the recount gives one. qwen's 28 rows on `038` (REPORT error 2): 5 printed in the standard table, 23 from the non-standard ones — the error stands, the gold format did not | step 11 (calibration) | ✅ `patch-11.1-gold-038`: gold re-drafted from `claude__v2__t0__val2` (its repair call returned exactly the five printed rows, 0 grounding errors), checked by Petro against the PDF; header regex requires `Description`; contract item 7 says so |
| F19 | **G2 compares characters, so a typographic apostrophe in a printed quota name (`doesn’t`, `010`) rejects a model answer that writes it straight (`doesn't`).** The one `failed` Claude record under validation "2" is this false flag: the repaired answer was correct on content. Fix: normalise `’ ‘ “ ”` to their ASCII forms on both sides before G2 (and in `check_gold.py`); a reader change inside validation "2", not a new validation version, since it can only turn a rejection into a pass. Needs the `010` document re-run afterwards | step 11 re-run (`patch-12.2`) | — | ⬜ deferred: after the deadline, together with D-lite (chunking); REPORT §3.3 and §6 state it |
| F20 | **On a part that prints no endpoints table, the local model invents one.** `qwen2.5-7b__v2__t0__parts__val2`, quotas parts: up to 80 invented endpoint rows (`047`), with schemes, `<Region>` placeholders and quota values as hostnames; on `037` (a 42-word part), `005` and `044` it kept generating until the output cap — a new kind of cut-off that whole documents never had. Claude: spill 0 on all 30. Two consequences: (1) the part was rejected by the schema's format checks on rows the merge never reads — fixed, the other kind's fields are dropped before the schema (`strip_other_kind`, contract item 21); (2) the tokens and time spent on the invented rows are real and stay in the measurements. Next experiment: a note inside the part that it prints no endpoints table — kept apart, it changes what the model is told | step 13, first qwen run | ✅ (1) `step-13-parts`, 26.10; (2) measured on the full re-run, 27.10: cut-offs 3 → 7, spill on every accepted quotas part — REPORT §3.5, error 4 |

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
| 24.10 | Patch 9.2: README "Stage 1 results" with the five main runs and the conclusion, pointing to `REPORT.md`; F16 accepted as is |
| 24.10 | Lecturer's feedback after the checkpoint, four remarks: (1) validation grounded in the source text, (2) run tied to the exact prompt and schema, (3) long documents in parts, (4) prompt changes checked on unseen data. Steps 10–13 planned in that order of cost: 10 provenance, 11 grounded validation, 12 held-out set, 13 chunking (13-lite before the deadline, full after) |
| 24.10 | Step 11: run id gets `__val<N>` for a validation other than the first (contract item 11); `validation_version` in every record (item 12); contract item 7 — every Standard Quota Table of the chapter counts; F18 gold `038` |
| 25.10 | Step 12: the Held-out Set (contract item 20) — 10 pool documents outside the Working Set, gold for 5, `__holdout` run id scope; no `short` document was left in the pool |
| 25.10 | API budget raised from $5 to $10 (Petro) for the held-out runs — variant B: Claude v1 and v2 on the five held-out gold documents |
| 26.10 | Steps 11 and 12 closed by the six overnight runs (`patch-12.2`); REPORT second edition; F19 (typographic apostrophe in G2) deferred with D-lite chunking to after the deadline |
| 26.10 | REPORT gets a four-row table "the lecturer's remarks of 24.10 — how each was closed" (remark → decision → steps / PRs → evidence), replacing the paragraph of the second edition (`patch-12.3`) |
| 26.10 | Step 13 added — long documents in parts, after the lecturer's answer at the Q&A: two parts by section kind (option A), same prompt, merged by code, `__parts` run id (contract item 21, ADR-0006); pages only if a part is still cut off |
| 26.10 | F20: a part is judged on its own fields by the schema too — the other kind's fields are dropped before validation (item 21 as written); the first qwen parts run (18 documents) is kept in `results/trials/` and re-done |
| 27.10 | Pre-submission check against the brief (`patch-13.2`): status rows of steps 9 and 13 closed; README and REPORT §7 state the cost to reproduce the required matrix (≈ $2.8) against the HW 1 total (≈ $6.5); README says plainly that the data has no typos or mixed languages; REPORT §7 names F1–F20 and the parts command |
| 27.10 | Step 13 measured: parts are the production configuration for Claude (0 failed, −6 % cost, −17 % latency) and a loss for qwen (F20); the qwen held-out parts run added at $0. Next experiments listed in step 13, none before the deadline |
