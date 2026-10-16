---
status: accepted
date: 2026-10-16
---

# Format and consistency checks are validation failures, not accuracy errors

The contract's first version said the validator only normalises whitespace and "makes outputs
comparable, not correct": a broken `region_code` such as `ca-centra l-1` would be scored as an
accuracy error on the Golden Set. We now treat three checks as validation failures that go
through the single repair call (contract item 16):

- `region_code` must look like an AWS Region code (`^[a-z]{2}(-gov)?-[a-z]+-\d+$`);
- `endpoint` must be a hostname without spaces on an AWS domain (`amazonaws.com`,
  `amazonaws.com.cn`, `api.aws`, `on.aws`);
- `quotas` must be empty unless `quota_table_format` is `standard`.

The checks test the *form* of a value, never its truth against the document; the model still
has to read the right value from the text, and wrong-but-well-formed values remain accuracy
errors.

## Considered options

- **Whitespace normalisation only (contract v1).** Rejected: with structured outputs Claude
  almost never returns schema-invalid JSON, so the repair loop would fire only on the `service`
  check, and the validation step would have little to show — while a line-wrapped token (the
  most typical PDF noise in this data) is exactly what one corrective call can fix.
- **Format checks as validation failures.** Chosen: the regexes are deterministic, unit-tested
  and identical for both models, so "% ok first try" and "% repaired" measure how often a model
  leaves PDF noise in its answer.

## Consequences

- Validity metrics (contract item 18) now include format errors; accuracy metrics see only
  answers that passed the checks or the repair.
- The domain list is taken from the Working Set; a new domain in a later document is a
  validation failure until the list is extended, so the README states it as a known limit.
- Hostname case and protocol order are not normalised (contract item 9 still holds: collapse
  whitespace, nothing else).
