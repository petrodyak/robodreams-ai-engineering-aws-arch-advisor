"""Extraction with structure (src/rag/ingest/extract_pdf.py, extract_html.py)."""

from src.rag.ingest.extract_html import extract_html
from src.rag.ingest.extract_pdf import extract_pdf
from tests.rag_fixtures import AWS_PAGE, EMPTY_PAGE, make_pdf

HEADER = "Test Pillar AWS Well-Architected Framework"
TITLE = "Test Pillar - AWS Well-Architected Framework"


def _page(n: int, *lines: str) -> list[str]:
    # every page carries the running header and the "<section> <n>" footer of AWS PDFs
    return [HEADER, *lines, f"Some section {n}"]


def _pillar(tmp_path, outline):
    pages = [
        _page(1, TITLE, "Abstract text of the pillar."),
        _page(
            2, "Failure management", "Failure management keeps the workload running."
        ),
        _page(
            3,
            "REL09-BP01 Identify data",
            "Identify all data that needs to be backed up.",
            "Implementation guidance",
            "Use AWS Backup for the inventory.",
        ),
        _page(4, "REL09-BP02 Secure backups", "Encrypt every backup at rest."),
    ]
    return make_pdf(tmp_path / "pillar.pdf", pages, outline, title=TITLE)


def test_pdf_sections_follow_outline(tmp_path):
    outline = [
        (0, TITLE, 0),
        (1, "Failure management", 1),
        (2, "REL09-BP01 Identify data", 2),
        (2, "REL09-BP02 Secure backups", 3),
    ]
    sections = extract_pdf(_pillar(tmp_path, outline))
    by_path = {tuple(s.path): s for s in sections}
    bp01 = by_path[("Failure management", "REL09-BP01 Identify data")]
    assert bp01.page_start == 3
    assert bp01.text.startswith("REL09-BP01 Identify data")
    assert "Use AWS Backup" in bp01.text
    assert all(HEADER not in s.text and "Some section" not in s.text for s in sections)
    # the document title is never part of a path
    assert all(TITLE not in s.path for s in sections)


def test_pdf_title_split_inside_page(tmp_path):
    outline = [
        (0, TITLE, 0),
        (1, "Failure management", 1),
        (2, "REL09-BP01 Identify data", 2),
        (3, "Implementation guidance", 2),
        (2, "REL09-BP02 Secure backups", 3),
    ]
    sections = extract_pdf(_pillar(tmp_path, outline))
    paths = [s.path for s in sections]
    guidance = [
        "Failure management",
        "REL09-BP01 Identify data",
        "Implementation guidance",
    ]
    assert guidance in paths
    second = sections[paths.index(guidance)]
    assert second.text.startswith("Implementation guidance")
    first = sections[paths.index(guidance[:2])]
    assert "Use AWS Backup" not in first.text


def test_pdf_wrong_outline_page_is_searched_forward(tmp_path):
    # real Well-Architected outlines point deep entries to a wrong, earlier page
    outline = [
        (0, TITLE, 0),
        (1, "Failure management", 1),
        (2, "REL09-BP01 Identify data", 2),
        (3, "Implementation guidance", 0),
        (2, "REL09-BP02 Secure backups", 3),
    ]
    sections = extract_pdf(_pillar(tmp_path, outline))
    guidance = next(s for s in sections if s.path[-1:] == ["Implementation guidance"])
    assert guidance.page_start == 3
    assert guidance.path[-2] == "REL09-BP01 Identify data"


def test_pdf_front_text_kept_unless_cover(tmp_path):
    # the archived 2020 edition: its first page, before any outline entry, says it is archived
    pages = [
        _page(
            1, "This paper has been archived.", "The latest version is available at: x"
        ),
        _page(
            2, "Failure management", "Failure management keeps the workload running."
        ),
    ]
    pdf = make_pdf(
        tmp_path / "old.pdf", pages, [(0, "Failure management", 1)], title=TITLE
    )
    sections = extract_pdf(pdf)
    assert sections[0].path == []
    assert "has been archived" in sections[0].text

    # a current edition: the first entry is the cover page, named like the document
    pages = [["Test Pillar", "Copyright © 2026 Amazon Web Services"], *pages[1:]]
    outline = [(0, "Test Pillar", 0), (0, "Failure management", 1)]
    pdf = make_pdf(tmp_path / "new.pdf", pages, outline, title=TITLE)
    assert all("Copyright" not in s.text for s in extract_pdf(pdf))


def test_pdf_without_outline_uses_patterns(tmp_path):
    sections = extract_pdf(_pillar(tmp_path, outline=[]))
    paths = [s.path for s in sections]
    assert ["REL09-BP01 Identify data"] in paths
    assert ["REL09-BP02 Secure backups"] in paths
    bp02 = sections[paths.index(["REL09-BP02 Secure backups"])]
    assert "Encrypt every backup" in bp02.text


def test_html_article_only():
    sections = extract_html(AWS_PAGE)
    text = "\n".join(s.text for s in sections)
    for noise in (
        "Docs home",
        "AWS > Guide",
        "var x",
        "Read in another",
        "PDF RSS",
        "Other page",
        "Copyright",
        "Did this page",
        "Privacy",
    ):
        assert noise not in text, noise
    paths = [s.path for s in sections]
    assert paths == [
        [],
        ["Sort keys"],
        ["Sort keys", "Tuning"],
        ["Sort keys", "Tuning", "Deep detail"],
        ["Distribution"],
    ]
    assert sections[0].text == "Intro paragraph about keys."
    assert "- First tip.\n- Second tip." in sections[1].text
    assert "| Style | Use |" in sections[4].text
    assert "| KEY | joins |" in sections[4].text
    assert all(s.page_start is None and s.page_end is None for s in sections)


def test_html_empty_article():
    assert extract_html(EMPTY_PAGE) == []
