---
status: accepted
date: 2026-11-24
---

# Side effects are gated in code, with an idempotency key and a finding status

The HW 3 brief requires that a tool which changes something outside the conversation runs only after a
human confirms, that the check is in the code and not in the prompt, that a missing required parameter
makes the agent ask instead of guess, and that a repeated request or a dropped connection does not
create a duplicate. The course lists "a side effect that only a line in the prompt guards" among the
mistakes that cost points. The agent's one side effect is `record_finding`, which writes a finding to the
findings registry in SQLite. Petro decided the key and the status (spec D13, 24.11; amended 25.11).

## Decision

- **Confirmation in code.** `guard(name, args, autonomy, confirm)` sits between the model and
  `record_finding` (lesson 11). Autonomy is `read_only` (never writes), `confirm` (the default: writes
  only if `confirm()` returns True) or `auto` (tests only). In the chat `confirm()` asks `[y/N]`; in the
  evals each task scripts the answer; the default is no. A refusal returns `NOT DONE: the person did not
  confirm; do not retry`.
- **Only on request** (D23). The model calls `record_finding` only when the user asks to record; a
  review alone records nothing.
- **Order of checks:** arguments → a rejection for this architecture version → a row that already exists
  (`already open since <date>`, no question to the person) → `confirm()` → write. A repeat therefore
  never asks twice.
- **Missing parameters.** Under `strict: true` a required argument cannot be left out, so `severity` and
  `best_practice` may be `null`; the code answers `null` with an error that tells the model to ask the
  user (or to search for the best practice) and writes nothing.
- **Grounded arguments.** `best_practice` matches `^[A-Z]{3,7}\d{2}-BP\d{2}$` and is one of the ids that
  occur in the corpus; the pillar is derived from the id, not sent by the model (ADR-0002); `source` is a
  label of this session's searches, not from a superseded edition and not from the adversarial overlay.
- **Idempotency.** The key is `architecture_id + best_practice`, held by a `UNIQUE` constraint. A finding
  has a status (`open` / `resolved`) and the hash of the architecture version it was found on; the same
  key on a `resolved` finding reopens that row instead of creating a new one.

## Considered options

- **Confirmation in the prompt** ("ask the user before recording") — the mistake the brief names; an
  injected document or a model slip would write.
- **A request id as the idempotency key** — protects against a retried HTTP call, but not against the
  same finding recorded in two sessions, which is the duplicate Petro actually cares about.
- **A new row per occurrence, with history** — keeps every event, but the registry would show one
  problem many times; one row per problem with `opened_at`, `resolved_at` and `reopened_count` keeps the
  history in one place.

## Consequences

- A test calls `record_finding` through the guard with `confirm → False`, without any model, and checks
  that the table is empty: the protection is a property of the code.
- A gap supported only by a source without a best-practice id (the Data Analytics Lens, Prescriptive
  Guidance, the service guides) is reported in the answer but cannot be recorded; README states the
  limit.
- `remember`, the other write the model can start, follows the same principle (D24): it saves only a
  value the user typed in the current turn.
