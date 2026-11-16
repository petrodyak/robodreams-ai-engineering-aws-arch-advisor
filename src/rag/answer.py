"""Answering with sources: search → context → Claude → citation check (spec §6).

- Context: the top-k hits in rank order, each block labelled [S1], [S2] ... with title, section and
  publication date. A block that does not fit the token budget is skipped, never cut, and a smaller
  later block may still go in, so a source is never cited for text the model did not see.
- Claude returns `ModelAnswer` (structured outputs): claims, each with the labels that support it.
- The code checks the citations: labels are normalized, unknown ones are dropped, and a claim with
  no valid label left is removed. If no claim survives, the answer is the not-found text.
- No context, no call: when the search (or its filters) leaves nothing, Claude is not asked.
"""

import re
import sys
from pathlib import Path

import anthropic
from pydantic import BaseModel, ValidationError

from src.extract.llm.base import short_sha
from src.rag.config import RagConfig
from src.rag.index import Index
from src.rag.models import ChunkRecord
from src.rag.search import Filters, Hit, search

NOT_FOUND = "The documents available to me do not answer this question."
PROMPTS_DIR = Path("prompts")
CLOSEST = 2  # titles named after the not-found text

_SECTION_RE = re.compile(r"^=== (\w+) ===$", re.MULTILINE)
_LABEL_RE = re.compile(r"^S\d+$")


class Claim(BaseModel):
    text: str
    citations: list[str]


class ModelAnswer(BaseModel):
    """What Claude returns; its JSON schema is the structured-output format."""

    found: bool
    claims: list[Claim]


class SourceRef(BaseModel):
    label: str
    chunk_id: str
    doc_id: str
    title: str
    section_path: list[str]
    page_start: int | None


class ValidClaim(BaseModel):
    text: str
    citations: list[str]  # normalized labels, each one in the context
    refs: list[SourceRef]


class AnswerRecord(BaseModel):
    """One answered question: what was retrieved, what Claude saw, what it said, what it cost."""

    question: str
    found: bool
    answer: str
    claims: list[ValidClaim]
    sources: dict[str, str]  # label → chunk_id, for the blocks in the context
    retrieved: list[str]  # chunk ids of the search hits, in rank order
    in_context: list[str]  # chunk ids that went into the prompt, in label order
    dropped_labels: list[str]
    uncited_claims: int
    context_tokens: int
    stop_reason: str | None  # None when Claude was not called
    model: str
    effort: str
    prompt_version: str
    prompt_sha: str
    input_tokens: int
    output_tokens: int
    cost_usd: float
    latency_ms: int


class RagPrompt(BaseModel):
    version: str
    sha: str
    system: str
    user: str

    def user_message(self, question: str, sources: str) -> str:
        # One pass over the template: braces inside the sources are data and stay as they are.
        values = {"question": question, "sources": sources}
        return re.sub(
            r"\{(question|sources)\}", lambda m: values[m.group(1)], self.user
        )


def load_prompt(version: str, prompts_dir: Path = PROMPTS_DIR) -> RagPrompt:
    """prompts/rag_<version>.txt: the `=== system ===` and `=== user ===` sections."""
    path = prompts_dir / f"rag_{version}.txt"
    raw = path.read_text(encoding="utf-8")
    parts = _SECTION_RE.split(raw)
    sections = {name: body.strip() for name, body in zip(parts[1::2], parts[2::2])}
    if set(sections) != {"system", "user"}:
        raise ValueError(
            f"{path.name}: sections {sorted(sections)}, expected system, user"
        )
    for placeholder in ("{question}", "{sources}"):
        if placeholder not in sections["user"]:
            raise ValueError(f"{path.name} [user]: no {placeholder}")
    return RagPrompt(version=version, sha=short_sha(raw), **sections)


def answer_schema() -> dict:
    """ModelAnswer as a schema structured outputs accept (as in HW 1)."""
    return anthropic.transform_schema(ModelAnswer)


def _block(label: str, c: ChunkRecord) -> str:
    return (
        f"[{label}] {c.title} · {' > '.join(c.section_path)} · {c.published}\n{c.text}"
    )


def build_context(hits: list[Hit], budget: int) -> tuple[str, dict[str, ChunkRecord]]:
    """The labelled blocks that fit `budget` tokens of chunk text, in rank order."""
    sources: dict[str, ChunkRecord] = {}
    blocks, used = [], 0
    for h in hits:
        if used + h.chunk.n_tokens > budget:
            continue  # skip, do not cut: a later, smaller chunk may still fit
        label = f"S{len(sources) + 1}"
        sources[label] = h.chunk
        blocks.append(_block(label, h.chunk))
        used += h.chunk.n_tokens
    return "\n\n".join(blocks), sources


def normalize_label(label: str) -> str:
    return label.strip().strip("[]").strip().upper()


def validate(
    ans: ModelAnswer, sources: dict[str, ChunkRecord]
) -> tuple[list[ValidClaim], list[str], int]:
    """(claims with only valid labels, labels dropped, claims removed for having none)."""
    claims, dropped, uncited = [], [], 0
    for claim in ans.claims:
        labels = []
        for raw in claim.citations:
            label = normalize_label(raw)
            if _LABEL_RE.match(label) and label in sources:
                if label not in labels:
                    labels.append(label)
            else:
                dropped.append(label)
        if not labels:
            uncited += 1
            continue
        refs = [
            SourceRef(
                label=label,
                chunk_id=sources[label].chunk_id,
                doc_id=sources[label].doc_id,
                title=sources[label].title,
                section_path=sources[label].section_path,
                page_start=sources[label].page_start,
            )
            for label in labels
        ]
        claims.append(ValidClaim(text=claim.text, citations=labels, refs=refs))
    return claims, dropped, uncited


def _not_found_text(hits: list[Hit]) -> str:
    titles = list(dict.fromkeys(h.chunk.title for h in hits))[:CLOSEST]
    return NOT_FOUND + (f"\nClosest sources: {'; '.join(titles)}" if titles else "")


def _answer_text(claims: list[ValidClaim]) -> str:
    return " ".join(
        f"{c.text} " + "".join(f"[{label}]" for label in c.citations) for c in claims
    )


class Prepared(BaseModel):
    """Everything before the Claude call: what `estimate` counts and `answer` sends."""

    prompt: RagPrompt
    hits: list[Hit]
    sources: dict[str, ChunkRecord]
    user: str  # the filled user message; empty when there are no sources


def prepare(
    question: str,
    index: Index,
    cfg: RagConfig,
    filters: Filters | None = None,
    *,
    k: int | None = None,
    budget: int | None = None,
) -> Prepared:
    prompt = load_prompt(cfg.prompt_version)
    hits = search(
        index,
        question,
        k=k or cfg.k,
        mode="hybrid_rerank",
        filters=filters,
        candidates=cfg.candidates,
        rrf_k=cfg.rrf_k,
    )
    context, sources = build_context(hits, budget or cfg.context_budget)
    user = prompt.user_message(question, context) if sources else ""
    return Prepared(prompt=prompt, hits=hits, sources=sources, user=user)


def answer(
    question: str,
    index: Index,
    llm,
    cfg: RagConfig,
    filters: Filters | None = None,
    *,
    k: int | None = None,
    budget: int | None = None,
) -> AnswerRecord:
    """Search, build the context, ask Claude, check the citations. `k` / `budget` default to
    the config; the k sweep (step 18) overrides them."""
    p = prepare(question, index, cfg, filters, k=k, budget=budget)
    prompt, hits, sources = p.prompt, p.hits, p.sources
    record = {
        "question": question,
        "found": False,
        "answer": _not_found_text(hits),
        "claims": [],
        "sources": {label: c.chunk_id for label, c in sources.items()},
        "retrieved": [h.chunk.chunk_id for h in hits],
        "in_context": [c.chunk_id for c in sources.values()],
        "dropped_labels": [],
        "uncited_claims": 0,
        "context_tokens": sum(c.n_tokens for c in sources.values()),
        "stop_reason": None,
        "model": llm.model,
        "effort": llm.effort,
        "prompt_version": prompt.version,
        "prompt_sha": prompt.sha,
        "input_tokens": 0,
        "output_tokens": 0,
        "cost_usd": 0.0,
        "latency_ms": 0,
    }
    if not sources:  # nothing to answer from: no call (Review Focus 2)
        return AnswerRecord(**record)

    result = llm.complete_json(prompt.system, p.user, answer_schema())
    record.update(
        stop_reason=result.stop_reason,
        input_tokens=result.input_tokens,
        output_tokens=result.output_tokens,
        cost_usd=result.cost_usd,
        latency_ms=result.latency_ms,
    )
    if result.text is None:
        return AnswerRecord(**record)  # refusal or cut-off: no text (Review Focus 3)
    try:
        ans = ModelAnswer.model_validate_json(result.text)
    except ValidationError:
        return AnswerRecord(**record)  # cut-off JSON (max_tokens)

    claims, dropped, uncited = validate(ans, sources)
    record.update(dropped_labels=dropped, uncited_claims=uncited)
    if ans.found and claims:
        record.update(found=True, answer=_answer_text(claims), claims=claims)
    return AnswerRecord(**record)


def main() -> None:
    """`make ask Q="..."`: one question, the answer, its sources and the cost."""
    from dotenv import load_dotenv

    from src.rag.config import load_config
    from src.rag.index import default_embed_fn, default_rerank_fn, load_chunks
    from src.rag.llm import ClaudeJSON

    if len(sys.argv) != 2 or not sys.argv[1].strip():
        sys.exit('usage: make ask Q="your question"')
    load_dotenv()  # ANTHROPIC_API_KEY
    cfg = load_config()
    index = Index(
        load_chunks(Path("data/rag/chunks.jsonl")),
        embed_fn=default_embed_fn(cfg.embed_model),
        rerank_fn=default_rerank_fn(cfg.rerank_model),
    )
    llm = ClaudeJSON(cfg.answer_model, cfg.answer_effort, cfg.answer_max_tokens)
    rec = answer(sys.argv[1], index, llm, cfg)

    by_id = {c.chunk_id: c for c in index.chunks}
    print(f"\n{rec.answer}\n")
    for label, chunk_id in rec.sources.items():
        c = by_id[chunk_id]
        page = f" p.{c.page_start}" if c.page_start else ""
        print(
            f"[{label}] {c.title} > {' > '.join(c.section_path)}{page}\n     {c.source_url}"
        )
    print(
        f"\nfound={rec.found} stop={rec.stop_reason} tokens in/out "
        f"{rec.input_tokens}/{rec.output_tokens} cost ${rec.cost_usd:.5f} "
        f"{rec.latency_ms} ms"
    )


if __name__ == "__main__":
    main()
