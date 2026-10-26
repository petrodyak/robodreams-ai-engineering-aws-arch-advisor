# aws-arch-advisor — Extraction

The language of stage 1: turning one per-service PDF from the *AWS General Reference* into
one structured record of that service's endpoints and quotas, and measuring how well two
models do it. Terms here are concepts, not implementation details.

## Data set

**Pool**:
All 100 per-service PDFs cut from the AWS General Reference by its bookmarks (`data/pool/`).
_Avoid_: corpus, dataset, all documents

**Working Set**:
The 30 documents from the Pool that the extraction pipeline actually runs on (`data/raw/`).
_Avoid_: raw set, sample, subset

**Group**:
One of three difficulty tiers a Working Set document belongs to: `short`, `medium`, `edge`.
_Avoid_: tier, category, bucket

**Golden Set**:
The 10 Working Set documents whose Service Document was produced by a model and then checked
and corrected by hand against the PDF; the reference every model run is scored against.
_Avoid_: ground truth, labels, gold data, test set

**Target Service**:
The single AWS service a document is about, as named in the manifest. Only its data counts.
_Avoid_: the service, main service

**Neighbour Tail**:
Text from the previous or next service that leaks into a document because the Pool was cut by
whole pages. It is left in the text and must be ignored by extraction.
_Avoid_: spillover, noise, garbage

## Extraction result

**Service Document**:
The one structured record extracted from one Working Set document: the Target Service, its
Endpoint Rows and its Quota Rows. The same shape is used for model output and for the Golden Set.
_Avoid_: extraction, result, output JSON, record

**Endpoint Row**:
One line of a service's *Service endpoints* table: one region name, one region code, one
endpoint hostname, one protocol. A region with two hostnames has two Endpoint Rows.
_Avoid_: endpoint (for the row), region entry

**Endpoint Type**:
The kind of an Endpoint Row's hostname (FIPS, dual-stack, FIPS + dual-stack, IPv4, global),
derived from the hostname itself; it is not printed in the table.
_Avoid_: endpoint kind, endpoint flavour

**Quota Row**:
One line of a service's Standard Quota Table: name, default, adjustable, description.
_Avoid_: limit, quota (for the row), service quota entry

**Standard Quota Table**:
A *Service quotas* table with exactly the columns `Name | Default | Adjustable | Description`.
Only its rows become Quota Rows.
_Avoid_: quotas table, the limits table

**Quota Table Format**:
What a document's *Service quotas* section contains: `standard` (a Standard Quota Table),
`non_standard` (quotas in another layout, e.g. per-region throttling tables) or `none`.
_Avoid_: has quotas, quota flag

## Evaluation

**Run**:
One model with one prompt version and one sampling configuration applied to the whole
Working Set; identified as `<model>__<prompt_version>__<sampling_name>`.
_Avoid_: experiment, batch, job, pass

**Run Record**:
What a Run produced for one document: the Service Document (or none), its validation status
(`ok`, `repaired`, `failed`), latency and token usage.
_Avoid_: result, row, output line

**Part**:
One of the two pieces a chapter is cut into for a run in parts (contract item 21): the
quotas part (its "Service quotas…" blocks) and the endpoints part (everything else). Each
is asked for with the same prompt, as a chapter of its own, and judged on its own rows; code
merges the two answers into one Service Document.
_Avoid_: chunk, segment, page

**Repaired**:
A Run Record whose first answer failed validation and whose single corrective call succeeded.
Counted separately from `ok` because "valid on first try" and "valid after repair" are
different measurements.
_Avoid_: fixed, retried
