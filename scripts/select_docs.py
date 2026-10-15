"""Copy the working subset of per-service PDFs from data/pool/ into data/raw/.

Which files to copy is defined by data/raw/manifest.csv (column `file`), so the
selection is reproducible: pool/ holds all 100 split PDFs, raw/ holds only the
30 the extraction pipeline works on. Existing files in raw/ are overwritten.

Usage:  python scripts/select_docs.py
"""
import csv
import shutil
from pathlib import Path

POOL = Path("data/pool")
RAW = Path("data/raw")
MANIFEST = RAW / "manifest.csv"

rows = list(csv.DictReader(MANIFEST.open()))
missing = [r["file"] for r in rows if not (POOL / r["file"]).exists()]
if missing:
    raise SystemExit(f"{len(missing)} file(s) listed in {MANIFEST} are missing from {POOL}: {missing}")

for r in rows:
    shutil.copy2(POOL / r["file"], RAW / r["file"])

groups = {g: sum(1 for r in rows if r["group"] == g) for g in dict.fromkeys(r["group"] for r in rows)}
print(f"copied {len(rows)} PDFs {POOL}/ -> {RAW}/  groups={groups}  gold={sum(int(r['gold']) for r in rows)}")
