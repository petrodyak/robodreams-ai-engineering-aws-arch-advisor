"""Small generated documents for the RAG ingestion tests (no binary fixtures in Git).

`make_pdf` writes a minimal text PDF by hand (one Helvetica font, one text block per page) and
optionally adds an outline with pypdf, so the tests control every page and bookmark exactly.
"""

from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def _escape(line: str) -> str:
    return line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _raw_pdf(pages: list[list[str]], title: str) -> bytes:
    objects: list[bytes] = []
    n_pages = len(pages)
    kids = " ".join(f"{4 + 2 * i} 0 R" for i in range(n_pages))
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objects.append(f"<< /Type /Pages /Kids [{kids}] /Count {n_pages} >>".encode())
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    for i, lines in enumerate(pages):
        body = " T* ".join(f"({_escape(line)}) Tj" for line in lines)
        stream = f"BT /F1 10 Tf 14 TL 50 780 Td {body} ET".encode()
        objects.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
            f"/Resources << /Font << /F1 3 0 R >> >> /Contents {5 + 2 * i} 0 R >>".encode()
        )
        objects.append(
            b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream"
        )
    objects.append(f"<< /Title ({_escape(title)}) >>".encode())

    out = BytesIO()
    out.write(b"%PDF-1.4\n")
    offsets = []
    for number, obj in enumerate(objects, start=1):
        offsets.append(out.tell())
        out.write(b"%d 0 obj\n" % number + obj + b"\nendobj\n")
    xref = out.tell()
    out.write(b"xref\n0 %d\n0000000000 65535 f \n" % (len(objects) + 1))
    for offset in offsets:
        out.write(b"%010d 00000 n \n" % offset)
    out.write(
        b"trailer\n<< /Size %d /Root 1 0 R /Info %d 0 R >>\nstartxref\n%d\n%%%%EOF\n"
        % (len(objects) + 1, len(objects), xref)
    )
    return out.getvalue()


def make_pdf(
    path: Path,
    pages: list[list[str]],
    outline: list[tuple[int, str, int]] = (),
    title: str = "Test Pillar - AWS Well-Architected Framework",
) -> Path:
    """Write a PDF with the given page lines and outline entries (level, title, 0-based page)."""
    writer = PdfWriter(clone_from=PdfReader(BytesIO(_raw_pdf(pages, title))))
    parents: dict[int, object] = {}
    for level, entry_title, page in outline:
        parents[level] = writer.add_outline_item(
            entry_title, page, parent=parents.get(level - 1)
        )
    writer.add_metadata({"/Title": title})
    with path.open("wb") as f:
        writer.write(f)
    return path


AWS_PAGE = """<html><head><title>Choose keys - AWS Prescriptive Guidance</title>
<script>var x = 1;</script><style>p {}</style></head>
<body><nav>Docs home > Guide</nav>
<div id="breadcrumbs">AWS > Guide > Page</div>
<div id="main-col-body">
<awsdocs-language-banner>Read in another language</awsdocs-language-banner>
<h1 class="topictitle">Choose keys</h1>
<div class="awsdocs-page-header-container"><awsdocs-page-header>PDF RSS</awsdocs-page-header></div>
<p>Intro paragraph about   keys.</p>
<h2>Sort keys</h2>
<p>Sort keys order the data.</p>
<div class="itemizedlist"><ul><li><p>First tip.</p></li><li><p>Second tip.</p></li></ul></div>
<h3>Tuning</h3>
<p>Tuning text.</p>
<h4>Deep detail</h4>
<p>Detail text.</p>
<h2>Distribution</h2>
<table><tr><th>Style</th><th>Use</th></tr><tr><td>KEY</td><td>joins</td></tr></table>
<div class="highlights"><h6>Topics</h6><ul><li><a href="x.html">Other page</a></li></ul></div>
<awsdocs-copyright>Copyright 2026</awsdocs-copyright>
<awsdocs-thumb-feedback>Did this page help you?</awsdocs-thumb-feedback>
</div>
<footer>Privacy | Terms</footer></body></html>
"""

EMPTY_PAGE = """<html><body><div id="main-col-body">
<h1>Empty</h1><awsdocs-thumb-feedback>Did this page help you?</awsdocs-thumb-feedback>
</div></body></html>"""
