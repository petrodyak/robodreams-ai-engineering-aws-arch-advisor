# CLAUDE.md — aws-arch-advisor

This file holds only what every session needs. Everything stage- or task-specific lives in `docs/`
and is read on demand — see "Read before you work on…" below.

## Who I am and what this is

I am a Data Architect (AWS lakehouse: Datalake, Iceberg, Athena/Trino, Aurora, OpenSearch, Redshift, Step Functions).
I am taking the AI Engineering course (RobotDreams, cohort 2). This repository is my end-to-end course project.

## Course project (4 stages, one system)

1. **Structured extraction** — extracting endpoint and service quota tables from the AWS General Reference PDFs (one per service). Comparison of a paid and a local model. Done (HW 1, submitted 27.10).
2. **RAG** — search over AWS Prescriptive Guidance / Well-Architected PDFs with answers that cite their sources, plus quality tests. Done (HW 2, last PR #47 merged 19.11; under the lecturer's review).
3. **Agent** — multi-step tasks with tools (AWS architecture review). ← **current stage (HW 3, deadline 02.12 23:59)**
4. **Service** — API, security, monitoring, cost tracking.

**The direction is fixed — do not suggest changing it.**
If a decision at the current stage affects later stages (data structure, file names, JSON format), say so explicitly.

## Constraints

- One person, 2 months, 3–4 h/week. Minimally sufficient solutions, no over-engineering.
- **Stack:** Python 3.12, `uv` (not poetry, not a hand-made pip venv), Anthropic (Claude) as the only paid model, Ollama with `qwen2.5:7b` as the local one. Do not suggest OpenAI or other providers. The `openai` SDK is a dependency only as the client for OpenRouter in course lectures and exercises; it is not a second paid provider for the HW 1 comparison (ADR-0004).
- New dependencies only via `uv add`, never by editing `pyproject.toml` by hand.
- No private data — public data only.
- API budget — up to $10 for the whole of HW 1 (raised from $5 on 25.10 for the held-out runs after the lecturer's feedback); up to $5 for HW 2 (spec D3); up to $10 for HW 3 (spec D19). Before bulk runs, estimate the cost and state it.
- HW 2 models (spec D4): answers on `claude-haiku-5-5`, judge on `claude-sonnet-5-5`; no `temperature` / `top_p` / `top_k` is sent. HW 1 code stays on `claude-haiku-4-5`.
- HW 3 model (spec D19): the agent on `claude-haiku-5-5`, `effort` from `config/agent.yaml`; no `temperature` / `top_p` / `top_k` and no assistant prefill.
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
- The unit's entry in the current tracking file (`docs/hw3-implementation-steps.md` for HW 3) is updated in the same PR; a status row names the PR, never "on main".
- Snapshot branch `backup/<branch>-local-snapshot` before any reset, rebase, force-push or branch delete.
- **Temporary (25.11):** until I say HW 2 is checked (expected by about 28.11), nothing is merged into `main` and HW 3 step branches are stacked, each cut from the previous one (`docs/superpowers/plans/2026-11-24-hw3-agent.md`, Global Constraints). The first PR after that window removes this line.

## Read before you work on…

| When you… | Read first |
|---|---|
| start any HW 3 step, or need the current status / next step | `docs/hw3-implementation-steps.md` (frozen records: HW 2 `docs/hw2-implementation-steps.md`, HW 1 `docs/Implementation_steps.md`) |
| write or change agent or MCP code: loop, tools, faults, memory, MCP server, agent evals | `docs/superpowers/specs/2026-11-24-hw3-agent-design.md` + `docs/superpowers/plans/2026-11-24-hw3-agent.md` + ADR-0009–0013 |
| need the HW 3 grading criteria, dates or required deliverables | `docs/hw3-brief.md` |
| write or change RAG code: ingest, search, answer, evals, CI | `docs/superpowers/specs/2026-11-08-hw2-rag-design.md` + `docs/superpowers/plans/2026-11-09-hw2-rag.md` + ADR-0007/0008 |
| need the HW 2 grading criteria, dates or required deliverables | `docs/hw2-brief.md` |
| write or change stage-1 schema, validation, prompts or metrics code | `docs/stage1-data-contract.md` + `docs/adr/` |
| touch `data/`, the prompts or the golden set | `docs/data-notes.md` |
| need the HW 1 grading criteria, dates or required deliverables | `docs/hw1-brief.md` |
| meet a project term (Service Document, Quota Row, Neighbour Tail …) | `GLOSSARY.md` |
| do anything with git | `docs/GIT_RULES.md` |

The contract is the source of truth for stage 1 code, the HW 2 spec for stage 2 code, the HW 3 spec for stage 3 code — write code against them, do not reinvent them.

## Repository structure (target)

```
.
├── CLAUDE.md
├── GLOSSARY.md                  # project terms (Service Document, Quota Row, Neighbour Tail …)
├── .env.example                 # ANTHROPIC_API_KEY, OLLAMA_HOST, OPENROUTER_API_KEY, LANGFUSE_*
├── .gitignore                   # .env, .venv, data/source/, data/pool/*.pdf, data/raw/*.pdf, var/
├── README.md                    # problem, user, 4 stages, how to run, how to reproduce the data
├── REPORT.md                    # HW 1 comparison report
├── REPORT-hw2.md                # HW 2 RAG report (step 20)
├── REPORT-hw3.md                # HW 3 agent report (step 26)
├── REFLECTION.md                # HW 3 AI-first reflection (step 26)
├── Makefile                     # make run — one-command launch
├── pyproject.toml               # uv
├── main.py                      # HW 1 entry point
├── prompts/                     # versioned prompts
│   ├── CHANGELOG.md
│   ├── extract_v1.txt
│   └── extract_v2.txt
├── config/
│   ├── sampling.yaml            # temperature/top_p configurations (HW 1)
│   ├── rag.yaml                 # HW 2: models, effort, k, budget, search settings
│   ├── eval_thresholds.yaml     # HW 2: CI thresholds
│   └── agent.yaml               # HW 3: model, effort, limits, TODAY, memory settings
├── data/
│   ├── source/                  # aws-general-endpoints-and-quotas.pdf (25 MB, not in Git)
│   ├── pool/                    # ALL 100 PDFs (not in Git) + manifest.csv, profile.csv (in Git)
│   ├── raw/                     # 30 selected: *.pdf (not in Git) + *.txt + manifest.csv (in Git)
│   ├── gold/                    # 10 golden set JSON files (in Git)
│   ├── rag/                     # HW 2: manifest.csv, chunks.jsonl, chunks_fixed.jsonl, ingest_manifest.json (in Git); raw/ (not in Git)
│   └── agent/                   # HW 3: overlay (adversarial_chunks.jsonl, supersedes.json)
├── architectures/               # HW 3: registry <team>/<architecture_id>.json + architecture.schema.json
├── results/                     # model outputs: JSONL per run + metrics (in Git)
├── scripts/
│   ├── split_pdf.py             # source → pool by PDF bookmarks
│   ├── select_docs.py           # pool → raw by data/raw/manifest.csv
│   ├── extract_text.py          # raw/*.pdf → raw/*.txt
│   └── download_rag_corpus.py   # HW 2: data/rag/manifest.csv → data/rag/raw/ (sha256-checked)
├── src/
│   ├── extract/                 # stage 1: schema.py, llm/ (shared interface), pipeline.py, metrics.py
│   ├── rag/                     # stage 2: ingest/, index.py, search.py, answer.py, llm.py
│   ├── agent/                   # stage 3: loop, tools, faults, store (SQLite), memory, tracing, cli
│   ├── mcp_server/              # stage 3: MCP server (list_architectures, get_architecture, get_service_quota)
│   └── api/                     # stage 4
├── evals/                       # HW 2: testset, scorers, judge, cache/, results/, labels/; agent/ — HW 3 tasks, checks, runner, results
├── var/                         # HW 3: agent.db (SQLite state), traces/ (chat traces); not in Git
├── .github/workflows/evals.yml  # HW 2: evals on every push / PR
├── tests/
└── docs/
    ├── GIT_RULES.md             # branches, commits, PRs, gates (make check)
    ├── Implementation_steps.md  # HW 1 plan + execution log: status, next step, deferred findings
    ├── hw2-implementation-steps.md  # HW 2 plan + execution log: status, next step, findings from F21
    ├── hw2-brief.md             # HW 2 assignment: HW steps, criteria, dates, deliverables
    ├── hw3-implementation-steps.md  # HW 3 plan + execution log: status, findings from F33, AI-first log
    ├── hw3-brief.md             # HW 3 assignment: HW steps, criteria, dates, deliverables
    ├── coding-agent-memory.md   # copy of the coding agent's standing rules from Claude Code's auto-memory
    ├── superpowers/             # HW 2 and HW 3 specs (specs/) and task-level plans (plans/)
    ├── stage1-data-contract.md  # stage 1 data contract — check code against it
    ├── data-notes.md            # dataset, text extraction, known data quirks
    ├── hw1-brief.md             # HW 1 assignment: HW steps, criteria, dates, deliverables
    └── adr/                     # 0001 standard quota tables only, 0002 model extracts / code derives,
                                 # 0003 format checks are validation failures,
                                 # 0004 OpenRouter is a course-exercise client, not an HW 1 provider,
                                 # 0005 validation is grounded in the source text,
                                 # 0006 long documents in parts: code splits, code merges,
                                 # 0007 structure-aware chunking, 0008 cached live evals in CI,
                                 # 0009 MCP for owned data, 0010 side effects gated in code,
                                 # 0011 retrieved text is data, 0012 agent state in SQLite,
                                 # 0013 local trace is the record
```
