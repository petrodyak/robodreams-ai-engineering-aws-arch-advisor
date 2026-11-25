"""Test-only wrapper around the MCP server: write the names of its environment variables to the
file given as the first argument, then become the server (os.execv). Used by
tests/test_mcp_stdio.py to check that no key reaches the server process (spec §9)."""

import os
import sys
from pathlib import Path

Path(sys.argv[1]).write_text("\n".join(sorted(os.environ)), encoding="utf-8")
os.execv(sys.executable, [sys.executable, "-m", "src.mcp_server"])
