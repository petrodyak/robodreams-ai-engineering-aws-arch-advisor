---
status: accepted
date: 2026-10-15
---

# The model extracts what is printed; code derives everything else

The extraction schema asks the language model only for values that are literally printed in
the table, and leaves every derived value to deterministic Python. Concretely:

- A Quota Row's `default` is kept as the printed text with whitespace normalised
  (`"Each supported Region: 10,000"`, `"us-east-1: 20,000; us-east-2: 6,000"`), not parsed into
  number / unit / scope / per-region overrides by the model.
- An Endpoint Row carries the four printed columns (region name, region code, endpoint
  hostname, protocol); its Endpoint Type (FIPS, dual-stack, IPv4, global) is computed from the
  hostname by code and is excluded from accuracy metrics.

## Why

- What a regex can do reliably should not be delegated to a 7B model: parsing failures would be
  booked as "model errors" and blur the comparison between the paid and the local model.
- Verbatim fields give an objective Golden Set and a simple metric (normalised string match).
  Asking the model for a value that is not printed (Endpoint Type) measures guessing, not
  extraction.
- The printed `default` strings follow a small number of fixed patterns, so a later numeric
  parser for the architecture-review agent (stage 3) can be written and unit-tested in
  isolation.

## Consequences

- Whitespace normalisation of `default` is part of the schema (a Pydantic validator), not of the
  prompt, so the Golden Set and every model run are normalised identically.
- Stage 3 depends on the stability of these strings; changing their normalisation later means
  re-running the parser, not re-labelling the Golden Set.
