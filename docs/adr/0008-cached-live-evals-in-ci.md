---
status: accepted
date: 2026-11-09
---

# Evals run live in CI, with answers and verdicts cached in Git

The HW 2 brief requires evals in CI "on every push or pull request, with a threshold below which the
run fails". Retrieval and the deterministic scorers are free and local. Answers and judge verdicts
need Claude, which costs money (HW 2 budget $5, spec D3), takes time, and needs a key that a fork's
pull request does not have. Petro chose live evals with a cache (spec D1, 08.11).

## Decision

- Retrieval eval and deterministic scorers always run, on every CI run.
- Answers and judge verdicts come from `evals/cache/*.jsonl`, committed to Git. The cache key is the
  sha256 of the model, the effort, the system prompt text, the user message (question + context) and
  the output schema. Any change to one of them is a cache miss; nothing stale is reused silently.
- A cache miss calls Claude with the `ANTHROPIC_API_KEY` repository secret. A miss **without** a key
  (a fork PR) fails the run with "cache is stale: run make eval locally and commit evals/cache/".
- **Cost guard:** more than 30 misses in one CI run fails the run before the API is called. A changed
  prompt is evaluated locally first, and its cache is committed with the change.
- Thresholds live in `config/eval_thresholds.yaml`, set from the first full baseline run minus a
  margin. They are recorded in the HW 2 report and never edited just to make a run pass.
- CI never commits; results are uploaded as a workflow artifact.

## Considered options

- **Deterministic only in CI, LLM evals local** — free and fast, but answer quality would never be
  checked in CI, which is what the brief grades.
- **Fully live, no cache** — every push pays for ~24 answers and ~40 judge calls and needs the key on
  every run, forks included.
- **Mocked LLM in CI** — green forever, measures nothing.

## Consequences

- A PR that changes a prompt, the model or the effort carries its refreshed `evals/cache/` in the same
  PR, and its cost was estimated before the local run.
- A CI run on unchanged inputs costs $0 and still checks the thresholds against the cached answers.
- The cache grows with every prompt version; old entries are harmless and can be pruned later.
