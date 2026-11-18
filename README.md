# AWS Quotas & Architecture Advisor

Course project for the AI Engineering course (RobotDreams).
Reports: HW 1 (extraction) [`REPORT.md`](REPORT.md) · HW 2 (RAG) [`REPORT-hw2.md`](REPORT-hw2.md).

**Problem.** AWS best practices and service limits are spread across thousands of
documentation pages. An architect reviewing a design has to read them by hand.
**User.** Cloud / data architects designing on AWS.
**Data.** Public AWS documentation: the *AWS General Reference* (service endpoints and
quotas, one PDF per service) for structured extraction, and AWS Prescriptive Guidance /
Well-Architected lenses for retrieval.

## Stages

| Stage | What the system does | Status |
|---|---|---|
| 1. Extraction | Extracts endpoint and quota tables from per-service PDFs; compares a paid model vs a local model against a gold set | HW 1 done — [`REPORT.md`](REPORT.md) |
| 2. RAG | Answers architecture questions with a citation to a document and section for every claim, or "I don't know" | HW 2 done — [`REPORT-hw2.md`](REPORT-hw2.md) |
| 3. Agent | Reviews a described architecture against best practices and limits | — |
| 4. Service | API with auth, logging, monitoring and per-request cost | — |

## Data layout

```
data/source/   original AWS General Reference PDF (git-ignored, ~25 MB)
data/pool/     100 per-service PDFs cut from it (git-ignored) + manifest.csv, profile.csv (committed)
data/raw/      working subset: 30 PDFs (git-ignored) + extracted *.txt + manifest.csv (committed)
data/gold/     ground-truth quotas/endpoints for 10 of the 30, JSON (committed)
data/rag/      HW 2 corpus: manifest.csv, chunks.jsonl, chunks_fixed.jsonl, ingest_manifest.json
               (committed); raw/ — the 34 downloaded PDF + HTML documents (git-ignored)
```

## Why this is not just table parsing

The source tables look structured on the page, but the pipeline never sees the page — it sees
the output of layout-mode text extraction, and that text is where the difficulty lives
(details and file examples in [`docs/data-notes.md`](docs/data-notes.md)):

- **Extraction noise.** Broken words, repeated running headers and footers, and column text
  that drifts across lines when a cell wraps.
- **Neighbour tails.** A per-service PDF is cut from one large document by page, so a file's
  first page may carry the tail of the previous service's tables. The model must extract only
  the target service and ignore the rest.
- **Non-standard layouts.** Not every service prints the standard quota table (name / default /
  adjustable / description). Some print prose, some a different table, some nothing. The model
  must recognise the layout and return an empty quota list where the standard table is absent
  ([ADR-0001](docs/adr/0001-standard-quota-tables-only.md)).
- **Irregular cells.** A single default cell may hold several regional values
  ("us-east-1: 20,000; us-east-2: 6,000"), a footnote marker, or a placeholder such as
  "Not supported", "—" or "N/A". The model keeps the printed text verbatim; derived values are
  computed by code ([ADR-0002](docs/adr/0002-model-extracts-code-derives.md)).

There are no typos and no mixed languages in this data — the source is an official reference
— so the "dirty" of the assignment is extraction noise, irregular layouts and missing
sections rather than human noise; it is the kind of noise the later stages of this project
(RAG over the same family of PDFs) will meet.

A regex or a PDF table extractor handles the clean cases and silently fails on the rest. These
failure modes are the substance of the error analysis in `REPORT.md`. The structured nature of
the source is also what makes the comparison measurable: the golden set has an objective answer
for every field, so field accuracy compares models rather than opinions.

## Reproduce the dataset

```bash
# 1. download https://docs.aws.amazon.com/pdfs/general/latest/gr/aws-general.pdf
#    into data/source/aws-general-endpoints-and-quotas.pdf
# 2. split it by bookmarks -> data/pool/
python scripts/split_pdf.py
# 3. copy the 30 selected PDFs (data/raw/manifest.csv) -> data/raw/
python scripts/select_docs.py
# 4. extract text "as is" (pypdf layout mode, only ligatures normalized) -> data/raw/*.txt
python scripts/extract_text.py
```

Setup is managed by [uv](https://docs.astral.sh/uv/): `make install` creates `.venv`
from `uv.lock`; `make data` runs steps 2–3 and `make text` runs step 4.

## Keys

Copy `.env.example` to `.env` (git-ignored) and fill it in. Stage 1 needs `ANTHROPIC_API_KEY`
(paid model) and a local Ollama (`OLLAMA_HOST`). `OPENROUTER_API_KEY` is optional: it serves
the course exercises only and no stage-1 step reads it (see `docs/adr/0004`). Stage 2 needs only
`ANTHROPIC_API_KEY`; in CI the same name is a GitHub repository secret. No key is in the code.

## Stage 1: run the extraction

Prerequisites: Python 3.12 and [uv](https://docs.astral.sh/uv/); for the local model,
[Ollama](https://ollama.com) with `ollama pull qwen2.5:7b` (≈4.7 GB; a 7B model needs ≈8 GB
of free memory). The 30 `*.txt` documents are committed, so a clean clone runs without the
PDFs.

```bash
make install                                   # .venv from uv.lock
make estimate                                  # input tokens and their cost, no paid call
make run                                       # Claude, prompt v1, temperature 0 -> results/runs/
make run MODEL=qwen2.5-7b SAMPLING=t05 GOLD=1  # local model, t05, the 10 Golden Set documents
make run PROMPT=v2 SET=holdout GOLD=1          # the 5 held-out gold documents (out of sample)
make run PROMPT=v2 PARTS=1                     # each chapter in two calls, merged by code (step 13)
make metrics                                   # every run -> results/metrics.csv
make check                                     # ruff + pytest, the pre-commit gate
```

**Cost to reproduce.** The required matrix — `claude__v1__t0`, `claude__v1__t05__gold`,
`claude__v2__t0` — costs ≈ $2.8 in API fees (measured: $1.21 + $0.27 + $1.28); the local
model costs nothing. Everything spent on HW 1, including the runs added after the lecturer's
feedback (grounded validation, the Held-out Set, parts), is ≈ $6.5 of a $10 limit; the
per-run figures are in `docs/Implementation_steps.md`, section 5.

One run = model × prompt version × sampling configuration, named
`<model>__<prompt>__<sampling>[__parts][__holdout][__gold][__val<N>]`; its records go to `results/runs/jsonl/<run_id>.jsonl`
(resumable: rerun the same command after an interruption) with a readable mirror in
`results/runs/md/`. Prompts are versioned files in `prompts/` with a `CHANGELOG.md`; sampling
configurations live in `config/sampling.yaml`; the metrics definitions are in
[`docs/stage1-data-contract.md`](docs/stage1-data-contract.md) (items 17–19). The comparison
itself is `REPORT.md`.

## Stage 1 results (HW 1)

Every document of the run for validity, latency and cost; the Golden Set documents for
recall (10 in the Working Set, 5 in the Held-out Set). Runs without `__val2` were judged by
the schema and the format checks only; `__val2` runs also require every row to be printed in
the chapter ([ADR-0005](docs/adr/0005-validation-grounded-in-the-source.md)). Full tables,
definitions and the error analysis: [`REPORT.md`](REPORT.md); the numbers come from
`results/metrics.csv` (`make metrics`).

| Run | n | ok + repaired % | latency p50 | $ per 1,000 docs | endpoints recall | quotas recall |
|---|---|---|---|---|---|---|
| `claude__v1__t0` | 30 | 100 | 36 s | 40.2 | 97.3 | 95.2 |
| `claude__v2__t0` | 30 | 100 | 44 s | 42.7 | **100** | 95.2 |
| `claude__v2__t0__val2` | 30 | 96.7 | 45 s | 50.6 | **100** | **100** |
| `claude__v2__t0__parts__val2` | 30 | **100** | **36 s** | **47.8** | **100** | **100** |
| `qwen2.5-7b__v1__t0` | 30 | 83.3 | 148 s | 0 | 78.6 | 77.1 |
| `qwen2.5-7b__v2__t0` | 30 | **86.7** | 136 s | 0 | **91.0** | **93.3** |
| `qwen2.5-7b__v2__t0__val2` | 30 | 56.7 | 221 s | 0 | 54.5 | 50.5 |
| `qwen2.5-7b__v2__t0__parts__val2` | 30 | 60.0 | 307 s | 0 | 43.2 | 26.7 |
| `claude__v1__t0__holdout__gold__val2` | 5 | 100 | 35 s | 31.3 | 91.8 | 100 |
| `claude__v2__t0__holdout__gold__val2` | 5 | 100 | 37 s | 33.2 | **100** | 100 |
| `qwen2.5-7b__v1__t0__holdout__val2` | 10 | 50.0 | 275 s | 0 | 42.1 | 16.2 |
| `qwen2.5-7b__v2__t0__holdout__val2` | 10 | 50.0 | 194 s | 0 | **55.4** | **42.9** |
| `qwen2.5-7b__v2__t0__parts__holdout__val2` | 10 | 30.0 | 233 s | 0 | 42.1 | 16.2 |

Claude Haiku 4.5 with prompt v2 recovers every Golden Set row in and out of sample and,
under grounded validation, is valid on 29 of 30 documents with nothing invented (the one
failure is a typographic apostrophe the judge did not normalise) at ≈ $51 per 1,000
documents — and on 30 of 30, 6 % cheaper and 17 % faster, when each chapter is extracted
in two parts (`__parts`, ADR-0006). The same cut makes the local model worse: given a part
without an endpoints table it invents one and runs to its output cap (finding F20). The local qwen2.5:7b is free; its 87 % validity under the first validation falls
to 57 % once every row must be printed in the chapter, it takes 5× longer and misreads
`region_name` on 10–30 % of the rows it finds. Prompt v2 helped both models on the documents
it was written from and on the held-out ones (a second endpoints table, placeholder
hostnames, tables across page breaks); temperature 0.5 changed nothing for Claude and only
hurt qwen. The production choice is Claude; the conditions under which it would flip are in
the report.

## Stage 2: RAG (HW 2)

**Problem.** An architect asks "how should we do X on AWS?" and needs an answer they can check:
every claim backed by a named section of an AWS document, and "I don't know" when the documents do
not say. The corpus is 34 public documents: the Well-Architected Framework (current and the archived
2020 edition), its six pillars, four lenses (PDF), and 22 Prescriptive Guidance, Athena, S3 Tables
and Glue pages on data lakes, Iceberg, Glue and Redshift (HTML).

```bash
make install            # .venv from uv.lock
make rag                # HW 2 from the committed chunks: retrieval eval, the answer run, score ($0)
make ask Q="How should I set the RPO for a backup strategy?"   # one cited answer (one Claude call)
make eval-ci            # what CI runs: recall@5 + cached answers and verdicts + thresholds
make check              # ruff + pytest
```

`make rag` is `retrieval-eval eval score`. It starts from the committed `data/rag/chunks.jsonl`,
the version every result was measured on, so a clean clone reproduces the report's numbers with no
key. `make rag-rebuild` (`rag-data ingest rag`) rebuilds from the source documents first; see
"Reproduce the corpus" for why it can fail. Each target also runs alone:

| Target | What it does | Cost |
|---|---|---|
| `make rag-data` | downloads the 34 documents of `data/rag/manifest.csv` into `data/rag/raw/`, checks each one's hash | $0 |
| `make ingest` | extraction with structure, cleaning, dedup, both chunk sets, `ingest_manifest.json` | $0 |
| `make retrieval-eval` | recall@5 / recall@10 / MRR of 5 search configurations → `evals/results/retrieval.json` | $0 (local models) |
| `make eval` | the 24 testset questions through RAG → `evals/results/<run_id>.jsonl` | $0 from the cache; ≈ $0.016 for a fresh run |
| `make score` | deterministic scorers + the two judges → `evals/results/<run_id>.json` | $0 from the cache; ≈ $0.21 for fresh verdicts |

The answers and the judge verdicts are cached in `evals/cache/` (committed), so a clean clone replays
them for free; only a changed prompt, model or context makes a new paid call. The first run downloads
the fastembed models (~150 MB) into `.cache/`.

**How it works.**

- **Search.** Hybrid: BM25 + vector search (`BAAI/bge-small-en-v1.5`, Qdrant in memory), fused by
  RRF, then a cross-encoder reranker, with `doc_type` and date filters.
- **Answer.** Claude Haiku 5.5 sees the top 5 chunks within a 3,000-token budget and answers in
  claims, each citing `[S1]`…. The code checks every label and drops a claim with no valid source.
- **Evals.**
  - A 24-item testset checked by hand: single-source questions, multi-source questions, similar
    documents, outdated editions, and questions not in the corpus.
  - Deterministic scorers.
  - Two Claude Sonnet 5.5 judges (correctness, faithfulness), calibrated on 17 hand-labelled answers.
  - `.github/workflows/evals.yml` runs them on every pull request and every push to `main` against
    `config/eval_thresholds.yaml`.
- **Prompts.** Versioned in `prompts/rag_v*.txt` and `prompts/judge_*.txt` with
  `prompts/CHANGELOG.md`.

**Result** (prompt v2, k = 5):

| Measure | Value |
|---|---|
| retrieval recall@5 | 1.00 |
| judge pass rate | 0.80 |
| faithfulness | 0.99 |
| right "I don't know" | 4 / 4 |
| false "I don't know" | 0 / 20 |
| cost | $0.65 per 1,000 questions |

Tables, calibration and error analysis: [`REPORT-hw2.md`](REPORT-hw2.md).

### Why this chunking

Decided in [ADR-0007](docs/adr/0007-structure-aware-chunking.md), measured in `REPORT-hw2.md` §3.

- **Chunks follow the documents' own sections.** These are the PDF outline and the HTML
  `h2`–`h4` headings (`h1` is the document title), with `REL09-BP01`-style ids as the fallback. Whole paragraphs are packed into
  a chunk. A long section is split at paragraphs, then lines, sentences and tokens. A short section
  is merged with its sibling, but never across a best-practice boundary.
- **Why sections.** The Well-Architected documents are built from best practices of a few hundred
  words each. One chunk ≈ one best practice ≈ what an answer should cite: the statement and its
  implementation guidance stay together, and every chunk has a section to name in the citation.
- **Why a target of 250–450 tokens, hard maximum 480.** The embedding model reads at most 512
  tokens, and the Contextual Header (`<title> > <Section Path>`, embedded and indexed with the
  text) takes some of them. 250 is where merging stops, not a floor: a short section with no
  sibling under the same parent stays short. The median chunk is 278 tokens, and 41 % are below
  250.
- **No overlap.** Sections are natural boundaries, and overlap would copy text across best
  practices.
- **Compared with fixed size.** The baseline is the lesson's fixed 400-token windows with 60 tokens
  of overlap, on the same text.
  - Structure chunks start mid-sentence 24 times against 137.
  - The fixed windows cut best practices in half: `wa-reliability#f0034` ends in the middle of a
    sentence, and `#f0146` cuts a best practice off before its risk level.
  - With vector search only, the windows reach a relevant passage in the top 5 slightly more often
    (0.80 vs 0.70), helped by their overlap, but rank it lower (MRR 0.58 vs 0.64).
  - With hybrid search and reranking, the structure chunks put every relevant section in the top 5.
- **Known limits.** Tables are kept as tables only from HTML: `pypdf` returns a PDF table as plain
  lines. 70 of the 2,869 chunks (text before a document's first heading) have no section, so their
  citation names only the document. 11 chunks are a heading line alone (F28).

### Reproduce the corpus

`data/rag/raw/` is not in Git, because the documents are large and AWS hosts them. Running
`make rag-data` downloads them from the URLs in `data/rag/manifest.csv` and checks each one's
`sha256` against the hash of its cleaned text. AWS regenerates its PDFs every few days, so the bytes
change while the text does not (F21). The committed `chunks.jsonl` is the version every result was
measured on (documents downloaded 14.11.2026).

**The source has moved since (F25).** On 16.11.2026 AWS published a new edition of the
Well-Architected Framework and edited one paragraph of the Cost Optimization pillar. `make rag-data`
now reports a hash mismatch for these 2 of the 34 documents and stops: the check keeps a changed
document from silently becoming a different corpus. AWS does not keep the previous edition at a
stable URL. That is why `make rag` starts from the committed chunks, and why `make rag-rebuild` is
a separate command. A rebuild on the new edition would need new hashes, new relevant-chunk labels and
a new paid answer and judge run.

## Known limits (stage 1)

- **Standard quota tables only.** Quota rows are extracted only from a table with exactly the
  columns Name, Default, Adjustable, Description; any other layout is classified as
  `non_standard` and yields no rows ([ADR-0001](docs/adr/0001-standard-quota-tables-only.md)).
- **AWS domains only.** An endpoint must be a hostname on `amazonaws.com`, `amazonaws.com.cn`,
  `api.aws` or `on.aws`; anything else fails validation
  ([ADR-0003](docs/adr/0003-format-checks-are-validation-failures.md)). A new AWS domain means a
  code change.
- **Neighbour tails are detected, not removed.** The text keeps the pieces of neighbouring
  chapters; the prompt tells the model to ignore them. Since step 11 every endpoint row must
  be printed in an endpoints table of the target chapter and every quota name in one of its
  Standard Quota Tables ([ADR-0005](docs/adr/0005-validation-grounded-in-the-source.md)), so
  a row taken from a neighbour fails validation; `region_name`, `default` and `description`
  are not grounded and are checked by the Golden Set only.
- **Text as extracted.** Broken words, split hostnames and repeated page headers are left in the
  input on purpose; the model is expected to rejoin them. Only ligatures are normalised.
- **Golden Set bias.** The reference was drafted by `claude__v1__t0` and corrected by hand
  against the PDF, so a Claude error the check did not catch counts as correct for Claude
  (`data/gold/README.md`); grounding found one such error after the fact (`038`). The held-out
  gold was drafted by a grounded Claude v2 run and checked the same way.
- **Long documents in parts, one cut tried.** `make run … PARTS=1` extracts each chapter as
  its endpoints part and its quotas part, two calls merged by code
  ([ADR-0006](docs/adr/0006-long-documents-in-parts.md)). Measured once: a win for Claude,
  a loss for the local model, which fills the field it does not see and runs to the cap
  (F20); the follow-ups (a per-part note, a per-part schema, a loop detector) are designed,
  not run.
- **Local model limits.** `qwen2.5:7b` runs with `num_ctx` 32768 and an output cap of 18432
  tokens; the largest documents fill them, and an answer cut off at the cap is `failed`
  without a repair call.
