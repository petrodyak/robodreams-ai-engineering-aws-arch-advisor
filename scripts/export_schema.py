"""Write the JSON Schema both models receive to docs/service-document.schema.json.

The file is a readable, versioned copy of `llm_schema()` (src/extract/llm/base.py), i.e.
ServiceDocument after `anthropic.transform_schema`, not the raw Pydantic schema. It is
generated, never edited by hand: `make check` runs this script first, and
tests/test_schema.py fails if the file is stale. The file is rewritten only when its
content changes, so an unchanged schema leaves no diff and no new mtime.

Usage:  python -m scripts.export_schema   (from the repository root: it imports src)
"""

from src.extract.llm import SCHEMA_FILE, llm_schema_json

text = llm_schema_json()
if SCHEMA_FILE.exists() and SCHEMA_FILE.read_text() == text:
    print(f"{SCHEMA_FILE} is up to date")
else:
    SCHEMA_FILE.write_text(text)
    print(f"wrote {SCHEMA_FILE}")
