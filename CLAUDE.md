# CLAUDE.md — aws-arch-advisor

## Who I am and what this is

I am a Data Architect (AWS lakehouse: Datalake, Iceberg, Athena/Trino, Aurora, OpenSearch, Redshift, Step Functions).
I am taking the AI Engineering course (RobotDreams, cohort 2). This repository is my end-to-end course project.

## Course project (4 stages, one system)

1. **Structured extraction** — extracting endpoint and service quota tables from the AWS General Reference PDFs (one per service). Comparison of a paid and a local model. ← **current stage (HW 1)**
2. **RAG** — search over AWS Prescriptive Guidance / Well-Architected PDFs with answers that cite their sources, plus quality tests.
3. **Agent** — multi-step tasks with tools (AWS architecture review).
4. **Service** — API, security, monitoring, cost tracking.

**The direction is fixed — do not suggest changing it.**
If a decision at the current stage affects later stages (data structure, file names, JSON format), say so explicitly.

## Constraints

- One person, 2 months, 3–4 h/week. Minimally sufficient solutions, no over-engineering.
- **Stack:** Python 3.12, `uv` (not poetry, not a hand-made pip venv), Anthropic (Claude) as the only paid model, Ollama with `qwen2.5:7b` as the local one. Do not suggest OpenAI or other providers.
- No private data — public data only.
- API budget — up to $5 for the whole of HW 1. Before bulk runs, estimate the cost and state it.
- Keys — only in `.env`; only `.env.example` goes into Git.

## How to work with me

- **Language split:** talk to me in Ukrainian (technical terms in English). **Every repository artefact is written in English** — all `.md` files (docs, ADRs, GLOSSARY, README, REPORT, CHANGELOG, this file), code comments, commit messages, PRs.
- **I am learning, not just assembling code.** Explain every change: what this piece does and why it is done this way. If there are 2–3 options, name them, recommend one and explain why.
- Short summary first, then details. No unnecessary preambles.
- Before writing code for a new step, show the plan and wait for my "ok".
- Code: complete files with their repository path, not fragments without context.
- Do not invent library APIs — if unsure, check the documentation or say you are not sure.
- Do not `git commit` / `git push` without my explicit command.
- Do not delete files in `data/` — only move them.
- Git work (branches, commits, PRs, pre-commit checks) follows the rules below. The checks run via `make check`.
> Git rules (branches, commits, PRs, gates) live in the repository's `docs/GIT_RULES.md`; `CLAUDE.md` pulls them in via `@docs/GIT_RULES.md`.
 
## Repository structure (target)
 
```
.
├── CLAUDE.md
├── GLOSSARY.md                  # project terms (Service Document, Quota Row, Neighbour Tail …)
├── .env.example                 # ANTHROPIC_API_KEY, OLLAMA_HOST
├── .gitignore                   # .env, .venv, data/source/, data/pool/*.pdf, data/raw/*.pdf
├── README.md                    # problem, user, 4 stages, how to run, how to reproduce the data
├── REPORT.md                    # HW 1 comparison report
├── Makefile                     # make run — one-command launch
├── pyproject.toml               # uv
├── main.py                      # HW 1 entry point
├── prompts/                     # versioned prompts
│   ├── CHANGELOG.md
│   ├── extract_v1.txt
│   └── extract_v2.txt
├── config/
│   └── sampling.yaml            # temperature/top_p configurations
├── data/
│   ├── source/                  # aws-general-endpoints-and-quotas.pdf (25 MB, not in Git)
│   ├── pool/                    # ALL 100 PDFs (not in Git) + manifest.csv, profile.csv (in Git)
│   ├── raw/                     # 30 selected: *.pdf (not in Git) + *.txt + manifest.csv (in Git)
│   └── gold/                    # 10 golden set JSON files (in Git)
├── results/                     # model outputs: JSONL per run + metrics (in Git)
├── scripts/
│   ├── split_pdf.py             # source → pool by PDF bookmarks
│   ├── select_docs.py           # pool → raw by data/raw/manifest.csv
│   └── extract_text.py          # raw/*.pdf → raw/*.txt
├── src/
│   ├── extract/                 # stage 1: schema.py, llm/ (shared interface), pipeline.py, metrics.py
│   ├── rag/                     # stage 2
│   ├── agent/                   # stage 3
│   └── api/                     # stage 4
├── evals/
├── tests/
└── docs/
    ├── GIT_RULES.md             # branches, commits, PRs, gates (make check)
    ├── stage1-data-contract.md  # stage 1 data contract — check code against it
    └── adr/                     # 0001 standard quota tables only, 0002 model extracts / code derives
```
 
## HW 1 — "Structured Extraction Service" (30 points, deadline 27.10 23:59)

A service that extracts structured data from "dirty" texts according to a schema, compares a provider model (Claude) with a local one (qwen2.5:7b), and justifies the production choice with numbers.

### Data

- Source: 100 per-service PDFs from the AWS General Reference (`data/pool/`).
- Working set: **30 documents** in `data/raw/`, selected in three groups (the list is in `data/raw/manifest.csv`, column `group`):
  - `short` (~10): 1–2 pages, endpoints + a few quotas — the baseline for the local 7B model;
  - `medium` (~10): 3–6 pages, several quota tables — this is where prompt differences show;
  - `edge` (~10): long / FIPS / dual-stack / footnotes / no quotas — for error analysis.
- Documents of 20+ pages (EC2, S3, IAM) are not used in HW 1 — they do not fit into the local model's context.
- The "dirtiness" of our data: varying length, missing fields (no quotas, "Not supported", "—"), PDF-extraction noise (broken columns, wrapped lines, merged cells, footnotes, running headers/footers). There are no typos and no mixed languages — the README says exactly that.
- **Golden set: 10 of 30** (3–4 from each group) in `data/gold/`. Approach: the model produces a draft JSON → I check it by hand against the PDF and correct it (model-assisted, human-verified) — documented as such.
- File names and the JSON format are fixed now: `raw/*.txt` and `gold/*.json` are later used by RAG (stage 2) and by the agent (stage 3).

### Steps

1. **Schema + baseline prompt** (lesson 3) — Pydantic schema: ≥6 fields, ≥1 enum, ≥1 nested object/list. Baseline prompt, Claude via the API with structured output, retry + timeout, run all 30, save to `results/`.
2. **Second model + measurements** (lessons 2–3) — qwen2.5:7b via Ollama **through a shared interface** with Claude. Sampling (temperature, top_p) in a config, ≥2 configurations. For each model: per-field accuracy on the golden set, % valid responses, latency p50/p95, cost per 1,000 documents.
3. **Prompt versioning and validation** (lesson 4) — prompts in separate files with a version and a CHANGELOG (≥2 versions, what changed and why). Validate every response against the schema; invalid → one repair attempt → `failed`. Log the model, prompt version and sampling parameters with every result.
4. **REPORT.md** (after the Q&A on 26.10) — a "model × prompt version × sampling" table with all metrics; analysis of 3–5 characteristic errors (what was produced instead of what, and why); the final production choice in 1 paragraph + under which conditions I would change the decision.

Stretch (no points, only if time remains): a third cheap model, a regression run of prompts on the golden set, a response cache.

### Dates

| Date | What |
|---|---|
| 24.10 | Checkpoint: steps 1–2 in the repo, link posted in the `#ai-engineering-2-flood` chat (no points) |
| 26.10 | Q&A: feedback on the checkpoint |
| 27.10 23:59 | Deadline: steps 1–4 |

### Criteria (30 points)

- Step 1 — 6: schema meets the requirements (2), structured output + retry/timeout (2), all texts run and saved (2)
- Step 2 — 8: local model through the shared interface (3), sampling in config + ≥2 configurations (2), correct measurements (3)
- Step 3 — 8: ≥2 prompt versions with a changelog (3), validation + handling of invalid responses (3), logging of model/version/parameters (2)
- Step 4 — 6: metrics table (2), analysis of 3–5 errors (2), justified choice (2)
- Repo quality — 2: README, one-command launch, no keys in code

Most points are for steps 2 and 3. Not needed: UI, deployment, fine-tuning, a large dataset, perfect accuracy.

### Technical requirements

- Python 3.11+ (we use 3.12), one-command launch (`make run` or `python main.py`).
- The local model must run on an ordinary laptop.
- Submission — a single link to the GitHub repository: https://github.com/petrodyak/robodreams-ai-engineering-aws-arch-advisor

### What must be in the repository
- the service code and the schema;
- a prompts/ folder with versions and a changelog;
- data/ with the texts and the golden set;
- results/ with the model outputs;
- REPORT.md with the comparison report;
- README.md: how to run it and what needs to be installed.

## Current state and next step

### Done (15.10, data)
- `data/pool/` — all 100 PDFs + `manifest.csv` + `profile.csv` (words, endpoint rows, FIPS/dual-stack/quotas markers for each file).
- `data/raw/manifest.csv` — 30 selected: columns `file, service, group (short|medium|edge), gold (1 = in the golden set), priority, pages, words, endpoint_rows, note`. All 16 `priority=1` services are included.
- `scripts/select_docs.py` — copies the 30 PDFs from `pool/` to `raw/` according to the manifest. Run; the 30 PDFs are in `raw/`.
- `scripts/split_pdf.py` now writes to `pool/`; `.gitignore` and README updated.
- Groups were split **by words, not pages** (tables are sparse: 4 pages = 489 words, 39 pages = 4,020 words; the 0.5k–5k word range ≈ 0.7k–8k tokens — all of it fits into the qwen2.5:7b context).

### Done (15.10, project and schema design)
- `pyproject.toml` + `uv.lock` (`anthropic`, `ollama`, `pydantic`, `pypdf`, `python-dotenv`, `pyyaml`; dev: `pytest`, `ruff`), `.python-version = 3.12`. New dependencies only via `uv add`, never by hand.
- `Makefile`: `install` (uv sync), `data` (split + select), `text` (extract), `check` (ruff check + ruff format --check + pytest). There is no `run` target yet — it will come together with `main.py`.
- `scripts/extract_text.py` — `pypdf` layout mode, 30 `.txt` files in `data/raw/`. The text is not cleaned; the only change is ligatures `ﬀ ﬁ ﬂ ﬃ ﬄ` → plain letters (decision made). Pages are separated by `\f`.
- Step 0 Git: `docs/GIT_RULES.md`, pre-commit gates via `make check`, PR #1 merged.
- Design interview → `GLOSSARY.md`, `docs/stage1-data-contract.md` (10 contract items), ADR-0001 and ADR-0002; 16.10 — contract amendments (items 6, 9, 14, 16) and ADR-0003 after reconciling with the grill branch (not to be merged). **The stage 1 schema is designed — write the code against the contract, do not reinvent it:**
  - `ServiceDocument`: `schema_version: Literal["1"]`, `service`, `quota_table_format: standard | non_standard | none`, `endpoints: list[EndpointRow]`, `quotas: list[QuotaRow]`.
  - `EndpointRow`: `region_name, region_code, endpoint, protocol (HTTPS|HTTP|HTTP and HTTPS)` — printed columns only; `endpoint_type (fips|dual_stack|fips_dual_stack|ipv4|global)` — a computed field from the hostname, not counted in accuracy metrics.
  - `QuotaRow`: `name, default: str (as printed), adjustable: bool, description` — only from a Standard Quota Table (`Name | Default | Adjustable | Description`); other formats → `quotas: []` + `quota_table_format = non_standard` (ADR-0001).
  - The model extracts only what is printed; parsing `default` into a number/scope is done in code, later (ADR-0002). Multi-region `default` → `"us-east-1: 20,000; us-east-2: 6,000"`.
  - Validator on every `str`: `" ".join(s.split())`. Validation failure → repair: `service` does not match the manifest (Neighbour Tail detector); `region_code` regex; `endpoint` — a hostname without spaces on an AWS domain; `quotas` non-empty while `quota_table_format != standard` (ADR-0003).
  - The paid model is `claude-haiku-4-5`: the new Claude generation does not accept `temperature`, and we need `t0`/`t05` (contract item 14).
  - Golden set: draft from the `claude__v1__t0` run → `data/gold/<name>.json` → manual correction against the PDF.

### Known data quirks (decisions made)
- **Neighbouring services' tails are left as is.** Splitting by bookmarks is page-based, so a file's first page contains the end of the previous service (e.g. `006-aurora-dsql` has a chunk of Aurora quotas), and a service's own quotas can leak into the next file. The prompt must extract only the target service; the golden set contains only the target service's data.
- Missing fields occur naturally: no quotas table (`007`, `042`, `047`), "N/A" (`047`, `048`), global services with 3 endpoint rows (`010`, `074`).
- The PDF text is dirty: broken words (`ap-\nsoutheast-4`), running headers/footers "AWS General Reference … Version 1.0 NNN". Ligatures are already normalised in the `.txt` files.
- `093-aws-services.pdf` is not a service (a summary list) — excluded.

### Next step (Claude Code)
1. ✅ (step 2, branch `step-2-schema`) `src/extract/schema.py` — Pydantic schema per `docs/stage1-data-contract.md` (fields above) + unit tests for the validators (whitespace, `endpoint_type`, the `service` check, format/consistency checks from ADR-0003; the test structure can be taken from the `step-0-1-grill-me-1` branch). The field plan already exists — show only the file/test plan and wait for "ok".
2. `src/extract/llm/` — a shared interface for Claude and Ollama (one function `extract(text, service, prompt, sampling) -> ServiceDocument | failed`), Claude implementation first, with structured output, retry + timeout.
3. `prompts/extract_v1.txt` + `prompts/CHANGELOG.md`, `config/sampling.yaml` (first configuration `t0`), `main.py` + the `make run` target; estimate the cost, run all 30 → `results/claude__v1__t0.jsonl` with logging of model/prompt version/sampling.
4. Golden set: copy the 10 `gold=1` files from the results of item 3 into `data/gold/` → I check them by hand against the PDF.
5. Then HW step 2: Ollama implementation of the same interface, the second sampling configuration, `metrics.py`.
