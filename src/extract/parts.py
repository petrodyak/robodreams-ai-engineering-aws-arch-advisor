"""Long documents in parts (step 13, lecturer's remark 3): code splits, code merges.

A chapter that does not fit the output cap in one answer (contract item 14; error 4 of
REPORT.md) is extracted in two parts, with the same prompt and the same schema:

- the **quotas part** — the "Service quotas…" sections of the Target Service's chapter;
  `quota_table_format` and `quotas` are taken from its answer;
- the **endpoints part** — everything else of the chapter: the endpoints sections under
  whatever heading the chapter gives them ("Service endpoints", "SMTP endpoints",
  "Service endpoint (global)" …) and the prose between them; `endpoints` are taken from
  its answer.

Each part is sent as a chapter of its own: the chapter title line, then its text, so that
prompt rule 1 ("use only the chapter titled …") still has a title to find. Nothing else of
the document goes into a call — not the Neighbour Tails — so the input tokens of the two
calls add up to about one whole-document call plus one extra copy of the instructions. The
model is never told it sees a part: the fields of the other kind in its answer (quotas in
the endpoints part, endpoints in the quotas part) are dropped before the schema sees the
answer and only counted as `spill`.

Merging is code and derives nothing (ADR-0002): the endpoints of one answer, the format
and quotas of the other, re-validated as one Service Document. A chapter with no quotas
section (`007`, `085`) gets no quotas call: the merged document says `none` with no rows,
which is what the schema means by `none`.

The cut is made at headings. A heading is a line in column 0 that is not a page footer,
has no sentence punctuation and at most twelve words; one that names quotas starts a quotas
block, one that names endpoints starts an endpoints block, any other heading ("DKIM
domains", "OpenSearch Serverless") continues the current block, and the chapter starts in
the endpoints block. Checked on all 40 chapters (step 13 log): the endpoints part prints
every hostname of the chapter's endpoints tables and no Standard Quota Table, the quotas
part the reverse.
"""

import re
from dataclasses import dataclass
from typing import Any

from src.extract.grounding import is_page_furniture, target_chapter
from src.extract.schema import (
    QuotaTableFormat,
    SchemaVersion,
    ServiceDocument,
    answer_context,
)

PART_NAMES = ("endpoints", "quotas")
PARTS_SCOPE = "__parts"  # run id suffix (contract item 11)

_PUNCTUATION_RE = re.compile(r"[.,;:]")
# The longest real heading is 11 words ("Service quotas for Tagging (Tag Editor and Resource
# Groups Tagging API)", 091); the shortest punctuation-free prose line naming endpoints or
# quotas is 13 ("The following table provides a list of Region-specific endpoints that
# Amazon Bedrock AgentCore", 007). 12 sits between them.
MAX_HEADING_WORDS = 12


def heading_kind(line: str) -> str | None:
    """ "endpoints" or "quotas" for a heading that names one, "other" for another heading,
    None for anything that is not a heading (blank, indented, page footer, prose)."""
    s = line.strip()
    if not s or line[0].isspace() or is_page_furniture(line):
        return None
    if _PUNCTUATION_RE.search(s) or len(s.split()) > MAX_HEADING_WORDS:
        return None
    low = s.lower()
    if "quota" in low:
        return "quotas"
    if "endpoint" in low:
        return "endpoints"
    return "other"


@dataclass(frozen=True)
class Parts:
    """The two parts of a chapter; "" when the chapter prints no quotas block."""

    title: str
    endpoints: str
    quotas: str

    def text(self, name: str) -> str:
        return getattr(self, name)


def split_chapter(text: str, service: str) -> Parts:
    """The Target Service's chapter as its endpoints part and its quotas part."""
    title, _, body = target_chapter(text, service).partition("\n")
    blocks: dict[str, list[str]] = {name: [] for name in PART_NAMES}
    current = "endpoints"
    for line in body.split("\n"):
        kind = heading_kind(line)
        if kind in PART_NAMES:
            current = kind
        blocks[current].append(line)
    return Parts(
        title=title.strip(),
        endpoints=_as_chapter(title, blocks["endpoints"]),
        quotas=_as_chapter(title, blocks["quotas"]),
    )


def _as_chapter(title: str, lines: list[str]) -> str:
    body = "\n".join(lines).strip("\n")
    return f"{title.strip()}\n\n{body}\n" if body else ""


def merge(
    service: str,
    endpoints_answer: ServiceDocument | None,
    quotas_answer: ServiceDocument | None,
) -> ServiceDocument:
    """One Service Document from the two part answers; `None` for a part that was not
    called because the chapter prints no block of that kind."""
    endpoints = endpoints_answer.endpoints if endpoints_answer else []
    if quotas_answer is None:
        fmt, quotas = QuotaTableFormat.NONE, []
    else:
        fmt, quotas = quotas_answer.quota_table_format, quotas_answer.quotas
    return ServiceDocument.model_validate(
        {
            "schema_version": SchemaVersion.V1.value,
            "service": service,
            "quota_table_format": fmt.value,
            "endpoints": [e.model_dump(exclude={"endpoint_type"}) for e in endpoints],
            "quotas": [q.model_dump() for q in quotas],
        },
        context=answer_context(service),
    )


OTHER_KIND = {"endpoints": "quotas", "quotas": "endpoints"}


def strip_other_kind(name: str, data: Any) -> int:
    """Drop the fields of the other kind from a part's raw answer, in place, and return
    how many rows were dropped (the part's `spill`).

    The part is judged on its own fields only (contract item 21): what the model wrote
    into the other kind is ignored before the schema sees it, so that an invented
    `endpoints` list in the quotas part — a 7B model fills the table the schema asks for
    even when the text prints none (finding F20) — cannot fail the part on format
    checks of rows the merge never reads. A non-object answer is left to the schema.
    """
    if not isinstance(data, dict):
        return 0
    other = OTHER_KIND[name]
    rows = data.get(other)
    dropped = len(rows) if isinstance(rows, list) else 0
    data[other] = []
    if name == "endpoints":
        # the format belongs to the quotas part; `none` is consistent with no rows
        data["quota_table_format"] = QuotaTableFormat.NONE.value
    return dropped


def part_rows(name: str, answer: ServiceDocument) -> int:
    """Rows of the part's own kind in its accepted answer."""
    return len(answer.endpoints) if name == "endpoints" else len(answer.quotas)
