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
metrics (edge on one document, no global service in gold) are in
`docs/data-notes.md`.

## Decisions taken while checking

- **`005-amazon-aurora`** prints the same 36 hostnames in two tables (MySQL- and
  PostgreSQL-Compatible): one row per hostname, 36 rows (contract item 6).
- **`007-amazon-bedrock-agentcore`** prints templated Gateway endpoints ("Replace gatewayId with
  the ID of your gateway"): kept as printed, e.g.
  `gatewayId.gateway.bedrock-agentcore.us-east-1.amazonaws.com` (contract item 6).
- All endpoints tables of the chapter count, not only the first (contract item 6).
- **`048-amazon-simple-queue-service`**: the draft missed the chapter's "Legacy endpoints"
  table (20 rows, `<region>.queue.amazonaws.com`); added from the text in table order
  (contract item 6). `af-south-1` is printed with `HTTP` only, the others `HTTP and HTTPS`;
  `queue.amazonaws.com` (us-east-1) has no Region code in it and is a `global` endpoint.
- **Rows removed by the reviewer after the PDF check (22.10).** Decision of the reviewer:
  these rows are not in the PDF or do not fall under contract items 6 / 7, so they are not
  part of the reference. They do appear in the extracted `.txt`, so `make gold-check` keeps
  listing the three hostnames; that is expected, not a new finding.
  - `033`: endpoint `kinesis.eu-south-1.amazonaws.com` (Europe (Milan));
  - `085`: endpoint `lakeformation.eu-central-1.api.aws` (Europe (Frankfurt));
  - `007`: endpoint `gatewayId.gateway.bedrock-agentcore.sa-east-1.amazonaws.com`;
  - `048`: Quota Row "Actions per Queue Policy";
  - `076`: Quota Row "Recipes per AWS account".

## Status

Checked against the PDF by the reviewer on 22.10.2026. `make gold-check` then lists only the
expected differences named above.

| File | Endpoints | Quotas | Checked |
|---|---|---|---|
| `006-amazon-aurora-dsql.json` | 25 | 4 | ✅ |
| `076-aws-glue-databrew.json` | 24 | 6 (1 removed) | ✅ |
| `033-amazon-kinesis-data-streams.json` | 79 (1 removed) | 1 | ✅ |
| `066-aws-datasync.json` | 88 | 0 (`non_standard`) | ✅ |
| `085-aws-lake-formation.json` | 87 (1 removed) | 0 (`none`) | ✅ |
| `007-amazon-bedrock-agentcore.json` | 38 (1 removed) | 0 (`none`) | ✅ |
| `005-amazon-aurora.json` | 36 | 25 | ✅ |
| `075-aws-glue.json` | 88 | 46 | ✅ |
| `048-amazon-simple-queue-service.json` | 104 (20 legacy added) | 18 (1 removed) | ✅ |
| `038-amazon-opensearch-service.json` | 183 | 0 (`non_standard`) | ✅ |

## Re-check of 25.10 (finding F18)

Grounding the gold files in their chapters (step 11, ADR-0005) found that
`038-amazon-opensearch-service.json` said `non_standard` while the chapter prints one Standard
Quota Table (the "domain and instance quotas" table: `Name | Default | Adjustable |
Description`, 5 rows). The ten other quota tables of the chapter have `Notes` instead of
`Description` or only three columns and are `non_standard` by definition — the draft of
21.10 saw those and called the whole document `non_standard`. Re-drafted from
`claude__v2__t0__val2` (whose repair call, carrying the G3 error, returned exactly the five
printed rows) and checked against the PDF by Petro on 25.10. `make gold-check` now lists
quota names and the format as well.
