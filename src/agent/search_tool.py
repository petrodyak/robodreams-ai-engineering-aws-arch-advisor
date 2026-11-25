"""`search_corpus`: the HW 2 search as a tool of the agent (spec §5, §10, ADR-0011).

- The search itself is `src/rag/search.py` in `hybrid_rerank` mode over the frozen HW 2 chunks, plus
  the agent's overlay when it is on (D22): no code of `src/rag/` changes.
- `search` runs in the worker thread and touches no SQLite; `label` runs on the main thread and
  assigns the session labels (spec §9 "Threads").
- Labels run across the session (`[S1]`–`[S5]`, then `[S6]`–`[S10]` …) and a chunk keeps its first
  label, so a label always means one chunk. A chunk already sent in the current request is not sent
  again: its tag says so and carries no text.
- Retrieved text is data (ADR-0011): every chunk is wrapped in a `<document>` tag, and a closing tag
  inside a chunk's own text is neutralised, so a planted chunk cannot end its tag early.
- The reranker score is an uncalibrated logit; the relevance band (`high` / `low`) is shown only when
  a threshold was measured (spec §10, Task 22.4 Step 5).
"""

import json
import re
from datetime import date
from html import escape
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field

from src.agent.store import Store
from src.agent.tools import ToolOutcome
from src.rag.config import RagConfig
from src.rag.index import Index, default_embed_fn, default_rerank_fn, load_chunks
from src.rag.ingest.chunk import header
from src.rag.models import ChunkRecord, DocType
from src.rag.search import Filters, Hit, search

CHUNKS_PATH = Path("data/rag/chunks.jsonl")
OVERLAY_PATH = Path("data/agent/adversarial_chunks.jsonl")
SUPERSEDES_PATH = Path("data/agent/supersedes.json")
OVERLAY_DOC = "agent-overlay-adversarial"  # the planted chunk's doc_id; never a finding's source (§8)
# any <document or </document inside a chunk's own text, in any case (ADR-0011)
_TAG = re.compile(r"<(/?)(document)", flags=re.IGNORECASE)
NOTHING_FOUND = (
    "no documents matched; try another query or say the corpus does not cover it"
)
# A Well-Architected best-practice id: 3-7 capital letters, two digits, -BP, two digits (spec §8;
# 6-7 letters for the Generative AI and Machine Learning lenses, e.g. GENSEC01-BP01).
BP_ID = re.compile(r"\b[A-Z]{3,7}\d{2}-BP\d{2}\b")


class SearchArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(min_length=3, max_length=200)
    doc_types: list[DocType] | None = None
    published_from: date | None = None


def load_overlay(path: Path = OVERLAY_PATH) -> list[ChunkRecord]:
    """The planted chunks of the adversarial overlay: complete ChunkRecords of `OVERLAY_DOC` (§10)."""
    chunks = load_chunks(path)
    stray = [c.chunk_id for c in chunks if c.doc_id != OVERLAY_DOC]
    if stray:
        raise ValueError(
            f"overlay chunks must have doc_id {OVERLAY_DOC!r}: {', '.join(stray)}"
        )
    return chunks


def load_supersedes(path: Path = SUPERSEDES_PATH) -> dict[str, str]:
    """`{older doc_id: newer doc_id}`: real edition metadata, always on (§10)."""
    return json.loads(path.read_text(encoding="utf-8"))


def edition_note(
    chunk: ChunkRecord, supersedes: dict[str, str], published_by_doc: dict[str, date]
) -> str | None:
    """`older edition (2020-07-01), superseded by wa-framework (2024-11-06)`, or None (§10).

    Only a chunk of a superseded document gets a note: two different documents with different
    `published` dates are not a conflict.
    """
    newer = supersedes.get(chunk.doc_id)
    if newer is None:
        return None
    note = f"older edition ({chunk.published.isoformat()}), superseded by {newer}"
    if newer in published_by_doc:
        note += f" ({published_by_doc[newer].isoformat()})"
    return note


def build_agent_index(
    rag_cfg: RagConfig,
    *,
    overlay: bool,
    embed_fn=None,
    rerank_fn=None,
    chunks_path: Path = CHUNKS_PATH,
    overlay_path: Path = OVERLAY_PATH,
) -> Index:
    """The HW 2 chunks, plus the adversarial overlay when `overlay` (spec §10, D22)."""
    chunks = load_chunks(chunks_path)
    if overlay:
        if not overlay_path.exists():
            raise FileNotFoundError(f"overlay is on but {overlay_path} does not exist")
        chunks += load_overlay(overlay_path)
    return Index(
        chunks,
        embed_fn=embed_fn or default_embed_fn(rag_cfg.embed_model),
        rerank_fn=rerank_fn or default_rerank_fn(rag_cfg.rerank_model),
    )


def relevance_band(score: float, threshold: float | None) -> str | None:
    if threshold is None:
        return None
    return "high" if score >= threshold else "low"


def best_practice_ids(chunks: list[ChunkRecord]) -> set[str]:
    """Every best-practice id that occurs in a chunk's text or section path."""
    ids: set[str] = set()
    for c in chunks:
        ids.update(BP_ID.findall(c.text))
        for part in c.section_path:
            ids.update(BP_ID.findall(part))
    return ids


def _attr(value: str) -> str:
    return escape(value, quote=True)


class SearchTool:
    def __init__(
        self,
        index: Index,
        store: Store,
        session_id: int,
        *,
        k: int,
        rag_cfg: RagConfig,
        relevance_threshold: float | None,
        supersedes: dict[str, str] | None = None,
    ):
        self.index = index
        self.store = store
        self.session_id = session_id
        self.k = k
        self.rag_cfg = rag_cfg
        self.relevance_threshold = relevance_threshold
        self.supersedes = supersedes or {}
        self._published = {c.doc_id: c.published for c in index.chunks}
        self._sent: set[str] = (
            set()
        )  # chunk ids whose text is already in the current request

    def new_request(self) -> None:
        """Called at the start of every request: earlier requests' chunk texts are not in context."""
        self._sent.clear()

    def search(self, args: SearchArgs) -> list[Hit]:
        """Runs in the worker thread: no SQLite here."""
        filters = Filters(doc_types=args.doc_types, published_from=args.published_from)
        return search(
            self.index,
            args.query,
            k=self.k,
            mode="hybrid_rerank",
            filters=filters,
            candidates=self.rag_cfg.candidates,
            rrf_k=self.rag_cfg.rrf_k,
        )

    def label(self, hits: list[Hit]) -> ToolOutcome:
        """Runs on the main thread: gives each hit its session label and renders the result."""
        if not hits:
            return ToolOutcome(text=NOTHING_FOUND, is_error=False, data={"labels": {}})
        known = {
            chunk_id: label
            for label, chunk_id in self.store.label_map(self.session_id).items()
        }
        next_n = self.store.next_label(self.session_id)
        new: dict[str, str] = {}
        labels: dict[str, str] = {}
        parts = []
        for hit in hits:
            chunk_id = hit.chunk.chunk_id
            label = known.get(chunk_id)
            if label is None:
                label = f"S{next_n}"
                next_n += 1
                known[chunk_id] = label
                new[label] = chunk_id
            labels[label] = chunk_id
            parts.append(self._render(label, hit))
            self._sent.add(chunk_id)
        if new:
            self.store.add_labels(self.session_id, new)
        return ToolOutcome(
            text="\n".join(parts), is_error=False, data={"labels": labels}
        )

    def _render(self, label: str, hit: Hit) -> str:
        c = hit.chunk
        attrs = [
            f'label="{label}"',
            f'title="{_attr(c.title)}"',
            f'section="{_attr(header("", c.section_path).removeprefix(" > "))}"',
            f'published="{c.published.isoformat()}"',
        ]
        band = relevance_band(hit.score, self.relevance_threshold)
        if band is not None:
            attrs.append(f'relevance="{band}"')
        attrs.append(f'score="{hit.score:.2f}"')
        note = edition_note(c, self.supersedes, self._published)
        if note is not None:
            attrs.append(f'edition="{_attr(note)}"')
        if c.chunk_id in self._sent:
            return f"<document {' '.join(attrs)}>(already shown above in this request)</document>"
        text = _TAG.sub(r"&lt;\1\2", c.text)
        return f"<document {' '.join(attrs)}>\n{text}\n</document>"
