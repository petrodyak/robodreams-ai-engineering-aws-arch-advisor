"""Extract text from the working-set PDFs: data/raw/*.pdf -> data/raw/*.txt.

The text is the extraction pipeline's input "as is": pypdf layout mode keeps
table columns aligned with spaces, and PDF noise (wrapped cells, broken words,
page headers/footers, tails of neighbouring services) is NOT cleaned.
The only change is replacing typographic ligatures (U+FB00..FB04, e.g. "ﬁ")
with plain letters: they are a font artifact, not data, and would break exact
matching of endpoints ("dsql-ﬁps...") and keyword search later in RAG.
Pages are separated by "\\n\\f" (form feed at the start of each new page), like pdftotext.

Which files to process is defined by the set's manifest.csv (column `file`): data/raw/
for the Working Set, data/holdout/ for the Held-out Set (step 12). Existing .txt files
are overwritten.

Usage:  python scripts/extract_text.py [--set raw|holdout]   (default: raw)
"""

import argparse
import csv
from pathlib import Path

from pypdf import PdfReader

parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
parser.add_argument("--set", choices=["raw", "holdout"], default="raw")
RAW = Path("data") / parser.parse_args().set
MANIFEST = RAW / "manifest.csv"
LIGATURES = str.maketrans({"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"})

rows = list(csv.DictReader(MANIFEST.open()))
missing = [r["file"] for r in rows if not (RAW / r["file"]).exists()]
if missing:
    raise SystemExit(
        f"{len(missing)} PDF(s) listed in {MANIFEST} are missing, run scripts/select_docs.py: {missing}"
    )

print(f"{'file':<52} {'group':<7} {'pages':>5} {'words':>6} {'manifest':>8}")
total = 0
for r in rows:
    pages = PdfReader(RAW / r["file"]).pages
    text = "\n\f".join(
        p.extract_text(extraction_mode="layout") for p in pages
    ).translate(LIGATURES)
    out = (RAW / r["file"]).with_suffix(".txt")
    out.write_text(text + "\n", encoding="utf-8")
    words = len(text.split())
    total += words
    # words in manifest come from the profiling step; a mismatch means the extraction differs
    flag = "" if str(words) == r["words"] else "  <- differs"
    print(
        f"{out.name:<52} {r['group']:<7} {len(pages):>5} {words:>6} {r['words']:>8}{flag}"
    )

print(f"wrote {len(rows)} .txt files to {RAW}/, {total} words total")
