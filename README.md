# AWS Quotas & Architecture Advisor

Course project for the AI Engineering course (RobotDreams).

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
| 2. RAG | Answers architecture questions with citations to document and page | — |
| 3. Agent | Reviews a described architecture against best practices and limits | — |
| 4. Service | API with auth, logging, monitoring and per-request cost | — |

## Data layout

```
data/source/   original AWS General Reference PDF (git-ignored, ~25 MB)
data/pool/     100 per-service PDFs cut from it (git-ignored) + manifest.csv, profile.csv (committed)
data/raw/      working subset: 30 PDFs (git-ignored) + extracted *.txt + manifest.csv (committed)
data/gold/     ground-truth quotas/endpoints for 10 of the 30, JSON (committed)
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
the course exercises only and no stage-1 step reads it (see `docs/adr/0004`).

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

## Known limits

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
