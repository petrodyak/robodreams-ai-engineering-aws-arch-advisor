# Coding agent memory — copy of the standing rules

Copied on **25.11** (step 21) from Claude Code's auto-memory for this project, which lives outside the
repository (`~/.claude/projects/<project>/memory/`). The HW 3 brief wants the instructions the coding
agent worked with in the repository; most of them are in [`CLAUDE.md`](../CLAUDE.md) and
[`GIT_RULES.md`](GIT_RULES.md), and these are the rest. Step 26 refreshes the copy, and `REFLECTION.md`
names this file.

Each rule is one memory file there. The text is carried over lightly edited: file pointers and dates
brought up to date (rules 3, 6), notes that were only about the memory itself left out (rules 4, 5), and
machine-local paths left out. "Why" is the reason Petro gave, "How to apply" is what the agent does.

## 1. Docs in English, chat in Ukrainian (feedback, 17.10)

Every `.md` file in the repo (CLAUDE.md, docs/, ADRs, GLOSSARY, README, REPORT, prompts/CHANGELOG, the
implementation-steps files, decision files from rule 2) is written in English, when creating new ones and
when updating existing ones. Communication with Petro in chat stays in Ukrainian (technical terms in
English).

- **Why:** Petro asked for this on 17.10 after all MD files were translated to English; repo artefacts
  are submitted on GitHub and outlive the chat (also consistent with `docs/GIT_RULES.md` §3–4).
- **How to apply:** never write Ukrainian text into a `.md` file, even when quoting a decision made in a
  Ukrainian conversation: translate it. Replies to Petro remain in Ukrainian.

## 2. Grill decisions go to `docs/` (feedback, 15.10)

After every grill session (the `grilling` skill), always save the agreed decisions to a file in `docs/`,
without being asked. Choose the file by content: extend an existing doc when the topic is already covered
there (e.g. schema changes → `docs/schema-decisions.md`), create a new `docs/<topic>-decisions.md` for a
new topic. Say in the reply which file was chosen and why.

- **Why:** Petro is learning and wants a durable record of design decisions (with reasons) in the repo,
  not only in chat; decisions here feed later course stages.
- **How to apply:** at the end of a grill (once Petro confirms shared understanding), write or update the
  docs file before starting any code. Format as in `docs/schema-decisions.md`: facts from data →
  decisions table (#, question, decision, why) → short summary → open questions. (25.11:
  `docs/schema-decisions.md` is no longer in the tree; the format stays as described.)

## 3. Cite decision and finding ids with their full text (feedback, 09.11)

Whenever a decision id (D1, D2, …) or a deferred-finding id (F1, F2, …) is mentioned, quote its full text
as written in the source file and give a clickable `file:line` link to it. D1–D9 live in the HW 2 spec
(§ "Decisions"), D10+ in the HW 3 spec (§2); F1–F20 in `docs/Implementation_steps.md`, F21–F32 in
`docs/hw2-implementation-steps.md`, F33+ in `docs/hw3-implementation-steps.md`. Grep for the current line
number every time: lines shift as files are edited.

- **Why:** Petro (09.11) could not tell what a bare "D2" referred to; the id alone gives no context, and
  he wants to find it by search in the project.
- **How to apply:** applies to any similar short id too (steps, ADRs): name + full text + link, never a
  bare code.

## 4. The term "Well-Architected" (feedback, 09.11)

The short form for the AWS Well-Architected Framework (and its pillars and lenses) is
**"Well-Architected"**, in chat and in every artefact. Never "WA" (unclear) and never "AWS WAF" (that is
the Web Application Firewall service, which the HW 2 corpus itself describes).

- **Why:** chosen by Petro on 09.11 for the HW 2 spec; an ambiguous short form would also confuse BM25
  and testset questions.
- **How to apply:** first use in a document: "AWS Well-Architected Framework (Well-Architected below)".
  The term is in `GLOSSARY.md` since step 14.

## 5. Paid runs under $1 go without asking (feedback, 16.11)

A paid API run whose estimate is under $1 starts without asking Petro (said 16.11, during the HW 2 step 18
sweep). The estimate is still made (`count_tokens`) and stated in the report, as `CLAUDE.md` asks; only
the wait for "ok" is dropped. At $1 or more, ask first as before.

- **Why:** waiting for an "ok" on a few-cent run (e.g. the $0.05 k sweep) only slows him down.
- **How to apply:** estimate → if under $1, run and report the estimate next to the real cost; if $1 or
  more, show the estimate and wait. The HW budgets and the cost guards still apply.

## 6. A project plan after HW 2 (project, 23.10; postponed 09.11)

After HW 2, Petro wants `docs/project-plan.md`: a lean (1–2 screens), English, whole-project plan for
stages 1–4. Take: per stage "What we build → Output → Done when"; how the stage-1 quota tables feed a
stage-3 agent tool; the course calendar (dates verified); a few measurable targets; the demo scenario,
risks, open questions. Skip: big requirement tables, a detailed stage-1 section (link
`docs/Implementation_steps.md`), the repository structure, out-of-scope ideas. Placement: a link from the
README and one row in `CLAUDE.md` "Read before you work on…".

- **Why:** stages 2–4 were one line each, so stage-1 decisions that affect later stages had nothing to be
  checked against. Postponed so that it did not compete with HW 1 points, and again by HW 2 spec decision
  D7 ("written after HW 2, not inside it").
- **How to apply:** in any session after 20.11, if it is not done yet, remind Petro and show the section
  outline first; write nothing until his "ok". The memory is deleted once the file is merged.
