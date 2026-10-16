# Stage 1 — extraction data contract

Decisions reached in the design interview of 2026-10-15. Terms are defined in
[`GLOSSARY.md`](../GLOSSARY.md); the two decisions that are hard to reverse have ADRs
([0001](adr/0001-standard-quota-tables-only.md), [0002](adr/0002-model-extracts-code-derives.md)).
This file is the single list to check code against; it is not a spec of the implementation.

## Unit of extraction

1. One Working Set document → one Service Document (one model call). The same Pydantic class is
   used for model output, Golden Set files and metrics. Files mirror names:
   `data/raw/<name>.txt` → `data/gold/<name>.json`.
2. The Target Service name comes from `data/raw/manifest.csv` and is passed in the prompt; the
   model echoes it as `service`. A mismatch (after normalisation) is a validation failure, not a
   field error — it is the cheap detector of a Neighbour Tail extraction.

## Shape of a Service Document

3. `schema_version: Literal["1"]` — the Golden Set carries the contract version.
4. `service: str`.
5. `quota_table_format: standard | non_standard | none` (enum).
6. `endpoints: list[EndpointRow]` — `region_name`, `region_code`, `endpoint`, `protocol`
   (`HTTPS | HTTP`), exactly the printed columns; one row per hostname. `endpoint_type`
   (`fips | dual_stack | ipv4 | global`) is a computed field derived from the hostname and is
   excluded from accuracy metrics.
7. `quotas: list[QuotaRow]` — `name`, `default: str`, `adjustable: bool`, `description`. Only
   rows of a Standard Quota Table (ADR-0001). `adjustable` is required: the column is always
   printed as Yes/No.
8. `default` is the printed text, not a parsed number (ADR-0002). Multi-region cells are
   serialised as `"us-east-1: 20,000; us-east-2: 6,000"` — separator `; `, table order;
   `"Each supported Region: 10,000"` stays verbatim. The convention lives in the field's
   `Field(description=...)`, which both models see through the JSON schema.
9. Normalisation on every `str` field: collapse whitespace (`" ".join(s.split())`), nothing
   else. Broken tokens (`ca-centra\nl-1`) are the model's job to repair; the validator makes
   outputs comparable, not correct. Footnote markers in `description` stay as printed.

## Golden Set

10. 10 of the 30 documents (`gold=1` in the manifest). Draft produced by the ordinary pipeline
    (run `claude__v1__t0`), copied to `data/gold/`, then corrected by hand against the PDF.
    `data/gold/README.md` records the draft's run id, date and the procedure
    ("model-assisted, human-verified"). A test validates every gold file against the schema and
    checks `service` against the manifest. The report must state that the drafting model has
    an advantage from this procedure.

## Runs and results

11. Run id: `<model>__<prompt_version>__<sampling_name>`, e.g. `claude__v1__t0`,
    `qwen2.5-7b__v2__t05`.
12. `results/runs/<run_id>.jsonl`, one Run Record per document:
    `file, group, model, prompt_version, sampling, attempts, latency_ms, usage{input_tokens,
    output_tokens}, status (ok | repaired | failed), output (Service Document | null), error`.
13. `results/metrics.csv` — one row per run × group plus a total row per run.
14. Sampling Configurations in `config/sampling.yaml`: `t0` (temperature 0) and `t05`
    (temperature 0.5); `top_p` left unset for both, because the Claude API asks for temperature
    *or* top_p, and a like-for-like comparison needs identical knobs. `max_tokens` is a provider
    constant (≈8k; S3 has 254 Endpoint Rows), not a sampling parameter.

## Failure handling

15. Transport retry (timeout, 5xx, rate limit): up to 3 attempts with backoff, invisible to
    the pipeline except for the `attempts` counter.
16. Repair: a response that fails schema validation or the `service` check gets exactly one
    corrective call carrying the previous answer and the validation error text. A second
    failure → `status: failed`. No blind re-sends with the same prompt.

## Metrics

17. Field accuracy: rows are matched by key — Endpoint Rows by normalised `endpoint`, Quota Rows
    by normalised `name`. Reported as key precision / recall (extra / missing rows) plus
    per-field accuracy on matched rows; `description` compared after whitespace and case
    normalisation, other fields exact after normalisation. Computed on the Golden Set only.
18. Validity (`% ok` first try, `% ok + repaired`), latency p50 / p95, and cost per 1,000
    documents are computed on all 30 documents and broken down by Group as well as in total.
19. `latency_ms` is the wall-clock time for the whole document, including transport retries and
    the repair call. Cost for Claude is derived from `usage` and list prices; for the local
    model the API cost is $0, reported together with the run's total wall-clock as the compute
    note.
