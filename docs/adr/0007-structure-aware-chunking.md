---
status: accepted
date: 2026-11-09
---

# Chunks follow the documents' sections; fixed-size windows are the measured baseline

The HW 2 brief grades the chunking strategy hardest ("justified, and compared with fixed size") and
names "fixed-length chunking because the tutorial did it" as a common mistake. The corpus is
Well-Architected PDFs and Prescriptive Guidance HTML. Both have a real structure: a PDF outline down to
single best practices (`REL09-BP01 …`), HTML headings. A citation has to name a document and a
section, and a section is what the retriever should return whole.

## Decision

- **Structure-aware.** Chunks are cut on section boundaries (the PDF outline, or the HTML `h1`–`h4`
  headings; heading patterns when a PDF has no outline). Whole paragraphs are packed up to the limit.
  A section that is too long is split at paragraphs, then lines, then sentences, then tokens. A
  section that is too short is merged with the next sibling under the same parent, and the merged
  chunk's Section Path is that parent.
- **Size: 250–450 tokens, hard maximum 480** (tiktoken `cl100k_base`). Three reasons:
  1. the embedding model (`BAAI/bge-small-en-v1.5`) reads at most 512 tokens, and the Contextual
     Header uses some of them;
  2. one Well-Architected best practice is typically a few hundred words, so one chunk ≈ one best
     practice ≈ what a citation should point to;
  3. smaller chunks would separate a best practice's statement from its implementation guidance.
- **No overlap:** sections are natural boundaries, and overlap would duplicate text across best
  practices.
- **Contextual Header** `<document title> > <Section Path>` is prepended to the text that is embedded
  and BM25-indexed, not to the text the answer model reads.
- **Baseline:** fixed windows of 400 tokens with 60 tokens of overlap, ignoring structure. Both chunk
  sets are built and indexed; the retrieval eval compares them on the same questions, and REPORT gives
  the numbers and two examples where a fixed window cut a best practice in half.

## Considered options

- **Fixed-size only** — simplest, but it cuts best practices and tables in half, and its chunks have no
  section to cite. Kept as the baseline, not as the strategy.
- **Semantic chunking** (cut where embeddings of neighbouring sentences diverge) — a brief stretch item;
  it costs an embedding pass per sentence and the documents already state their own boundaries.
- **Parent-child** (small chunks for search, the parent section for the answer) — a stretch item; one
  chunk ≈ one best practice already gives the answer model the whole unit.

## Consequences

- `data/rag/chunks.jsonl` field names (spec §4) are fixed by this decision. Stage 3 (the agent) reads
  them and calls the search API on top of them, so a rename later is a breaking change.
- A chunk can be larger than a short question needs; the context budget (3,000 tokens) holds about
  6–8 chunks, which is why k is measured at 3 / 5 / 8.
- Token counts are an approximation of the embedding tokenizer; the 480 maximum leaves a margin for
  the difference.
