"""Copy a document set's per-service PDFs from data/pool/ into its folder.

Which files to copy is defined by the set's manifest.csv (column `file`), so the
selection is reproducible: pool/ holds all 100 split PDFs, raw/ holds the 30 the
extraction pipeline works on (the Working Set), holdout/ the 10 documents of the
Held-out Set (step 12). Existing files in the folder are overwritten.

Usage:  python scripts/select_docs.py [--set raw|holdout]   (default: raw)
"""

import argparse
import csv
import shutil
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
parser.add_argument("--set", choices=["raw", "holdout"], default="raw")
POOL = Path("data/pool")
RAW = Path("data") / parser.parse_args().set
MANIFEST = RAW / "manifest.csv"

rows = list(csv.DictReader(MANIFEST.open()))
missing = [r["file"] for r in rows if not (POOL / r["file"]).exists()]
if missing:
    raise SystemExit(
        f"{len(missing)} file(s) listed in {MANIFEST} are missing from {POOL}: {missing}"
    )

for r in rows:
    shutil.copy2(POOL / r["file"], RAW / r["file"])

groups = {
    g: sum(1 for r in rows if r["group"] == g)
    for g in dict.fromkeys(r["group"] for r in rows)
}
print(
    f"copied {len(rows)} PDFs {POOL}/ -> {RAW}/  groups={groups}  gold={sum(int(r['gold']) for r in rows)}"
)
