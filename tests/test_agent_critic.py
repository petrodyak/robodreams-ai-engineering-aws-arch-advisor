"""The critic: code checks of the final answer before it is shown (spec §10; src/agent/critic.py)."""

from src.agent.critic import (
    CITE,
    critic,
    critic_messages,
    labels_in,
    unverified_numbers,
)

MAP = {f"S{i}": f"doc#{i:04d}" for i in range(1, 6)}
PILLARS = (
    "Operational Excellence",
    "Security",
    "Reliability",
    "Performance Efficiency",
    "Cost Optimization",
    "Sustainability",
)


def check(answer: str, **kw) -> list[str]:
    args = {
        "label_map": MAP,
        "searched": True,
        "number_sources": [],
        "rejected_bp": set(),
        "tools_failed": False,
    }
    args.update(kw)
    return critic(answer, **args)


def test_unknown_label():
    problems = check("Back up all data [S9].")
    assert len(problems) == 1
    assert "S9" in problems[0]


def test_label_lists_are_read():
    assert labels_in("Operational Excellence [S1, S31], Security [S7]") == [
        "S1",
        "S31",
        "S7",
    ]
    assert CITE.findall("[S2]")
    problems = check("Security [S1, S9].")
    assert any("S9" in p for p in problems)


def test_searched_but_no_citation():
    problems = check("Back up all data.")
    assert any("cite at least one" in p for p in problems)
    assert check("Hello!", searched=False) == []


def test_unverified_numbers():
    assert unverified_numbers("Run 30 jobs at once.", ["the plan"]) == ["30"]
    assert unverified_numbers("Keep 3 copies.", []) == []  # below SMALL
    assert unverified_numbers("Run 30 jobs at once.", ["user: we run 30 jobs"]) == []
    problems = check("The quota is 750 DPUs [S1].")
    assert any("750" in p for p in problems)


def test_numbers_thousands_separator():
    sources = ["Max concurrent job runs per account: Each supported Region: 10,000"]
    assert unverified_numbers("The quota is 10,000 runs.", sources) == []
    assert unverified_numbers("The quota is 10000 runs.", sources) == []
    assert unverified_numbers("The quota is 10 runs.", sources) == ["10"]


def test_numbers_from_earlier_turn():
    history = ["assistant: the Glue quota is 500 DPUs in eu-central-1"]
    assert unverified_numbers("As said, 500 DPUs.", history) == []


def test_labels_ids_dates_are_not_numbers():
    sources = ["published 2024-11-06"]
    assert (
        unverified_numbers(
            "See [S12]: REL09-BP01 (2024-11-06), in eu-central-1.", sources
        )
        == []
    )


def test_rejected_bp_in_answer():
    problems = check(
        "Finding 1 [medium · Reliability · REL01-BP01] quotas [S1]",
        rejected_bp={"REL01-BP01"},
    )
    assert any("REL01-BP01" in p and "rejected" in p for p in problems)


def _review(lines: list[str]) -> str:
    return "\n".join(lines)


def test_review_every_pillar_cited():
    five = [
        "Finding 1 [high · Reliability · REL09-BP01] no backup [S1]",
        "Finding 2 [medium · Security · SEC08-BP02] results not encrypted [S2]",
        "Finding 3 [medium · Operational Excellence · OPS08-BP04] no alerts [S3]",
        "Finding 4 [medium · Performance Efficiency · PERF03-BP04] no compaction [S4]",
        "Finding 5 [low · Cost Optimization · COST05-BP01] no scan limit [S5]",
        "Pillars covered: 5 of 6",
    ]
    problems = check(_review(five))
    assert any("Sustainability" in p for p in problems)
    assert not any(p for p in problems if any(x in p for x in PILLARS[:5]))
    fixed = [
        *five[:-1],
        "Sustainability: no gap found in what was retrieved [S2]",
        "Pillars covered: 6 of 6",
    ]
    assert check(_review(fixed)) == []


def test_pillars_line_with_labels_counts():
    answer = _review(
        [
            "Finding 1 [high · Reliability · REL09-BP01] no backup [S1]",
            (
                "Pillars covered: 6 of 6 (Operational Excellence [S2], Security [S3, S4], "
                "Reliability [S1], Performance Efficiency [S5], Cost Optimization [S2], "
                "Sustainability [S3])"
            ),
        ]
    )
    assert check(answer) == []


def test_not_covered_only_after_a_tool_failure():
    answer = "I could not read the architecture.\nPillars covered: 0 of 6 (not covered: the registry was unavailable)"
    assert check(answer, searched=False, tools_failed=True) == []
    assert check(answer, searched=False, tools_failed=False)


def test_question_is_not_a_review():
    assert check("REL09-BP01 asks to back up all data [S1].") == []


def test_critic_messages_form():
    messages = critic_messages(["label [S9] is not a label of this session"])
    assert [m["role"] for m in messages] == ["user", "system"]
    assert messages[0]["content"] == "(automatic check of the answer)"
    assert "[S9]" in messages[1]["content"]


def test_rejected_bp_may_be_named_in_an_explanation():
    # first step 24 run (t29): naming the rejected id to explain it is not raising it (spec §10)
    answer = "The backup finding is not included: you rejected REL09-BP01 for this version [S1]."
    assert check(answer, rejected_bp={"REL09-BP01"}) == []
    raised = "Finding 1 [high · Reliability · REL09-BP01] no backup [S1]\nPillars covered: 1 of 6"
    assert any("REL09-BP01" in p for p in check(raised, rejected_bp={"REL09-BP01"}))


def test_one_recorded_finding_is_not_a_review():
    # first step 24 run (t18b): "record this finding" answered with one Finding line is not a review
    answer = "Recorded.\nFinding 1 [high · Reliability · REL09-BP01] no backup [S1]"
    assert check(answer) == []


# --- step 24 review fixes ------------------------------------------------------------------

from src.agent.critic import finding_ids


def test_finding_heads_in_other_shapes():
    # review I3: bold heads, a colon, a lower-case id
    assert finding_ids("**Finding 1** [high · Reliability · REL09-BP01] x") == {
        "REL09-BP01"
    }
    assert finding_ids("Finding 2: [medium · Security · sec08-bp02] x") == {
        "SEC08-BP02"
    }
    raised = "**Finding 1** [high · Reliability · REL09-BP01] no backup [S1]"
    assert any("REL09-BP01" in p for p in check(raised, rejected_bp={"REL09-BP01"}))


def test_numbers_inside_names_are_not_numbers():
    # review I6: digits that belong to a name or a code
    assert unverified_numbers("Use AES-256 and SHA-256, 24/7, on EC2 and S3.", []) == []
    assert unverified_numbers("Run 30 jobs.", []) == ["30"]
