# Every target runs inside the uv-managed .venv (`uv run` syncs it first if needed).
.PHONY: install data text check

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

# pre-commit gates (docs/GIT_RULES.md §1): all three always run, exit non-zero if any failed
check:
	@status=0; \
	uv run ruff check . || status=1; \
	uv run ruff format --check . || status=1; \
	uv run pytest || status=1; \
	exit $$status
