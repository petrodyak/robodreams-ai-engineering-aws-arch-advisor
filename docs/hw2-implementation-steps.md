# Implementation steps — HW 2 (RAG with sources and evals in CI)

Working plan and execution log for stage 2 up to the deadline **20.11 23:59** (moved from 13.11 on 13.11). What we build is in the
spec [`superpowers/specs/2026-11-08-hw2-rag-design.md`](superpowers/specs/2026-11-08-hw2-rag-design.md)
and the ADRs ([0007](adr/0007-structure-aware-chunking.md), [0008](adr/0008-cached-live-evals-in-ci.md));
the task-level plan is [`superpowers/plans/2026-11-09-hw2-rag.md`](superpowers/plans/2026-11-09-hw2-rag.md);
the assignment is [`hw2-brief.md`](hw2-brief.md); how we work with Git is in [`GIT_RULES.md`](GIT_RULES.md).
HW 1 is tracked, frozen, in [`Implementation_steps.md`](Implementation_steps.md); step numbers and
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
- **Money before the run.** Before every paid Claude run, an estimate via `count_tokens`, stated and
  agreed; actual spend goes into section 5 after the run. The limit is **$5** for the whole of HW 2 (D3).
- **Keys only in `.env`**, only `.env.example` in Git; CI reads the `ANTHROPIC_API_KEY` repository secret.
- **Nothing in `data/` is deleted** — only moved.
- **One branch = one step = one PR**; before a PR, `make check` is green; commit/push only on
  Petro's command.
- **Status rows (D9).** A step's own PR sets its row to `🔄 PR #N` (a `docs:` commit after
  `gh pr create`, as `GIT_RULES.md` §5 allows). The next step's PR flips it to `✅ PR #N (merge sha)`.
  Step 20's row is closed by the pre-submission check against the brief. A row lags git by at most one
  step; no PR exists only for a status row.
- **A finding is not fixed inside someone else's step.** It is recorded under "Deferred findings" (from
  F21) with the step where it will be closed, and closed separately.
- **Entries are short:** the "Done" subsection is at most 10 lines.
- **Terms:** "Well-Architected" for the AWS Well-Architected Framework — never "WA", never "AWS WAF"
  (that is the Web Application Firewall).

## 2. Prerequisites

| What | Who | Needed before step | Status |
|---|---|---|---|
| `.env` with `ANTHROPIC_API_KEY` (same key as HW 1) | Petro | 18 | ✅ (HW 1) |
| "ok" on the corpus list | Petro | 15 | ✅ 13.11 (34 documents) |
| Relevant-chunk labels for the 20 answerable questions (~1 h) | Petro | 17 | ⬜ |
| Testset check + ≥ 12 hand-labelled answers (~2 h) | Petro | 19 | ⬜ |
| `ANTHROPIC_API_KEY` repository secret in GitHub | Petro | 20 | ⬜ |

## 3. Steps overview

| # | Step | Branch | Who / Petro's time | Points (HW criterion) | By | Status |
|---|---|---|---|---|---|---|
| 14 | Housekeeping: brief, this file, CLAUDE.md, GLOSSARY, ADR-0007/0008, spec + plan in Git | `step-14-hw2-setup` | review 15 min | — | 09.11 | ✅ PR #32 (c3b5034) |
| 15 | Corpus list, download script, manifest | `step-15-corpus` | pick and "ok" the list, 30 min | 1: ingestion ≥ 2 formats (part of 3) | 14.11 | ✅ PR #33 (99c73ee) |
| 16 | Ingestion → `chunks.jsonl` + `chunks_fixed.jsonl` + ingest manifest | `step-16-ingest` | review | 1: ingestion (3), cleaning + dedup (3), chunking + metadata (4) | 15.11 | 🔄 PR #34 |
| 17 | Index, hybrid, rerank, filters, retrieval eval | `step-17-search` | **label relevant chunks, ~1 h** | 2: embeddings + DB (3), hybrid (3), rerank + filters (2), retrieval measured (2) | 16.11 | ⬜ |
| 18 | RAG answering, prompt v1, eval cache, first run | `step-18-answer` | "ok" on the estimate | 3: citations (4), context control (4) | 17.11 | ⬜ |
| 19 | Testset, scorers, judge, calibration, prompt v2 | `step-19-evals` | **check the testset ~1 h, label ≥ 12 answers ~1 h** | 4: testset (3), scoring (4) | 18.11 | ⬜ |
| 20 | CI workflow + thresholds, `REPORT-hw2.md`, README, pre-submission check | `step-20-ci-report` | review, add the secret | 4: evals in CI (3); repository (2) | 19.11 | ⬜ |

## 4. Steps

For every step: **goal · files · done when · open** (the plan) and **done** (the log, after the
merge). The task-level detail (interfaces, tests) is in the plan file.

### Step 14 — Housekeeping

- **Goal:** everything a later step reads exists in the repository: the brief, this file, the terms,
  the two ADRs, the approved spec and plan.
- **Files:** `docs/hw2-brief.md`, this file, `CLAUDE.md`, `GLOSSARY.md`, ADR-0007, ADR-0008,
  `.gitignore`, `.env.example`, `docs/superpowers/`.
- **Done when:** `make check` green; `CLAUDE.md` points every HW 2 question to the right file.
- **Done:** `docs/hw2-brief.md` (the brief translated almost verbatim; HW 2 command `make rag`,
  report `REPORT-hw2.md`); this file; `CLAUDE.md` → stage 2 (budget $5, models of D4, three new
  "Read before…" rows, structure block); `GLOSSARY.md` section "RAG (stage 2)", 17 terms; ADR-0007,
  ADR-0008; `.gitignore` (`data/rag/raw/`, `.cache/`, `.superpowers/`); `Implementation_steps.md`
  marked frozen; the approved spec and plan added. `make check`: 264 passed (no code change).

### Step 15 — Corpus

- **Goal:** ≥ 30 public documents in 2 formats, reproducible without committing them.
- **Files:** `data/rag/manifest.csv`, `scripts/download_rag_corpus.py`, `tests/test_rag_manifest.py`.
- **Done when:** the manifest tests pass; `make rag-data` downloads and hash-checks every document.
- **Open:** is an older Well-Architected edition still downloadable (the outdated-version trap)?
- **Done:** `data/rag/manifest.csv`, 34 documents: 12 PDF (Framework, 6 pillars, 4 lenses, and the
  archived July 2020 Framework edition for the outdated-version trap, still on `d1.awsstatic.com`)
  and 22 HTML (15 Prescriptive Guidance pages, 7 Athena / S3 Tables / Glue pages on Iceberg and the
  Data Catalog, `doc_type` `guide`: the Prescriptive Guidance Iceberg guide now returns 404).
  `published` = the PDF's printed "Publication date", or the guide's latest "Document history" entry
  for HTML (`Last-Modified` is the site build date). `scripts/download_rag_corpus.py` (stdlib
  `urllib`, sha256 check, `--record`) and `make rag-data`: 34/34 match on a second download, 56.6 MB.
  `make check`: 267 passed (+3 in `test_rag_manifest.py`).

### Step 16 — Ingestion

- **Goal:** `data/rag/chunks.jsonl` (structure) and `chunks_fixed.jsonl` (baseline) with the §4
  metadata; an ingest manifest with duplicates and chunk statistics.
- **Files:** `src/rag/models.py`, `src/rag/ingest/*`, tests `test_rag_{clean,dedup,extract,chunk,pipeline}.py`.
- **Done when:** every structure chunk ≤ 480 tokens; deterministic re-run; two "cut in half" fixed
  examples chosen for the report.
- **Done:** `src/rag/{models,ingest/*}.py`, `make ingest` → `chunks.jsonl` (2,869 structure chunks,
  6.4 MB; max 480, avg 270 tokens, 41 % under 250: merging stops at a best-practice boundary or 450),
  `chunks_fixed.jsonl` (3,102 baseline windows, kept apart so stage 3 never reads them) and
  `ingest_manifest.json`. PDF titles are searched in the text (deep outline entries point to wrong
  pages); cover and contents dropped, the archived edition keeps "This paper has been archived".
  1,057 duplicate chunks stay in the most specific document (the Framework repeats the pillars).
  Byte-identical after a re-download. Cut-in-half: `wa-reliability#f0034`, `#f0146`. F21 closed: the
  manifest hash is the text hash (= `doc_hash`). `make check`: 301 passed (+34).

### Step 17 — Index, search, retrieval eval

- **Goal:** `search(...)` in 4 modes with filters; recall@5 / recall@10 / MRR for the 5 configurations.
- **Files:** `src/rag/{config,index,search}.py`, `config/rag.yaml`, `evals/{testset,retrieval,run}.py`,
  `evals/testset.jsonl`, `scripts/retrieval_candidates.py`.
- **Done when:** the retrieval table is in `evals/results/retrieval.json` and here; the RAG mode is chosen
  from the numbers.
- **Open:** fastembed `TextCrossEncoder` API and both model names, checked against the docs.

### Step 18 — Answering with sources

- **Goal:** per-claim cited answers, the not-found answer, cached answers, the real cost per 1,000
  questions.
- **Files:** `src/rag/{llm,answer}.py`, `prompts/rag_v1.txt`, `evals/cache.py`, `evals/cache/`.
- **Done when:** the first live run and the k = 3 / 5 / 8 sweep are recorded in section 5.

### Step 19 — Testset, scorers, judge, calibration, prompt v2

- **Goal:** ≥ 24 items checked by Petro; deterministic scorers; two judges with agreement and κ on
  ≥ 12 hand labels; prompt v2 from the error analysis.
- **Files:** `evals/{scorers,judge,calibration}.py`, judge prompts, `evals/labels/`, `prompts/rag_v2.txt`.
- **Done when:** every testset item has `verified_by`; judge agreement ≥ 80 % (or v2 judge prompt);
  CHANGELOG v2 row with measured effect.

### Step 20 — CI, REPORT, README

- **Goal:** evals in GitHub Actions with failing thresholds; `REPORT-hw2.md`; README stage 2.
- **Files:** `.github/workflows/evals.yml`, `config/eval_thresholds.yaml`, `evals/thresholds.py`,
  `REPORT-hw2.md`, `README.md`.
- **Done when:** CI green on the PR with 0 cache misses, a deliberate threshold break goes red; every
  line of the brief's "What must be in the repository" has an evidence path.

## 5. Run matrix and budget

| Run id | Step | Required | Cost estimate | Actual |
|---|---|---|---|---|
| `claude-haiku-5-5__v1__medium__k5` | 18 | yes | ≈ $0.03 (24 questions) | — |
| k sweep 3 / 5 / 8 | 18 | yes | ≈ $0.1 | — |
| judges on the v1 run | 19 | yes | ≈ $0.5–1 | — |
| `claude-haiku-5-5__v2__medium__k5` + judges | 19 | yes | ≈ $0.5–1 | — |
| CI cache misses | 20 | as needed | ≤ 30 misses per run (guard) | — |

**API budget:** $5 for the whole of HW 2 (D3); the spec estimates under $3 in total. Spent so far: $0.

## 6. Deferred findings

Numbering continues from HW 1 (F1–F20 are in `Implementation_steps.md`).

| # | Finding | Found in | Closed in | Status |
|---|---|---|---|---|
| F21 | AWS regenerates its documentation PDFs every few days (`CreationDate` of the downloads is the download day), so a later `make rag-data` may report a sha256 mismatch although the content did not change. The committed `chunks.jsonl` records the version used | 15 | 16: the manifest `sha256` is now the hash of the cleaned text (the `doc_hash` of `chunks.jsonl`); 18 of 34 files had new bytes and the same text a day later | closed (step 16) |

## 7. Risks

From spec §11:

| Risk | What we do |
|---|---|
| No older Well-Architected edition is downloadable | the outdated-version trap uses the "Document revisions" table |
| PDF outline missing or shallow | fall back to heading patterns (numbered titles, `XXXnn-BPnn` IDs) |
| CI too slow (model download + embedding) | `actions/cache` for the models and the embedding cache |
| Haiku 5.5 thinks too long or refuses a benign AWS question | `effort` is a config value; a refusal is logged and scored as a failed answer |
| Judge disagrees with Petro | judge prompt v2 before reporting; REPORT states the agreement as measured |
| Time | each step is one PR; if time runs out, the REPORT is cut to the brief's minimum, never the CI or the calibration |

## 8. Plan change log

| Date | What changed |
|---|---|
| 09.11 | First version: steps 14–20 from the approved spec and plan; D1–D9 decided (D4: answers on Haiku 5.5); `REPORT-hw2.md` instead of `REPORT.md`, which holds HW 1 |
| 13.11 | Deadline moved to 20.11 23:59 (Petro). Nothing is cut from scope; steps 15–20 re-dated 14.11–19.11, 20.11 is the buffer |
| 13.11 | Corpus list approved (34 documents); Iceberg pages taken from the Athena, S3 and Glue guides because the Prescriptive Guidance Iceberg guide was withdrawn |
| 14.11 | F21 decided as option A (Petro): the manifest records the text hash, not the byte hash; duplicate chunks are kept in the most specific document; the fixed baseline moves to `chunks_fixed.jsonl` (Petro), so `chunks.jsonl` holds only what stage 3 reads |
