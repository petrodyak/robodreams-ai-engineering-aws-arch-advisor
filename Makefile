# Every target runs inside the uv-managed .venv (`uv run` syncs it first if needed).
.PHONY: install data text rag-data ingest index retrieval-candidates retrieval-eval ask eval-estimate eval eval-sweep judge-estimate score calibration-sheet calibrate eval-ci rag rag-rebuild run estimate runs-md metrics schema gold-drafts gold-check check

# One Run = model × prompt version × sampling; override, e.g. `make run SAMPLING=t05`,
# `make run MODEL=qwen2.5-7b`, `make run SAMPLING=t05 GOLD=1` (Golden Set only), or
# `make run PROMPT=v2 SET=holdout` (the Held-out Set, step 12), or `make run PROMPT=v2 PARTS=1`
# (each chapter in two calls, step 13).
MODEL ?= claude
PROMPT ?= v1
SAMPLING ?= t0
GOLD ?=
SET ?= raw
PARTS ?=
RUN_ARGS = --model $(MODEL) --prompt $(PROMPT) --sampling $(SAMPLING) --set $(SET) $(if $(GOLD),--gold) $(if $(PARTS),--parts)

# create .venv and install the locked dependencies from uv.lock
install:
	uv sync

# source PDF -> data/pool/ (100 per-service PDFs) -> data/raw/ (30 selected)
data:
	uv run python scripts/split_pdf.py
	uv run python scripts/select_docs.py

# data/raw/*.pdf -> data/raw/*.txt (text "as is", only ligatures normalized)
text:
	uv run python scripts/extract_text.py

# HW 2 corpus: data/rag/manifest.csv -> data/rag/raw/ (34 public AWS documents, sha256-checked)
rag-data:
	uv run python -m scripts.download_rag_corpus

# HW 2 ingestion: data/rag/raw/ -> data/rag/chunks.jsonl (structure-aware chunks),
# chunks_fixed.jsonl (fixed-size baseline) and ingest_manifest.json; deterministic, committed
ingest:
	uv run python -m src.rag.ingest.pipeline

# HW 2 index: embeds both chunk files (cached in .cache/embeddings.json, models in .cache/models)
# and builds Qdrant :memory: + BM25; prints the counts
index:
	uv run python -m src.rag.index

# HW 2 labelling sheet: vector top 10 + BM25 top 10 per answerable item -> evals/labels/
retrieval-candidates:
	uv run python -m scripts.retrieval_candidates

# HW 2 retrieval eval: 5 configurations of spec §5 -> evals/results/retrieval.json (local, no API)
retrieval-eval:
	uv run python -m evals.run retrieval

# HW 2 one question: make ask Q="..." -> the cited answer, its sources and the cost (one Claude call)
ask:
	uv run python -m src.rag.answer "$(Q)"

# HW 2 answer eval: the cost estimate (free), the cached answer run, and the k = 3 / 5 / 8 sweep;
# RAG_PROMPT=v2 measures another prompt version without editing config/rag.yaml (also for score)
eval-estimate:
	uv run python -m evals.run estimate $(if $(RAG_PROMPT),--prompt $(RAG_PROMPT))

eval:
	uv run python -m evals.run answers $(if $(RAG_PROMPT),--prompt $(RAG_PROMPT))

eval-sweep:
	uv run python -m evals.run sweep $(if $(RAG_PROMPT),--prompt $(RAG_PROMPT))

# HW 2 scoring: judge cost (free count), scorers + judges over the latest run, the hand-label sheet,
# and the judges' agreement / kappa with the hand labels
judge-estimate:
	uv run python -m evals.run judge-estimate $(if $(RAG_PROMPT),--prompt $(RAG_PROMPT))

score:
	uv run python -m evals.run score $(if $(RAG_PROMPT),--prompt $(RAG_PROMPT))

calibration-sheet:
	uv run python -m scripts.calibration_sheet

calibrate:
	uv run python -m evals.run calibrate

# HW 2 CI gate (spec §8, the GitHub workflow runs it): recall@5 of hybrid_rerank, cached answers and
# verdicts, score, config/eval_thresholds.yaml -> evals/results/ci/; exit 1 on a broken threshold, a stale
# cache (no ANTHROPIC_API_KEY and a miss) or more than 30 new calls
eval-ci:
	uv run python -m evals.run ci

# HW 2 in one command (D6, amended 17.11 for F25): from the committed chunks.jsonl, the version every
# result was measured on: retrieval eval, the cached answer run, score. $0 and no key on a clean clone
rag: retrieval-eval eval score

# HW 2 rebuilt from the source documents: download, ingestion, then `make rag`. AWS updates its
# documents (a new Well-Architected Framework edition on 16.11.2026), so rag-data can fail on a
# changed document's hash, and a new chunks.jsonl makes cache misses (paid calls, F25)
rag-rebuild: rag-data ingest rag

# extract all 30 documents -> results/runs/jsonl/<run_id>.jsonl (resumable)
# + a readable mirror results/runs/md/<run_id>.md, rewritten after every record
run:
	uv run python main.py $(RUN_ARGS)

# rebuild every results/runs/md/*.md from results/runs/jsonl/*.jsonl (after a layout change)
runs-md:
	uv run python -m scripts.render_runs_md

# every results/runs/jsonl/*.jsonl -> results/metrics.csv (contract items 13, 17-19)
metrics:
	uv run python -m src.extract.metrics

# input tokens and their cost before a paid run (free count_tokens endpoint)
estimate:
	uv run python main.py $(RUN_ARGS) --estimate

# the JSON Schema both models receive -> docs/service-document.schema.json
schema:
	uv run python -m scripts.export_schema

# Golden Set (data/gold/README.md): drafts from claude__v1__t0 (never overwrites a file),
# then the list of endpoint rows to check by hand against the PDF
gold-drafts:
	uv run python -m scripts.make_gold_drafts --set $(SET)

gold-check:
	uv run python -m scripts.check_gold --set $(SET)

# pre-commit gates (docs/GIT_RULES.md §1): all three always run, exit non-zero if any failed;
# `schema` first, so a schema.py change always lands in the documented schema file
check: schema
	@status=0; \
	uv run ruff check . || status=1; \
	uv run ruff format --check . || status=1; \
	uv run pytest || status=1; \
	exit $$status
