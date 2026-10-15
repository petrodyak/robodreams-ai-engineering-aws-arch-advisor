"""Split the AWS General Reference PDF into one PDF per service section.

Uses the PDF's own bookmarks ("<Service> endpoints and quotas") to find page
ranges, keeps sections of MIN..MAX pages, always keeps services from KEEP,
and writes data/pool/<slug>.pdf plus data/pool/manifest.csv.
The working subset (data/raw/) is then produced by scripts/select_docs.py.
"""

import csv
import re
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

SRC = Path(
    sys.argv[1]
    if len(sys.argv) > 1
    else "data/source/aws-general-endpoints-and-quotas.pdf"
)
OUT = Path("data/pool")
OUT.mkdir(exist_ok=True)
MIN_PAGES, MAX_PAGES, TARGET = 3, 40, 100
KEEP = [
    "Athena",
    "Aurora",
    "Glue",
    "OpenSearch",
    "Simple Storage Service",
    "Lambda",
    "Relational Database",
    "Lake Formation",
    "EMR",
    "Redshift",
    "Kinesis Data Streams",
    "DynamoDB",
    "Step Functions",
    "Bedrock AgentCore",
]

r = PdfReader(SRC)


def walk(o, d=0, out=None):
    out = [] if out is None else out
    for it in o:
        if isinstance(it, list):
            walk(it, d + 1, out)
        else:
            out.append((d, it.title, r.get_destination_page_number(it)))
    return out


secs = [(t, p) for d, t, p in walk(r.outline) if d == 1 and "endpoints and quotas" in t]
ends = [p for _, p in secs[1:]] + [len(r.pages)]
rows = []
for (title, start), end in zip(secs, ends):
    n = end - start
    service = title.replace(" endpoints and quotas", "")
    keep = any(k in service for k in KEEP)
    if not keep and not (MIN_PAGES <= n <= MAX_PAGES):
        continue
    rows.append(
        {
            "service": service,
            "start": start + 1,
            "end": end,
            "pages": n,
            "priority": int(keep),
        }
    )

# priority services first, then the rest by page count (richest tables first), cap at TARGET
rows.sort(key=lambda x: (-x["priority"], -x["pages"]))
rows = rows[:TARGET]
rows.sort(key=lambda x: x["service"].lower())

for i, row in enumerate(rows, 1):
    slug = re.sub(r"[^a-z0-9]+", "-", row["service"].lower()).strip("-")
    row["file"] = f"{i:03d}-{slug}.pdf"
    w = PdfWriter()
    for p in range(row["start"] - 1, row["end"]):
        w.add_page(r.pages[p])
    with open(OUT / row["file"], "wb") as f:
        w.write(f)

with open(OUT / "manifest.csv", "w", newline="") as f:
    wr = csv.DictWriter(
        f, fieldnames=["file", "service", "start", "end", "pages", "priority"]
    )
    wr.writeheader()
    wr.writerows(rows)

print(f"wrote {len(rows)} files, {sum(x['pages'] for x in rows)} pages total -> {OUT}/")
print("priority services:", sum(x["priority"] for x in rows))
