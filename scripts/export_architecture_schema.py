"""Write architectures/architecture.schema.json from the Pydantic `Architecture` model (spec §9).

Generated, never edited by hand: `make check` runs this script first, and
tests/test_mcp_registry.py fails if the file is stale. Rewritten only when its content changes.

Usage:  python -m scripts.export_architecture_schema
"""

import json

from src.mcp_server.registry import REGISTRY, Architecture

path = REGISTRY / "architecture.schema.json"
text = json.dumps(Architecture.model_json_schema(), indent=2) + "\n"
if path.exists() and path.read_text(encoding="utf-8") == text:
    print(f"{path} is up to date")
else:
    path.write_text(text, encoding="utf-8")
    print(f"wrote {path}")
