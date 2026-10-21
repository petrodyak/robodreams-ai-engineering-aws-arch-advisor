# Stage 1 — extraction data contract

Decisions reached in the design interview of 2026-10-15, amended on 2026-10-16 (items 6, 9,
14, 16; review of the earlier schema grill against this contract) and on 2026-10-21 (items 14,
15, 16, 18; the S3 trial call and the reviews of step 4). Terms are defined in
[`GLOSSARY.md`](../GLOSSARY.md); the decisions that are hard to reverse have ADRs
([0001](adr/0001-standard-quota-tables-only.md), [0002](adr/0002-model-extracts-code-derives.md),
[0003](adr/0003-format-checks-are-validation-failures.md)).
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
   (`HTTPS | HTTP | HTTP and HTTPS` — the printed value, 7 Working Set files print
   "HTTP and HTTPS"), exactly the printed columns; one row per hostname. `endpoint_type`
   (`fips | dual_stack | fips_dual_stack | ipv4 | global`) is a computed field derived from the
   hostname and is excluded from accuracy metrics: `global` when the hostname does not contain
   `region_code`; dual-stack when the domain is `api.aws` / `on.aws` or a label is `dualstack`;
   FIPS when the hostname contains `fips`; both → `fips_dual_stack`; otherwise `ipv4`.
7. `quotas: list[QuotaRow]` — `name`, `default: str`, `adjustable: bool`, `description`. Only
   rows of a Standard Quota Table (ADR-0001). `adjustable` is required: the column is always
   printed as Yes/No.
8. `default` is the printed text, not a parsed number (ADR-0002). Multi-region cells are
   serialised as `"us-east-1: 20,000; us-east-2: 6,000"` — separator `; `, table order;
   `"Each supported Region: 10,000"` stays verbatim. The convention lives in the field's
   `Field(description=...)`, which both models see through the JSON schema.
9. Normalisation on every `str` field: collapse whitespace (`" ".join(s.split())`), nothing
   else. Broken tokens (`ca-centra\nl-1`) are the model's job to repair. Footnote markers in
   `description` stay as printed. On top of normalisation, three format/consistency checks are
   validation failures (ADR-0003): `region_code` must match an AWS Region code
   (`^[a-z]{2}(-gov)?-[a-z]+-\d+$`), `endpoint` must be a hostname without spaces on an AWS
   domain (`amazonaws.com`, `amazonaws.com.cn`, `api.aws`, `on.aws`), and `quotas` must be
   empty unless `quota_table_format` is `standard`.

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
    constant, not a sampling parameter: 32000 for Claude. Measured 21.10 on S3 (254 Endpoint
    Rows): a complete answer is ≈14.4k Claude tokens (≈57 tokens per Endpoint Row, not the ≈35
    first assumed), so the earlier ≈8k and the first raise to 16384 both cut S3 off. The same holds for
    Ollama's `num_ctx`: a provider constant under `providers.ollama` in the same file, set
    explicitly to 32768 (S3 input is 13,129 qwen tokens plus ≈9k output; Ollama's default
    varies with version and memory and truncates silently).
    The paid model is `claude-haiku-4-5` (short name `claude` in run ids): the current Claude
    generation (Opus 5.5 / 5, Sonnet 5.5, Haiku 5.5) rejects non-default `temperature`, so
    `t0`/`t05` would be impossible there; Haiku 4.5 accepts it, supports structured outputs and
    fits the $5 budget (≈$1 per 30-document run, to be confirmed with `count_tokens` before the
    first run). If the budget is tight, cut the number of Claude runs, not schema fields.

## Failure handling

15. Transport retry (timeout, 5xx, rate limit): up to 3 attempts with backoff (1 s, 2 s, or the
    server's `retry-after` when longer, capped at 60 s), invisible to the pipeline except for
    the `attempts` counter. A document that still has no answer — on the first or the repair
    call, or at once on a non-retryable error such as an exhausted credit balance — gets no
    Run Record: a transport failure says nothing about the model. It is left out of the run
    file, the run command exits non-zero, and running it again retries just those documents.
    If the same error comes back, it is permanent (e.g. a request the API rejects for this
    document): the document stays without a record, and item 18 counts it as failed. Tokens
    paid before such a failure (the first call when the repair call has no answer) are
    added to the run's cost summary.
16. Repair: a response that fails schema validation, a format/consistency check (item 9) or
    the `service` check gets exactly one
    corrective call carrying the previous answer and the validation error text. A second
    failure → `status: failed`. No blind re-sends with the same prompt. Exception: an answer
    cut off at `max_tokens` (`stop_reason: max_tokens`) is `failed` at once, without a repair
    call — the corrected answer is as long as the cut one and is cut again (S3 trial, 21.10).

## Metrics

17. Field accuracy: rows are matched by key — Endpoint Rows by normalised `endpoint`, Quota Rows
    by normalised `name`. Reported as key precision / recall (extra / missing rows) plus
    per-field accuracy on matched rows; `description` compared after whitespace and case
    normalisation, other fields exact after normalisation. Computed on the Golden Set only.
18. Validity (`% ok` first try, `% ok + repaired`), latency p50 / p95, and cost per 1,000
    documents are computed on all 30 documents and broken down by Group as well as in total.
    The denominator comes from the manifest, not from the run file: a document without a Run
    Record (item 15) counts as failed and is also reported separately as "no answer".
19. `latency_ms` is the wall-clock time for the whole document, including transport retries and
    the repair call. Cost for Claude is derived from `usage` and list prices; for the local
    model the API cost is $0, reported together with the run's total wall-clock as the compute
    note.
