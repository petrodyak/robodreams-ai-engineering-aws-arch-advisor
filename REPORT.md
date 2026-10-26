# HW 1 — Structured extraction: Claude Haiku 4.5 vs qwen2.5:7b

**Snapshot of 2026-10-26** (second edition; the first, of 24.10, preceded the lecturer's
feedback). Numbers taken from `results/metrics.csv`, which `make metrics` rebuilds from the
fourteen run files in `results/runs/jsonl/` of `patch-12.2-val2-and-holdout-runs` (code as
merged in PR #26, `900b1d9`): the eight runs of 24.10 (`claude__v1__t0`, `claude__v2__t0`,
`claude__v1__t05__gold`, `qwen2.5-7b__v1__t0`, `qwen2.5-7b__v2__t0`, `qwen2.5-7b__v2__t05`,
`qwen2.5-7b__v1__t0__gold`, `qwen2.5-7b__v1__t05__gold`), the two re-runs under grounded
validation (`claude__v2__t0__val2`, `qwen2.5-7b__v2__t0__val2`) and the four Held-out Set runs
(`claude__v1__t0__holdout__gold__val2`, `claude__v2__t0__holdout__gold__val2`,
`qwen2.5-7b__v1__t0__holdout__val2`, `qwen2.5-7b__v2__t0__holdout__val2`). The Golden Set
file for `038` was corrected on 25.10 (finding F18), so the 24.10 runs' accuracy was
recomputed against the corrected reference. Later code changes do not edit this report.

### The lecturer's remarks of 24.10 — how each was closed

The first edition was reviewed with four remarks. One row per remark: the decision taken,
the steps and PRs that carried it, and where in this report or the repository the evidence
is. The detailed logs (goal, files, what was tried, what was rejected and why) are the
step entries in `docs/Implementation_steps.md` §4.

| # | Remark | Decision | Steps / PRs | Evidence |
|---|---|---|---|---|
| 1 | Validation should check the data against the **source**, not what the model copied from the prompt | A grounding layer after the schema, by code and the same for both models: G1 every `endpoint` is printed in the Endpoint column of an endpoints table of the Target Service's chapter; G2 every quota `name` is a Name cell of a Standard Quota Table of the chapter; G3 `quota_table_format` follows the printed header. A violation is a validation failure like a schema error and goes into the one repair call. Readers calibrated on the real data: every gold file passes, every flagged Claude row confirmed by hand; three reader faults fixed on the way, and one gold file found wrong (F18). `validation_version` in every record, `__val2` in the run id, so old and new judgements never mix | Step 11 — PR #23, PR #24 (gold `038`); re-runs PR #27 | ADR-0005; contract items 7, 9, 11, 12, 16; `src/extract/grounding.py`, `tests/test_grounding.py`; §3.3 of this report (validation 1 vs 2 on the same documents), error 2, F19 |
| 2 | Tie every run to the **exact prompt and schema version** | Two fields in every Run Record: `prompt_sha` (sha256 of the prompt file bytes) and `schema_sha` (sha256 of the JSON Schema sent to the model), 12 hex chars, required. The eight earlier runs backfilled from git at the commit each was made. Two guards: `run()` refuses to resume a run file made with another prompt or schema (`ProvenanceMismatch`), and `make metrics` refuses a file whose records mix two pairs. A schema file per prompt version was rejected on purpose: the remark asks for a binding, not an isolation (one schema for all runs is contract item 1). Result in the data: F17 (`qwen2.5-7b__v1__t0` = v1 text + enum schema) is visible in `metrics.csv` and tested | Step 10 — PR #21, PR #22 (guard + property test) | Contract item 12; `prompts/CHANGELOG.md` version → sha table; `scripts/backfill_provenance.py`; `tests/test_provenance.py`; `prompt_sha` / `schema_sha` columns of `results/metrics.csv` and of §3 |
| 3 | Process **long documents in parts** | **Not done.** Decision: not before the deadline — chunking changes what the model returns and what the code merges (ADR-0002 would need a new clause), and a day-old pipeline change would have had no time to be measured. The output-cap failures stay as error 4 (3 qwen documents, 0 Claude with the raised `max_tokens`); a design (split the chapter by its tables, one call per part, merge by code, validate the whole) is written and is the first step after HW 1 | — | §4 error 4, §6; `docs/Implementation_steps.md` deferred findings |
| 4 | Test prompt improvements on **unseen data** | A Held-out Set: 10 pool documents outside the Working Set, selected by a fixed rule (seed 20261025), 6 `medium` + 4 `edge` (the pool had no `short` document left), gold for 5 drafted by a grounded Claude v2 run and checked against the PDF; `DocumentSet` in the code, `__holdout` scope in the run id, every reader of `data/raw` / `data/gold` takes the set. v1 and v2 run on it for both models — Claude on the five gold documents (budget raised $5 → $10 for this), qwen on all ten | Step 12 — PR #25, PR #26 (gold); runs PR #27 | Contract item 20; `data/holdout/`, `data/holdout/gold/README.md`; `tests/test_holdout.py`; §3.4 of this report (out of sample v1 → v2), §6 |

## 1. Summary

Both models turn the layout-mode text of an AWS General Reference chapter into a Service
Document that passes the schema most of the time; once validation asks whether every row is
actually printed in the chapter, only the paid model stays reliable. **Under grounded
validation, Claude Haiku 4.5 with prompt v2 is valid on 29/30 documents (25 first try, 4 after
the repair call, 1 failed) and recovers 100 % of the Golden Set endpoint rows and 100 % of the
quota rows with nothing invented, at $50.6 per 1,000 documents and 45 s per document.** The
local **qwen2.5:7b with prompt v2 is valid on 17/30**: 13 documents fail because a hostname,
a quota name or the table format is not what the chapter prints (7), the answer does not fit
the output cap (3) or a hostname is malformed (3); on the documents it does finish, precision
is 99.5 %. The same validation that passed 26/30 of its answers before now passes 17/30 — the
other nine were plausible, not true. **Prompt v2 generalises:** on five held-out documents
never seen while writing it, Claude's endpoint recall goes from 91.8 % (v1, a second table
missed in `068`) to 100 % (v2), the same mechanism as on the Working Set; qwen's validity on
the ten held-out documents goes from 30 to 50 % first try and its endpoint recall from 42 to
55 %. Temperature 0.5 changed nothing for Claude and only hurt qwen. **For production,
Claude**; qwen is the choice only when the data cannot leave the machine, and then with a
review of the invalid half.

## 2. What was compared

- **Task.** One chapter of the *AWS General Reference* ("<service> endpoints and quotas", text
  extracted from the per-service PDF with pypdf in layout mode, ligatures normalised, nothing
  else cleaned) → one `ServiceDocument`: `service`, `quota_table_format` (`standard |
  non_standard | none`), `endpoints[]` (`region_name`, `region_code`, `endpoint`, `protocol`),
  `quotas[]` (`name`, `default`, `adjustable`, `description`). Rules in
  `docs/stage1-data-contract.md`; the README section "Why this is not just table parsing"
  says where the difficulty lives.
- **Data.** 30 documents (`data/raw/`), 10 `short` / 10 `medium` / 10 `edge` by word count.
  **Golden Set:** 10 of them (6 / 3 / 1), drafted by `claude__v1__t0` and corrected by hand
  against the PDF (`data/gold/README.md`).
- **Models.** `claude-haiku-4-5` with structured outputs (the newer Claude generation rejects a
  non-default temperature), and `qwen2.5:7b` through Ollama with `format` = the same JSON
  Schema, `num_ctx` 32768, output cap `num_predict` 18432. One pipeline for both: validate
  → at most one repair call carrying the error text → `ok | repaired | failed`.
- **Prompts.** v1 (baseline) and v2 (`prompts/CHANGELOG.md`): three targeted rule changes,
  each tied to a v1 error (section 5), and `schema_version` as an enum instead of a
  `Literal` — see F15 below.
- **Sampling.** `t0` (temperature 0) and `t05` (0.5); `top_p` unset for both so that the two
  providers get identical knobs.
- **Metrics** (contract items 17–19). *Validity:* `% ok` on the first answer and `% ok +
  repaired`, denominator = the documents of the run's scope from the manifest (30, or the 10
  Golden Set documents for a `__gold` run); a document without a record counts as failed.
  *Accuracy, Golden Set only:* endpoint rows matched by `endpoint`, quota rows by `name`, as
  precision / recall of the key sets, then per-field accuracy on matched rows
  (`description` case-insensitive, everything else exact); a gold document without an output
  is an empty extraction — every gold row missing. Totals are micro-averages over rows.
  *Latency:* wall clock per document, retries and repair included, p50 / p95. *Cost:* Claude
  from `usage` at list prices ($1 / $5 per Mtok); qwen $0, with the run's wall clock as the
  compute note.
- **Which schema which run saw (finding F17).** The `schema_version` fix (enum) landed with
  prompt v2 but lives in `schema.py`, which every run shares. The three `__gold` v1 runs of
  23.10 saw the old `Literal` schema; the 30-document `qwen2.5-7b__v1__t0` of 24.10 already
  saw the enum. So the 30-document v1 → v2 comparison isolates the rule text, and the effect
  of the schema fix is read from the `__gold` v1 runs. Since step 10 every record pins this:
  `prompt_sha` and `schema_sha` in the run files and in `results/metrics.csv` (two schemas,
  `e707d2e9616f` and `d4010de95c65`; two prompts, `8a0da697aa92` and `a3adf0379524`; the
  table in `prompts/CHANGELOG.md`).

## 3. Results

Full table with per-group rows and per-field accuracy: `results/metrics.csv`. Tables 3.1 and
3.2 are the 24.10 runs under the first validation (schema + format checks); 3.3 shows what
grounded validation changed on the same documents; 3.4 is the Held-out Set.

#### 3.1 Validity, latency and cost — every document of the run (`n`), validation "1"

Columns:

- **Run** — `<model>__<prompt version>__<sampling>`; `__gold` when only the Golden Set was run.
- **n** — documents in the run's scope: the denominator of every percentage. A document
  without a record would count as failed.
- **ok %** — the first answer was valid against the schema and the format checks.
- **ok + repaired %** — valid on the first answer, or after the one repair call that carries
  the validation error back to the model (contract item 16).
- **failed** — still invalid after the repair call, or cut off at the output cap (no repair
  call then).
- **latency p50 / p95** — wall-clock seconds per document, median and 95th percentile;
  transport retries and the repair call included.
- **$ per 1,000 docs** — the run's tokens at list prices ($1 / $5 per million input / output
  tokens for Haiku 4.5), scaled to 1,000 documents; $0 for the local model.
- **wall clock** — the sum of the per-document times; the documents ran one after another,
  so this is how long the run took.

| Run | n | ok % | ok + repaired % | failed | latency p50 / p95 | $ per 1,000 docs | wall clock |
|---|---|---|---|---|---|---|---|
| `claude__v1__t0` | 30 | 100 | 100 | 0 | 36 / 86 s | 40.2 | 21 min |
| `claude__v2__t0` | 30 | 96.7 | **100** | 0 | 44 / 89 s | 42.7 | 23 min |
| `claude__v1__t05__gold` | 10 | 100 | 100 | 0 | 30 / 56 s | 27.3 | 5 min |
| `qwen2.5-7b__v1__t0` | 30 | 70.0 | 83.3 | 5 | 148 / 548 s | 0 | 110 min |
| `qwen2.5-7b__v2__t0` | 30 | **86.7** | 86.7 | 4 | 136 / 565 s | 0 | 99 min |
| `qwen2.5-7b__v2__t05` | 30 | 70.0 | 73.3 | 8 | 154 / 553 s | 0 | 113 min |
| `qwen2.5-7b__v1__t0__gold` † | 10 | 0 | 90.0 | 1 | 198 / 543 s | 0 | 40 min |
| `qwen2.5-7b__v1__t05__gold` † | 10 | 0 | 70.0 | 3 | 195 / 438 s | 0 | 37 min |

#### 3.2 Accuracy — the 10 Golden Set documents only (752 endpoint rows, 105 quota rows), validation "1"

Columns:

- **endpoints precision / recall** — rows matched by hostname. Precision: of the endpoint
  rows the model returned, the share that exist in the gold file. Recall: of the gold rows,
  the share the model found.
- **quotas precision / recall** — the same for quota rows, matched by `name`.
- **`quota_table_format`** — documents (of 10) where the model's `standard | non_standard |
  none` equals the gold value.
- **`region_name`**, **`default`** — share of matched rows where that field equals the gold
  value exactly (whitespace collapsed).
- A gold document the run failed on counts as an empty extraction: nothing returned, every
  gold row missing.

| Run | endpoints precision / recall | quotas precision / recall | `quota_table_format` | `region_name` | `default` |
|---|---|---|---|---|---|
| `claude__v1__t0` | 99.6 / 97.3 | 98.0 / 95.2 | 9/10 | 100 | 100 |
| `claude__v2__t0` | 99.6 / **100** | 98.0 / 95.2 | 9/10 | 100 | 99.0 |
| `claude__v1__t05__gold` | 99.6 / 97.3 | 98.0 / 95.2 | 9/10 | 100 | 100 |
| `qwen2.5-7b__v1__t0` | 97.2 / 78.6 | 79.4 / 77.1 | 8/10 | 63.1 | 94.7 |
| `qwen2.5-7b__v2__t0` | 97.7 / **91.0** | 73.7 / **93.3** | **9/10** | 70.3 | 93.5 |
| `qwen2.5-7b__v2__t05` | 97.2 / 79.8 | 70.4 / 77.1 | 8/10 | 66.0 | 93.4 |
| `qwen2.5-7b__v1__t0__gold` † | 96.8 / 75.8 | 64.8 / 77.1 | 8/10 | 65.4 | 94.7 |
| `qwen2.5-7b__v1__t05__gold` † | 93.0 / 46.3 | 87.8 / 34.3 | 6/10 | 86.5 | 88.9 |

Recomputed against the Golden Set as corrected on 25.10 (F18: `038` is `standard` with the
five rows of its one Standard Quota Table): Claude's quota recall is 95.2, not 100, because
every Claude run called `038` `non_standard` and returned no quotas; qwen's quota precision
rose a little because five of its `038` rows are now in the reference.

The three `__gold` runs cover the same 10 documents as the accuracy table, so for them the
validity and accuracy denominators coincide.

† old `Literal` schema (F15 / F17): every first answer failed on `schema_version: "1.0"`.

The other scored fields, `claude__v2__t0` vs `qwen2.5-7b__v2__t0`: `region_code` 100 / 98.1,
`protocol` 100 / 95.6, `adjustable` 100 / 100, `description` 100 / 96.8.

#### 3.3 The same runs under grounded validation — Working Set, validation "2"

The re-runs `claude__v2__t0__val2` and `qwen2.5-7b__v2__t0__val2` repeat the v2 / t0
configuration with validation "2" (ADR-0005): after the schema, every endpoint must be
printed in an endpoints table of the chapter, every quota name in a Standard Quota Table,
and `quota_table_format` must follow the printed header; a violation goes into the one repair
call like a schema error. Same prompt bytes, same schema bytes (the `prompt_sha` /
`schema_sha` columns of the CSV), only the judge changed.

| Run | n | ok % | ok + repaired % | failed | first-answer failures by cause | p50 / p95 | $ per 1,000 |
|---|---|---|---|---|---|---|---|
| `claude__v2__t0` (val. 1) | 30 | 96.7 | 100 | 0 | 1 format | 44 / 89 s | 42.7 |
| `claude__v2__t0__val2` | 30 | 83.3 | 96.7 | 1 | 2 format (G3), 1 endpoint (G1), 1 quota name (G2), 1 schema (error 5) | 45 / 123 s | 50.6 |
| `qwen2.5-7b__v2__t0` (val. 1) | 30 | 86.7 | 86.7 | 4 | 3 cut off, 1 format | 136 / 565 s | 0 |
| `qwen2.5-7b__v2__t0__val2` | 30 | 50.0 | 56.7 | 13 | 7 endpoint (G1), 3 quota name (G2), 1 format (G3), 3 cut off, 1 malformed hostname | 221 / 763 s | 0 |

| Run | endpoints precision / recall | quotas precision / recall | `quota_table_format` |
|---|---|---|---|
| `claude__v2__t0` (val. 1) | 99.6 / 100 | 98.0 / 95.2 | 9/10 |
| `claude__v2__t0__val2` | 99.6 / 100 | 98.1 / **100** | **10/10** |
| `qwen2.5-7b__v2__t0` (val. 1) | 97.7 / 91.0 | 73.7 / 93.3 | 9/10 |
| `qwen2.5-7b__v2__t0__val2` | **99.5** / 54.5 | **96.4** / 50.5 | 6/10 |

What grounding changed:

- **Claude: four answers that validation "1" passed were not true to the chapter.** `044` a
  dual-stack hostname completed by pattern, `025` a quota name paraphrased from the
  neighbouring rows, `091` and `038` a Standard Quota Table called `non_standard`. All four
  were fixed by the repair call that now carries the grounding error (`038`: the repair
  returned exactly the five printed rows — quota recall 95.2 → 100, format 9/10 → 10/10).
  The fifth repair, `010` (the prose-line row of error 5), fixed that row but is the first
  `failed` Claude record of the HW — and a false one: the repaired answer wrote `doesn't` in
  a quota name where the PDF prints a typographic apostrophe (`doesn’t`), and G2 compares
  characters (finding F19, deferred). On content Claude is 30/30. The price of the judge:
  `% ok` 96.7 → 83.3, p95 89 → 123 s, +$8 per 1,000 for the repair calls.
- **qwen: the validity it had was half plausibility.** 15 of 30 first answers fail under
  validation "2": seven on hostnames the chapter does not print (FIPS and dual-stack twins,
  `us-gov` rows, `osis.*` in `038`), three on quota names (the Resource / Quota tables of
  `066` and `047` reported as `standard`; names shortened or stripped of their trailing
  period in `075`), one on the format (`037`: `none` with a Standard Quota Table printed),
  three cut off at the output cap (error 4), one malformed hostname (`074`). The repair call
  fixed two — the two Resource / Quota tables, which came back with no rows — so 13 end
  `failed`. Precision on the documents it does finish rises to 99.5 / 96.4 — what grounding
  is for — while recall over the gold rows halves, because a failed document counts as an
  empty extraction.
- **Latency and cost move for the same reason.** A repair call doubles a document's calls;
  qwen's p50 goes from 136 to 221 s.

#### 3.4 Out of sample — the Held-out Set, validation "2"

Prompt v2 was written from the v1 errors on the 30 Working Set documents (§4), so its
Working Set numbers are in-sample. The Held-out Set is 10 documents of the pool never looked
at while writing v2 (contract item 20): 6 `medium`, 4 `edge` — the pool had no `short`
document left — with a hand-checked gold for 5 of the 10. Claude ran on the five gold
documents only (budget); qwen on all ten. Accuracy on the five gold documents (390 endpoint
rows, 105 quota rows); validity on the run's documents.

| Run | n | ok % | ok + repaired % | endpoints precision / recall | quotas precision / recall | `quota_table_format` |
|---|---|---|---|---|---|---|
| `claude__v1__t0__holdout__gold__val2` | 5 | 100 | 100 | 100 / 91.8 | 100 / 100 | 5/5 |
| `claude__v2__t0__holdout__gold__val2` | 5 | 100 | 100 | 100 / **100** | 100 / 100 | 5/5 |
| `qwen2.5-7b__v1__t0__holdout__val2` | 10 | 30.0 | 50.0 | 100 / 42.1 | 100 / 16.2 | 2/5 |
| `qwen2.5-7b__v2__t0__holdout__val2` | 10 | 50.0 | 50.0 | 100 / **55.4** | 100 / **42.9** | 3/5 |

- **v2's gain is out of sample, and it is the same gain.** Claude v1 returned 76 of the 108
  endpoint rows of `068` Elastic Beanstalk — it stopped after the first endpoints table, as
  it had on `048` in the Working Set; v2 returned all 108. The other four documents were
  complete under both prompts. Nothing in v2 was written with `068` in view.
- **qwen improves out of sample too, from a lower base.** First-answer validity 30 → 50 %,
  endpoint recall 42 → 55 %, quota recall 16 → 43 %, format 2/5 → 3/5; four documents fail
  under both prompts (`016`, `051`, `059`, `073`) and one under each (`028` v1, `046` v2),
  on the same causes as in the Working Set — FIPS hostnames the tables do not print,
  malformed hostnames, quota names of non-standard tables, one cut-off.
- **The held-out numbers are harder than the Working Set's**, not easier: no `short`
  document, 1,275–2,929 words. Claude's absolute numbers hold (100 % valid, 100 % recall
  with v2); qwen's are lower than on the Working Set for that reason.

What the tables say:

- **Prompt v2 helped both models, for different reasons.** Claude: the wider rule 2 ("every
  endpoints table, across page breaks") recovered the rows v1 missed — gold recall 97.3 → 100,
  and outside gold `078` 78 → 234, `017` 94 → 248, `044` 78 → 166 rows — at +$2.5 per 1,000
  and +8 s p50 for the extra output. qwen: validity 70 → 86.7 %, endpoints recall 78.6 →
  91.0, quotas recall 76 → 93, and **no repair call at all** once the schema enum told it the
  one allowed `schema_version`.
- **Temperature 0.5 is a no-op for Claude and a loss for qwen.** `claude__v1__t05__gold`
  reproduces `t0` to the decimal (same row counts on all 10 documents). qwen at `t05` loses
  17 pp of validity and half of its gold recall in the v1 `__gold` pair, because it starts
  merging a Region's several hostnames into one `endpoint` cell (section 5, error 4).
- **qwen's remaining gap is three things:** two documents whose quota layout it misreads
  (error 2), the Region code written as `region_name` (error 3), and the largest documents,
  which it cannot finish within the output cap (error 4). None of these is a schema or
  validity problem a repair call can fix.
- **The paid model is ≈ 3–5× faster and ≈ 97 % valid under grounded validation; the local
  model is free and 57 % valid.** Per document: 45 s vs 221 s at p50; $0.051 vs $0.

## 4. Error analysis

Format: what → how often → one document, expected vs got → why → what v2 did → effect.

**Error 1 — A second endpoints table is skipped (Claude v1).**
*How often:* 1 of 10 gold documents (`048` SQS), and three non-gold documents with the same
signature (`078`, `017`, `044`: 78–94 rows where the manifest counts 165–234).
*Example:* `048` prints a "Service endpoints" table (84 rows) and, after it, a "Legacy
endpoints" table (20 rows). Expected 104 rows; `claude__v1__t0` returned 84.
*Why:* rule 2 of v1 said "the target service's *Service endpoints* table" — singular, by
name. The model took it literally.
*v2:* rule 2 names several tables ("a main table and separate tables for FIPS, dual-stack,
legacy or control-plane endpoints") and tells the model to continue across page breaks.
*Effect:* `048` 84 → 104 rows; gold endpoint recall 97.3 → 100 %; `078` / `017` / `044` as
above. The only cost is error 5.

**Error 2 — Rows of a non-standard quota table are reported as Standard Quota Table rows
(qwen, both prompts) — and the reference was wrong on one of the two documents.**
*How often:* 2 of 10 gold documents (`066` DataSync, `038` OpenSearch) in every qwen run.
On `066`, Claude is right in every run. On `038`, the first edition of this report counted
qwen's 28 rows as invented and Claude's `non_standard` as correct; grounding the gold file
itself in its chapter (step 11, finding F18) showed the chapter prints **one** Standard
Quota Table (domain and instance quotas, 5 rows) and ten other tables with `Notes` instead
of `Description` or three columns. So the correct answer is `standard` with five rows:
qwen's 28 rows are 5 printed ones plus 23 from the non-standard tables, and every Claude run
had the format wrong (`non_standard`, no rows). The gold was re-drafted and re-checked on
25.10; §3.2 is recomputed against it.
*Example:* `066` prints a table with the columns *Resource / Quota / Adjustable* — no
Default, no Description. Expected `non_standard`, `quotas: []`; qwen returned `standard` and
four rows, with the Resource text as `name` and the Quota text as `default`.
*Why:* a 7B model maps the table it sees onto the four fields it is asked for; "exactly the
columns Name, Default, Adjustable, Description" does not stop it when three of the four look
close enough. Claude's `038` error is the mirror image: ten non-standard tables outweighed
the one standard table.
*v2:* rule 3 decides by the header row and names the Resource / Quota layout explicitly as
`non_standard`. Effect on the model: none — `066` still 4 rows, `038` 15 → 28 rows.
*Grounded validation (step 11):* G3 compares the format with the printed header and G2 every
quota name with the printed Name cells, by code. Under it, Claude's `038` answer is repaired
into exactly the five printed rows (quota recall 95.2 → 100). qwen's `066` is rejected and
repaired into an answer with no rows (format `none` — still not the gold's `non_standard`,
but nothing invented); its `038` is rejected with 23 of the 28 rows flagged — exactly the
rows of the non-standard tables — plus two `osis.*` hostnames the tables do not print, and
the repair returns the same answer: `failed`. The validation now catches what the prompt
could not; the model still cannot read the layout.

**Error 3 — The Region code is written as `region_name` (qwen).**
*How often:* 205 of 686 matched gold rows in `qwen2.5-7b__v2__t0` (`region_name` accuracy
70.3 %); concentrated in two documents — `038` 116 of 182 rows, `085` 40 of 83 — plus a
milder form in `005` (33 of 35 rows: "US East" instead of "US East (Ohio)") and "Canada West
(Calgary)" shortened to "Canada (Calgary)" in five documents (2–4 rows each). Claude: 0.
*Example:* `085`, row `lakeformation.af-south-1.amazonaws.com`: expected `region_name`
"Africa (Cape Town)", `region_code` "af-south-1"; got "af-south-1" in both fields.
*Why:* in layout text the Region Name and Region columns are separated by spaces only, and
on long tables the model drifts to the nearer, shorter token. `region_code` stays right
(98 %), which is why key matching and recall are unaffected — only the name field is.
*v2:* nothing — rule 5 already says "copy, never paraphrase". This is a model limit.
*Effect:* none; reported as a field-level weakness. If `region_name` matters downstream, it
is derivable from `region_code` by code (ADR-0002 would allow it).

**Error 4 — The answer does not fit the output cap (qwen).**
*How often:* 14 of the 17 qwen `failed` records across the three 30-document runs; always the
same six documents (`017` DynamoDB, `049` S3, `025` EMR, `042` Redshift, `086` Lambda, `048`
SQS). Every one has `output_tokens` = 18,432 exactly, i.e. hit `num_predict`. Claude hit its
own cap once, in the S3 trial of 21.10 at `max_tokens` 16,384, and never after it was raised
to 32,000.
*Example:* `048` in `qwen2.5-7b__v1__t0`: input 4,761 tokens, a complete answer is ≈ 6k
tokens (Claude's), qwen produced 18,432 and was cut mid-string — a repetition loop, not a
long document. `049` S3 (13.9k tokens in, 290 rows) is the real case: the answer needs
≈ 17k tokens and the cap plus the input do not fit in `num_ctx` 32,768.
*Why:* two causes under one symptom: (a) the document is too large for a 32k context with
indented JSON output; (b) the model loops on a mid-size document. A cut-off answer gets no
repair call by design (contract item 16: the corrected answer would be as long).
*v2:* no change in the prompt; v2 at `t0` reduced the cut-offs from 5 to 3 (`042`, `086`,
`048` finished), `t05` brought them back to 6.
*Effect:* this is where the local model's validity ceiling is — the 10 % of the corpus that
is `edge`-sized. Options outside this HW: a larger context, a chunked extraction per table,
or a loop detector that stops after a repeated row.

**Error 5 — A prose line is taken as an endpoint row (Claude v2, side effect of error 1's
fix).**
*How often:* 1 of 30 (`010` CloudFront), the only non-`ok` record of `claude__v2__t0`.
qwen's one `repaired` in `qwen2.5-7b__v2__t05` and its `074` failure are the same family:
a hostname that is not a hostname ("globalaccelerator-fips.us-west-2.zonaws.com", a wrap
rejoined wrongly).
*Example:* `010` prints, under the table, a sentence about the key-value store endpoint
"…in your AWS account.cloudfront-kvs.global.api.aws"; v2 returned it as a row with
`region_code: ""` and `endpoint: "AWS account.cloudfront-kvs.global.api.aws"`.
*Why:* the wider rule 2 ("return every endpoints table") made the model look for rows
beyond the last table.
*Caught by:* the format checks of ADR-0003 (`region_code` pattern, hostname pattern), so
the row never reached the output; the repair call removed it and the record is `repaired`.
*Effect:* `% ok` 100 → 96.7 for Claude v2 while `% ok + repaired` stays 100 — the validation
layer did exactly what it was designed for. Under grounded validation the repair fixes the
row, and the same document is nevertheless Claude's one `failed` record — a straight
apostrophe in a quota name where the PDF prints a typographic one (§3.3, F19).

## 5. Choice for production, and when it would change

**Claude Haiku 4.5, prompt v2, temperature 0, grounded validation.** 97 % valid after one
repair with nothing invented (the one failure is a prose line it keeps returning as a row),
100 % gold recall on endpoints and quotas in and out of sample, every scored field ≥ 99 %,
and nothing in the error analysis is a Claude-side limit except the S3-sized output, which
the raised `max_tokens` covers.

The scale arithmetic, from the measured numbers under grounded validation: **100,000
documents cost ≈ $5,100 with Claude** and, with parallel requests, finish in hours. The same
corpus on **qwen2.5:7b costs $0 in fees and ≈ 256 days of one M4 Pro laptop at the measured
p50 of 221 s per document** — and 43 % of the documents come back invalid, with hostnames
the chapter does not print as the first cause.

The decision would change if: (a) the documents cannot leave the machine — then qwen is the
only option, and the output needs a post-check of `quota_table_format` against the printed
header row and a `region_name` lookup from `region_code`; (b) a GPU server replaces the
laptop — at ≈ 20× the throughput the corpus takes two weeks, and 57 % validity with 99 %
precision on the valid half may be acceptable for a draft-then-review workflow; (c) the
corpus is a few hundred documents — nights of laptop time, no budget line, and the invalid
half reviewed by hand; (d) a larger local model (14B–32B) closes errors 2–4 — to be measured,
not assumed.

## 6. Limitations

- **The Golden Set was drafted by `claude__v1__t0`** and corrected by hand against the PDF.
  A Claude error the check did not catch is counted as correct for Claude and as an error for
  qwen. The step 5 check found one such error (the `048` legacy table); grounding found a
  second one three days later (`038`, F18), which the hand check had confirmed because the
  draft was empty. The held-out gold was drafted by a grounded run and checked the same way,
  with the same advantage for Claude.
- **10 gold documents, one run per configuration.** Recall is computed over 752 endpoint rows
  and 100 quota rows, so a single document moves it by several points; `edge` is represented
  by one gold document (`038`). Differences under ≈ 2 pp are noise.
- **`claude__v1__t05` ran on the Golden Set only** (budget decision of 21.10, $5 for the
  whole HW): its validity and latency rest on 10 documents.
- **Two schemas (F17).** The `__gold` v1 runs saw the `Literal` schema, the 30-document v1
  run the enum; the table marks them (†).
- **The local model's caps are a laptop's caps.** `num_ctx` 32,768 and `num_predict` 18,432
  were set for a 48 GB machine; the six documents that hit the cap would need a larger
  context or chunking, not a better prompt.
- **The Held-out Set is small and skewed.** 10 documents, gold for 5, no `short` document
  (the Working Set took all of them), one run per configuration; Claude ran on the five gold
  documents only. It shows that v2's gain is not an artefact of the documents it was written
  on; it does not give precise out-of-sample rates.
- **Grounding is a reader of layout text.** G1–G3 were calibrated so that every gold file
  passes and every flagged Claude row was confirmed by hand; `region_name`, `default` and
  `description` are not grounded and are checked by the Golden Set only. A reader fault shows
  as a false repair, never as a silent pass — the one case found, the typographic apostrophe
  of `010` (F19), cost Claude one `failed` record out of 30.
- **Long documents are not processed in parts** (lecturer's remark 3): the output-cap
  failures of error 4 stand; chunking is the planned next step.

## 7. Reproduce

```bash
make install                      # .venv from uv.lock
make metrics                      # results/runs/jsonl/*.jsonl -> results/metrics.csv
make run PROMPT=v2                # Claude, all 30 documents (needs ANTHROPIC_API_KEY, ≈ $1.3)
make run MODEL=qwen2.5-7b PROMPT=v2   # local model (needs Ollama with qwen2.5:7b, ≈ 100 min)
```

The README section "Stage 1: run the extraction" has the rest; the metric definitions are
contract items 17–19 in `docs/stage1-data-contract.md`; every finding (F1–F17) is in
`docs/Implementation_steps.md`, section 6.
