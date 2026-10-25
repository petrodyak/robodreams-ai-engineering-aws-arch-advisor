---
status: accepted
date: 2026-10-24
---

# Validation is grounded in the source text, not in the answer's shape

The lecturer's review of the checkpoint (24.10) said it in one line: *validation should check
the data against the source, not what the model copied from the prompt anyway.* Our
validation did the second thing. The `service` check (contract item 2) compares a value the
model copied from the prompt; the `schema_version` check compares a value copied from the
schema; the format checks of ADR-0003 say whether a hostname or a Region code *looks* right.
None of them asks whether a row is printed in the document. Two consequences showed up in the
runs: qwen reported Standard Quota Tables with invented rows on `066` and `038` as valid
`ok` answers, and the Golden Set itself carried a wrong `quota_table_format` for `038` that
nobody noticed because the drafting model agreed with it (finding F18).

## Decision

Every answer is validated against the chapter it was extracted from, by code, the same way
for both providers, after the schema and before the repair call (`src/extract/grounding.py`):

- **G1** — every `endpoint` is a hostname printed in the Endpoint column of an endpoints table
  of the Target Service's chapter (line wraps rejoined).
- **G2** — every quota `name` is the Name cell of a row of a Standard Quota Table of the
  chapter, compared with whitespace collapsed or — for a name the PDF wrapped mid-word — with
  all whitespace removed.
- **G3** — `quota_table_format` is `standard` if and only if the chapter prints at least one
  Standard Quota Table header.

A violation is a validation failure in the schema's `- path: message` form and goes into the
one repair call (item 16). Records carry `validation_version` ("1" before, "2" with
grounding), and a run under a new validation gets its own run id (`__val2`, item 11).

## Considered options

- **Keep validation as it was and rely on the Golden Set.** Rejected: the Golden Set covers 10
  of 30 documents and is itself drafted by a model; invented rows on the other 20 are invisible.
- **Grounding by substring search over the whole chapter.** Rejected for hostnames: the prose
  prints hostnames too, and the one row that must fail (`010`, a sentence fragment glued to a
  hostname) would pass. The readers are column-based, the same ones a person used to verify
  the Golden Set in step 5.
- **Ground every field.** Rejected for v1: `region_name` and `region_code` sit in neighbouring
  columns and cannot be paired to a row without a full table parser; `default` and
  `description` are free text broken by page furniture. Grounding is about nothing invented;
  completeness and field accuracy stay with the Golden Set metrics.
- **Punctuation-insensitive G2.** Rejected: a dropped trailing period is a copy error against
  the source and the repair call is the place to fix it; the cost is a few more repair calls
  for the local model.

## Consequences

- The validity numbers of every run judged by validation "1" are not comparable with "2": an
  answer that was `ok` can be `repaired` or `failed` now. The runs are kept and marked; the
  report shows both.
- The readers are heuristics over layout-mode text. They were calibrated so that every Golden
  Set file passes and every flagged model row was confirmed against the raw text by hand
  (step 11 log); a reader failure shows up as a false repair, never as a silent pass.
- The `service` and `schema_version` checks stay as the cheap first layer; they are no longer
  the validation.
