# Prompt changelog

Every prompt version is one file, `prompts/extract_<version>.txt`, with three sections that
`src/extract/pipeline.py` loads:

- `=== system ===` — the instructions;
- `=== user ===` — the message with the document; placeholders `{service}` and `{document}`;
- `=== repair ===` — the one corrective message after a failed validation (contract item 16);
  placeholder `{error}`.

**What a prompt version covers.** The model sees two things: the text of this file and the JSON
Schema of `ServiceDocument`, whose `Field(description=...)` texts are instructions too (for
example the multi-Region convention for `default`). Both are part of a prompt version: a change
to either one is a new version with an entry here, so that a run id
(`<model>__<prompt_version>__<sampling_name>`) always names exactly what the model was told.

Each entry says what changed and why; from v2 on, every change is tied to a specific error seen
in the runs of the previous version.

## v1 — 2026-10-21

Baseline prompt.

- **System:** the task (one chapter of the AWS General Reference → one JSON object), the noise
  in the PDF text (wrapped cells, split Region codes and hostnames, page headers/footers,
  repeated table headers), and five rules: only the target service's chapter (Neighbour Tail),
  every endpoint row one per hostname, the three Quota Table Formats (ADR-0001), quota values as
  printed (ADR-0002), copy text without paraphrasing.
- **User:** the target service name from `data/raw/manifest.csv` and the document text inside
  `<document>` tags, so that instructions and data are clearly separated.
- **Repair:** the validation errors as a list of `field path: message`, and a request for the
  complete corrected object.
- **Schema descriptions:** as in `src/extract/schema.py` at schema version 1.
