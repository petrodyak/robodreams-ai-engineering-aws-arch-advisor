# HW 2 brief — "RAG with sources and evals in CI"

40 points, deadline **13.11 23:59**. The course assignment as given (translated from Ukrainian,
carried over almost verbatim), kept here so that `CLAUDE.md` holds only what every session needs.
The design that implements it is
[`superpowers/specs/2026-11-08-hw2-rag-design.md`](superpowers/specs/2026-11-08-hw2-rag-design.md);
the working plan and status are in [`hw2-implementation-steps.md`](hw2-implementation-steps.md).

> The four **HW steps** below are grading units. They are not the same as the numbered
> **implementation steps** (14–20) in `hw2-implementation-steps.md`, whose overview table maps one to
> the other.

## Goal

Build a full slice of a RAG system on the corpus of the course project: from raw documents to answers
with references to their sources. The quality of the answers is checked by an automatic eval pipeline
that runs in CI.

```
documents (PDF / DOCX / HTML) → cleaning → chunks + metadata → vector DB (hybrid search + reranking)
→ model answer with sources → evals in CI
```

This is the second slice of the same course project as block 1 (HW 1). The agent of block 3 will work
on this corpus.

## HW steps

Each step builds on the corresponding lesson. Do them in order: each step uses the result of the
previous one.

1. **Corpus and chunking** (lesson 6, `ai-engineeering-2/lesson-06-data-ingestion`)
   - Collect a corpus for the project: ≥ 30 documents in at least 2 formats (PDF, DOCX, HTML,
     Markdown). Public documents of the subject area are fine. No personal data.
   - Write an ingestion pipeline:
     - text extraction that keeps the structure (headings, lists, tables);
     - cleaning and normalization (headers and footers, hyphenation, encoding, HTML boilerplate);
     - deduplication (content hash; optionally near-duplicates).
   - Choose a chunking strategy and justify it in the README: why this size and this way of cutting
     for these documents. Compare it with fixed-size chunking on at least a few documents.
   - Add metadata to every chunk: source, title, section, date or version, document hash.
   - Result: a chunk file (for example `chunks.jsonl`) and a manifest.

   The base is the lesson-6 practice: the own solution may be taken and adapted to the corpus.
2. **Index and hybrid search** (lesson 7, `ai-engineeering-2/lesson-07-embeddings`)
   - Compute embeddings for the chunks (a provider or a local model) and store them in a vector DB
     (Qdrant, Chroma, FAISS or similar).
   - Implement hybrid search: lexical (BM25) + vector search, with the results merged.
   - Add reranking and metadata filters (for example by date, document type or access group).
   - Measure search quality: 10–15 questions for which the right chunk is known, and the metric
     recall@k or MRR. Compare at least two configurations (vector only / hybrid / hybrid + reranking).
3. **RAG with sources** (lesson 8, `ai-engineeering-2/lesson-08-rag`)
   - The model's answer is built only from the retrieved chunks and cites the sources (document and
     section) for every claim.
   - Context control: a token budget for the context. When there is no relevant data, the system
     answers "I don't know" / "the documents do not contain this" instead of inventing.
   - Prompts live in versioned files with a changelog, as in block 1.
4. **Testset and evals in CI**
   - A testset of ≥ 20 questions with expected answers and sources. It must include questions the
     corpus has no answer to, and trap questions (similar documents, outdated versions).
   - Scoring functions:
     - deterministic where possible: the right source among the citations, presence of key facts,
       "I don't know" where it is due;
     - LLM-as-a-judge for the rest, with calibration: check the judge on 10+ answers graded by hand,
       and state how far it agrees with you;
     - a faithfulness check: is every claim of the answer supported by the context.
   - Evals run in CI (GitHub Actions or similar) on every push or pull request, with a threshold below
     which the run fails.
   - A short REPORT.md: a table of retrieval and answer metrics, an analysis of 3–5 characteristic
     errors (what was expected → what came out → why), and what to improve next.

Stretch (no points, only if time remains): semantic or parent-child chunking with a comparison;
contextual chunk headers; incremental ingestion; embedding caching.

## Dates

| Date | What |
|---|---|
| after lesson 8 | Checkpoint: HW steps 1–2 in the repo, link in the cohort chat (no points) |
| lesson 10 (Q&A) | Feedback on the checkpoint |
| 13.11 23:59 (the day after the Q&A) | Deadline: HW steps 1–4 |

## Criteria (40 points)

| HW step | Item | Points |
|---|---|---|
| 1. Corpus and chunking | Ingestion of ≥ 2 formats (PDF / DOCX / HTML) | 3 |
| | Cleaning + deduplication (content hash or embeddings) | 3 |
| | Justified chunking strategy + metadata | 4 |
| 2. Index and search | Embeddings + vector DB | 3 |
| | Hybrid search (lexical + vector) | 3 |
| | Reranking and metadata filters | 2 |
| | Retrieval quality measured (recall@k / MRR or similar) | 2 |
| 3. RAG with sources | Answers that cite their sources | 4 |
| | Context control: token budget, "I don't know" when there is no data | 4 |
| 4. Evals in CI | Testset of ≥ 20 questions with expected answers | 3 |
| | Scoring: deterministic + calibrated LLM-as-a-judge + faithfulness | 4 |
| | Evals run in CI | 3 |
| Repository | README, one-command launch, keys not in code | 2 |

Most points are for justified chunking, sources, "I don't know" and the scoring functions: that is
where RAG systems break most often.

## Common mistakes (cost points)

- Fixed-length chunking "because the tutorial did it", with no justification and no comparison.
- No "I don't know" answer, so the model invents when the corpus has no answer.
- An LLM-as-a-judge never checked against hand labels: nobody knows whether the judge is right.
- A testset generated by AI from the same documents and checked by nobody.
- Search quality not measured: "it seems to find things".

## Not needed

UI, deployment, fine-tuning, a large corpus (30–100 documents is enough), perfect accuracy.

## Technical requirements

- Python 3.10+ (we use 3.12), one-command launch (`make run` or `python main.py`; for HW 2 the command
  is `make rag`, spec decision D6).
- Any model for answers and embeddings, provider or local. State the cost per 1,000 questions if the
  model is paid.
- Keys only in `.env`; the repository holds only `.env.example`.
- Submission — a single link to the public GitHub repository:
  https://github.com/petrodyak/robodreams-ai-engineering-aws-arch-advisor

## What must be in the repository

- the code of ingestion, indexing, RAG and evals;
- `data/` — the corpus or a script that downloads it (if the documents are large or licensed), plus a
  manifest;
- `prompts/` with versions and a changelog;
- `evals/` — the testset, the scoring functions, the run results;
- `.github/workflows/` (or similar) with the eval run;
- `REPORT.md` — metrics, error analysis, conclusions (for HW 2: `REPORT-hw2.md`, because `REPORT.md`
  holds the HW 1 report; decided by Petro on 09.11);
- `README.md` — what the project is, how to run it, the justification of the chunking strategy.
