"""Judge calibration (spec §7): Petro's hand labels against the judges' verdicts.

- `evals/labels/calibration.jsonl`: one row per labelled answer, `human_pass` (the correctness label)
  and `human_unsupported` (the answer has a claim its sources do not support).
- Agreement is the share of matching labels. Cohen's kappa removes the agreement two raters would
  reach by chance: kappa = (p_o - p_e) / (1 - p_e), with p_e from each rater's own pass rate. A judge
  that passes everything agrees often on a mostly-passing set, but its kappa is near 0.
"""

from datetime import date
from pathlib import Path

from pydantic import BaseModel, ConfigDict


class CalibrationRow(BaseModel):
    model_config = ConfigDict(extra="forbid")

    item_id: str
    run_id: str
    human_pass: bool | None
    human_unsupported: bool | None
    labelled_on: date | None


def load_calibration(path: Path) -> list[CalibrationRow]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    return [CalibrationRow.model_validate_json(line) for line in lines if line.strip()]


def agreement(pairs: list[tuple[bool, bool]]) -> float:
    return sum(a == b for a, b in pairs) / len(pairs)


def cohens_kappa(pairs: list[tuple[bool, bool]]) -> float:
    p_o = agreement(pairs)
    n = len(pairs)
    yes_a = sum(a for a, _ in pairs) / n
    yes_b = sum(b for _, b in pairs) / n
    p_e = yes_a * yes_b + (1 - yes_a) * (1 - yes_b)
    if p_e == 1.0:  # both raters gave one label to everything: kappa is 1 if they agree
        return 1.0 if p_o == 1.0 else 0.0
    return (p_o - p_e) / (1 - p_e)
