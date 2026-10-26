# Stage 1 — extraction data contract

Decisions reached in the design interview of 2026-10-15, amended on 2026-10-16 (items 6, 9,
14, 16; review of the earlier schema grill against this contract) and on 2026-10-21 (items 14,
15, 16, 18; the S3 trial call and the reviews of step 4; item 6, the Golden Set check of
step 5; on 2026-10-22 items 11, 14, 18 for the Ollama provider and the Golden-Set-only run of
step 6; on 2026-10-24 item 12 for run provenance, items 7, 9, 11, 12, 16 for grounded
validation; on 2026-10-25 item 20, the Held-out Set). Terms are defined in
[`GLOSSARY.md`](../GLOSSARY.md); the decisions that are hard to reverse have ADRs
([0001](adr/0001-standard-quota-tables-only.md), [0002](adr/0002-model-extracts-code-derives.md),
[0003](adr/0003-format-checks-are-validation-failures.md),
[0005](adr/0005-validation-grounded-in-the-source.md)).
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
   "HTTP and HTTPS"), exactly the printed columns; one row per hostname. The rows come from
   every endpoints table of the Target Service's chapter (S3 prints four: `s3`, `s3tables`,
   `s3-accesspoint`, `s3-control`). A hostname printed twice (Aurora prints the same 36 in its
   MySQL- and PostgreSQL-Compatible tables) is one row, so metrics compare key sets. A
   templated hostname is kept as printed (`gatewayId.gateway.bedrock-agentcore.us-east-1.
   amazonaws.com`, AgentCore). `endpoint_type`
   (`fips | dual_stack | fips_dual_stack | ipv4 | global`) is a computed field derived from the
   hostname and is excluded from accuracy metrics: `global` when the hostname does not contain
   `region_code`; dual-stack when the domain is `api.aws` / `on.aws` or a label is `dualstack`;
   FIPS when the hostname contains `fips`; both → `fips_dual_stack`; otherwise `ipv4`.
7. `quotas: list[QuotaRow]` — `name`, `default: str`, `adjustable: bool`, `description`. Only
   rows of a Standard Quota Table (ADR-0001) — every table of the chapter whose header is
   exactly `Name | Default | Adjustable | Description`, as every endpoints table counts in
   item 6. A table with `Notes` instead of `Description`, or with three columns, is not one
   (24.10: `038` prints one Standard Quota Table and ten such others). `adjustable` is
   required: the column is always printed as Yes/No.
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
   empty unless `quota_table_format` is `standard`. On top of those, since 24.10 every answer
   is grounded in the chapter it was extracted from (ADR-0005, `src/extract/grounding.py`):
   every `endpoint` must be printed in the Endpoint column of an endpoints table of the
   chapter, every quota `name` must be the Name cell of a Standard Quota Table row (whitespace
   collapsed, or with all whitespace removed for a name the PDF wrapped mid-word), and
   `quota_table_format` is `standard` if and only if the chapter prints a Standard Quota
   Table header. A grounding violation is a validation failure like the three above.

## Golden Set

10. 10 of the 30 documents (`gold=1` in the manifest). Draft produced by the ordinary pipeline
    (run `claude__v1__t0`), copied to `data/gold/`, then corrected by hand against the PDF.
    `data/gold/README.md` records the draft's run id, date and the procedure
    ("model-assisted, human-verified"). A test validates every gold file against the schema and
    checks `service` against the manifest. The report must state that the drafting model has
    an advantage from this procedure.

## Runs and results

11. Run id: `<model>__<prompt_version>__<sampling_name>`, e.g. `claude__v1__t0`,
    `qwen2.5-7b__v2__t05`. A run over the Golden Set only adds the scope suffix `__gold`
    (`claude__v1__t05__gold`, budget decision of 21.10): the scope is part of the name, so a
    later full run with the same model, prompt and sampling never resumes into its file.
    A run judged by a validation other than the first adds `__val<N>` after the scope
    (`claude__v2__t0__val2`, 24.10): the runs of validation "1" keep their names, and a
    re-run under grounding never shares a file with them. A run in parts (item 21, 26.10)
    adds `__parts` right after the sampling name and before any scope
    (`claude__v2__t0__parts__val2`, `qwen2.5-7b__v2__t0__parts__holdout__val2`): it is a
    configuration, like the prompt version, not a scope. In full:
    `<model>__<prompt>__<sampling>[__parts][__holdout][__gold][__val<N>]`.
12. `results/runs/jsonl/<run_id>.jsonl`, one Run Record per document:
    `file, group, model, prompt_version, prompt_sha, schema_sha, validation_version, sampling, attempts,
    latency_ms, usage{input_tokens, output_tokens}, status (ok | repaired | failed), output
    (Service Document | null), error`. `prompt_sha` and `schema_sha` (24.10) are the first 12
    hex chars of sha256 of the prompt file and of the JSON Schema text sent to the model: the
    run id names a configuration, the two shas pin the exact bytes the model saw.
    `validation_version` (24.10) names the validation that judged the answer: "1" = schema and
    the checks of ADR-0003, "2" = "1" plus grounding (ADR-0005); the same answer can be `ok`
    under "1" and `repaired` or `failed` under "2". A prompt version name and the shared
    `schema.py` can drift under a run (finding F17), so a resume into a run file whose
    records carry another (prompt_sha, schema_sha, validation_version) triple is refused
    before any call, and metrics refuse a file that already mixes two.
    A record of a run in parts (item 21) also carries `parts`: one entry per part called,
    `{name (endpoints | quotas), words, attempts, latency_ms, usage, status, rows, spill,
    error}`; the record's `attempts`, `latency_ms` and `usage` are their sums and its
    `status` the worst of theirs. The field is absent in a whole-document record, and
    metrics refuse a run file whose records disagree with the run id about it.
    This file is the source of truth and the only one code reads. `results/runs/md/<run_id>.md`
    is its mirror for a person (summary table, then the endpoint and quota tables and the error
    text per document), rewritten from the whole JSONL after every record; its layout is free
    to change (22.10).
13. `results/metrics.csv` — one row per run × group plus a total row per run.
14. Sampling Configurations in `config/sampling.yaml`: `t0` (temperature 0) and `t05`
    (temperature 0.5); `top_p` left unset for both, because the Claude API asks for temperature
    *or* top_p, and a like-for-like comparison needs identical knobs. `max_tokens` is a provider
    constant, not a sampling parameter: 32000 for Claude. Measured 21.10 on S3 (254 Endpoint
    Rows): a complete answer is ≈14.4k Claude tokens (≈57 tokens per Endpoint Row, not the ≈35
    first assumed), so the earlier ≈8k and the first raise to 16384 both cut S3 off. The same holds for
    Ollama's `num_ctx`: a provider constant under `providers.ollama` in the same file, set
    explicitly to 32768 (S3 input is 13,714 qwen tokens plus a complete answer of ≈16.6k
    Claude tokens, about as many qwen tokens; Ollama's default varies with version and memory and
    truncates silently). Its output cap `num_predict` is 18432 (the S3 trial at 16384 was cut
    off: qwen writes about as many output tokens as Claude), the counterpart of
    `max_tokens`; a reply that hits it, or fills `num_ctx`, counts as cut off (item 16).
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
16. Repair: a response that fails schema validation, a format/consistency check (item 9), a
    grounding check (item 9, ADR-0005) or the `service` check gets exactly one
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
    Record (item 15) counts as failed and is also reported separately as "no answer". For a
    `__gold` run (item 11) the denominator is the `gold=1` rows of the manifest, and the
    report marks its numbers as computed on the Golden Set only.
19. `latency_ms` is the wall-clock time for the whole document, including transport retries and
    the repair call. Cost for Claude is derived from `usage` and list prices; for the local
    model the API cost is $0, reported together with the run's total wall-clock as the compute
    note.

## Held-out Set (25.10, lecturer's remark 4)

20. A prompt change is judged on documents that were not seen while writing it. The Held-out
    Set is 10 documents of `data/pool/` outside the Working Set, selected once by a fixed
    rule (seed 20261025, under 20 pages, `093-aws-services` excluded, stratified by the
    Working Set's word thresholds — the pool had no `short` document left, so 6 `medium` and
    4 `edge`), in `data/holdout/` with the same files as `data/raw/` (`manifest.csv`, the
    `.txt` texts; PDFs not in Git) and its own gold files in `data/holdout/gold/` for 5 of the
    10 (`gold=1`), drafted by `claude__v2__t0__holdout__gold__val2` and checked by hand
    against the PDF. A run over the Held-out Set adds the scope `__holdout` to its id after
    the sampling name and before `__gold` (item 11); metrics take the manifest and gold
    files from the run's set. Items 10 and 17–19 apply to the set as to the Working Set,
    with its own denominators. Prompt v2 was written from the v1 errors on the Working Set
    only, so its v1 → v2 difference on the Held-out Set is the out-of-sample number the
    report quotes; the Working Set numbers are in-sample for v2 and the report says so.

## Long documents in parts (26.10, lecturer's remark 3)

21. A chapter can be extracted in two parts instead of one answer, with the same prompt and
    the same schema (`src/extract/parts.py`, ADR-0006). Code splits the Target Service's
    chapter at its headings: the "Service quotas…" blocks are the **quotas part**, everything
    else — the endpoints tables under whatever heading, and the prose between them — is the
    **endpoints part**; each part is sent as a chapter of its own (title line first), and
    nothing else of the document, so the two inputs add up to about one whole-document call
    plus one more copy of the instructions. Each part goes through the ask → validate → one
    repair of item 16, judged on the rows it is responsible for: G1 for the endpoints part,
    G2 and G3 for the quotas part (ADR-0005); the fields of the other kind in a part's answer
    are dropped from the raw answer before the schema sees it and counted as `spill` — a
    part is never rejected for rows the merge does not read (finding F20: the local model
    fills the endpoints table the schema asks for even when its part prints none). Code merges the two answers — `endpoints` from one,
    `quota_table_format` and `quotas` from the other — into one Service Document, validated
    once more as a whole (G1–G3, no call), and derives nothing (ADR-0002); a chapter with no
    quotas block (`007`, `085`) has no quotas part and the merged document says `none`. The
    document's status is the worst of its parts' (`failed` if any failed, else `repaired` if
    any repaired); a `failed` document has no output, as in item 16. The run id carries
    `__parts` (item 11) and the record `parts` (item 12). Items 17–19 apply unchanged:
    latency is the sum of the parts' (they are called one after the other), cost the sum of
    every call.
