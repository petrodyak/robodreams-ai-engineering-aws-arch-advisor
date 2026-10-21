---
status: accepted
date: 2026-10-19
---

# OpenRouter is a course-exercise client, not an HW 1 provider

The course lectures and exercises call models through OpenRouter with the `openai` SDK (the
model there at the moment is the free `nvidia/nemotron-3-ultra-550b-a55b:free`; the model is
chosen per request by its slug, not by the key). We decided to keep that code in this repository
and its single `uv` environment: `openai` is a dependency and `OPENROUTER_API_KEY` lives in `.env`
next to the other keys, but OpenRouter is **not** a provider of the HW 1 comparison. The
comparison stays exactly two providers — Anthropic (paid) and Ollama (local) — and nothing in
`src/extract/` imports `openai` or reads `OPENROUTER_API_KEY`.

## Considered options

- **A separate repository or virtual environment for the exercises.** Rejected: one more `uv`
  project to keep in sync on 3–4 h/week of study time, with nothing but one dependency and one
  key to separate.
- **OpenRouter as a third HW 1 provider** (the "third cheap model" stretch goal, no points).
  Rejected for now: HW steps 2–3 carry most of the points and are not done yet, and a third model
  multiplies the runs, the Golden Set checks and the REPORT rows without adding points. If the
  stretch is ever taken, it is a new ADR that supersedes this one, and the provider goes through
  the same `complete(system, messages, sampling)` interface as Claude and Ollama, not a side path.
- **Same repository, exercise code outside `src/` and `tests/`, key in `.env`.** Chosen: the
  "do not suggest other providers" constraint in `CLAUDE.md` keeps its meaning (it is about the
  HW 1 comparison), the key follows the one rule we already have ("keys only in `.env`"), and the
  exercises reuse the environment and the lockfile.

## Consequences

- `pyproject.toml` lists `openai` although HW 1 code never imports it; a reader of `CLAUDE.md`'s
  "do not suggest OpenAI or other providers" must not "fix" this by removing the dependency, and
  must not read it as permission to add a third provider to the comparison.
- `OPENROUTER_API_KEY` is optional: every HW 1 step and `make check` run without it.
- The free OpenRouter endpoint is rate-limited and its provider (NVIDIA) may record what is sent,
  so only public course material and public AWS documents go through it — never `.env` contents
  or anything private.
- The HW 1 budget ($5) counts Anthropic spend only; free OpenRouter models cost $0 and do not
  enter the cost table.
