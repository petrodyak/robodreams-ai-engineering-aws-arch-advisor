---
status: accepted
date: 2026-11-24
---

# Agent state lives in one SQLite database

The agent keeps several kinds of state: the messages of a session, facts about Petro, rules from his
feedback, rejected findings, session summaries, the session label map and the findings registry. The HW 3
brief asks to describe what memory stores, when, and how stale data is removed; idempotency of
`record_finding` needs a constraint, not a check-then-write. Petro decided on SQLite (spec D14, 24.11).

## Decision

- One database, `var/agent.db` (not in Git), stdlib `sqlite3`, one connection owned by the main thread,
  with the busy timeout set to `tool_timeout_s`. Eval runs use a fresh database per task.
- Tables and how each ages (spec §11):

| What | Table | Written when | How it ages |
|---|---|---|---|
| Messages of a session (question and final answer) | `messages` | after every turn | sessions older than 30 days are deleted at start-up; their episode stays |
| Sessions (id, team, start time) | `sessions` | `/new`, start-up | deleted after 30 days, with their messages and labels |
| Session label map (`[Sn]` → chunk id, spec §10) | `labels` | after every search | deleted with its session |
| Facts about Petro (`region`, `focus_pillars`, `answer_style`) | `facts` | `remember`, with a value the user typed in this turn (D24) | a new value replaces the old one; `/forget <key>` deletes one |
| Rules from feedback | `feedback_rules` | `/down <comment>` | no duplicates, at most 5, the oldest goes first |
| Rejected findings | `rejections` | `/reject <BP> <reason>` | void when the architecture hash changes |
| Session summaries | `episodes` | `/new`, `/quit` | deterministic text, at most 20 |
| Scores from `/up` and `/down` | `scores` | `/up`, `/down` | kept; mirrored to Langfuse as scores |
| Findings | `findings` (`UNIQUE(architecture_id, best_practice)`, status, architecture hash) | `record_finding` after a yes | never deleted; a repeat of a resolved finding reopens its row |

- Tool calls and results are not stored as messages; they live in the trace (ADR-0013), as in lesson 13.

## Considered options

- **JSON files per kind of state** — easy to read, but no constraint for idempotency, no transaction,
  and a race between two writes.
- **A vector store for memory** — the lesson-13 pattern for semantic recall, but the long-term memory
  here is three keys, five rules and twenty episodes: nothing to search.
- **PostgreSQL now** — the stage-4 target, but a server to run for a single-user CLI.

## Consequences

- Idempotency is a database property (`UNIQUE`), tested without a model.
- **Stage 4:** the schema moves to Aurora PostgreSQL as a driver change; the tables and the findings
  registry are formats meant to last (spec §19).
- `sqlite3`'s one-thread rule shapes the threads: the writing tools run on the main thread, and the
  read-only tools run in worker threads that never touch the database (spec §9 "Threads").
