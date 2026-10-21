# Every target runs inside the uv-managed .venv (`uv run` syncs it first if needed).
.PHONY: install data text run estimate schema check

# One Run = model × prompt version × sampling; override, e.g. `make run SAMPLING=t05`.
MODEL ?= claude
PROMPT ?= v1
SAMPLING ?= t0
RUN_ARGS = --model $(MODEL) --prompt $(PROMPT) --sampling $(SAMPLING)

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

# extract all 30 documents -> results/runs/<model>__<prompt>__<sampling>.jsonl (resumable)
run:
	uv run python main.py $(RUN_ARGS)

# input tokens and their cost before a paid run (free count_tokens endpoint)
estimate:
	uv run python main.py $(RUN_ARGS) --estimate

# the JSON Schema both models receive -> docs/service-document.schema.json
schema:
	uv run python -m scripts.export_schema

# pre-commit gates (docs/GIT_RULES.md §1): all three always run, exit non-zero if any failed;
# `schema` first, so a schema.py change always lands in the documented schema file
check: schema
	@status=0; \
	uv run ruff check . || status=1; \
	uv run ruff format --check . || status=1; \
	uv run pytest || status=1; \
	exit $$status
