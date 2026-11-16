"""The testset: one JSON line per question in evals/testset.jsonl (spec §7).

The same items serve the retrieval eval (step 17: `relevant_chunk_ids`, labelled by Petro) and the
answer eval (step 19: `expected_answer`, `key_facts`, `expected_sources`). `verified_by` and
`verified_on` record the manual check the brief asks for.
"""

from datetime import date
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, model_validator

Kind = Literal["single", "multi", "no_answer", "similar", "outdated"]


class ExpectedSource(BaseModel):
    model_config = ConfigDict(extra="forbid")

    doc_id: str
    section: str


class TestItem(BaseModel):
    __test__ = False  # not a pytest test class, despite the name

    model_config = ConfigDict(extra="forbid")

    id: str
    question: str
    kind: Kind
    expected_answer: str
    key_facts: list[str]
    expected_sources: list[ExpectedSource]
    relevant_chunk_ids: list[str]
    answerable: bool
    verified_by: str | None
    verified_on: date | None

    @model_validator(mode="after")
    def _answerable_follows_kind(self) -> "TestItem":
        if self.answerable != (self.kind != "no_answer"):
            raise ValueError(
                f"{self.id}: answerable must be {self.kind != 'no_answer'} for kind {self.kind}"
            )
        return self


def load_testset(path: Path = Path("evals/testset.jsonl")) -> list[TestItem]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [TestItem.model_validate_json(line) for line in lines if line.strip()]
