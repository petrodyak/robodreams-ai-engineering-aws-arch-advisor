# HW 2 — RAG with sources and evals in CI

Stage 2 of the course project: answers to AWS architecture questions, built only from public AWS
Well-Architected and Prescriptive Guidance documents, with a citation for every claim, an
"I don't know" answer when the documents do not cover the question, and evals that run in GitHub
Actions on every pull request and every push to `main`.

```
data/rag/manifest.csv → make rag-data → data/rag/raw/ (PDF + HTML)
  → make ingest → data/rag/chunks.jsonl (structure) + chunks_fixed.jsonl (baseline) + ingest_manifest.json
  → index: fastembed (bge-small) → Qdrant :memory: + BM25 → RRF → cross-encoder rerank
  → answer: Claude Haiku 5.5, structured output, [S1]… per claim, a 3,000-token context budget
  → evals: 24-item testset, deterministic scorers, two calibrated Sonnet judges, CI thresholds
```

Every number below comes from a committed file: `data/rag/ingest_manifest.json`,
`evals/results/retrieval.json`, `evals/results/<run_id>.summary.json` and `<run_id>.json`,
`evals/results/calibration*.json`. How to run it is in the README, section "Stage 2: RAG (HW 2)".

**Testset ids.** The testset is `evals/testset.jsonl`, 24 items, every one checked by Petro. Each
item has an `id` made of a short word for its kind and a number. The number counts the items within
one kind. A short word rather than one letter keeps an id readable in a results table without
looking up the kind.

| Prefix | `kind` | What the item checks | Items |
|---|---|---|---|
| `one` | `single` | The answer sits in one place in one document. | one01–one10 |
| `many` | `multi` | The answer combines two documents, and both must be cited. | many01–many04 |
| `sim` | `similar` | A similar best practice from another pillar is nearby. The trap is to answer from the neighbour. | sim01–sim03 |
| `old` | `outdated` | The answer changed between the archived July 2020 Well-Architected Framework (`wa-framework-old`) and the current edition. The trap is the outdated text; the expected answer is the current one. | old01–old03 |
| `none` | `no_answer` | The corpus does not hold the answer; the system must say so. | none01–none04 |

The `one`, `many`, `sim` and `old` items are answerable. Only these carry `relevant_chunk_ids` and
enter the retrieval eval.

## 1. Summary

| | Result |
|---|---|
| Corpus | 34 public AWS documents, 12 PDF + 22 HTML, 1.05 M tokens, 1,057 duplicate chunks removed |
| Chunking | structure-aware, 2,869 chunks (avg 270, max 480 tokens) vs fixed 400 / 60: 3,102 windows |
| Retrieval | hybrid + rerank: recall@5 **1.00**, MRR 0.81 on 20 labelled questions (vector only: 0.70 / 0.64) |
| Answers (prompt v2, k = 5) | judge pass **0.80**, faithfulness **0.99**, right "I don't know" **4 / 4**, false "I don't know" **0 / 20**, an expected source cited **20 / 20** |
| Judges | agree with Petro's 17 hand labels: correctness 88 % (κ 0.77), faithfulness 100 % (κ 1.00) |
| Cost | **$0.65 per 1,000 questions** (Claude Haiku 5.5; embeddings and reranking run locally, $0) |
| CI | `make eval-ci` in GitHub Actions: 6 thresholds, answers and verdicts replayed from `evals/cache/` |

## 2. Corpus and ingestion

`data/rag/manifest.csv` lists 34 documents with their URL, type, publication date and sha256;
`make rag-data` downloads and checks them (`data/rag/raw/` is not in Git).

| Type | Format | Documents | Content |
|---|---|---|---|
| framework | PDF | 2 | the Well-Architected Framework, current and the archived July 2020 edition (the outdated-version trap) |
| pillar | PDF | 6 | the six Well-Architected pillars |
| lens | PDF | 4 | Data Analytics, Machine Learning, Generative AI, Serverless |
| guide | HTML | 22 | 15 Prescriptive Guidance pages (data lake, data mesh, Glue, Redshift), 7 Athena / S3 Tables / Glue pages on Iceberg |

Ingestion (`src/rag/ingest/`, `make ingest`):

- **Extraction with structure.** A PDF gets its sections from its outline (titles are searched in the
  text, because deep outline entries point to wrong pages). HTML gets them from `h2`–`h4` (`h1` is
  the document title), with tables kept as markdown rows; a PDF table comes out of `pypdf` as plain
  lines and is not rebuilt. Every chunk carries its Section Path, for example
  `Failure management > REL09-BP01 …`.
- **Cleaning.** Repeated headers and footers (a line on more than 50 % of the pages), page numbers,
  hyphenation, NFKC, zero-width characters, line unwrapping; cover pages and tables of contents are
  dropped.
- **Deduplication.** A content hash (sha256 of the normalised text) per document and per chunk, and
  5-word-shingle Jaccard ≥ 0.8 for near-duplicates. No document was a duplicate. 1,057 chunks were:
  the Framework PDF repeats the text of the pillars, so 1,045 of its chunks are dropped and each
  best practice stays in its most specific document (the pillar). No near-duplicate documents.
- **Metadata per chunk:** `doc_id`, title, URL, `doc_type`, publication date, Section Path, pages,
  `doc_hash`, chunk hash, token count. `ingest_manifest.json` records the dataset version, the
  duplicates and the chunk statistics. A re-run is byte-identical.

Two findings on the way. AWS regenerates its PDFs every few days, so the bytes change while the text
does not; the manifest hash is therefore the hash of the cleaned text (F21). The Prescriptive
Guidance Iceberg guide was withdrawn (404), so the Iceberg pages come from the Athena, S3 Tables and
Glue guides.

## 3. Chunking: structure-aware vs fixed size

The decision and its reasons are in ADR-0007 and, condensed, in the README. In short: chunks follow
the documents' own sections, a target of 250–450 tokens with a hard maximum of 480, no overlap, and a Contextual
Header (`<title> > <Section Path>`) that is embedded and indexed but not shown to the answer model.
One Well-Architected best practice ≈ one chunk ≈ what a citation should point to; the embedding model
reads at most 512 tokens.

The baseline is the lesson's fixed window, 400 tokens with 60 tokens of overlap, built from the same
cleaned text (`chunks_fixed.jsonl`).

| | Structure | Fixed 400 / 60 |
|---|---|---|
| chunks | 2,869 | 3,102 |
| tokens per chunk, avg / max | 270 / 480 | 398 / 400 |
| chunks that start mid-sentence | **24** | 137 |
| tokens per chunk, median / share below 250 | 278 / 41 % | 400 / 1 % |
| a section to cite | 2,799 of 2,869 | no (a window spans sections) |

250 tokens is where merging stops, not a floor: a short section with no sibling under the same
parent stays short, so 41 % of the structure chunks are below it. The 70 chunks without a section
are the text before a document's first heading; their citation names only the document. An earlier
version of this table also counted "tables cut across two chunks" (29 against 72). That count is
removed (F27): it matched any line with a `|`, which in the PDFs is a link title such as
"… | AWS Big Data Blog", not a table.

Two windows that cut a best practice in half (`chunks_fixed.jsonl`):

- `wa-reliability#f0034` starts with "…over cases that might occur due to some degradation", in the
  middle of REL01-BP06's implementation guidance, and ends with "Consider using On-Demand Capacity
  Reservations to schedule capacity ahead of any" — the sentence goes on in the next window.
- `wa-reliability#f0146` starts with "once per year, or before critical performance periods)" and
  ends with "Level of risk exposed if this best practice is" — the risk level, the one line an
  architecture review needs, lands in another window.

Retrieval on the same 20 questions (section 4): with vector search only, the fixed windows find a
relevant text in the top 5 more often (0.80 vs 0.70) but rank it lower (MRR 0.58 vs 0.64). The
comparison is in the windows' favour: a window counts as relevant when it shares ≥ 50 % of its
shingles with any relevant chunk, and its 60-token overlap gives every passage two chances. The
structure chunks win where it matters for this system: in the hybrid + rerank configuration that
answers questions, every relevant section is in the top 5, and the answer can cite a named section.

## 4. Index and search

`src/rag/index.py`, `src/rag/search.py`, settings in `config/rag.yaml`:

- embeddings `BAAI/bge-small-en-v1.5` (384 dims), local through fastembed, cached on disk; Qdrant
  `:memory:` with cosine distance;
- BM25 (`rank-bm25`) over the same Contextual Header + text, on lower-case word tokens, so
  `REL09-BP01.` and `rel09-bp01` match the same chunk;
- hybrid: Reciprocal Rank Fusion, k = 60, over the top 20 of each search;
- reranking: the cross-encoder `Xenova/ms-marco-MiniLM-L-6-v2` over the RRF top 20;
- metadata filters: `doc_types`, `exclude_doc_types` and `published_from`; filters that leave
  nothing return `[]`, and the answer is then "I don't know" without a model call.

Retrieval eval (`make retrieval-eval`, `evals/results/retrieval.json`), the 20 answerable items with
their relevant chunks labelled by Petro (55 chunk ids, none from the archived edition):

| Configuration | recall@5 | recall@10 | MRR | ms / query | missed in the top 10 |
|---|---|---|---|---|---|
| vector, fixed chunks | 0.80 | 0.95 | 0.58 | 215 | sim01 |
| vector | 0.70 | 0.95 | 0.64 | 130 | sim01 |
| BM25 | 0.85 | 0.90 | 0.81 | 6 | one09, old02 |
| hybrid (RRF) | 0.85 | 0.95 | 0.74 | 137 | old02 |
| **hybrid + rerank** | **1.00** | **1.00** | **0.81** | 450 | — |

Hybrid + rerank is the configuration the answers use. Each search alone misses a different item
(vector misses the reworded `sim01`, BM25 misses `one09` and `old02`), and the reranker lifts all 20
into the top 5. The first measurement (step 17, before Petro reworded the six traps in his own words)
was vector 0.85 / hybrid 0.95 / hybrid + rerank 1.00: the reworded traps share fewer words with the
documents, which costs vector and hybrid search, not the reranked hybrid.

## 5. Answers with sources

`src/rag/answer.py`, `prompts/rag_v2.txt`:

- **Context.** The top k = 5 hits in rank order, labelled `[S1]…[S5]`, each with its title and
  Section Path, within a budget of 3,000 tokens. A block that does not fit is skipped, never cut.
- **Answer.** Claude Haiku 5.5 (effort `medium`, no sampling parameters) returns structured output:
  `found` and a list of claims, each with its source labels.
- **Checks in code.** Unknown labels are dropped, and a claim left with no valid label is removed.
  Each label is resolved to its document, section and page, so a citation names a real source.
- **"I don't know".** With no hits, or `found = false`, the answer is
  "The documents available to me do not answer this question." When there are no hits, no call is
  made.

The k sweep (prompt v1, 24 items, `evals/results/*__k{3,5,8}.summary.json`):

| k | context budget | relevant chunk in the context | avg tokens in / out | $ per 1,000 |
|---|---|---|---|---|
| 3 | 3,000 | 0.90 | 2,602 / 535 | 0.53 |
| **5** | 3,000 | **1.00** | 3,780 / 607 | **0.68** |
| 8 | 3,840 | 1.00 | 5,561 / 675 | 0.89 |

k = 5 is the smallest k with a relevant chunk in the context for every item, at $0.15 per 1,000 more
than k = 3; k = 8 adds cost and no recall on this testset.

**Prompt v1 → v2** (`prompts/CHANGELOG.md`). The only change is rule 5 (F22). v1 said "a partial
answer is an answer", so the Athena price question got "billed by the data scanned" and the Google
Kubernetes Engine question got Amazon EKS advice. v2 sets `found = false` when no source states the
specific value asked for, or no source covers the product asked about. Measured at k = 5:

| prompt | judge pass | faithfulness | right "I don't know" | false "I don't know" | expected source cited | key facts | $ per 1,000 | failed items |
|---|---|---|---|---|---|---|---|---|
| v1 | 0.75 | 0.97 | 0.50 (2 / 4) | 0.00 | 1.00 | 0.93 | 0.68 | one02, many03, many04, sim02, old02, old03, none02, none04 |
| **v2** | **0.80** | **0.99** | **1.00 (4 / 4)** | **0.00** | 1.00 | 0.96 | **0.65** | one02, many03, many04, old03 |

The stricter rule cost no false "I don't know" on the 20 answerable items. v2 is the configured
prompt.

## 6. Evals: testset, scorers, judges

**Testset** (`evals/testset.jsonl`). 24 items: 20 answerable and 4 with no answer in the corpus.
Each item holds the question, the reference answer, its key facts, the expected sources and the
relevant chunk ids. Claude drafted the items from the documents. Petro checked every item against
its source sentence (`evals/labels/testset_review.md`, `testset_review_evidence.md`) and wrote the
six traps in his own words (`verified_by`).

**Deterministic scorers** (`evals/scorers.py`):

- right "I don't know" on the `none` items;
- false "I don't know" on the answerable items;
- an expected source cited (document + section);
- key facts present, as whole words;
- every citation valid;
- a relevant chunk retrieved / in the context;
- the share of the relevant chunks in the context (diagnostic).

**LLM judges** (`evals/judge.py`, Claude Sonnet 5.5, `prompts/judge_*_v1.txt`):

- **correctness:** pass / fail of the answer against the reference answer, with a reason;
- **faithfulness:** for each claim, do its cited source texts support it. The score is supported
  claims / all claims, so a true fact cited to the wrong source counts as unsupported.

**Calibration** (`evals/labels/calibration.jsonl`, `make calibrate`). Petro labelled 17 answers by
hand in `calibration_sheet.md`: 12 from the k = 5 run and 5 from the k = 3 run, so that the set
holds enough failures (7 fails, 10 passes). The judges ran on the same answers:

| | n | agreement, raw | κ, raw | agreement, after re-check | κ, after re-check |
|---|---|---|---|---|---|
| correctness | 17 | 82 % | 0.65 | **88 %** | **0.77** |
| faithfulness | 17 | 94 % | 0.77 | **100 %** | **1.00** |

Raw is Petro's first pass (`calibration_before_review.json`). He then re-read the 4 disagreements
and changed 2 of his own labels (many03, sim01 at k = 3), where the judge's reason showed he had
missed something. The other 2 (old02, old03) stay judge errors (F24, section 8). 88 % is above the
80 % bar set in the spec, so the judge prompt stays v1. Every judge number in this report comes from
these calibrated judges.

## 7. Evals in CI

`.github/workflows/evals.yml` runs on every pull request (on the merge of the branch into `main`) and
on every push to `main`:

1. `uv sync`;
2. `actions/cache` restores the fastembed models and the embedding cache;
3. `make check` (ruff + pytest);
4. `make eval-ci`: recall@5 of hybrid + rerank on the 20 labelled items, the answers and the judge
   verdicts, the score, and the thresholds;
5. the results (`evals/results/ci/`) are uploaded as an artifact.

**Paid calls in CI.** Answers and verdicts are replayed from `evals/cache/*.jsonl` (in Git, ADR-0008).
The cache key is the model, the effort, and the sha256 of the system prompt, the user message
(question + context) and the schema. A change to the prompt, the context or the model is a miss.

- A miss calls Claude with the `ANTHROPIC_API_KEY` repository secret.
- Without the secret (a fork PR), a miss fails the run with "cache is stale: run make eval locally
  and commit evals/cache/".
- More than 30 new calls in one run (answers and verdicts together) fail it before the 31st call.
  The worst case is about $0.2 per run.
- CI never commits.

**Thresholds** (`config/eval_thresholds.yaml`): the v2 baseline minus a margin of 0.05, rounded down
to 0.05. On 20 answerable items one item is 0.05, so each threshold allows at most one more failed
item than the baseline, and no miss on the 4 `none` items.

| Metric | Baseline | Threshold |
|---|---|---|
| retrieval recall@5 (hybrid + rerank) | 1.00 | ≥ 0.95 |
| right "I don't know" (abstain accuracy) | 1.00 | ≥ 0.95 |
| false "I don't know" (false-abstain rate) | 0.00 | ≤ 0.05 |
| expected source cited (source hit) | 1.00 | ≥ 0.95 |
| faithfulness | 0.99 | ≥ 0.90 |
| judge pass rate | 0.80 | ≥ 0.75 |

**The CI runs of step 20** (17.11):

| Run | What happened | Result |
|---|---|---|
| [44132869739](https://github.com/petrodyak/robodreams-ai-engineering-aws-arch-advisor/actions/runs/44132869739) | the first run: with no `.cache/` the runner embedded both chunk sets (~6,000 texts on 4 CPU cores) and built the index twice | timed out at 30 min; fixed: the gate embeds only the structure chunks, once |
| [44139898238](https://github.com/petrodyak/robodreams-ai-engineering-aws-arch-advisor/actions/runs/44139898238) | cold cache: 25 of its 27 min are embeddings; answers and verdicts all replayed | **green**, 0 new calls, all six thresholds pass |
| [44144978410](https://github.com/petrodyak/robodreams-ai-engineering-aws-arch-advisor/actions/runs/44144978410) | a throwaway branch raises `judge_pass_rate_min` to 0.85 (baseline 0.80); never merged | **red**, as intended: `eval-ci FAILED: judge_pass_rate 0.80 < 0.85`, 0 new calls |

**Determinism held.** The cache key contains the context text, and the context depends on the
ranking. Vectors computed on the Linux runner gave the same top 5 for all 24 questions as on the
Mac, so the run made 0 new calls.

**The cost of a cold run** is time, not money. GitHub caches are per branch: a branch reads its own
caches and those of `main`. That is why the workflow runs on pushes to `main` and on pull requests
only: the run on `main` after a merge saves the cache that every later pull request restores. Until
then a run embeds the chunks again (~27 min). A warm run takes about 3 minutes in all: [44149747967](https://github.com/petrodyak/robodreams-ai-engineering-aws-arch-advisor/actions/runs/44149747967), green, 0 new calls. The runs of 17–18.11 after the merges took ~13 min although the restore
reported a hit: a cancelled run had saved the models without the embeddings under `main`, and a saved key
is never saved again (F26). Patch 20.3 saves the cache only after a finished `make eval-ci`.

## 8. Error analysis

Five characteristic errors, each as expected → got → why:

1. **A question outside the corpus got an answer (F22, v1; fixed by v2).**
   - Expected: none04 "How do I configure the Horizontal Pod Autoscaler in Google Kubernetes
     Engine?" → "I don't know"; the corpus names the autoscaler only for Amazon EKS.
   - Got (v1): seven claims of EKS scaling advice, one of them saying the sources do not cover GKE,
     each with a citation. none02 (the Athena price per terabyte) got "billed by the data scanned".
   - Why: rule 5 of v1 counted a related partial answer as an answer. v2 names the two cases, a value
     no source states and a product no source covers. Right "I don't know" went 0.50 → 1.00, with no
     false "I don't know".
2. **A two-part question loses its second part at retrieval (F23, open).**
   - Expected: many04 "An AWS Glue Spark job is slow: how do I see that it lacks parallelism, and
     how can it read less data?" → idle executors, few tasks per stage, RDD partitions; and Parquet /
     ORC plus `push_down_predicate`.
   - Got: a correct and faithful first half, then file size and grouping for the second half.
   - Why: the chunk with Parquet and `push_down_predicate` (`pg-glue-reduce-data-scan#0003`) is not
     in the top 5, nor in the top 8. The scorers counted the item as retrieved, because one relevant
     chunk was. The diagnostic `context_share` (0.78 over the testset) shows it. many03 (Redshift
     tables vs Spectrum) is the same case: its distribution-style chunk enters only at k = 8.
     Improvement: in stage 3 the agent splits the question into its parts and searches each one.
3. **The correctness judge fails a true answer (F24, open).**
   - Expected: old03, the Performance Efficiency pillar's areas → the five current areas; the
     reference also notes the archived 2020 edition's four.
   - Got: the five areas, plus "restructured in October 2023 … down from eight", which is true and
     cited.
   - Why: the judge compares the answer with the reference answer, not with the sources, so a true
     detail the reference does not hold reads as a contradiction. Petro passed the answer; the
     faithfulness judge marked every claim supported. old02 (v1) failed the same way. Improvement: a
     judge v2 that also reads the cited sources. Agreement is 88 % with this error included.
4. **A deterministic scorer is stricter than the meaning (v1).**
   - Expected: sim02 (which backups can be skipped for sustainability) → the key fact "ephemeral
     storage".
   - Got: "You can exclude ephemeral data from your backups…".
   - Why: key facts match whole words. The judge and Petro both passed the answer, but the key-fact
     scorer failed it. The v2 answer happened to use the reference's wording. Improvement: key facts
     with listed variants. Until then, the gated metrics are the judge and the source hit, not key
     facts.
5. **The reference answer asks more than the question.**
   - Expected: one02, the default snapshot retention settings of S3 Tables → `MinimumSnapshots` 1,
     `MaximumSnapshotAge` 120 hours. The reference adds what then happens to expired snapshots.
   - Got: exactly the two defaults, with citations.
   - Why: the judge and Petro both failed it against the reference. The answer is complete for the
     question asked. Improvement: trim the reference to the question. The baseline keeps the item as
     it is, because thresholds are not tuned by editing the testset.

The traps worked as designed:

- old01 and old03 had the archived 2020 edition in the context and answered from the current one.
- old02 had a current document that still lists the older five security areas first in the context
  (the Serverless Lens), and still answered "seven" from the Framework.
- The `sim` traps sit next to similar sections of other pillars; all three are retrieved in the top 5.

## 9. Cost

| What | Model | Cost |
|---|---|---|
| embeddings, reranking, BM25, retrieval eval | local (fastembed) | $0 |
| one answer, k = 5, prompt v2: avg 3,863 input / 528 output tokens | Claude Haiku 5.5 | **$0.65 per 1,000 questions** |
| scoring one run of 24 items: 40 judge calls (all verdicts) | Claude Sonnet 5.5 | $0.21 (≈ $8.9 per 1,000 scored questions; eval only) |
| a CI run with a warm cache | — | $0 |
| HW 2 in total, all paid runs to step 19 | | $0.61 of the $5 budget |

The cost per 1,000 questions is the answer cost, the one a user of the system pays. The judges are
an eval cost: they run once per change, and their verdicts are cached.

## 10. Limits and what to improve next

- **Small testset.** 24 items, so one item moves a rate by 0.05 (0.25 on `none`). The thresholds
  allow exactly one more failure. A larger testset would make them less coarse.
- **Two-part questions (F23).** Retrieval returns one search's top 5. Query decomposition belongs to
  the stage-3 agent, which calls `search` once per part.
- **Correctness judge (F24).** It reads the reference, not the sources. A judge v2 could also read
  the cited sources; it would need a new calibration.
- **Key facts are exact words.** They are a diagnostic, not a gate (error 4).
- **Cross-machine determinism.** The cache key holds the context text, so a different ranking on the
  CI runner (float differences in the embeddings or the reranker) would be a cache miss and a paid
  call. Section 7 records what the first CI runs showed.
- **Heading-only chunks and PDF tables (F28).** 11 structure chunks are a heading line alone
  (`wa-operational-excellence#0172` is just "Implementation guidance"), because the merge rule
  joins a short section only to a following one under the same parent. PDF tables are flat text.
  Fixing either changes `chunks.jsonl`, so it needs new relevant-chunk labels and new paid runs.
- **The corpus is a snapshot (F25).** AWS updates its documents. `chunks.jsonl` and the manifest's
  text hashes record the version used (downloaded 14.11.2026). On 16.11.2026 AWS published a new
  edition of the Well-Architected Framework and edited one paragraph of the Cost Optimization
  pillar, so `make rag-data` now stops on 2 of the 34 hashes. `make rag` therefore runs from the
  committed chunks and reproduces every number of this report with no key (checked on a clean clone:
  0 new calls). `make rag-rebuild` downloads and ingests first. Moving to the new edition is a new
  measurement: new hashes, new relevant-chunk labels, new answer and judge runs.

## What was adapted from the lessons

Adapted (copied, changed, covered by our own tests):

- lesson 6: HTML / PDF extraction, normalisation, content hash and shingle dedup, `chunk_fixed`,
  `chunk_by_headings`, `chunk_stats`, the dataset version;
- lesson 7: the cached embeddings, the index, vector search with a filter, the retrieval evaluation;
- lesson 8: BM25 + RRF, the context builder, citation validation, the k sweep, the prompt rules and
  the CHANGELOG table, the base of the deterministic scorers.

New in this project:

- PDF section paths from the outline;
- the cross-encoder reranking (only a hint in lesson 7);
- the merge of short sections at best-practice boundaries;
- the Contextual Header;
- the filters;
- the structured, per-claim cited answer with label checks;
- the eval cache;
- the testset, the scorers, the judges and their calibration;
- the CI gate.

The table is in spec §9 "Reuse from the lessons".
