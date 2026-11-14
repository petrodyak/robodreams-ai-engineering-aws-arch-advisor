"""Download the HW 2 corpus listed in data/rag/manifest.csv into data/rag/raw/.

Every document is checked against the sha256 recorded in the manifest. A document
whose bytes differ is not written, and the run ends with a non-zero exit code. A
mismatch means AWS republished that document after the manifest was recorded.
The committed chunks.jsonl was built from the recorded version.

--record fills the empty sha256 cells from what it downloads and rewrites the
manifest. It is used once, when a document is added; a filled cell is always checked.

Usage:  python scripts/download_rag_corpus.py [--record]
"""

import argparse
import csv
import hashlib
import sys
import urllib.request
from collections.abc import Callable
from pathlib import Path

MANIFEST = Path("data/rag/manifest.csv")
RAW = Path("data/rag/raw")
# a generic client name: docs.aws.amazon.com answers an empty urllib User-Agent too, but
# a browser-like one is what the pages were checked with
USER_AGENT = "Mozilla/5.0 (compatible; aws-arch-advisor-corpus/1.0)"


def fetch_url(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()


def download(row: dict, raw_dir: Path, *, fetch: Callable[[str], bytes]) -> Path:
    """Fetch one manifest row and write it to raw_dir/<doc_id>.<format>.

    Raises ValueError, and writes nothing, if the bytes do not match row["sha256"].
    """
    data = fetch(row["url"])
    digest = hashlib.sha256(data).hexdigest()
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
                row["sha256"] = hashlib.sha256(data).hexdigest()
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
