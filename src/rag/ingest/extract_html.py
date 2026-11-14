"""HTML -> sections, adapted from the lesson-6 `extract_html` (spec §4).

AWS documentation pages keep the article in `#main-col-body`; everything else on the page
(navigation, breadcrumbs, the language banner, the "Topics" link list, copyright, the
"Did this page help you?" widget) is boilerplate. `h1` is the page title, which is already the
document title, so `h2`-`h4` build the section path. Lists become "- " lines and tables
"| a | b |" rows, so the chunker can keep them whole.
"""

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

from src.rag.ingest.clean import normalize
from src.rag.models import Section

DROP_TAGS = [
    "script",
    "style",
    "nav",
    "footer",
    "header",
    "aside",
    "noscript",
    "form",
    "button",
]
DROP_SELECTORS = (
    "[id*=breadcrumb], [class*=breadcrumb], [id*=feedback], [class*=feedback], "
    ".highlights, .awsdocs-page-header-container"
)
HEADINGS = {"h2": 2, "h3": 3, "h4": 4}


def _text(el: Tag) -> str:
    return " ".join(el.get_text().split())


def _table(el: Tag) -> str:
    rows = [
        [_text(cell) for cell in tr.find_all(["th", "td"])] for tr in el.find_all("tr")
    ]
    rows = [r for r in rows if any(r)]
    if not rows:
        return ""
    lines = ["| " + " | ".join(r) + " |" for r in rows]
    lines.insert(1, "| " + " | ".join("---" for _ in rows[0]) + " |")
    return "\n".join(lines)


def _blocks(root: Tag):
    """Yield ("heading", level, text) and ("block", kind, text) in document order."""
    for child in root.children:
        if isinstance(child, Comment):
            continue
        if isinstance(child, NavigableString):
            if child.strip():
                yield ("block", "p", " ".join(child.split()))
            continue
        name = child.name
        if name in HEADINGS:
            yield ("heading", HEADINGS[name], _text(child))
        elif name == "h1":
            continue
        elif name in ("p", "h5", "h6", "dt", "dd"):
            if text := _text(child):
                yield ("block", "p", text)
        elif name == "pre":
            yield ("block", "pre", child.get_text().strip("\n"))
        elif name in ("ul", "ol"):
            items = [_text(li) for li in child.find_all("li", recursive=False)]
            if items := [f"- {item}" for item in items if item]:
                yield ("block", "list", "\n".join(items))
        elif name == "table":
            if table := _table(child):
                yield ("block", "table", table)
        else:
            yield from _blocks(child)


def extract_html(html: str) -> list[Section]:
    """Sections of one HTML page; [] when the article has no text."""
    soup = BeautifulSoup(html, "html.parser")
    # pick the article first, then clean inside it: on AWS pages <awsdocs-view> wraps the whole
    # main column, so dropping every awsdocs-* tag page-wide would drop the article too
    root = soup.select_one("#main-col-body") or soup.find("main") or soup.body or soup
    junk = root(DROP_TAGS) + root.select(DROP_SELECTORS)
    junk += root.find_all(lambda t: t.name.startswith("awsdocs-"))
    for tag in junk:
        if not tag.decomposed:
            tag.decompose()

    sections: list[Section] = []
    stack: list[tuple[int, str]] = []
    blocks: list[str] = []

    def flush() -> None:
        body = "\n\n".join(blocks).strip()
        blocks.clear()
        if not body:
            return
        path = [t for _, t in stack]
        text = f"{path[-1]}\n\n{body}" if path else body
        sections.append(Section(path=path, text=text))

    for kind, detail, text in _blocks(root):
        if kind == "heading":
            flush()
            while stack and stack[-1][0] >= detail:
                stack.pop()
            stack.append((detail, text))
        elif detail == "pre":
            blocks.append(text.rstrip())  # code keeps its own lines
        else:
            blocks.append(normalize(text))
    flush()
    return sections
