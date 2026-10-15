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
data/raw/      100 per-service PDFs cut from it (git-ignored) + manifest.csv (committed)
data/gold/     ground-truth quotas/endpoints per service, JSON (committed)
```

## Reproduce the dataset

```bash
# 1. download https://docs.aws.amazon.com/pdfs/general/latest/gr/aws-general.pdf
#    into data/source/aws-general-endpoints-and-quotas.pdf
# 2. split it by bookmarks
python scripts/split_pdf.py
```
