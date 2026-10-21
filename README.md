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
| 1. Extraction | Extracts endpoint and quota tables from per-service PDFs; compares a paid model vs a local model against a gold set | in progress |
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
