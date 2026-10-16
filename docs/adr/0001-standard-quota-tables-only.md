---
status: accepted
date: 2026-10-15
---

# Only Standard Quota Tables become Quota Rows in schema v1

Some services (e.g. SNS, Redshift) publish their quotas in non-standard layouts: `Resource |
Default` tables with bulleted values, per-region API-throttling tables, policy matrices with
`N/A`. We decided that schema v1 extracts Quota Rows only from a Standard Quota Table
(`Name | Default | Adjustable | Description`); any other layout yields `quotas: []` and the
document's Quota Table Format is recorded as `non_standard` (or `none` when there is no
quotas section at all).

## Considered options

- **Any "name + value" row counts as a quota, `adjustable` optional.** Rejected: for 3 of the 10
  Golden Set documents it is subjective what the "name" of a throttling row per region is, so
  the model comparison would measure disagreement about the labelling rather than the models.
- **Standard tables only, plus an explicit format marker.** Chosen: the Golden Set stays
  unambiguous, and whether a model *recognises* that there is no standard table (instead of
  inventing rows) becomes a measurable field.

## Consequences

- Golden Set files are built against this scope; widening it later means re-labelling, so it is
  a deliberate v1 boundary, not an omission. The README states it as a known limit.
- Stage 3 (architecture review) can add non-standard quotas as a separate extension keyed on
  Quota Table Format without invalidating v1 Golden Set files.
