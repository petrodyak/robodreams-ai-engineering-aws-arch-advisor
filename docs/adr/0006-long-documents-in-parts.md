---
status: accepted
date: 2026-10-26
---

# Long documents are extracted in parts: code splits, code merges, the prompt is the same

The lecturer's third remark of 24.10 was to *process long documents in parts*. Three
documents of the Working Set do not fit the local model's output cap in one answer (error 4
of REPORT.md: `017`, `049`, `025`, `qwen2.5-7b` writes 18,432 tokens and is cut off), and
the S3 chapter needed a raised `max_tokens` for Claude. Asked how (Q&A, 26.10), the lecturer
was specific: no separate prompts — the prompt stays the same; code splits the document
first (the endpoints table and the quotas table apart, or by pages) and makes one call per
part with only that part's text, so the document is not read twice and no tokens go to the
other parts; the short system prompt is what repeats, and prompt caching makes that cheap;
code then merges the parts' results, drops duplicates and validates; different approaches
are tried and each one is measured.

## Decision

A run in parts (`--parts`, run id suffix `__parts`, contract item 21) extracts each chapter
in **two parts**: the quotas part — the "Service quotas…" blocks of the Target Service's
chapter — and the endpoints part — everything else of the chapter. The cut is made by code
at headings (`src/extract/parts.py`); each part is sent with the unchanged prompt as a
chapter of its own, with the chapter's title line on top so that prompt rule 1 ("use only
the chapter titled …") still holds; nothing else of the document is sent. Each part is
validated and repaired like a whole document, judged only on the rows it is responsible for
(G1 for endpoints, G2 and G3 for quotas); code merges the two answers into one Service
Document, re-validates the whole against the chapter, and derives nothing. A chapter with
no quotas block has no quotas part: the merged document says `none`, which is the schema's
word for exactly that.

## Considered options

- **Two parts by section kind (chosen).** The cut is semantic — an endpoints table and a
  quotas table are never one row — so no row is cut in half, no part overlaps another, and
  the merge has nothing to de-duplicate. Checked on all 40 chapters: the endpoints part
  prints every hostname of the chapter's endpoints tables and no Standard Quota Table, the
  quotas part the reverse (`tests/test_parts.py`). The limit: a part can still be too long
  for the cap — the endpoints part of `049` is 3,300 words — and that is what the run
  measures.
- **Parts by page.** The page footers mark page ends, so the cut is easy, and every page
  fits any cap. Rejected for the first version: a row that wraps across a page break (a
  hostname, a quota name — exactly the rows step 11's readers rejoin) is cut in half, so the
  parts need an overlap and the merge a de-duplication, and every page repeats the
  instructions. Kept as the second step if the section-kind parts of `017` / `049` are still
  cut off for the local model: split only the part that was cut off, by pages.
- **Continue the answer** ("go on from the last complete row"). Rejected: not what the remark
  asks, and continuing a JSON array across calls is fragile at the seam.
- **A schema per part** (an endpoints-only and a quotas-only schema). Rejected for now: the
  shared schema is contract item 1 and its sha the provenance of every record; with the full
  schema a part simply leaves the other kind empty, and the grounding checks catch a model
  that fills it anyway (counted as `spill`).

## Consequences

- A `__parts` run is a configuration next to the whole-document run of the same model,
  prompt and sampling, and is compared with it on the same documents: validity (did the
  cut-offs go away), recall (was anything lost at the seam — by construction nothing is,
  the test says so), cost and latency (one more copy of the instructions per document, two
  sequential calls).
- A part is judged on its own fields by the schema as well as by the grounding: the other
  kind's fields are dropped from the raw answer first. The first run showed why (F20): on a
  quotas part, which prints no endpoints table, `qwen2.5:7b` invents one — up to 80 rows,
  with schemes, placeholders and quota values as hostnames — and on three documents kept
  inventing until the output cap. Dropping the rows keeps the judgement fair; the tokens
  and the time the model spends on them are measured as they are, and a note inside the
  part ("this part prints no endpoints table") is the next experiment, kept apart because
  it changes what the model is told.
- The parts see the chapter only, never the Neighbour Tails; the whole-document runs saw
  them. The report names this as a second difference between the two configurations.
- Prompt caching is not used in this version: the system prompt is ≈ 800 tokens, so the
  extra copy costs between 4 % (a long chapter) and 10 % (a short one) of a document's
  input, and the local model costs nothing. Whether the prompt is above the model's
  cacheable minimum was not checked; it is the first thing to try if the cost line matters.
- Stage 2 (RAG) starts from the same question — how to cut a document into pieces a model
  can answer about — and this is its first, measured answer.
