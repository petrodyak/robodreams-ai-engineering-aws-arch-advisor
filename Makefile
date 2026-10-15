# Every target runs inside the uv-managed .venv (`uv run` syncs it first if needed).
.PHONY: install data text

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
