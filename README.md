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
