"""Download the HW 2 corpus listed in data/rag/manifest.csv into data/rag/raw/.

Every document is checked against the sha256 recorded in the manifest. That hash is of the
document's cleaned text (the Document hash of chunks.jsonl), not of the file's bytes: AWS
rebuilds its PDFs and pages every few days, with a new CreationDate or new markup around the
same text (F21). A document whose text differs is not written, and the run ends with a
non-zero exit code: AWS changed the content after the manifest was recorded, and the
committed chunks.jsonl was built from the recorded version.

--record fills the empty sha256 cells from what it downloads and rewrites the
manifest. It is used once, when a document is added; a filled cell is always checked.

Usage:  python -m scripts.download_rag_corpus [--record]      (make rag-data)
"""

import argparse
import csv
import sys
import urllib.request
from collections.abc import Callable
from io import BytesIO
from pathlib import Path

from src.rag.ingest.extract_html import extract_html
from src.rag.ingest.extract_pdf import extract_pdf
from src.rag.ingest.pipeline import document_hash

MANIFEST = Path("data/rag/manifest.csv")
RAW = Path("data/rag/raw")
# a generic client name: docs.aws.amazon.com answers an empty urllib User-Agent too, but
# a browser-like one is what the pages were checked with
USER_AGENT = "Mozilla/5.0 (compatible; aws-arch-advisor-corpus/1.0)"


def fetch_url(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()


def text_sha256(data: bytes, fmt: str) -> str:
    """64-hex sha256 of the document's cleaned text: its Document hash without "sha256:"."""
    if fmt == "pdf":
        sections = extract_pdf(BytesIO(data))
    else:
        sections = extract_html(data.decode("utf-8"))
    return document_hash(sections).removeprefix("sha256:")


def download(row: dict, raw_dir: Path, *, fetch: Callable[[str], bytes]) -> Path:
    """Fetch one manifest row and write it to raw_dir/<doc_id>.<format>.

    Raises ValueError, and writes nothing, if the text does not match row["sha256"].
    """
    data = fetch(row["url"])
    digest = text_sha256(data, row["format"])
    if digest != row["sha256"]:
        raise ValueError(
            f"{row['doc_id']}: sha256 mismatch "
            f"(manifest {row['sha256'][:12]}…, downloaded {digest[:12]}…)"
        )
    path = raw_dir / f"{row['doc_id']}.{row['format']}"
    partial = path.with_name(path.name + ".part")
    partial.write_bytes(data)
    partial.replace(path)  # atomic: a crash never leaves a half-written document
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--record",
        action="store_true",
        help="fill empty sha256 cells instead of failing on them",
    )
    args = parser.parse_args()

    with MANIFEST.open(newline="") as f:
        reader = csv.DictReader(f)
        columns = list(reader.fieldnames or [])
        rows = list(reader)
    RAW.mkdir(parents=True, exist_ok=True)

    failed: list[str] = []
    recorded = 0
    for row in rows:
        try:
            if args.record and not row["sha256"]:
                data = fetch_url(row["url"])
                row["sha256"] = text_sha256(data, row["format"])
                recorded += 1
                path = download(row, RAW, fetch=lambda _url, data=data: data)
            else:
                path = download(row, RAW, fetch=fetch_url)
        # ValueError: sha256 mismatch; OSError: urllib's URLError / HTTPError, timeouts
        except (ValueError, OSError) as error:
            failed.append(f"{row['doc_id']}: {error}")
            continue
        print(f"ok  {path}  ({path.stat().st_size:,} bytes)")

    if recorded:
        with MANIFEST.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=columns, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        print(f"recorded {recorded} sha256 value(s) in {MANIFEST}")

    print(f"{len(rows) - len(failed)}/{len(rows)} documents in {RAW}/ match {MANIFEST}")
    for line in failed:
        print(f"FAILED  {line}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
