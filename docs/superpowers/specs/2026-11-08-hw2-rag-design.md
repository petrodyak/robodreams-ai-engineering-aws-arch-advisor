# HW 2 — RAG with sources and evals in CI: design

Status: **approved by Petro (09.11)**: decisions D1–D9 and the whole spec. Deadline: **20.11 23:59** (moved from 13.11 on 13.11; scope unchanged). Stage 2 of the course project
(`CLAUDE.md`, "Course project"). The assignment text is in the chat of 08.11; step 14 saves it as
`docs/hw2-brief.md`, the same way `docs/hw1-brief.md` holds HW 1.

**Terms.** *Well-Architected* is short for the **AWS Well-Architected Framework** and its documents: the
Framework itself, its six pillars and its lenses. No acronym is used for it: "WA" is unclear, and
"AWS WAF" is the AWS Web Application Firewall, a different service that the corpus itself describes
(Security pillar). *Prescriptive Guidance* is AWS Prescriptive Guidance. The same terms go into
`GLOSSARY.md` in step 14.

## 1. Goal and success criteria

Answer AWS architecture questions from a corpus of AWS Well-Architected and Prescriptive Guidance
documents. Every claim in an answer cites a document and a section. When the corpus has no answer,
the system says so instead of guessing. An eval pipeline measures retrieval and answer quality,
and GitHub Actions runs it on every push and pull request. The run fails when a metric drops below its
threshold.

Done when every row of the grading table (40 points) has evidence in the repository:

| Brief item | Points | Evidence |
|---|---|---|
| Ingestion of ≥ 2 formats | 3 | PDF + HTML extractors, `data/rag/manifest.csv` |
| Cleaning + dedup | 3 | `clean.py`, content hash + near-duplicate report in the ingest manifest |
| Chunking strategy justified + metadata | 4 | README section, fixed vs structure comparison in REPORT |
| Embeddings + vector DB | 3 | `index.py`, Qdrant |
| Hybrid search | 3 | BM25 + vector + RRF |
| Reranking + metadata filters | 2 | cross-encoder, `doc_type` / date filters |
| Retrieval quality measured | 2 | recall@k + MRR for ≥ 3 configurations |
| Answers cite sources | 4 | per-claim citations, validated by code |
| Context control | 4 | token budget, "not in the documents" answer |
| Testset ≥ 20 | 3 | `evals/testset.jsonl`, checked by Petro |
| Scorers: deterministic + calibrated judge + faithfulness | 4 | `evals/scorers.py`, `evals/judge.py`, calibration table |
| Evals in CI | 3 | `.github/workflows/evals.yml` with thresholds |
| README, one command, keys not in code | 2 | `make rag`, `.env.example` |

**Out of scope** (the brief says not needed, or YAGNI): UI, deploy, fine-tuning, a local-model
comparison (Ollama is not used in HW 2), follow-up questions and condense, map-reduce, access
groups (the corpus is public, so the metadata filter is `doc_type` and date, not access).

## 2. Decisions

| # | Decision | Status |
|---|---|---|
| D1 | Evals in CI run **live with a cache**: retrieval eval and deterministic scorers always run locally. Answers and judge verdicts are cached in Git. Claude is called only for cache misses | ✅ Petro, 08.11 |
| D2 | Corpus = **Well-Architected core + data**: Framework + 6 pillars + data-oriented lenses (PDF), Prescriptive Guidance data guides (HTML) | ✅ Petro, 09.11 |
| D3 | HW 2 API budget **$5**, estimated before every paid run (same rule as HW 1) | ✅ Petro, 09.11 |
| D4 | Answer model **`claude-haiku-5-5`** with `effort` set explicitly in `config/rag.yaml` (start `medium`, the default). Judge model `claude-sonnet-5-5`: a different, stronger model than the one it grades | ✅ Petro, 09.11 |
| D5 | Embeddings and reranker are local (`fastembed`), vector DB is Qdrant in-process: no key, no Docker, works in CI | ✅ Petro, 09.11 |
| D6 | One command for HW 2 is **`make rag`** (ingest → index → eval). `make run` stays the HW 1 extraction. **Amended 17.11 (F25):** `make rag` starts from the committed `chunks.jsonl` (index → eval); `make rag-rebuild` downloads and ingests first | ✅ Petro, 09.11; amended by Petro, 17.11 |
| D7 | `docs/project-plan.md` (whole-project plan, memory note of 23.10) is written **after** HW 2, not inside it | ✅ Petro, 09.11 |
| D8 | The assignment is kept in **`docs/hw2-brief.md`**, structured like `docs/hw1-brief.md`; the brief text is carried over almost verbatim, decisions stay in this spec, the ADRs and the tracking file | ✅ Petro, 09.11 |
| D9 | Tracking lives in a **separate file `docs/hw2-implementation-steps.md`** with the 8 sections of the HW 1 file; `docs/Implementation_steps.md` is frozen as the HW 1 record. Numbering continues: steps 14–20, findings from F21. Status-row rule (a Standing rule of the new file only; `GIT_RULES.md` §5 already allows it and does not change): a step's own PR sets its row to `🔄 PR #N`; the next step's PR flips it to `✅ PR #N (merge sha)`; step 20 is closed by the pre-submission check against the brief. A row lags git by at most one step, and "if the table and `git log` disagree, git is right" covers that window. No PR exists only for a status row | ✅ Petro, 09.11 |

Why D4: Haiku 5.5 is the current Haiku, ten times cheaper than Haiku 4.5 ($0.10 / $0.50 per MTok for
prompts up to 100 K tokens, against $1 / $5) and better at following instructions such as "cite every
claim". `src/rag/llm.py` is new code, so the Haiku 4.5 code path of HW 1 is not reused; HW 1 stays on
Haiku 4.5 unchanged. What Haiku 5.5 changes for the client (checked against the Claude API reference):
adaptive thinking is on by default, so the answer is read from content blocks by `type`, not from
`content[0]`, and `max_tokens` leaves room for thinking; `temperature` / `top_p` / `top_k` and assistant
prefill return a 400 (none is sent); a request can end with `stop_reason: "refusal"`, which is handled
before `content` is read; the tokenizer counts the same text as about 30 % more tokens, so costs come from
the API `usage`, never from `tiktoken`. The judge must be stronger than the model it grades and not the
same model: a model grading its own answers is lenient towards them. Sonnet 5.5 costs $2 / $10 per MTok;
it also thinks by default (default effort `high`), so the judge's `effort` is a config value too (start
`medium`) and is part of the cache key.

## 3. Corpus (step 15)

**Composition** (target ≥ 30 documents, two formats):

| Group | Format | Count | Examples |
|---|---|---|---|
| Well-Architected Framework | PDF | 1 | AWS Well-Architected Framework |
| Well-Architected pillars | PDF | 6 | Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability |
| Well-Architected lenses (data-oriented) | PDF | 3–4 | Data Analytics Lens, Machine Learning Lens, Generative AI Lens, Serverless Lens |
| Prescriptive Guidance | HTML | ~20 | data lake / lakehouse, Apache Iceberg on AWS, data mesh, Glue / Athena / Redshift guides and patterns |

The final list is a step-15 deliverable with Petro's "ok"; the URLs above are not checked yet.

**Traps the testset needs** (brief, step 4):

- *Similar documents:* a pillar and a lens describe the same topic differently (Reliability pillar vs
  Data Analytics Lens on backups). Two lenses overlap (Data Analytics vs ML on data pipelines).
- *Outdated versions:* step 15 checks whether an older edition of one Well-Architected document can still be
  downloaded. If it can, it goes into the corpus with its date, and a trap question has to prefer the newer
  edition. If none can, the trap uses the "Document revisions" table that every Well-Architected document carries,
  for example "what changed in the edition of <date>".

**Storage**, following the HW 1 pattern (originals are not in Git, everything derived is):

```
data/rag/
├── manifest.csv        # doc_id, title, format, url, doc_type, published, sha256 (in Git)
├── raw/                # downloaded *.pdf / *.html (not in Git, .gitignore)
├── chunks.jsonl        # structure-aware chunks + metadata (in Git; stage 3 reads it)
├── chunks_fixed.jsonl  # the fixed-size baseline, same record format (in Git; retrieval eval only)
└── ingest_manifest.json  # dataset version, per-document stats, duplicates found (in Git)
```

`scripts/download_rag_corpus.py` downloads every URL from `manifest.csv` and checks its sha256. That
makes the corpus reproducible without committing third-party files. The sha256 is that of the
document's cleaned text, the same value as `doc_hash` in `chunks.jsonl`, not of the file's bytes: AWS
rebuilds its PDFs and pages every few days around the same text (amended 14.11, finding F21).

**Affects stage 3:** the agent reads `data/rag/chunks.jsonl` and the search API in section 5. Their field
names are fixed by this spec.

## 4. Ingestion (step 16)

Pipeline per document: `extract → clean → dedup → chunk → metadata`. It adapts the lesson-6 starter
(`ingest.py`) to two formats and drops what does not apply (DOCX, OCR, access rules).

**Extract with structure:**

- *PDF* (`pypdf`, already a dependency): text per page. Section structure comes from the PDF outline
  (bookmarks), as HW 1 split the source PDF. Each page knows the outline path it falls under. Tables
  stay as text rows. Well-Architected best-practice IDs (`REL10-BP01`) are kept verbatim: they are the strongest
  exact-match terms in the corpus.
- *HTML* (`beautifulsoup4`): keep the main article and drop navigation, breadcrumbs, the feedback
  widget, scripts and the footer. `h1–h4` become markdown headings, lists stay lists, and tables become
  markdown rows.

**Clean and normalize:** remove repeated page headers and footers (a line seen on > 50 % of pages),
page numbers, hyphenation at line ends, ligatures and zero-width characters, and the HTML boilerplate
above. Use one Unicode form (NFKC, as the lesson-6 `normalize`: it also turns ligatures such as "ﬁ" into "fi",
which NFC does not) so hashing sees one canonical text.

**Dedup:**

- *exact:* `sha256` of the normalized text, per document and per chunk. A duplicate document or chunk
  is dropped, and the drop is counted in the ingest manifest. The copy that stays is the one in the
  most specific document (pillar, then lens, then guide, then framework): the current Framework PDF
  repeats every pillar's best practices, and a citation should name the pillar (amended 14.11).
- *near:* Jaccard similarity over word 5-shingles between documents above 0.8 is reported in
  `ingest_manifest.json`. An HTML guide that repeats a PDF chapter is the expected case.

**Chunking strategy (the main justification for the README):**

- **Structure-aware.** Split on section boundaries (outline or headings), then pack whole paragraphs up
  to the limit. A section that is too long is split at paragraph boundaries. One that is too short is
  merged with the next section under the same parent.
- **Size: 250–450 tokens, hard maximum 480.** Why:
  1. the embedding model reads at most 512 tokens, and the contextual header (below) uses some of them;
  2. a Well-Architected best practice (one `XXXnn-BPnn` section) is typically one self-contained unit of a few
     hundred words, so one chunk ≈ one best practice, which is also what a citation should point to;
  3. smaller chunks split a best practice's "implementation guidance" from its statement.
- **No overlap** within the structure strategy: sections are natural boundaries, and overlap would
  duplicate text across best practices.
- **Contextual header:** `"<doc title> > <section path>"` is prepended to the text that is embedded and
  BM25-indexed, but not to the text shown to the model. This is a stretch item of the brief and costs
  one line.
- **Baseline for comparison:** fixed windows of 400 tokens with 60 tokens of overlap, ignoring
  structure. Both chunk sets are indexed, and the retrieval eval (section 5) compares them on the same
  questions. REPORT gives the numbers and two examples where a fixed window cut a best practice in half.
- Tokens are counted with `tiktoken` `cl100k_base` as an approximation of the embedding tokenizer. The
  limit leaves a margin for the difference.

**Chunk record** (`data/rag/chunks.jsonl`, one JSON object per line; `chunks_fixed.jsonl` uses the same
record with `strategy: "fixed"` and ids `<doc_id>#f0000`. The two files are separate so that stage 3
reads only the structure-aware chunks; amended 14.11):

```json
{
  "chunk_id": "wa-reliability#0123",
  "doc_id": "wa-reliability",
  "title": "Reliability Pillar - AWS Well-Architected Framework",
  "doc_type": "pillar",
  "format": "pdf",
  "source_url": "https://docs.aws.amazon.com/...",
  "published": "2024-11-06",
  "section_path": ["Failure management", "Back up data", "REL09-BP01 ..."],
  "page_start": 87, "page_end": 88,
  "text": "...",
  "n_tokens": 341,
  "chunk_hash": "sha256:...",
  "doc_hash": "sha256:...",
  "strategy": "structure",
  "pipeline_version": "ingest-v1"
}
```

`doc_type` ∈ `framework | pillar | lens | guide`. `published` is the edition date printed in the
document (Well-Architected), or the page's last-updated date (HTML). `page_*` is `null` for HTML.

## 5. Index and search (step 17)

Adapts the lesson-7 `search.py` and lesson-8 `retrieval.py`.

- **Embeddings:** `fastembed` with `BAAI/bge-small-en-v1.5` (384 dimensions, English: the corpus and the
  questions are English). The lesson used a multilingual model because its questions were Ukrainian. A
  cache keyed by `sha256(model + text)` means a re-run embeds only new chunks. It is a local file
  (`.cache/`, not in Git) and is restored by `actions/cache` in CI.
- **Vector DB:** Qdrant in-process (`QdrantClient(":memory:")`), cosine, the chunk record as payload. It
  is rebuilt from `chunks.jsonl` (and `chunks_fixed.jsonl` for the baseline) on every run, which takes about a minute for an estimated 2–3 k chunks.
- **Lexical:** `rank-bm25` over the same texts (header included).
- **Hybrid:** Reciprocal Rank Fusion (k = 60) of the top 20 from each.
- **Reranker:** `fastembed` cross-encoder `Xenova/ms-marco-MiniLM-L-6-v2` (English) re-orders the 20
  hybrid candidates. Step 17 checks both model names against fastembed's supported list.
- **Filters:** `doc_type` (in / not in) and `published >= date`. They are applied as Qdrant payload filters
  and to BM25 by post-filtering. Example use: "answer only from pillars", "only editions after 2023".
- **API** (`src/rag/search.py`), which stage 3 will call as a tool:
  `search(query, k=5, mode="hybrid_rerank", filters=None) -> list[Hit]`.

**Retrieval eval:** the 20 answerable questions of the testset (section 7), each with the `chunk_id`s
that answer it, marked by Petro. The brief asks for 10–15; one labelled set serves both evals, so there
is no second set to maintain.
Metrics: recall@5, recall@10, MRR. Configurations, all on structure chunks unless noted:

| Config | Purpose |
|---|---|
| `vector` on **fixed** chunks | the chunking baseline |
| `vector` | structure vs fixed chunks |
| `bm25` | where exact IDs win |
| `hybrid` | the fusion gain |
| `hybrid_rerank` | the reranker gain; the configuration RAG uses if the numbers confirm it |

## 6. Answering with sources (step 18)

Adapts the lesson-8 `rag.py` to the Anthropic SDK (`CLAUDE.md`: Claude is the only paid model).

1. `search()` → reranked hits.
2. **Context budget:** sources are added in rank order until **3,000 tokens** of source text. A chunk
   that does not fit is skipped, not truncated. Each source is labelled `[S1]…[Sn]` with its document title
   and section path. The budget and k are config values. Step 18 measures k = 3 / 5 / 8 if the budget allows.
3. **Generate** with structured output (`output_config.format`, as HW 1):
   `{found: bool, claims: [{text, citations: ["S2", ...]}]}`. Every claim carries its own citations,
   which makes "a source for every claim" checkable by code.
4. **Validate** in code: drop citation labels the model was not given. A claim left with no citation is
   flagged. Labels are mapped to `doc_id + section_path (+ page)`.
5. **"Not in the documents":** `found = false` (or no claim survives validation) → the fixed answer
   *"The documents available to me do not answer this question."* plus the titles of the closest
   sources, and no claims. The prompt says: answer only from the sources, no outside knowledge;
   `found = false` when no source addresses the question; prefer the newer edition when two sources
   conflict.
6. **Prompts** live in `prompts/rag_v1.txt` → `rag_v2.txt` after the first error analysis.
   `prompts/CHANGELOG.md` gets a RAG section in the HW 1 format (what changed, why, measured effect).
7. **Logging and cost:** one JSONL record per question with question, hits, context tokens, answer,
   usage, latency and cost. Cost per 1,000 questions is computed from real usage and goes into REPORT.

No `temperature` is sent: Haiku 5.5 and Sonnet 5.5 reject non-default sampling parameters (the 2026-10-21
API version rejects any value), and greedy decoding is not needed for answers.

## 7. Testset and scorers (step 19)

**Testset** `evals/testset.jsonl`, ≥ 24 items:

| Kind | Count | What it checks |
|---|---|---|
| answerable, one source | 10 | facts, citation |
| answerable, several sources | 4 | combining, citing all |
| not in the corpus | 4 | "not in the documents" (e.g. a service quota, which lives in the HW 1 corpus, not this one) |
| similar documents | 3 | picks the right document of two near ones |
| outdated version | 3 | prefers the newer edition |

Item fields: `id, question, kind, expected_answer, key_facts[], expected_sources[{doc_id, section}],
relevant_chunk_ids[], answerable, verified_by, verified_on`.

**How it is made** (the brief penalizes an unchecked AI-generated testset): Claude drafts candidates from
the chunks. Petro checks every item against the source document, edits it or rejects it, and writes at
least the trap questions himself. `verified_by` and `verified_on` record that. This is the HW 1 golden-set
process (drafts → manual check).

**Deterministic scorers** (`evals/scorers.py`, unit-tested):

- `abstain_correct`: `found` matches `answerable`. Reported as two rates: abstain accuracy on
  no-answer items, and false-abstain rate on answerable items.
- `source_hit`: an expected `(doc_id, section)` is among the validated citations.
- `key_facts`: share of `key_facts` present in the answer (normalized, case-insensitive).
- `citations_valid`: every claim has ≥ 1 valid citation.
- `retrieved` / `in_context`: a relevant chunk is in the hits / in the budgeted context. This separates a
  retrieval failure from a generation failure in the error analysis.

**LLM judge** (`evals/judge.py`, `claude-sonnet-5-5`, prompt `prompts/judge_correctness_v1.txt`):
pass / fail on "the answer states the expected answer's facts and does not contradict it", plus a one-line
reason. It is used for answerable items, where key-fact matching is too literal.

**Faithfulness** (`prompts/judge_faithfulness_v1.txt`): for every claim, is it supported by the
sources it cites? The score is supported claims / all claims, so it also catches a correct fact cited to
the wrong source.

**Calibration:** Petro labels ≥ 12 answers by hand (pass / fail and "has an unsupported claim"), chosen
to include failures from the v1 run. The labels go into `evals/labels/calibration.jsonl`. REPORT gives
agreement % and Cohen's κ for both judges. If agreement is below 80 %, the judge prompt gets a v2
before any judge number is reported.

## 8. Evals in CI (step 20)

`.github/workflows/evals.yml`, on `push` and `pull_request`:

1. `uv sync`. Restore `actions/cache` for the fastembed models and the embedding cache.
2. `make check` (ruff + pytest), the existing gate.
3. `make eval-ci`: build the index from `data/rag/chunks.jsonl`, run the retrieval eval, then answer and
   score the testset.
4. Answers and judge verdicts come from `evals/cache/*.jsonl` (in Git), keyed by
   `sha256(model, effort, prompt version, question, context hash)`. A cache miss calls Claude with the
   `ANTHROPIC_API_KEY` repository secret. A miss without a secret (a fork PR) fails with "cache is stale:
   run `make eval` locally and commit `evals/cache/`". CI never commits.
5. **Cost guard:** more than 30 misses in one CI run → fail before calling the API. A changed prompt is
   evaluated locally first, and the cache is committed with the change.
6. **Thresholds** in `config/eval_thresholds.yaml`, set from the first full baseline run minus a margin.
   The values are recorded in REPORT, never edited just to make a run pass (GIT_RULES). Gated metrics:
   retrieval recall@5, abstain accuracy, false-abstain rate (maximum), source hit, faithfulness, judge
   pass rate.
7. Results are uploaded as a workflow artifact. `evals/results/<run_id>.json` is committed by the developer
   for the runs that REPORT cites.

## 9. Code layout

```
src/rag/
├── ingest/        extract_pdf.py, extract_html.py, clean.py, dedup.py, chunk.py, pipeline.py
├── index.py       embeddings (+ cache), Qdrant, BM25
├── search.py      hybrid, RRF, rerank, filters — the stage-3 tool
├── answer.py      context budget, generate, validate citations, not-found
└── llm.py         thin Claude client (structured output, effort, refusal handling, retry, usage, cost)
evals/
├── testset.jsonl, labels/calibration.jsonl
├── scorers.py, judge.py, run.py           # run.py: retrieval eval + answer eval + thresholds
├── cache/                                  # answers + verdicts (in Git)
└── results/                                # run summaries cited by REPORT
scripts/download_rag_corpus.py
config/rag.yaml, config/eval_thresholds.yaml
prompts/rag_v1.txt, rag_v2.txt, judge_correctness_v1.txt, judge_faithfulness_v1.txt
.github/workflows/evals.yml
```

Make targets: `rag-data` (download), `ingest`, `index`, `retrieval-eval`, `eval`, `eval-ci`, `ask Q="…"`,
`rag` (all of them in order). New dependencies, via `uv add` only: `beautifulsoup4`, `tiktoken`,
`fastembed`, `qdrant-client`, `rank-bm25`.

### Reuse from the lessons

The course starters live outside this repository, in `ai-engineeering-2/lesson-0N-*/`. Code is adapted,
not imported: each piece is copied into the file below, changed as listed, and covered by our own tests.
README and REPORT say what was adapted and what is new.

| Lesson piece | HW 2 file (step) | What changes |
|---|---|---|
| L6 `ingest.py` `extract_html` | `ingest/extract_html.py` (16) | adds `h4` and tables as markdown rows; selectors for docs.aws.amazon.com pages |
| L6 `extract_pdf` | `ingest/extract_pdf.py` (16) | adds the section path from the PDF outline (as HW 1 `scripts/split_pdf.py`); the lesson has none |
| L6 `normalize`, `unwrap`, `PAGE_NUMBER`, `ZERO_WIDTH` | `ingest/clean.py` (16) | almost as is; the page-number pattern is checked on the AWS PDFs |
| L6 `content_hash`, `shingles`, `jaccard`, `near_duplicates` | `ingest/dedup.py` (16) | as is |
| L6 `chunk_fixed` | `ingest/chunk.py` (16) | the baseline: 400 tokens, overlap 60 |
| L6 `chunk_by_headings`, `split_block`, `is_heading` | `ingest/chunk.py` (16) | 250–450 / 480 tokens; merges short sections (new); falls back to `XXXnn-BPnn` IDs |
| L6 `chunk_stats` | `ingest/pipeline.py` (16) | the mid-sentence / cut-table counts go to the ingest manifest and the REPORT chunking comparison |
| L6 `dataset_version`, `audit` | `ingest/pipeline.py` (16) | written to `ingest_manifest.json` |
| L7 `search.py` `embed` (cache by `sha256(model + text)`), `build_index` | `index.py` (17) | model `BAAI/bge-small-en-v1.5` instead of the multilingual one |
| L8 `retrieval.py` `Retriever` (BM25 + RRF; the L7 starter leaves them as TODO) | `index.py`, `search.py` (17) | as is |
| L7 `vector_search` + `access_filter` | `search.py` (17) | the filter becomes `doc_type` + `published`, no access groups |
| L7 `rerank` (a hint only, not solved in any lesson) | `search.py` (17) | **new code**; the `TextCrossEncoder` API is checked in the fastembed docs first |
| L7 `evaluate`, `make_configs` | `evals/run.py` (17) | adds recall@10; the 5 configurations of section 5 |
| L7 `similar_pairs` (optional TODO 10) | helper for the testset (19) | finds candidates for the "similar documents" traps |
| L8 `rag.py` `build_context` | `answer.py` (18) | budget 3,000; the label carries title, section path and `published` |
| L8 `generate`, `Answer`, `validate_citations`, `rag()` | `answer.py` (18) | Anthropic SDK with `output_config.format`; `claims[]` with citations per claim; no condense |
| L8 `sweep` | `evals/run.py` (18) | k = 3 / 5 / 8 (the lesson used 3 / 5 / 10) |
| L8 `prompts/v2/system.txt` rules | `prompts/rag_v1.txt` (18) | keeps the conflict, several-sources and `found = false` rules; "later date" becomes "newer edition"; no language rule (English corpus) |
| L8 `prompts/CHANGELOG.md` table | `prompts/CHANGELOG.md` (18–19) | same columns: metrics, $/1000, failed items |
| L8 `evaluate` (retrieved, in_context, correct, cited, abstain, false_abstain) | `evals/scorers.py` (19) | the base of the deterministic scorers of section 7 |
| L8 `check.py` (checks on fake data) | `tests/` (16–19) | same idea as pytest unit tests |

**Not taken:** L8 `LLM` (OpenAI SDK over OpenRouter, a course-exercise client only, ADR-0004), condense,
map-reduce and summary (out of scope), L6 DOCX / OCR / access rules. L3 and L4 code is not reused: their
patterns (retry, usage and cost, versioned prompts, golden set) are already in HW 1.
**No lesson code exists** for the LLM judge, calibration or CI (L8 points to lesson 9, not published
yet): steps 19–20 are new code and are checked against lesson 9 if it appears before 20.11.

## 10. Steps, dates, Petro's time

| # | Step | By | Petro |
|---|---|---|---|
| 14 | Housekeeping: CLAUDE.md → stage 2 (and its "Read before you work on…" rows point to the HW 2 files), `docs/hw2-brief.md` (D8), `docs/hw2-implementation-steps.md` (D9, with the status-row rule among its Standing rules), GLOSSARY terms, ADR-0007 (structure-aware chunking), ADR-0008 (cached live evals in CI) | 09.11 | review 15 min |
| 15 | Corpus list, download script, manifest | 14.11 | pick and "ok" the list, 30 min |
| 16 | Ingestion → `chunks.jsonl` + `chunks_fixed.jsonl` + ingest manifest | 15.11 | review |
| 17 | Index, hybrid, rerank, filters, retrieval eval (drafts the 20 answerable questions early) | 16.11 | **label relevant chunks, ~1 h** |
| 18 | RAG answering, prompt v1, first run | 17.11 | "ok" on the estimate |
| 19 | Testset, scorers, judge, calibration, prompt v2 | 18.11 | **check the testset ~1 h, label ≥ 12 answers ~1 h** |
| 20 | CI workflow + thresholds, REPORT, README | 19.11 | review, add the secret |

Petro's time this week is about 4–5 h, above the usual 3–4 h. The hand labelling of steps 17 and 19 is what
the brief grades hardest.

**Cost estimate (to be re-measured with `count_tokens` before step 18):** about 3.5 k input + 0.4 k output
tokens per answer, about 4.6 k + 1 k with the Haiku 5.5 tokenizer and some thinking at `medium` effort:
about $0.001 per question or about $1 per 1,000 questions. Two judge calls per answerable item with
Sonnet 5.5 cost about $0.02–0.04 per question (the upper end if the judge thinks a lot), so the judge, not
the answers, is most of the cost. A full live run of 24 questions is therefore about $0.5–1, and the whole
HW 2 (v1, v2, calibration, CI misses) should stay under $3 of the $5.

## 11. Risks

| Risk | Mitigation |
|---|---|
| No older Well-Architected edition is downloadable | Fall back to the "Document revisions" trap (section 3) |
| PDF outline missing or shallow in a document | Fall back to detecting heading lines by pattern (numbered titles, `XXXnn-BPnn` IDs), as the lesson-6 `is_heading` does |
| CI too slow (model download + embedding) | `actions/cache` for models and the embedding cache |
| Haiku 5.5 thinks too long or refuses a benign AWS question | `effort` is a config value (`low` if answers are slow or costly); a refusal is logged and scored as a failed answer, never retried silently |
| Judge disagrees with Petro | Judge prompt v2 before reporting; REPORT states the agreement as measured |
| Time | Each step is one PR. If time runs out, step 20's REPORT is cut to the brief's minimum, never the CI or the calibration |
