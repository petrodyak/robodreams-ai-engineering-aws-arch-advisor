"""Deterministic scorers (spec §7), adapted from the lesson-8 `evaluate`.

Each scorer looks at one stage, so the error analysis can say where an item broke:
- `retrieved` / `in_context`: a relevant chunk is among the hits / in the budgeted prompt
  (search vs context budget);
- `abstain_correct`: the answer says "not found" exactly when the item has no answer;
- `key_facts`: the share of key facts present in the answer text (literal: the judge covers wording);
- `source_hit`: a validated citation names an expected document and section;
- `citations_valid`: no claim lost its labels and none was removed.

None means "does not apply" (e.g. `source_hit` on a no-answer item) and is left out of the averages.
Text is compared after NFKC, casefold and collapsed whitespace.
"""

import unicodedata

from evals.testset import TestItem
from src.rag.answer import AnswerRecord


def normalize(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def abstain_correct(item: TestItem, rec: AnswerRecord) -> bool:
    return rec.found == item.answerable


def key_facts(item: TestItem, rec: AnswerRecord) -> float | None:
    if not item.answerable or not item.key_facts:
        return None
    answer = normalize(rec.answer)
    return sum(normalize(f) in answer for f in item.key_facts) / len(item.key_facts)


def source_hit(item: TestItem, rec: AnswerRecord) -> bool | None:
    """A cited chunk of an expected document whose section path holds the expected section.
    An empty expected section (a document without headings) matches the document."""
    if not item.answerable:
        return None
    refs = [r for c in rec.claims for r in c.refs]
    for s in item.expected_sources:
        for r in refs:
            if r.doc_id != s.doc_id:
                continue
            if not s.section or normalize(s.section) in map(normalize, r.section_path):
                return True
    return False


def citations_valid(rec: AnswerRecord) -> bool:
    return (
        rec.uncited_claims == 0
        and not rec.dropped_labels
        and all(c.citations for c in rec.claims)
    )


def retrieved(item: TestItem, rec: AnswerRecord) -> bool | None:
    if not item.answerable or not item.relevant_chunk_ids:
        return None
    return bool(set(item.relevant_chunk_ids) & set(rec.retrieved))


def in_context(item: TestItem, rec: AnswerRecord) -> bool | None:
    if not item.answerable or not item.relevant_chunk_ids:
        return None
    return bool(set(item.relevant_chunk_ids) & set(rec.in_context))


def _mean(values: list) -> float | None:
    present = [float(v) for v in values if v is not None]
    return sum(present) / len(present) if present else None


def passed(item: TestItem, rec: AnswerRecord) -> bool:
    """The deterministic verdict: right abstention; for an answerable item also every key fact,
    an expected source cited, and valid citations."""
    if not abstain_correct(item, rec):
        return False
    if not item.answerable:
        return True
    return (
        key_facts(item, rec) in (None, 1.0)
        and source_hit(item, rec) is True
        and citations_valid(rec)
    )


def aggregate(items: list[TestItem], recs: list[AnswerRecord]) -> dict:
    """Averages over the items each metric applies to; `recs` is in the order of `items`."""
    for it, rec in zip(items, recs, strict=True):
        if rec.question != it.question:
            raise ValueError(f"{it.id}: the record answers another question")
    answerable = [(it, r) for it, r in zip(items, recs) if it.answerable]
    no_answer = [(it, r) for it, r in zip(items, recs) if not it.answerable]
    return {
        "abstain_accuracy": _mean([abstain_correct(it, r) for it, r in no_answer]),
        "false_abstain_rate": _mean([not r.found for _, r in answerable]),
        "source_hit": _mean([source_hit(it, r) for it, r in answerable]),
        "key_facts": _mean([key_facts(it, r) for it, r in answerable]),
        "citations_valid": _mean([citations_valid(r) for r in recs]),
        "retrieved": _mean([retrieved(it, r) for it, r in answerable]),
        "in_context": _mean([in_context(it, r) for it, r in answerable]),
        "failed": [it.id for it, r in zip(items, recs) if not passed(it, r)],
    }
