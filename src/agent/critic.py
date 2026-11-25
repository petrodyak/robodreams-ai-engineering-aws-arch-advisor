"""The critic: code checks of the final answer before it is shown (spec §10; lesson 13 TODO 4).

Five checks, no model call:

1. every cited label is a label of this session's searches (the HW 2 `validate()` idea);
2. an answer that searched cites at least once;
3. `unverified_numbers` (lesson 11 TODO 5): numbers >= SMALL that no tool returned and nobody gave;
4. no best practice the user rejected for this architecture version is raised as a finding (a
   `Finding` line with its id); naming it to explain the rejection is fine (§6.1);
5. in a review (an answer with the `Pillars covered:` line, rule 2), each of the six pillars carries a
   citation: on a finding of that pillar, next to its "no gap found", or next to the pillar's name in
   the `Pillars covered:` line (D25). "Not covered" counts only when a tool failed in this request.

A failed check goes back to the model once (`critic_messages`, spec §6): a `user` marker, then a
mid-conversation `system` message with the problems; the API accepts `system` only right after a
`user` message.
"""

import re

SMALL = 10  # numbers below this are list items and counts in words ("3 copies"), as in lesson 11
PILLARS = (
    "Operational Excellence",
    "Security",
    "Reliability",
    "Performance Efficiency",
    "Cost Optimization",
    "Sustainability",
)
# a label group: [S3] or [S1, S31]
CITE = re.compile(r"\[(S\d+(?:\s*,\s*S\d+)*)\]")
_BP = re.compile(r"\b[A-Z]{2,7}\d{2}-BP\d{2}\b")
_DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
_REGION = re.compile(r"\b[a-z]{2}(?:-[a-z]+)+-\d\b")
# a number: 10,000 (thousands separator), 99.5, 600
_NUMBER = re.compile(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?")
# digits that belong to a name or a code, not a quantity: AES-256, SHA-256, EC2, S3, 24/7, 2xlarge
_NAMED = re.compile(r"\b[A-Za-z]+-?\d+[A-Za-z]*\b|\b\d+/\d+\b|\b\d+[A-Za-z]+\b")
# a finding head: "Finding 1 [", "**Finding 1** [", "Finding 1: [" (review I3)
_FINDING = re.compile(r"\**Finding\s+\d+\**\s*[:.\-—]?\s*\[([^\]]*)\]", re.IGNORECASE)
MARKER = "(automatic check of the answer)"


def labels_in(text: str) -> list[str]:
    """Every label of every group, in order: "[S1, S31] … [S7]" → ["S1", "S31", "S7"]."""
    return [label.strip() for group in CITE.findall(text) for label in group.split(",")]


def _value(token: str) -> str:
    number = float(token.replace(",", ""))
    return str(int(number)) if number.is_integer() else repr(number)


def _numbers(text: str) -> list[str]:
    return _NUMBER.findall(text)


def unverified_numbers(answer: str, sources: list[str]) -> list[str]:
    """Numbers >= SMALL in `answer` that occur in none of `sources`, in order, without duplicates.

    Labels, best-practice ids, ISO dates and Region codes are not numbers. A comma between digit groups
    is a thousands separator (`10,000` in the gold quotas), so `10,000` verifies `10000`, never `10`.
    """
    cleaned = CITE.sub(" ", answer)
    for pattern in (_BP, _DATE, _REGION, _NAMED):
        cleaned = pattern.sub(" ", cleaned)
    known = {_value(t) for source in sources for t in _numbers(source)}
    out: list[str] = []
    for token in _numbers(cleaned):
        value = _value(token)
        if float(value) >= SMALL and value not in known and token not in out:
            out.append(token)
    return out


def finding_ids(answer: str) -> set[str]:
    """The best-practice ids in the heads of the answer's `Finding N [severity · pillar · id]` lines."""
    return {
        bp.upper()
        for head in _FINDING.findall(answer)
        for bp in re.findall(_BP.pattern, head, flags=re.IGNORECASE)
    }


def _covered_pillars(answer: str) -> set[str]:
    covered: set[str] = set()
    for line in answer.splitlines():
        cited = bool(labels_in(line))
        head = _FINDING.search(line)
        if head and cited:
            covered.update(p for p in PILLARS if p.lower() in head.group(1).lower())
        lower = line.lower()
        if "no gap" in lower and cited:
            covered.update(p for p in PILLARS if p.lower() in lower)
        if "pillars covered:" in lower:
            for p in PILLARS:
                if re.search(
                    re.escape(p) + r"\s*" + CITE.pattern, line, flags=re.IGNORECASE
                ):
                    covered.add(p)
    return covered


def critic(
    answer: str,
    label_map: dict[str, str],
    searched: bool,
    number_sources: list[str],
    rejected_bp: set[str],
    tools_failed: bool = False,
) -> list[str]:
    """The problems of the answer; an empty list means it is clean."""
    problems: list[str] = []
    labels = labels_in(answer)
    unknown = [label for label in dict.fromkeys(labels) if label not in label_map]
    if unknown:
        problems.append(
            f"labels {', '.join(f'[{x}]' for x in unknown)} are not labels of this session's searches: "
            "cite only labels that a search returned"
        )
    if searched and not labels:
        problems.append(
            "you searched the corpus but the answer cites no label: cite at least one [Sn] for every "
            "statement about AWS"
        )
    numbers = unverified_numbers(answer, number_sources)
    if numbers:
        problems.append(
            f"these numbers come from no tool result and no user message: {', '.join(numbers)}; give "
            "only numbers a tool returned or the user gave, or say that you do not know"
        )
    raised = sorted(rejected_bp & finding_ids(answer))  # raised as a finding, not named
    if raised:
        problems.append(
            f"{', '.join(raised)} was rejected by the user for this version of the architecture: "
            "do not raise it again"
        )
    lower = answer.lower()
    is_review = "pillars covered:" in lower  # rule 2: every review ends with this line
    if is_review and not (tools_failed and "not covered" in lower):
        missing = [p for p in PILLARS if p not in _covered_pillars(answer)]
        if missing:
            problems.append(
                f"the review gives no cited line for: {', '.join(missing)}; give each a finding or "
                "'no gap found in what was retrieved' with the label of what you read"
            )
    return problems


def critic_messages(problems: list[str]) -> list[dict]:
    """The two entries appended after the assistant's answer for its one retry (spec §6)."""
    text = (
        "The answer was checked automatically and has these problems:\n"
        + "\n".join(f"- {p}" for p in problems)
        + "\nWrite the whole answer again with them fixed."
    )
    return [{"role": "user", "content": MARKER}, {"role": "system", "content": text}]
