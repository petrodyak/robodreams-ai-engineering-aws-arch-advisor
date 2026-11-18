# aws-arch-advisor — Extraction

The language of stage 1: turning one per-service PDF from the *AWS General Reference* into
one structured record of that service's endpoints and quotas, and measuring how well two
models do it. Terms here are concepts, not implementation details.
Stage 2 (RAG, HW 2) has its own section at the end: **RAG (stage 2)**.

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

## RAG (stage 2)

The language of stage 2: answering AWS architecture questions from public AWS guidance, with a
source for every claim, and measuring how well retrieval and answers work. A stage-1 word keeps its
stage-1 meaning; where a stage-2 word sounds similar, the entry says how they differ.

**Well-Architected**:
Short for the *AWS Well-Architected Framework* and its documents: the Framework itself, its six
pillars and its lenses.
_Avoid_: WA (unclear), AWS WAF (that is the Web Application Firewall, a different service that the
corpus itself describes)

**Prescriptive Guidance**:
AWS Prescriptive Guidance: HTML guides and patterns on docs.aws.amazon.com; the second format of the
Corpus.
_Avoid_: PG, AWS docs

**Corpus**:
The 30+ public documents stage 2 answers from (`data/rag/manifest.csv`): Well-Architected PDFs and
Prescriptive Guidance HTML pages. Not the stage-1 Pool, which stays "Pool".
_Avoid_: dataset, knowledge base, Pool

**Corpus Document**:
One row of the corpus manifest: one PDF or one HTML page, with its `doc_id`, `doc_type`
(`framework`, `pillar`, `lens`, `guide`) and `published` date.
_Avoid_: file, source (a Source is what an answer cites)

**Section Path**:
The chain of headings above a piece of text inside a Corpus Document, e.g. `Failure management >
Back up data > REL09-BP01 …`. Taken from the PDF outline or the HTML headings; it is what a citation
names besides the document.
_Avoid_: breadcrumb, heading, chapter

**Chunk**:
One retrievable piece of a Corpus Document with its metadata (a line of `data/rag/chunks.jsonl`, or of
`chunks_fixed.jsonl` for the fixed-size baseline).
Not a stage-1 Part, which is a piece of a chapter sent to the extraction model.
_Avoid_: passage, segment, Part

**Chunking Strategy**:
How a Corpus Document is cut into Chunks: `structure` (on section boundaries, a target of 250–450 tokens, no
overlap, ADR-0007) or `fixed` (400-token windows with a 60-token overlap, the measured baseline).
_Avoid_: splitter, chunker settings

**Contextual Header**:
`<document title> > <Section Path>`, put in front of a Chunk's text for embedding and BM25 only, never
shown to the answer model as part of the text.
_Avoid_: prefix, title line

**Hit**:
One Chunk returned by search, with its score and rank.
_Avoid_: result, match, document

**Source Label**:
The `[S1]`, `[S2]` … tag a Chunk gets when it is put into the answer model's context; a Claim cites
Source Labels, code maps them back to document + Section Path.
_Avoid_: reference number, footnote

**Claim**:
One statement of an answer, with the Source Labels that support it. "A source for every claim" is
checked per Claim, by code.
_Avoid_: sentence, fact

**Abstain**:
The fixed answer "The documents available to me do not answer this question." given instead of a
guess when the Corpus has no answer.
_Avoid_: refusal (a refusal is the model declining a request), fallback

**Testset Item**:
One question of `evals/testset.jsonl` with its kind, expected answer, key facts, expected sources and
relevant Chunks, checked by Petro (`verified_by`).
_Avoid_: test case, golden question (the Golden Set is stage 1)

**Trap**:
A Testset Item built to catch a typical RAG failure: *similar documents* (a pillar and a lens on the
same topic) or *outdated version* (an older edition or a revisions table).
_Avoid_: tricky question, adversarial question

**Judge**:
The LLM (`claude-sonnet-5-5`) that grades an answer where code cannot: correctness against the
expected answer, and faithfulness of each Claim to its sources.
_Avoid_: grader, evaluator model

**Calibration Set**:
The ≥ 12 answers Petro graded by hand (`evals/labels/calibration.jsonl`); the Judge's agreement with
them (% and Cohen's κ) is what makes a Judge number reportable.
_Avoid_: labels, ground truth

**Eval Cache**:
Answers and Judge verdicts stored in Git (`evals/cache/`), keyed by model, effort, prompt and input,
so a CI run calls Claude only for what changed (ADR-0008).
_Avoid_: snapshot, fixture
