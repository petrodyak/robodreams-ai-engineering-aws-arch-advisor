"""Choosing the answers of the calibration sheet (scripts/calibration_sheet.py, spec §7)."""

from scripts.calibration_sheet import pick
from tests.test_evals_scorers import item, record


def test_pick_failures_first_and_skips_labelled_answers():
    items = [
        item("one01"),
        item("one02"),
        item("one03"),
        item("none01", kind="no_answer"),
    ]
    recs = [
        record("question one01"),  # all key facts: pass
        record("question one02", text="Set an rpo. [S1]"),  # half the key facts: fail
        record("question one03", text="Nothing here. [S1]"),  # no key fact: fail
        record("question none01", found=False),  # not answerable: never picked
    ]

    chosen = pick(items, recs, n=2, skip=set())
    assert [it.id for _, _, it, _ in chosen] == ["one03", "one02"]

    chosen = pick(items, recs, n=2, skip={"one03"})
    assert [it.id for _, _, it, _ in chosen] == ["one02", "one01"]
