# Data notes

What the dataset is, how it was prepared, and the quirks we decided to live with. Read this before
touching `data/`, the prompts, or the golden set. The schema the data is extracted into is
[`stage1-data-contract.md`](stage1-data-contract.md); terms are in [`GLOSSARY.md`](../GLOSSARY.md).

## Dataset

- Source: `data/source/aws-general-endpoints-and-quotas.pdf` (25 MB, not in Git), split by PDF
  bookmarks into 100 per-service PDFs in `data/pool/` (`scripts/split_pdf.py`).
- `data/pool/manifest.csv` + `profile.csv` (in Git): words, endpoint rows, FIPS / dual-stack /
  quotas markers for each file.
- Working set: **30 documents** in `data/raw/`, listed in `data/raw/manifest.csv` with the columns
  `file, service, group (short|medium|edge), gold (1 = in the golden set), priority, pages, words,
  endpoint_rows, note`. All 16 `priority=1` services are included. `scripts/select_docs.py` copies
  them from `pool/` to `raw/` by the manifest.
  - `short` (~10): 1–2 pages, endpoints + a few quotas — the baseline for the local 7B model;
  - `medium` (~10): 3–6 pages, several quota tables — this is where prompt differences show;
  - `edge` (~10): long / FIPS / dual-stack / footnotes / no quotas — for error analysis.
- Groups were split **by words, not pages**: tables are sparse (4 pages = 489 words, 39 pages =
  4,020 words). The 0.5k–5k word range ≈ 0.7k–8k tokens — all of it fits into the qwen2.5:7b context.
- Documents of 20+ pages (EC2, S3, IAM) are not used in HW 1 — they do not fit into the local model's
  context.
- `093-aws-services.pdf` is not a service (a summary list) — excluded.
- **Golden set: 10 of 30** (`gold=1`) in `data/gold/`. Model-assisted, human-verified: a draft
  from the `claude__v1__t0` run → `data/gold/<name>.json` → manual correction against the PDF;
  documented as such.
  - **Selection (decision of 21.10): 6 `short` / 3 `medium` / 1 `edge`** — `006`, `076`, `085`,
    `033`, `007`, `066` / `005`, `075`, `048` / `038`. It replaced the first selection of 3–4 per
    group (`042`, `004`, `095`, `010` out; `085`, `033`, `066`, `075` in). **Why:** the manual
    check against the PDF is the largest block of Petro's time before the deadline, and short
    documents (4–12 pages) take a fraction of the time of edge ones (16–26 pages).
  - **Limits this sets on the metrics** (the report states them):
    - *`edge` rests on one document (`038` OpenSearch).* Per-field accuracy for the `edge` group
      is an anecdote, not a measurement; the group breakdown in REPORT is read for `short` and
      `medium` only. Errors on long, FIPS-heavy or quota-heavy documents (S3, DynamoDB, EMR) are
      shown through validity (`% ok`, truncation) and the error analysis, not through accuracy.
    - *All three Quota Table Formats are still in gold* (corrected 22.10: the first version of
      this note said `non_standard` was missing — it relied on the manifest notes, not on the
      checked files). `standard`: six files; `none`: `007`, `085`; `non_standard`: `066`, `038`,
      both confirmed against the PDF. So `quota_table_format` accuracy covers every value;
      Redshift `042` (`none` in the draft) is left to the error analysis.
    - *No global service in gold* (CloudFront `010` left it). `endpoint_type` is excluded from
      accuracy anyway (contract item 6), so only the error analysis can show how a model handles
      the 3-row global table.

**Affects later stages:** the file names and the JSON format are fixed — `raw/*.txt` and
`gold/*.json` are reused by RAG (stage 2) and by the agent (stage 3).

## Held-out Set (step 12, 25.10)

- **10 documents in `data/holdout/`**, never used while writing prompt v2 (contract item 20):
  selected from the 69 pool documents outside the Working Set by a fixed rule (seed 20261025,
  under 20 pages, `093` excluded). **No `short` document was left in the pool** — the Working
  Set took all ten of them — so the set is 6 `medium` (1,275–1,624 words) and 4 `edge`
  (2,417–2,929 words): on average harder than the Working Set, which the report states.
- **Gold for 5 of the 10**, the five lightest `medium` documents (`027`, `068`, `051`, `028`,
  `073`; 39–88 endpoint rows each), in `data/holdout/gold/`. Drafted from
  `claude__v2__t0__holdout__gold__val2` — so, unlike the step 5 drafts, every drafted row is
  grounded in the chapter (ADR-0005) — and checked by hand against the PDF.
- Same text extraction as the Working Set (`scripts/extract_text.py --set holdout`); word
  counts match the pool profile for all ten.

## Text extraction

- `scripts/extract_text.py` — `pypdf` layout mode → 30 `.txt` files in `data/raw/`; pages are
  separated by `\f`.
- The text is **not cleaned**. The only change is ligatures `ﬀ ﬁ ﬂ ﬃ ﬄ` → plain letters (decision made).

## What makes the data "dirty"

Varying length; missing fields (no quotas, "Not supported", "—"); PDF-extraction noise (broken
columns, wrapped lines, merged cells, footnotes, running headers/footers). There are no typos and no
mixed languages — the README ("Why this is not just table parsing") says exactly that.

## Known quirks (decisions made)

- **Neighbouring services' tails are left as is.** Splitting by bookmarks is page-based, so a file's
  first page contains the end of the previous service (e.g. `006-aurora-dsql` has a chunk of Aurora
  quotas), and a service's own quotas can leak into the next file. The prompt must extract only the
  target service; the golden set contains only the target service's data (see Neighbour Tail in the
  glossary).
- Missing fields occur naturally: no quotas table (`007`, `042`, `047`), "N/A" (`047`, `048`), global
  services with 3 endpoint rows (`010`, `074`).
- Broken words (`ap-\nsoutheast-4`) and running headers/footers "AWS General Reference … Version 1.0
  NNN". Ligatures are already normalised in the `.txt` files.

## HW 2 corpus (data/rag/, step 15–16)

What the 34 documents of `data/rag/manifest.csv` look like to the ingestion code, and what was decided:

- **AWS rebuilds the files.** Every PDF gets a new `CreationDate` every few days and the HTML pages new
  markup around the same text (18 of 34 changed bytes within a day). The manifest therefore records the
  hash of the cleaned text, not of the bytes (F21).
- **PDF outlines are partly wrong.** Deep entries ("Implementation guidance", "Resources") point to the
  same early page for every best practice. Titles are searched as text lines instead; an entry whose
  title is not found nearby is skipped and its text stays with the parent.
- **Running header and footer.** Every page starts with "<Pillar> AWS Well-Architected Framework" and
  ends with "<section title> <page number>". The first is dropped as a line on > 50 % of pages, the
  second when its number fits the page numbering (so a year or a quota at the page end is kept).
- **Front matter.** The cover (copyright) and the table of contents are dropped. The archived July 2020
  Framework edition keeps its first page, which says "This paper has been archived" with a link to
  the latest version: the evidence for the outdated-version trap.
- **The Framework repeats the pillars.** The current Framework PDF (1,003 pages) contains every pillar's
  best practices in its appendix. 1,057 chunks are exact duplicates; each stays in the pillar.
- **PDF tables come out as narrow columns.** pypdf extracts table cells as short wrapped lines, which is
  most of the 24 structure chunks that "start mid-sentence". Not fixed: it is extraction noise.
- **HTML.** The article is `#main-col-body`; `<awsdocs-view>` wraps the whole page, so `awsdocs-*`
  tags are dropped only inside the article (language banner, copyright, "Did this page help you?").

