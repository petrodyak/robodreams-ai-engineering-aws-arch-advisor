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
| Relevant-chunk labels for the 20 answerable questions (~1 h) | Petro | 17 | ✅ 16.11 (55 chunk ids) |
| Testset check + ≥ 12 hand-labelled answers (~2 h) | Petro | 19 | ✅ 17.11 (24 items, 17 answers) |
| `ANTHROPIC_API_KEY` repository secret in GitHub | Petro | 20 | ✅ 17.11 |

## 3. Steps overview

| # | Step | Branch | Who / Petro's time | Points (HW criterion) | By | Status |
|---|---|---|---|---|---|---|
| 14 | Housekeeping: brief, this file, CLAUDE.md, GLOSSARY, ADR-0007/0008, spec + plan in Git | `step-14-hw2-setup` | review 15 min | — | 09.11 | ✅ PR #32 (c3b5034) |
| 15 | Corpus list, download script, manifest | `step-15-corpus` | pick and "ok" the list, 30 min | 1: ingestion ≥ 2 formats (part of 3) | 14.11 | ✅ PR #33 (99c73ee) |
| 16 | Ingestion → `chunks.jsonl` + `chunks_fixed.jsonl` + ingest manifest | `step-16-ingest` | review | 1: ingestion (3), cleaning + dedup (3), chunking + metadata (4) | 15.11 | ✅ PR #34 (0e33962) |
| 17 | Index, hybrid, rerank, filters, retrieval eval | `step-17-search` | **label relevant chunks, ~1 h** | 2: embeddings + DB (3), hybrid (3), rerank + filters (2), retrieval measured (2) | 16.11 | ✅ PR #36 (9e06453) |
| 18 | RAG answering, prompt v1, eval cache, first run | `step-18-answer` | "ok" on the estimate | 3: citations (4), context control (4) | 17.11 | ✅ PR #37 (6636c8d) |
| 19 | Testset, scorers, judge, calibration, prompt v2 | `step-19-evals` | **check the testset ~1 h, label ≥ 12 answers ~1 h** | 4: testset (3), scoring (4) | 18.11 | ✅ PR #38 (9ddc66f) |
| 20 | CI workflow + thresholds, `REPORT-hw2.md`, README, pre-submission check | `step-20-ci-report` | review, add the secret | 4: evals in CI (3); repository (2) | 19.11 | ✅ PR #40 (359ccf1) |

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
- **Done:** `src/rag/{config,index,search}.py`: Qdrant `:memory:` (cosine) + BM25 over the same
  "Contextual Header + text", RRF (k = 60) over the top 20 of each, cross-encoder rerank of the RRF
  top 20, filters by `doc_type` and `published`. Embeddings `BAAI/bge-small-en-v1.5`, reranker
  `Xenova/ms-marco-MiniLM-L-6-v2`, both local through fastembed 0.9.1 (`TextCrossEncoder.rerank`
  checked against the installed package); vectors cached on disk. `evals/testset.jsonl` holds the 20
  answerable items (ids `one`/`many`/`sim`/`old`, legend in `REPORT-hw2.md`); the relevant chunks were
  proposed by Claude from `make retrieval-candidates` plus a full-text search, and each one was checked
  by Petro in `evals/labels/retrieval_candidates.md` (55 ids, none from the archived edition). Fixed
  windows count as relevant by ≥ 50 % shingle overlap with a relevant chunk. `make retrieval-eval`,
  20 items, $0:

  | Configuration | recall@5 | recall@10 | MRR | ms/query | Misses (top 10) |
  |---|---|---|---|---|---|
  | vector, fixed chunks | 0.85 | 0.95 | 0.66 | 129 | sim01 |
  | vector | 0.85 | 0.95 | 0.76 | 130 | sim01 |
  | BM25 | 0.90 | 0.90 | 0.82 | 6 | one09, old02 |
  | hybrid (RRF) | 0.95 | 1.00 | 0.80 | 137 | — |
  | **hybrid + rerank** | **1.00** | **1.00** | **0.87** | 466 | — |

  `hybrid_rerank` stays the default: the only configuration with every item in the top 5, and the
  best MRR. Structure chunks beat the fixed windows on MRR (0.76 vs 0.66). The reranker puts a wrong
  chunk first on 5 items; on old02 it is `wa-serverless-lens#0039`, a current document that still
  lists the five security areas of an older Framework edition, so a date filter cannot catch it.
  `make check`: 327 passed (+26).

### Step 18 — Answering with sources

- **Goal:** per-claim cited answers, the not-found answer, cached answers, the real cost per 1,000
  questions.
- **Files:** `src/rag/{llm,answer}.py`, `prompts/rag_v1.txt`, `evals/cache.py`, `evals/cache/`.
- **Done when:** the first live run and the k = 3 / 5 / 8 sweep are recorded in section 5.
- **Done:** `src/rag/llm.py` (`ClaudeJSON`: structured outputs, effort `medium`, no sampling
  parameters, no `thinking`, HW 1 retry imported), `src/rag/answer.py` (context of the top k in rank
  order, a block that does not fit is skipped, never cut; labels checked, unknown ones dropped, a
  claim with no valid label removed; no sources → not-found with no call), `prompts/rag_v1.txt`,
  `evals/cache.py` (key = model + effort + sha256 of system, user and schema; append-only JSONL;
  `live=False` raises the stale message; guard at 30 new calls), `evals/answers.py`,
  `make ask` / `eval-estimate` / `eval` / `eval-sweep`. The 20 answerable items (the `none` items
  come in step 19), $0.041 for the sweep, estimate $0.053:

  | k | context budget | found | context recall | citation recall | avg in / out tokens | $ per 1,000 questions |
  |---|---|---|---|---|---|---|
  | 3 | 3,000 | 20 / 20 | 1.00 | 1.00 | 2,513 / 561 | 0.53 |
  | **5** | 3,000 | 20 / 20 | 1.00 | 1.00 | 3,568 / 591 | **0.65** |
  | 8 | 3,840 | 20 / 20 | 1.00 | 1.00 | 5,293 / 668 | 0.86 |

  No label was dropped and no claim removed. k = 5 stays: k = 3 already has every relevant chunk in
  the context on this testset, so the sweep cannot show a quality gain yet; the judge (step 19)
  decides between 3 and 5. The outdated traps held: old02 had the Serverless Lens's five-area list
  first in the context and answered "seven" from the newer Framework; old01 and old03 had the 2020
  edition in the context and answered "six" and "five". A rerun of `make eval` made 0 new calls.
  Two questions outside the corpus by `make ask`: the Aurora ACU price gave the not-found text; the
  GKE autoscaler question gave `found = true` with EKS advice (F22). `make check`: 350 passed (+23).

### Step 19 — Testset, scorers, judge, calibration, prompt v2

- **Goal:** ≥ 24 items checked by Petro; deterministic scorers; two judges with agreement and κ on
  ≥ 12 hand labels; prompt v2 from the error analysis.
- **Files:** `evals/{scorers,judge,calibration}.py`, judge prompts, `evals/labels/`, `prompts/rag_v2.txt`.
- **Done when:** every testset item has `verified_by`; judge agreement ≥ 80 % (or v2 judge prompt);
  CHANGELOG v2 row with measured effect.
- **Done:** 24 items checked by Petro (4 `none` added, the six traps in his words, many01 and many04
  get the chunk of a missing fact); `evals/{scorers,judge,calibration,score}.py`, two Sonnet judges,
  `scripts/calibration_sheet.py` (`--append`), `make score` / `calibrate`, `RAG_PROMPT=v2` to measure
  a version before the config switches. The reworded traps cut recall@5 of vector to 0.70, hybrid to
  0.85; hybrid_rerank stays 1.00. Calibration, 17 hand labels (5 from k = 3 for ≥ 3 failures):
  correctness 82 % / κ 0.65 raw, 88 % / 0.77 after Petro re-checked (2 labels changed); faithfulness
  94 % → 100 %. Prompt v2 changes rule 5 only (F22): abstain 0.50 → 1.00, false abstain 0.00, judge
  pass 0.75 → 0.80, faithfulness 0.97 → 0.99, $0.65 per 1,000; the config is v2 (CHANGELOG table).
  The four left are not prompt failures: retrieval (F23), judge (F24), one02 beyond the question.
  Review fixes: key facts match whole words, calibration skips a malformed verdict and fails a
  false abstain, `judge_usd` is new spend only, runs load with a check. `make check`: 381 passed (+31).

### Step 20 — CI, REPORT, README

- **Goal:** evals in GitHub Actions with failing thresholds; `REPORT-hw2.md`; README stage 2.
- **Files:** `.github/workflows/evals.yml`, `config/eval_thresholds.yaml`, `evals/thresholds.py`,
  `REPORT-hw2.md`, `README.md`.
- **Done when:** CI green on the PR with 0 cache misses, a deliberate threshold break goes red; every
  line of the brief's "What must be in the repository" has an evidence path.
- **Done:** `config/eval_thresholds.yaml` (the v2 baseline minus 0.05, rounded down to 0.05: recall@5
  ≥ 0.95, abstain ≥ 0.95, false abstain ≤ 0.05, source hit ≥ 0.95, faithfulness ≥ 0.90, judge pass
  ≥ 0.75), `evals/thresholds.py` (`check`: an equal value passes, a missing metric fails),
  `python -m evals.run ci` / `make eval-ci` (recall@5 of hybrid_rerank on the answer index, cached
  answers and verdicts, score, thresholds → `evals/results/ci/`, gitignored; exit 1 on a broken threshold, a stale cache or more
  than 30 new calls, answers and verdicts counted together), `make rag` (D6),
  `.github/workflows/evals.yml` (checkout v7, setup-uv pinned to the v10.3.3 commit because it
  publishes no major tag, `actions/cache` v6 restore + save for `.cache/`, upload-artifact v7). The first CI run timed out at
  30 min: a cold runner embedded both chunk sets (~6,000 texts, ~24 / s even on the Mac) and built
  the index twice; the gate now embeds only the structure chunks once, and the timeout is 45 min. Locally `make
  eval-ci`: 0 new calls, all six pass, with and without the key. CI on the branch: [44139898238](https://github.com/petrodyak/robodreams-ai-engineering-aws-arch-advisor/actions/runs/44139898238)
  green (0 new calls, the runner's ranking matched the Mac's for all 24 questions), and the throwaway
  branch `step-20-red-threshold-demo` (`judge_pass_rate_min` 0.85) went red as intended:
  [44144978410](https://github.com/petrodyak/robodreams-ai-engineering-aws-arch-advisor/actions/runs/44144978410), `judge_pass_rate 0.80 < 0.85`.
  `REPORT-hw2.md`, README "Stage 2: RAG (HW 2)" with the chunking justification, the pre-submission
  check (section 9). `make check`: 389 passed (+8).

## 5. Run matrix and budget

| Run id | Step | Required | Cost estimate | Actual |
|---|---|---|---|---|
| `claude-haiku-5-5__v1__medium__k5` | 18 | yes | ≈ $0.03 (24 questions) | $0.0130 (20 questions; in the sweep) |
| k sweep 3 / 5 / 8 | 18 | yes | ≈ $0.1 (count_tokens: $0.053) | $0.0409 |
| answers for the 4 `none` items and the reworded traps (k = 3 / 5 / 8) | 19 | yes | < $0.03 | $0.0218 |
| judges on the v1 run (calibration + `make score`) | 19 | yes | ≈ $0.5–1 (count_tokens: $0.48) | $0.3164 |
| `claude-haiku-5-5__v2__medium__k5` + judges | 19 | yes | ≈ $0.45 (count_tokens: $0.021 + $0.432) | $0.2258 |
| two `make ask` checks outside the corpus | 18 | no | ≈ $0.002 | $0.0017 |
| CI cache misses | 20 | as needed | ≤ 30 misses per run (guard) | $0 (0 misses in the 3 CI runs of 17.11) |

**API budget:** $5 for the whole of HW 2 (D3); the spec estimates under $3 in total. Spent so far: $0.607 (step 18: $0.043; step 19: $0.564).

## 6. Deferred findings

Numbering continues from HW 1 (F1–F20 are in `Implementation_steps.md`).

| # | Finding | Found in | Closed in | Status |
|---|---|---|---|---|
| F21 | AWS regenerates its documentation PDFs every few days (`CreationDate` of the downloads is the download day), so a later `make rag-data` may report a sha256 mismatch although the content did not change. The committed `chunks.jsonl` records the version used | 15 | 16: the manifest `sha256` is now the hash of the cleaned text (the `doc_hash` of `chunks.jsonl`); 18 of 34 files had new bytes and the same text a day later | closed (step 16) |
| F22 | Rule 5 of `rag_v1` ("a partial answer is an answer") lets a question outside the corpus pass: "How do I configure the Horizontal Pod Autoscaler in Google Kubernetes Engine?" got `found = true`, EKS advice from REL07-BP03, and a last claim saying the sources do not cover GKE, with citations | 18 | 19: prompt v2 rule 5 names the two cases (a value no source states, a product no source covers); abstain 0.50 → 1.00, false abstain stays 0.00 | closed (step 19) |
| F23 | A question in two parts can lose the chunk of its second part at retrieval: many03 (Redshift tables) has it at k = 8 but not at k = 5, many04 (Glue: Parquet, `push_down_predicate`) not even at k = 8. `retrieved` / `in_context` count one relevant chunk and stay 1.00; the new diagnostic `context_share` is 0.78 | 19 | | open (stage 3: the agent can split a question into its parts; REPORT names it) |
| F24 | The correctness judge sees the reference answer, not the sources, so a true detail the reference does not hold reads as a contradiction: old02 (v1, the 2020 Security area) and old03 ("down from eight", the October 2023 revision). Agreement 88 % is above the 80 % bar, so no judge v2 | 19 | | open (REPORT names it; a judge v2 could pass the cited sources too) |
| F25 | The source moved: on 16.11.2026 AWS published a new Well-Architected Framework edition ("Last updated: November 16, 2026", 1,355 sections against 1,320) and edited one paragraph of the Cost Optimization pillar (export types). A clean clone's `make rag` stopped at `rag-data` on these 2 of 34 text hashes; the previous edition has no stable URL. From the committed chunks, `make retrieval-eval eval score` reproduced every committed number with no key and 0 new calls (4 min 49 s) | 20 (pre-submission check on a clean clone) | patch 20.2: `make rag` runs from the committed chunks, `make rag-rebuild` downloads and ingests first (Petro, option A; D6 amended) | closed (patch 20.2, PR #42); a move to the new edition is a stage-3 decision |

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
| 15.11 | Fixed-window relevance counts overlap with a relevant chunk of any document, not only the same one (Petro, option B; plan Task 17 amended) |
| 16.11 | Relevant chunks proposed by Claude and checked one by one by Petro; the archived Framework edition never counts as relevant. Testset ids renamed to `one` / `many` / `sim` / `old` (`none` in step 19). many04 `expected_sources`: the "Parallelize tasks" section did not exist, now `""` |
| 17.11 | Calibration set extended with 5 answers of the k = 3 run, so ≥ 3 of the hand labels are failures (plan Task 19.3 gate); calibration reads each label from its own run. Sheet question "Unsupported claim?" renamed "Claim not in its source?" (same yes / no meaning). Raw and re-checked calibration both kept for the REPORT |
| 17.11 | Prompt v2 measured with `RAG_PROMPT=v2` before the config switched to it (Makefile variable `PROMPT` belongs to HW 1); config `prompt_version: v2`. F22 closed; F23 and F24 recorded |
| 17.11 | Row 19 flipped by its own patch PR, not by step 20 (Petro): the status commit `dedeaf8` was pushed after PR #38 merged, so it never reached `main` |
| 17.11 | Step 20: thresholds set from the v2 baseline (Petro "ok" on the plan); the cost guard of 30 counts answers and verdicts of a CI run together; Petro added the `ANTHROPIC_API_KEY` repository secret and allowed commit + push of this branch while away (PR and merge stay his) |
| 17.11 | CI triggers: `push` on `main` + `pull_request` instead of `push` on every branch + `pull_request` (Petro, option B). Spec §8 says "push and pull_request"; the brief's "on every push or pull request" still holds. Each PR commit now runs once, on the merge into `main`, and the run on `main` after a merge saves the `.cache/` that every PR can restore (a branch's own cache is not visible to its PR) |
| 17.11 | Row 20 and the secret prerequisite closed by their own patch PR (Petro): step 20 is the last step, so no later step PR would flip them as D9 expects |
| 17.11 | D6 amended (Petro, option A, F25): `make rag` = `retrieval-eval eval score` from the committed chunks; `make rag-rebuild` = `rag-data ingest rag`. A rebuild on AWS's new Framework edition was rejected: new hashes, new labels and new paid runs three days before the deadline |

## 9. Pre-submission check (step 20)

`docs/hw2-brief.md`, line by line. The evidence is a path in this repository.

### Criteria (40 points)

| HW step | Item | Points | Evidence |
|---|---|---|---|
| 1 | Ingestion of ≥ 2 formats | 3 | `data/rag/manifest.csv` (12 PDF + 22 HTML), `src/rag/ingest/extract_pdf.py`, `extract_html.py`; REPORT-hw2 §2 |
| 1 | Cleaning + deduplication | 3 | `src/rag/ingest/clean.py`, `dedup.py`; `ingest_manifest.json` `exact_duplicates_dropped` (1,057 chunks), `near_duplicates`; REPORT-hw2 §2 |
| 1 | Justified chunking + metadata | 4 | README "Why this chunking", ADR-0007, REPORT-hw2 §3 (fixed vs structure, two cut examples); chunk fields in `src/rag/models.py` `ChunkRecord` |
| 2 | Embeddings + vector DB | 3 | `src/rag/index.py` (fastembed `bge-small-en-v1.5`, Qdrant `:memory:`, embedding cache) |
| 2 | Hybrid search | 3 | `src/rag/search.py` modes `bm25`, `hybrid` (RRF k = 60) |
| 2 | Reranking + metadata filters | 2 | `src/rag/search.py` `hybrid_rerank` (cross-encoder), `Filters` (`doc_types`, `exclude_doc_types`, `published_from`) |
| 2 | Retrieval quality measured | 2 | `evals/results/retrieval.json`: 5 configurations, recall@5 / recall@10 / MRR; REPORT-hw2 §4 |
| 3 | Answers cite their sources | 4 | `src/rag/answer.py` (claims with `[S#]`, labels checked), `prompts/rag_v2.txt`; source hit 1.00, faithfulness 0.99 |
| 3 | Token budget, "I don't know" | 4 | `config/rag.yaml` `context_budget: 3000`, `answer.py` `NOT_FOUND`; abstain 4 / 4, false abstain 0 / 20 (REPORT-hw2 §5) |
| 4 | Testset ≥ 20 with expected answers | 3 | `evals/testset.jsonl`: 24 items incl. 4 no-answer, 3 similar-document and 3 outdated-version traps, each `verified_by` Petro; `evals/labels/testset_review*.md` |
| 4 | Deterministic + calibrated judge + faithfulness | 4 | `evals/scorers.py`, `evals/judge.py`, `evals/labels/calibration.jsonl` (17 hand labels), `evals/results/calibration.json` (88 % / κ 0.77, 100 % / κ 1.00); REPORT-hw2 §6 |
| 4 | Evals in CI | 3 | `.github/workflows/evals.yml`, `make eval-ci`, `config/eval_thresholds.yaml`; REPORT-hw2 §7 (green and red runs) |
| — | README, one-command launch, keys not in code | 2 | README "Stage 2: RAG (HW 2)" (`make rag`, from the committed chunks, checked on a clean clone; `make rag-rebuild` from the source), `.env.example` only, CI key as a repository secret |

### What must be in the repository

| Item | Evidence |
|---|---|
| code of ingestion, indexing, RAG, evals | `src/rag/ingest/`, `src/rag/index.py`, `search.py`, `answer.py`, `llm.py`, `evals/` |
| `data/`: corpus or download script + manifest | `scripts/download_rag_corpus.py` (`make rag-data`), `data/rag/manifest.csv`, `chunks.jsonl`, `ingest_manifest.json` |
| `prompts/` with versions and changelog | `prompts/rag_v1.txt`, `rag_v2.txt`, `judge_*_v1.txt`, `prompts/CHANGELOG.md` |
| `evals/`: testset, scoring, run results | `evals/testset.jsonl`, `scorers.py`, `judge.py`, `evals/results/*.json` |
| `.github/workflows/` with the eval run | `.github/workflows/evals.yml` |
| report: metrics, error analysis, conclusions | `REPORT-hw2.md` (§4–§7 metrics, §8 five errors, §10 next steps) |
| README: project, how to run, chunking justification | `README.md` "Stage 2: RAG (HW 2)", "Why this chunking" |
| technical: Python 3.12, keys in `.env`, cost per 1,000 | `pyproject.toml`, `.env.example`, REPORT-hw2 §9 ($0.65 per 1,000 questions) |

**Clean-clone check (17.11, after PR #41).** The public repository cloned into an empty folder, no
`.env`, no key: `make install` ok; `make rag` as it was then stopped at `rag-data` (F25); `make
retrieval-eval eval score` reproduced every committed number with 0 new calls, only the timings
(`ms`) and `new_calls` of the summary differ. Patch 20.2 makes that the `make rag` path.
