# HW 1 brief — "Structured Extraction Service"

30 points, deadline **27.10 23:59**. The course assignment as given, kept here so that `CLAUDE.md`
holds only what every session needs. The working plan that implements it is
[`Implementation_steps.md`](Implementation_steps.md); the dataset is described in
[`data-notes.md`](data-notes.md).

> The four **HW steps** below are grading units. They are not the same as the numbered
> **implementation steps** (0–9) in `Implementation_steps.md`, whose overview table maps one to the other.

## Goal

A service that extracts structured data from "dirty" texts according to a schema, compares a provider
model (Claude) with a local one (qwen2.5:7b), and justifies the production choice with numbers.

## HW steps

1. **Schema + baseline prompt** (lesson 3) — Pydantic schema: ≥6 fields, ≥1 enum, ≥1 nested
   object/list. Baseline prompt, Claude via the API with structured output, retry + timeout, run all
   30, save to `results/`.
2. **Second model + measurements** (lessons 2–3) — qwen2.5:7b via Ollama **through a shared
   interface** with Claude. Sampling (temperature, top_p) in a config, ≥2 configurations. For each
   model: per-field accuracy on the golden set, % valid responses, latency p50/p95, cost per 1,000
   documents.
3. **Prompt versioning and validation** (lesson 4) — prompts in separate files with a version and a
   CHANGELOG (≥2 versions, what changed and why). Validate every response against the schema; invalid →
   one repair attempt → `failed`. Log the model, prompt version and sampling parameters with every
   result.
4. **REPORT.md** (after the Q&A on 26.10) — a "model × prompt version × sampling" table with all
   metrics; analysis of 3–5 characteristic errors (what was produced instead of what, and why); the
   final production choice in 1 paragraph + under which conditions I would change the decision.

Stretch (no points, only if time remains): a third cheap model, a regression run of prompts on the
golden set, a response cache.

## Dates

| Date | What |
|---|---|
| 24.10 | Checkpoint: HW steps 1–2 in the repo, link posted in the `#ai-engineering-2-flood` chat (no points) |
| 26.10 | Q&A: feedback on the checkpoint |
| 27.10 23:59 | Deadline: HW steps 1–4 |

## Criteria (30 points)

- HW step 1 — 6: schema meets the requirements (2), structured output + retry/timeout (2), all texts
  run and saved (2)
- HW step 2 — 8: local model through the shared interface (3), sampling in config + ≥2 configurations
  (2), correct measurements (3)
- HW step 3 — 8: ≥2 prompt versions with a changelog (3), validation + handling of invalid responses
  (3), logging of model/version/parameters (2)
- HW step 4 — 6: metrics table (2), analysis of 3–5 errors (2), justified choice (2)
- Repo quality — 2: README, one-command launch, no keys in code

Most points are for HW steps 2 and 3. Not needed: UI, deployment, fine-tuning, a large dataset,
perfect accuracy.

## Technical requirements

- Python 3.11+ (we use 3.12), one-command launch (`make run` or `python main.py`).
- The local model must run on an ordinary laptop.
- Submission — a single link to the GitHub repository:
  https://github.com/petrodyak/robodreams-ai-engineering-aws-arch-advisor

## What must be in the repository

- the service code and the schema;
- a `prompts/` folder with versions and a changelog;
- `data/` with the texts and the golden set;
- `results/` with the model outputs;
- `REPORT.md` with the comparison report;
- `README.md`: how to run it and what needs to be installed.
