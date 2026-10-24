# HW 1 — Structured extraction: Claude Haiku 4.5 vs qwen2.5:7b

**Snapshot of 2026-10-24.** Numbers taken at commit `55892ec` (`patch-8.2-qwen-runs`) from
`results/metrics.csv`, which `make metrics` rebuilds from the eight run files in
`results/runs/jsonl/`: `claude__v1__t0`, `claude__v2__t0`, `claude__v1__t05__gold`,
`qwen2.5-7b__v1__t0`, `qwen2.5-7b__v2__t0`, `qwen2.5-7b__v2__t05`, `qwen2.5-7b__v1__t0__gold`,
`qwen2.5-7b__v1__t05__gold`. Later code changes do not edit this report.

## 1. Summary

Both models turn the layout-mode text of an AWS General Reference chapter into a valid
Service Document most of the time, but only the paid model does it reliably: **Claude Haiku
4.5 with prompt v2 is valid on 30/30 documents (29 first try, 1 after the repair call) and
recovers 100 % of the Golden Set endpoint rows and 100 % of the quota rows at $42.7 per 1,000
documents and 44 s per document.** The local **qwen2.5:7b with prompt v2 is valid on 26/30**,
recovers 91 % of the endpoint rows and 93 % of the quota rows, costs nothing in API fees but
takes 136 s per document on an M4 Pro, and gets `region_name` wrong on 30 % of the rows it
does find. Prompt v2 was worth it for both — Claude's endpoint recall went from 97.3 to 100 %,
qwen's validity from 70 to 87 % — while temperature 0.5 changed nothing for Claude and only
hurt qwen. **For production, Claude**; qwen is the choice only when the data cannot leave the
machine or the volume is small enough that a day of laptop time per 600 documents is fine.

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
  of the schema fix is read from the `__gold` v1 runs.

## 3. Results

Full table with per-group rows and per-field accuracy: `results/metrics.csv`.

#### 3.1 Validity, latency and cost — every document of the run (`n`)

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

#### 3.2 Accuracy — the 10 Golden Set documents only (752 endpoint rows, 100 quota rows)

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
| `claude__v1__t0` | 99.6 / 97.3 | 98.0 / 100 | 10/10 | 100 | 100 |
| `claude__v2__t0` | 99.6 / **100** | 98.0 / 100 | 10/10 | 100 | 99.0 |
| `claude__v1__t05__gold` | 99.6 / 97.3 | 98.0 / 100 | 10/10 | 100 | 100 |
| `qwen2.5-7b__v1__t0` | 97.2 / 78.6 | 74.5 / 76.0 | 7/10 | 63.1 | 94.7 |
| `qwen2.5-7b__v2__t0` | 97.7 / **91.0** | 69.9 / **93.0** | **8/10** | 70.3 | 93.5 |
| `qwen2.5-7b__v2__t05` | 97.2 / 79.8 | 66.1 / 76.0 | 7/10 | 66.0 | 93.4 |
| `qwen2.5-7b__v1__t0__gold` † | 96.8 / 75.8 | 60.8 / 76.0 | 7/10 | 65.4 | 94.7 |
| `qwen2.5-7b__v1__t05__gold` † | 93.0 / 46.3 | 87.8 / 36.0 | 6/10 | 86.5 | 88.9 |

The three `__gold` runs cover the same 10 documents as the accuracy table, so for them the
validity and accuracy denominators coincide.

† old `Literal` schema (F15 / F17): every first answer failed on `schema_version: "1.0"`.

The other scored fields, `claude__v2__t0` vs `qwen2.5-7b__v2__t0`: `region_code` 100 / 98.1,
`protocol` 100 / 95.6, `adjustable` 100 / 100, `description` 100 / 96.8.

What the table says:

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
- **The paid model is ≈ 3× faster and ≈ 100 % valid; the local model is free and 87 % valid.**
  Per document: 44 s vs 136 s at p50; $0.043 vs $0.

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

**Error 2 — A non-standard quota table is reported as `standard` with invented rows (qwen,
both prompts).**
*How often:* 2 of 10 gold documents (`066` DataSync, `038` OpenSearch) in every qwen run;
0 of 10 for Claude. This is the whole of qwen's `quota_table_format` gap (8/10) and most of
its quota precision gap (69.9 %).
*Example:* `066` prints a table with the columns *Resource / Quota / Adjustable* — no
Default, no Description. Expected `non_standard`, `quotas: []`; qwen returned `standard` and
four rows, with the Resource text as `name` and the Quota text as `default`.
*Why:* a 7B model maps the table it sees onto the four fields it is asked for; "exactly the
columns Name, Default, Adjustable, Description" does not stop it when three of the four look
close enough.
*v2:* rule 3 decides by the header row and names the Resource / Quota layout explicitly as
`non_standard`.
*Effect:* none on qwen — `066` still 4 rows, `038` went from 15 to 28 invented rows. The
rule works for Claude (which was already right) and not for the model it was written for.
A code-side check (the printed header row must contain "Default" and "Description") would
close this; it is a contract change, deferred.

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
layer did exactly what it was designed for.

## 5. Choice for production, and when it would change

**Claude Haiku 4.5, prompt v2, temperature 0.** 100 % valid after one repair, 100 % gold
recall on endpoints and quotas, every scored field ≥ 99 %, and nothing in the error analysis
is a Claude-side limit except the S3-sized output, which the raised `max_tokens` covers.

The scale arithmetic, from the measured numbers: **100,000 documents cost ≈ $4,300 with
Claude** and, with parallel requests, finish in hours. The same corpus on **qwen2.5:7b costs
$0 in fees and ≈ 157 days of one M4 Pro laptop at the measured p50 of 136 s per document**
(≈ 230 days at the mean, because the `edge` documents take 8–10 min each) — and 13 % of the
documents come back invalid, with two systematic errors (2, 3) no prompt fixed.

The decision would change if: (a) the documents cannot leave the machine — then qwen is the
only option, and the output needs a post-check of `quota_table_format` against the printed
header row and a `region_name` lookup from `region_code`; (b) a GPU server replaces the
laptop — at ≈ 20× the throughput the corpus takes a week, and the 87 % validity may be
acceptable for a draft-then-review workflow; (c) the corpus is a few hundred documents — a
night of laptop time, no budget line, and the invalid 13 % reviewed by hand; (d) a larger
local model (14B–32B) closes errors 2–4 — to be measured, not assumed.

## 6. Limitations

- **The Golden Set was drafted by `claude__v1__t0`** and corrected by hand against the PDF.
  A Claude error the check did not catch is counted as correct for Claude and as an error for
  qwen. The step 5 check did find and fix one such error (the `048` legacy table), which is
  the reason Claude v1 recall is 97.3 and not 100.
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
- **No held-out test set.** Prompt v2 was written from the v1 errors on the same 30
  documents it is then measured on; the Golden Set recall of v2 is therefore an in-sample
  number.

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
