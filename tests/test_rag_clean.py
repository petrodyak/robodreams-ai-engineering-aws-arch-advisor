"""Cleaning of extracted text (src/rag/ingest/clean.py): page furniture and normalization."""

from src.rag.ingest.clean import normalize, strip_page_furniture

HEADER = "Reliability Pillar AWS Well-Architected Framework"


def test_furniture_removed():
    pages = [
        f"{HEADER}\nBody of page {n}, with its own words.\n{n}"
        for n in (12, 13, 14, 15)
    ]
    cleaned = strip_page_furniture(pages)
    assert len(cleaned) == 4
    for n, page in zip((12, 13, 14, 15), cleaned, strict=True):
        assert HEADER not in page
        assert page.strip() == f"Body of page {n}, with its own words."


def test_running_footer_with_section_title_removed():
    # AWS PDFs end every page with "<section title> <printed page number>"
    pages = [
        f"{HEADER}\nText {i}.\nManage service quotas and constraints {15 + i}"
        for i in range(4)
    ]
    cleaned = strip_page_furniture(pages)
    assert all("Manage service quotas" not in page for page in cleaned)
    assert cleaned[0].strip() == "Text 0."


def test_number_out_of_sequence_is_kept():
    pages = [f"{HEADER}\nIntro {n}.\nFooter {n}" for n in (3, 4, 5, 6)]
    pages[1] = (
        f"{HEADER}\nUse at most\n2024"  # a year at the page end, not the page number
    )
    cleaned = strip_page_furniture(pages)
    assert "2024" in cleaned[1]


def test_one_page_keeps_lines():
    page = f"{HEADER}\nOnly page.\n7"
    assert strip_page_furniture([page]) == [f"{HEADER}\nOnly page.\n7"]


def test_normalize():
    assert normalize("ﬁle") == "file"
    assert normalize("secur-\nity") == "security"
    assert normalize("e-mail") == "e-mail"
    assert normalize("a\u200bb") == "ab"
    assert normalize("one\n\n\n\ntwo") == "one\n\ntwo"
    assert normalize("a  \t b\r\nc") == "a b\nc"


def test_normalize_unwraps_but_keeps_bullets_and_ids():
    wrapped = (
        "Foundational requirements are those whose scope extends beyond a single\n"
        "workload or project.\n"
        "• REL01-BP01 Aware of service quotas and constraints\n"
        "• REL01-BP02 Manage service quotas across accounts and regions"
    )
    out = normalize(wrapped).split("\n")
    assert out[0].endswith("single workload or project.")
    assert out[1].startswith("• REL01-BP01")
    assert out[2].startswith("• REL01-BP02")
