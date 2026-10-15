# Git rules for an agent-driven repository

Project-agnostic. Imported from `CLAUDE.md`. The only project-specific part is the gate
commands in §1.

---

## 0. Prime directives

1. **Committing, pushing, opening a PR and merging happen only on the user's explicit word.**
   Finishing the work, running the gates and running the review do not. Never end a report with
   "shall I commit?" — report that it is ready to commit, and wait.
2. **Evidence before assertions.** Never say "committed", "pushed", "merged" or "green" without
   the command output that proves it. A claim about git state is checked against git, not memory.
3. **Never work on the default branch.** Every change lives on its own branch, even a one-line
   docs fix.
4. **Explain before approval.** Every command sent for approval — including `git status` — is
   preceded by 1–2 sentences in the reply text: what it does, why it is needed.

---

## 1. Before the first commit: the gates

Before any commit, all verification commands pass locally (`make check` runs all three):

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

No type checker yet — deliberately deferred to keep the toolchain minimal.

- Red tree → no commit, no review, no PR. Fix first.
- Run all of them, even when an earlier one fails, so one round trip reports every problem.
- CI runs the **identical** commands on every PR. A green local run that goes red in CI is a bug
  in one of the two, and it gets fixed, not worked around.
- **Never change an expected value to turn a test green.** Fix the code, or mark the test as a
  known failure with its reason and carry it to the next unit of work. A weakened assertion must
  never enter a commit.
- Once the gates are green, run the code review straight away, without asking. Which findings to
  fix is the user's call; running the review is not.

---

## 2. Branches

- **One branch = one unit of work = one PR.** No unrelated changes ride along.
- Branch off an up-to-date default branch: sync it first, then cut.
- **Naming:** lowercase kebab-case, `<kind>-<number>-<slug>`.
  - planned unit of work: `step-42-the-regression-suite`
  - follow-up to a unit already merged: `patch-42.1-the-last-three-survivors`
  - a slug is 2–6 words from the unit's own title, not a date and not a ticket id alone
- A branch that gets split keeps the number and adds a suffix: `step-42-...-part-2`.
- **Before any destructive history operation** (reset, rebase, force-push, branch delete) create
  a snapshot branch first: `backup/<branch>-local-snapshot`. It costs one command and it is the
  only reason a lost commit is ever recoverable.
- Interactive git (`git rebase -i`, `git add -i`) does not work in an agent shell. Don't reach
  for it.
- Never rewrite or force-push history that is already pushed or already under review.

---

## 3. Commit messages

Format — subject, blank line, prose paragraph, bullets, evidence line, trailer:

```
<type>: <Unit name> — <what it is>

One short paragraph: what this changes and why, in prose. State what was
deliberately *not* changed when that is the interesting part.

- Each bullet is one real change, named by its subject, not by its file.
- A bullet says the effect, not the diff.
- A decision that was reversed mid-work is worth a bullet.

<verification evidence: test counts, run results>

Co-Authored-By: <agent> <noreply@...>
```

Rules:

- **Type prefix** from a fixed set: `feat:`, `fix:`, `test:`, `docs:`, `chore:`, `refactor:`.
  The type describes the commit's own nature — a step that adds only tests is `test:`, not `feat:`.
- The subject names the **unit of work** and reads as a title: `feat: Step 42 — the regression
  suite`. Em dash, no trailing period, ≤ 72 characters.
- **Body is mandatory** for anything but a trivial fix, wrapped at ~76 columns.
- The body carries the **evidence line** — the suite counts and any live-run result — so the
  commit itself records what was green when it was made.
- **Commit messages, code comments and repository documentation are always in English**, whatever
  language the conversation uses.
- End with the agent attribution trailer the harness requires.
- One commit per logical change; a tightly-scoped unit of work is normally one commit, plus one
  `docs:` commit when the documentation row needs the PR number (see §5).

---

## 4. Pull requests

- **Title and body in English**, always, even when the whole conversation is in another language.
  A PR is a repository artefact sitting next to commit messages and code comments — all English —
  and it outlives the chat.
- The body states, per item:
  1. the problem or the bug,
  2. its root cause,
  3. the change,
  4. the test that proves it.
- The body also lists: the verification evidence (gate output, counts), anything **deliberately
  deferred**, and every known-failing test as a named bug for the next unit of work.
- A finding that turns out to be an external data issue rather than a bug in this code is recorded
  in the PR as a known external discrepancy — never patched around silently.
- Merge through the PR (merge commit), not with a local merge into the default branch.
- End the body with the harness's generated-with attribution line.
- After opening it, read its CI status; never poll CI in a loop.

---

## 5. Documentation is part of the same PR

Never a follow-up, never "later":

- **The outcome record** (`docs/implementation-steps.md` or equivalent): files touched with line
  and test counts, decisions and their rationale, course corrections *including reversed ones*,
  bugs found and how they were fixed, what was deferred. A unit of work is not finished until its
  entry exists.
- **The handoff/status document**: the "state as of" header, the status table, the current task,
  the exact next steps, known issues.
- **The instruction that produced the work** (the prompt), committed as its own file, one per
  unit, paste-clean — prompt text only, no commentary. Revise it freely *before* the work runs;
  never rewrite it afterwards to match what was built. If the prompt was wrong, that belongs in
  the outcome record, not in a quietly corrected file.
- **A status row names the PR that delivered the work — never "on main", never "uncommitted".**
  A PR number is a fact a later merge cannot invert; both of the other two phrasings go stale on
  the next merge, in both directions. Write the row after the PR number exists, which is why a
  small `docs:` commit after `gh pr create` is normal.
- Prose must never be the authority on git state. `git log --oneline -5 origin/<default>` is.
  In documentation, prefer what is structurally true (what a milestone contains, what a rule
  forbids) over anything a merge can falsify.

---

## 6. After the merge: verify, then delete

The user saying "merged" is not proof of a merge. Before deleting any branch:

```bash
gh pr view <n> --json state,mergedAt,mergeCommit
git switch <default> && git pull
git log --oneline -5
<run tests>   # the counts must have moved
```

Only when the PR reads `MERGED`, the default branch actually contains the commit, and the suite
count has moved, delete the local and remote branch.

**Why this is a rule and not advice:** deleting the head branch of an *unmerged* PR makes the
host auto-close it. Recovery depends entirely on the commit still existing locally.

---

## 7. What never enters a commit

- Secrets, tokens, `.env` files, credentials, live API keys.
- Raw captured payloads, logs or fixtures containing personal data. Commit masked fixtures only,
  and keep the masking rule beside the test that enforces it, with a positive control (plant a
  phone number, an email, a token, an address; assert each is caught). A scanner that matches
  nothing passes everything, silently.
- Raw-capture directories are gitignored as whole directories, not file by file.
- Machine-local configuration. Split tracked vs ignored **by portability, not by directory**: a
  script that behaves identically on any clone is tracked; an absolute path or a personal
  preference is local (`*.local.json`) and gitignored.
- Generated artefacts that the build reproduces.

A tracked hook or script that the agent harness executes is tracked deliberately — but anyone who
can push can then cause it to run on a maintainer's machine. Review changes under the agent
configuration directory with that in mind.

---

## 8. Checklists

**Before committing**

- [ ] gates green, output seen
- [ ] review run, findings reported verbatim
- [ ] no weakened assertions, no expected value edited to pass
- [ ] outcome record + handoff updated
- [ ] prompt file committed
- [ ] message: type prefix, unit name, prose body, evidence line, trailer, English
- [ ] user said to commit

**Before opening a PR**

- [ ] branch named `<kind>-<n>-<slug>`, scoped to one unit
- [ ] title and body in English
- [ ] body: problem → root cause → change → proving test, per item
- [ ] deferred items and known-failing tests listed as named bugs
- [ ] CI status read after opening

**Before deleting a branch**

- [ ] `gh pr view` says `MERGED`
- [ ] default branch pulled and contains the commit
- [ ] suite count moved
- [ ] backup snapshot branch exists if anything was rewritten
