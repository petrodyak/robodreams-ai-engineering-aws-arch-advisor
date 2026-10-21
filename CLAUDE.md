# CLAUDE.md — aws-arch-advisor

This file holds only what every session needs. Everything stage- or task-specific lives in `docs/`
and is read on demand — see "Read before you work on…" below.

## Who I am and what this is

I am a Data Architect (AWS lakehouse: Datalake, Iceberg, Athena/Trino, Aurora, OpenSearch, Redshift, Step Functions).
I am taking the AI Engineering course (RobotDreams, cohort 2). This repository is my end-to-end course project.

## Course project (4 stages, one system)

1. **Structured extraction** — extracting endpoint and service quota tables from the AWS General Reference PDFs (one per service). Comparison of a paid and a local model. ← **current stage (HW 1, deadline 27.10 23:59)**
2. **RAG** — search over AWS Prescriptive Guidance / Well-Architected PDFs with answers that cite their sources, plus quality tests.
3. **Agent** — multi-step tasks with tools (AWS architecture review).
4. **Service** — API, security, monitoring, cost tracking.

**The direction is fixed — do not suggest changing it.**
If a decision at the current stage affects later stages (data structure, file names, JSON format), say so explicitly.

## Constraints

- One person, 2 months, 3–4 h/week. Minimally sufficient solutions, no over-engineering.
- **Stack:** Python 3.12, `uv` (not poetry, not a hand-made pip venv), Anthropic (Claude) as the only paid model, Ollama with `qwen2.5:7b` as the local one. Do not suggest OpenAI or other providers. The `openai` SDK is a dependency only as the client for OpenRouter in course lectures and exercises; it is not a second paid provider for the HW 1 comparison (ADR-0004).
- New dependencies only via `uv add`, never by editing `pyproject.toml` by hand.
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
- Do not delete files in `data/` — only move them.

## Git — the hard rules

The full rules are in `docs/GIT_RULES.md`. **Read it before any branch, commit, PR or merge.** The ones that must never slip:

- Commit, push, PR and merge only on my explicit word. "Ready to commit" is a report, not a question.
- Never work on `main`: one branch = one unit of work = one PR. Names: `step-<n>-<slug>`, follow-ups `patch-<n>.<m>-<slug>`.
- `make check` (ruff check + ruff format --check + pytest) is green before every commit; never edit an expected value to make a test pass.
- Commit subject `<type>: <Unit name> — <what it is>` (`feat|fix|test|docs|chore|refactor`), prose body, evidence line, trailer.
- The unit's entry in `docs/Implementation_steps.md` is updated in the same PR; a status row names the PR, never "on main".
- Snapshot branch `backup/<branch>-local-snapshot` before any reset, rebase, force-push or branch delete.

## Read before you work on…

| When you… | Read first |
|---|---|
| start any step, or need the current status / next step | `docs/Implementation_steps.md` |
| write or change schema, validation, prompts or metrics code | `docs/stage1-data-contract.md` + `docs/adr/` |
| touch `data/`, the prompts or the golden set | `docs/data-notes.md` |
| need the HW 1 grading criteria, dates or required deliverables | `docs/hw1-brief.md` |
| meet a project term (Service Document, Quota Row, Neighbour Tail …) | `GLOSSARY.md` |
| do anything with git | `docs/GIT_RULES.md` |

The contract is the source of truth for stage 1 code — write code against it, do not reinvent it.

## Repository structure (target)

```
.
├── CLAUDE.md
├── GLOSSARY.md                  # project terms (Service Document, Quota Row, Neighbour Tail …)
├── .env.example                 # ANTHROPIC_API_KEY, OLLAMA_HOST, OPENROUTER_API_KEY
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
    ├── Implementation_steps.md  # HW 1 plan + execution log: status, next step, deferred findings
    ├── stage1-data-contract.md  # stage 1 data contract — check code against it
    ├── data-notes.md            # dataset, text extraction, known data quirks
    ├── hw1-brief.md             # HW 1 assignment: HW steps, criteria, dates, deliverables
    └── adr/                     # 0001 standard quota tables only, 0002 model extracts / code derives,
                                 # 0003 format checks are validation failures,
                                 # 0004 OpenRouter is a course-exercise client, not an HW 1 provider
```
