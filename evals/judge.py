"""The two LLM judges of the answer eval (spec §7), on claude-sonnet-5-5 behind the eval cache.

- Correctness: pass / fail of the answer against the reference answer, plus a one-line reason. Used
  for answerable items with an answer; a not-found answer on an answerable item already fails as a
  false abstain, and a no-answer item is scored by `abstain_correct`.
- Faithfulness: for each claim, are its cited source texts enough to support it. The score is
  supported / all claims, so a true fact cited to the wrong source counts as unsupported.

Both are calibrated against Petro's hand labels before any of their numbers is reported.
"""

import re
from collections.abc import Callable
from pathlib import Path

import anthropic
from pydantic import BaseModel, ValidationError

from evals.testset import TestItem
from src.extract.llm.base import short_sha
from src.rag.answer import AnswerRecord

PROMPTS_DIR = Path("prompts")
JUDGE_MAX_TOKENS = 4000
_SECTION_RE = re.compile(r"^=== (\w+) ===$", re.MULTILINE)


class Verdict(BaseModel):
    passed: bool
    reason: str


class _Support(BaseModel):
    supported: list[bool]


class FaithVerdict(BaseModel):
    supported: list[bool]  # one per claim, in order
    score: float | None  # None when the judge returned the wrong number of values


class JudgePrompt(BaseModel):
    name: str
    sha: str
    system: str
    user: str

    def user_message(self, **values: str) -> str:
        # one pass over the template: braces inside the answer or the sources stay as they are
        return re.sub(r"\{(\w+)\}", lambda m: values[m.group(1)], self.user)


def load_judge_prompt(name: str, prompts_dir: Path = PROMPTS_DIR) -> JudgePrompt:
    """prompts/<name>.txt with `=== system ===` and `=== user ===` sections."""
    raw = (prompts_dir / f"{name}.txt").read_text(encoding="utf-8")
    parts = _SECTION_RE.split(raw)
    sections = {k: v.strip() for k, v in zip(parts[1::2], parts[2::2])}
    if set(sections) != {"system", "user"}:
        raise ValueError(
            f"{name}.txt: sections {sorted(sections)}, expected system, user"
        )
    return JudgePrompt(name=name, sha=short_sha(raw), **sections)


def judge_correctness(
    item: TestItem, rec: AnswerRecord, llm, version: str = "v1"
) -> Verdict | None:
    if not item.answerable or not rec.found:
        return None
    prompt = load_judge_prompt(f"judge_correctness_{version}")
    user = prompt.user_message(
        question=item.question, expected=item.expected_answer, answer=rec.answer
    )
    result = llm.complete_json(prompt.system, user, anthropic.transform_schema(Verdict))
    try:
        return Verdict.model_validate_json(result.text or "")
    except ValidationError:
        return Verdict(passed=False, reason=f"no verdict (stop: {result.stop_reason})")


def _claims_block(rec: AnswerRecord, chunk_text: Callable[[str], str]) -> str:
    blocks = []
    for n, claim in enumerate(rec.claims, 1):
        sources = "\n".join(
            f"[{r.label}] {r.title} > {' > '.join(r.section_path)}\n{chunk_text(r.chunk_id)}"
            for r in claim.refs
        )
        blocks.append(f"Claim {n}: {claim.text}\nCited sources:\n{sources}")
    return f"The answer has {len(rec.claims)} claims.\n\n" + "\n\n".join(blocks)


def judge_faithfulness(
    rec: AnswerRecord, chunk_text: Callable[[str], str], llm, version: str = "v1"
) -> FaithVerdict | None:
    if not rec.claims:
        return None
    prompt = load_judge_prompt(f"judge_faithfulness_{version}")
    user = prompt.user_message(claims=_claims_block(rec, chunk_text))
    result = llm.complete_json(
        prompt.system, user, anthropic.transform_schema(_Support)
    )
    try:
        supported = _Support.model_validate_json(result.text or "").supported
    except ValidationError:
        return FaithVerdict(supported=[], score=None)
    if len(supported) != len(rec.claims):
        return FaithVerdict(supported=supported, score=None)
    return FaithVerdict(supported=supported, score=sum(supported) / len(supported))
