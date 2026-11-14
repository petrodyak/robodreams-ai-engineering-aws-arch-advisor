# Every target runs inside the uv-managed .venv (`uv run` syncs it first if needed).
.PHONY: install data text rag-data run estimate runs-md metrics schema gold-drafts gold-check check

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
	uv run python scripts/download_rag_corpus.py

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
