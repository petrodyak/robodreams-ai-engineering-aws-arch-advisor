# Golden Set

The reference every accuracy metric is computed against (contract items 10 and 17): one
Service Document per manifest row with `gold=1`, as `data/gold/<name>.json`. The format is
`ServiceDocument` of `src/extract/schema.py` (schema version 1) without the computed
`endpoint_type`, which is derived from the hostname when a file is loaded.

## Procedure: model-assisted, human-verified

1. **Draft.** `python -m scripts.make_gold_drafts` copied the answer of run
   **`claude__v1__t0`** (claude-haiku-4-5, prompt v1, temperature 0; 21.10.2026) for each gold
   document. The script never overwrites an existing file.
2. **Narrow.** `python -m scripts.check_gold` compares the Endpoint Rows with the hostnames
   printed in the Target Service's chapter of `data/raw/<name>.txt` (line wraps rejoined) and
   lists what to look at: printed but missing, present but not printed, a hostname without its
   Region code, a `region_name` that differs from the drafts' usual name for that Region.
3. **Verify by hand against the PDF.** Every Quota Row (`name`, `default`, `adjustable`,
   `description`), `quota_table_format`, and every row the check lists. Corrections are made
   in the JSON file; `tests/test_gold.py` then validates it with the same schema and checks as
   a model answer.

**The drafting model has an advantage.** The reference starts from Claude's own answer, so a
Claude mistake that the check does not catch stays in the reference and counts as correct for
Claude and as an error for the other model. The report states this next to the accuracy
numbers.

## Selection

6 `short` / 3 `medium` / 1 `edge`, to keep the manual check short; the limits this sets on the
metrics (edge on one document, no `non_standard` and no global service in gold) are in
`docs/data-notes.md`.

## Decisions taken while checking

- **`005-amazon-aurora`** prints the same 36 hostnames in two tables (MySQL- and
  PostgreSQL-Compatible): one row per hostname, 36 rows (contract item 6).
- **`007-amazon-bedrock-agentcore`** prints templated Gateway endpoints ("Replace gatewayId with
  the ID of your gateway"): kept as printed, e.g.
  `gatewayId.gateway.bedrock-agentcore.us-east-1.amazonaws.com` (contract item 6).
- All endpoints tables of the chapter count, not only the first (contract item 6).

## Status

| File | Endpoints (check) | Quotas by hand | Checked |
|---|---|---|---|
| `006-amazon-aurora-dsql.json` | match | 4 | ⬜ |
| `076-aws-glue-databrew.json` | match | 7 | ⬜ |
| `033-amazon-kinesis-data-streams.json` | match | 1 | ⬜ |
| `066-aws-datasync.json` | match | 0 (`non_standard`) | ⬜ |
| `085-aws-lake-formation.json` | match | 0 (`none`) | ⬜ |
| `007-amazon-bedrock-agentcore.json` | match | 0 (`none`) | ⬜ |
| `005-amazon-aurora.json` | match | 25 | ⬜ |
| `075-aws-glue.json` | match | 46 | ⬜ |
| `048-amazon-simple-queue-service.json` | 20 printed hostnames missing | 19 | ⬜ |
| `038-amazon-opensearch-service.json` | match | 0 (`non_standard`) | ⬜ |
