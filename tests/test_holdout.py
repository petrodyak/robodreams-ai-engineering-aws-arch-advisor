"""The Held-out Set (step 12, lecturer's remark 4): documents never seen while writing
prompt v2, with their own manifest, text, gold folder and run id scope (contract item 20)."""

import pytest

from src.extract import grounding, metrics, pipeline

HOLDOUT = pipeline.HOLDOUT_SET
WORKING = pipeline.load_manifest(pipeline.WORKING_SET.manifest)
DOCS = pipeline.load_manifest(HOLDOUT.manifest)


def test_held_out_set_is_disjoint_from_the_working_set():
    assert len(DOCS) == 10
    assert {d.file for d in DOCS}.isdisjoint({d.file for d in WORKING})
    assert sum(d.gold for d in DOCS) == 5
    # the pool had no `short` document left (data-notes): 6 medium, 4 edge
    assert sorted(d.group.value for d in DOCS) == ["edge"] * 4 + ["medium"] * 6


def test_every_held_out_document_has_its_text_and_a_readable_chapter():
    for d in DOCS:
        text = d.text(HOLDOUT.dir)
        chapter = grounding.target_chapter(text, d.service)
        assert grounding.printed_hostnames(chapter), d.file  # an endpoints table exists


@pytest.mark.parametrize(
    "gold, expected",
    [
        (False, "claude__v2__t0__holdout__val2"),
        (True, "claude__v2__t0__holdout__gold__val2"),
    ],
)
def test_held_out_run_ids_carry_the_scope(gold, expected):
    assert pipeline.make_run_id("claude", "v2", "t0", gold=gold, doc_set=HOLDOUT) == (
        expected
    )
    run = metrics.parse_run_id(expected)
    assert run.doc_set is HOLDOUT and run.gold is gold and run.validation == "2"
    assert run.scope == ("holdout-gold" if gold else "holdout-full")


def test_held_out_scope_uses_the_held_out_manifest():
    run = metrics.parse_run_id("qwen2.5-7b__v1__t0__holdout__gold")
    assert len(metrics.run_scope(run, DOCS)) == 5
    full = metrics.parse_run_id("qwen2.5-7b__v1__t0__holdout")
    assert len(metrics.run_scope(full, DOCS)) == 10


def test_working_set_run_ids_are_unchanged():
    assert pipeline.make_run_id("claude", "v1", "t0", validation_version="1") == (
        "claude__v1__t0"
    )
    assert metrics.parse_run_id("claude__v1__t0").doc_set is pipeline.WORKING_SET
