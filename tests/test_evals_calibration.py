"""Judge calibration (evals/calibration.py, spec §7): agreement, Cohen's kappa, and the label gate."""

from pathlib import Path

import pytest

from evals.calibration import agreement, cohens_kappa, load_calibration

T, F = True, False
LABELS = Path("evals/labels/calibration.jsonl")


def test_kappa_known_value():
    pairs = [(T, T), (T, F), (F, F), (F, F)]

    assert agreement(pairs) == 0.75
    assert cohens_kappa(pairs) == pytest.approx(0.5)


def test_kappa_all_same():
    assert cohens_kappa([(T, T)] * 5) == 1.0


def test_kappa_chance_agreement_is_zero():
    # the judge always says pass, the human splits evenly: agreement 0.5 is pure chance
    assert cohens_kappa([(T, T), (F, T)] * 3) == pytest.approx(0.0)


def test_calibration_complete():
    """Data gate (spec §7): ≥ 12 hand labels, ≥ 3 of them failures of the v1 run."""
    rows = [r for r in load_calibration(LABELS) if r.human_pass is not None]

    assert len(rows) >= 12
    assert sum(r.human_pass is False for r in rows) >= 3
