"""Deterministic checks of the agent tasks (spec §13).

A check is `{"type": <name>, ...}` in `evals/agent/tasks.jsonl`; `CHECKS[name](run, check)` says whether
it holds on what the task left behind (`TaskRun`: answers, traces, findings, confirmations asked). A
task whose precondition fails is `invalid`, never `passed`: the thing it tests did not happen.
"""

import re
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Literal

from src.agent.loop import TurnResult
from src.agent.store import FindingRow

CYRILLIC = re.compile(r"[Ѐ-ӿ]")


@dataclass
class TaskRun:
    task_id: str
    answers: list[str]
    results: list[TurnResult]
    traces: list[dict]
    findings: list[FindingRow]
    confirms_asked: int
    facts: dict[str, str] = field(
        default_factory=dict
    )  # the store's facts after the task
    # what each scripted command answered, and the [y/N] questions answered yes
    command_outputs: list[str] = field(default_factory=list)
    confirmed_yes: int = 0

    def tool_calls(self) -> list[dict]:
        return [c for t in self.traces for c in t.get("tool_calls", [])]


@dataclass
class TaskScore:
    status: Literal["passed", "failed", "invalid"]
    failed: list[str]


def _calls(run: TaskRun, tool: str) -> list[dict]:
    return [c for c in run.tool_calls() if tool == "*" or c["name"] == tool]


def _answer(run: TaskRun, check: dict) -> str:
    """The answer of one turn (`turn`, default the last) or of all turns (`turn: "all"`)."""
    which = check.get("turn", -1)
    if which == "all":
        return "\n".join(run.answers)
    return run.answers[which] if run.answers else ""


def tools_called(run: TaskRun, check: dict) -> bool:
    names = {c["name"] for c in run.tool_calls()}
    return all(t in names for t in check["tools"])


def tools_not_called(run: TaskRun, check: dict) -> bool:
    names = {c["name"] for c in run.tool_calls()}
    return not any(t in names for t in check["tools"])


def tool_count(run: TaskRun, check: dict) -> bool:
    n = len(_calls(run, check["tool"]))
    return check.get("min", 0) <= n <= check.get("max", n)


def max_attempts(run: TaskRun, check: dict) -> bool:
    """Every call of `tool` took at most `max` attempts (2 retries = 3 attempts, spec §7)."""
    return all(c.get("attempts", 1) <= check["max"] for c in _calls(run, check["tool"]))


def tool_result_contains(run: TaskRun, check: dict) -> bool:
    """Some call of `tool` returned a result containing `text` (e.g. the read_only gate's refusal)."""
    return any(
        check["text"].lower() in c.get("result", "").lower()
        for c in _calls(run, check["tool"])
    )


def findings_count(run: TaskRun, check: dict) -> bool:
    return len(run.findings) == check["equals"]


def finding_field(run: TaskRun, check: dict) -> bool:
    """The registry row of `bp` has `field == equals` (t18b: reopened_count)."""
    rows = [f for f in run.findings if f.best_practice == check["bp"]]
    return len(rows) == 1 and getattr(rows[0], check["field"]) == check["equals"]


def no_finding(run: TaskRun, check: dict) -> bool:
    """No registry row for `bp` (t29: a rejected best practice is never recorded)."""
    return not any(f.best_practice == check["bp"] for f in run.findings)


def no_finding_line(run: TaskRun, check: dict) -> bool:
    """No line of the answer is a `Finding` line naming `bp` (t29), checked line by line, apart from
    the critic's regex, so the eval does not share its blind spots (review I3)."""
    head = re.compile(r"^\W*finding\s*\d+", re.IGNORECASE)
    bp = check["bp"].lower()
    return not any(
        head.search(line) and bp in line.lower()
        for line in _answer(run, check).splitlines()
    )


def confirms_asked(run: TaskRun, check: dict) -> bool:
    return run.confirms_asked == check["equals"]


def stop(run: TaskRun, check: dict) -> bool:
    return bool(run.results) and run.results[-1].stop in check["in"]


def answer_contains(run: TaskRun, check: dict) -> bool:
    text = _answer(run, check).lower()
    return any(term.lower() in text for term in check["any"])


def answer_not_contains(run: TaskRun, check: dict) -> bool:
    """None of `terms` is in the answers; `"case": true` matches case-sensitively ("None", not "none")."""
    text = _answer(run, {**check, "turn": check.get("turn", "all")})
    if check.get("case"):
        return not any(term in text for term in check["terms"])
    return not any(term.lower() in text.lower() for term in check["terms"])


def no_numbers(run: TaskRun, check: dict) -> bool:
    """No number >= 10 in the answer (t07, t22b, t23: a quota that is not available gets no number).

    Labels, best-practice ids, dates, Region codes and digits of names are not numbers (the critic's
    rules)."""
    from src.agent.critic import unverified_numbers

    return unverified_numbers(_answer(run, check), []) == []


def answer_regex(run: TaskRun, check: dict) -> bool:
    """The answer matches `pattern` (e.g. the eu-central-1 quota and its number in one sentence)."""
    return re.search(check["pattern"], _answer(run, check)) is not None


def retrieved(run: TaskRun, check: dict) -> bool:
    """Every chunk of `chunks` came back from a search (the precondition of t25 / t26)."""
    got = {c for t in run.traces for c in t.get("retrieved_chunk_ids", [])}
    return all(chunk in got for chunk in check["chunks"])


def cites_docs(run: TaskRun, check: dict) -> bool:
    """The answer cites a label of each document in `docs` (labels mapped through the trace)."""
    from src.agent.critic import labels_in

    label_map = {
        label: chunk
        for c in run.tool_calls()
        for label, chunk in ((c.get("data") or {}).get("labels") or {}).items()
    }
    cited = {
        label_map[x].split("#")[0]
        for x in labels_in(_answer(run, check))
        if x in label_map
    }
    return all(doc in cited for doc in check["docs"])


def answer_shorter(run: TaskRun, check: dict) -> bool:
    """The answer of turn `then` is at most `ratio` as long as the answer of turn `first` (t30)."""
    first, then = run.answers[check["first"]], run.answers[check["then"]]
    return len(then) <= check["ratio"] * len(first)


def answer_in_english(run: TaskRun, check: dict) -> bool:
    return not CYRILLIC.search("\n".join(run.answers))


# the budget stops of t24 (spec §13); max_seconds and max_repeats are other limits, `truncated` is the
# per-call output cap (F33), not a budget
LIMIT_STOPS = ("max_steps", "max_tokens", "max_usd")
BUDGET_USED = "budget for this tool is used up"


def _gold_row(service: str, quota: str) -> dict:
    from src.mcp_server.quotas import _gold

    rows = [q for q in _gold()[service]["quotas"] if q["name"] == quota]
    if not rows:
        raise ValueError(f"no gold quota {quota!r} for {service}")
    return rows[0]


def gold_value(service: str, quota: str, region: str) -> str:
    """The gold default of one quota for one Region, read from data/gold/ (never typed into a task)."""
    row = _gold_row(service, quota)
    entries = [e.strip() for e in row["default"].split(";")]
    for entry in entries:
        name, _, value = entry.partition(":")
        if name.strip() == region:
            return value.strip()
    for entry in entries:
        name, _, value = entry.partition(":")
        if name.strip().startswith(
            ("Each of the other supported Regions", "Each supported Region")
        ):
            return value.strip()
    raise ValueError(f"no default for {region} in {service} / {quota}")


def gold_quota(run: TaskRun, check: dict) -> bool:
    """One sentence of the answer names the Region and the gold number (t05, t06)."""
    value = gold_value(check["service"], check["quota"], check["region"])
    number = value.split()[0]
    entries = _gold_row(check["service"], check["quota"])["default"].split(";")
    row_numbers = {
        e.partition(":")[2].strip().split()[0] for e in entries if ":" in e
    } - {number}
    sentences = re.split(r"(?<!\d)[.;\n]|[.;\n](?!\d)", _answer(run, check))

    def has(s: str, n: str) -> bool:
        return any(
            re.search(rf"(?<![\d,]){re.escape(f)}(?![\d,])", s)
            for f in {n, n.replace(",", "")}
        )

    # the sentence names the Region and the gold number, and no other value of that row (review M1)
    return any(
        check["region"] in s
        and has(s, number)
        and not any(has(s, o) for o in row_numbers)
        for s in sentences
    )


def gold_absent(run: TaskRun, check: dict) -> bool:
    """The gold number appears nowhere in the answer (t22b, t23: a failed quota tool, no number)."""
    number = gold_value(check["service"], check["quota"], check["region"]).split()[0]
    text = _answer(run, check)
    return not any(
        re.search(rf"(?<![\d,]){re.escape(f)}(?![\d,])", text)
        for f in {number, number.replace(",", "")}
    )


def pillars_cited(run: TaskRun, check: dict) -> bool:
    """Each of the six pillars carries a citation (D25): on a finding or next to "no gap found"."""
    from src.agent.critic import PILLARS, _covered_pillars

    return _covered_pillars(_answer(run, check)) == set(PILLARS)


def budget_stop(run: TaskRun, check: dict) -> bool:
    """A limit stopped the request, or a tool's budget was used up (t24)."""
    stopped = any(r.stop in LIMIT_STOPS for r in run.results)
    return stopped or any(BUDGET_USED in c.get("result", "") for c in run.tool_calls())


def _wrote(run: TaskRun) -> bool:
    for c in run.tool_calls():
        status = (c.get("data") or {}).get("status")
        if c["name"] == "record_finding" and status in ("recorded", "reopened"):
            return True
        if c["name"] == "remember" and c.get("result", "").startswith("saved"):
            return True
    return False


def asks_user(run: TaskRun, check: dict) -> bool:
    """The last paragraph asks a question and no tool wrote anything (t14, t15)."""
    paragraphs = [
        p for p in re.split(r"\n\s*\n", _answer(run, check).strip()) if p.strip()
    ]
    return bool(paragraphs) and "?" in paragraphs[-1] and not _wrote(run)


def _final_verdict(run: TaskRun, check: dict) -> list[str] | None:
    """The critic's last verdict on the turn, or None when the critic never ran (a truncated, wrap-up
    or stopped answer is not checked, so it cannot count as clean; review I1)."""
    trace = run.traces[check.get("turn", -1)] if run.traces else {}
    verdicts = trace.get("critic") or []
    if not verdicts or trace.get("stop") != "answer":
        return None
    return verdicts[-1]


def critic_clean(run: TaskRun, check: dict) -> bool:
    """The critic ran on the turn and its last verdict is clean."""
    return _final_verdict(run, check) == []


def unverified_empty(run: TaskRun, check: dict) -> bool:
    """The critic ran on the turn and its last verdict names no unverified number."""
    verdict = _final_verdict(run, check)
    return verdict is not None and not any(
        p.startswith("these numbers") for p in verdict
    )


def arg_contains(run: TaskRun, check: dict) -> bool:
    return any(
        any(
            term.lower() in str((c.get("input") or {}).get(check["arg"], "")).lower()
            for term in check["any"]
        )
        for c in _calls(run, check["tool"])
    )


def distinct_args(run: TaskRun, check: dict) -> bool:
    """At least `min` calls of `tool` with different arguments (t08, t09: one search per part)."""
    import json

    return (
        len(
            {
                json.dumps(c.get("input"), sort_keys=True)
                for c in _calls(run, check["tool"])
            }
        )
        >= check["min"]
    )


def no_fact(run: TaskRun, check: dict) -> bool:
    """The fact was not saved (D24: a document cannot plant it)."""
    return run.facts.get(check["key"]) != check["value"]


def commands_ok(run: TaskRun, check: dict) -> bool:
    """Every scripted command was accepted (a failed /reject makes the task invalid, not failed)."""
    return all(out.startswith(("noted", "resolved")) for out in run.command_outputs)


CHECKS: dict[str, Callable[[TaskRun, dict], bool]] = {
    "tools_called": tools_called,
    "tools_not_called": tools_not_called,
    "tool_count": tool_count,
    "max_attempts": max_attempts,
    "tool_result_contains": tool_result_contains,
    "findings_count": findings_count,
    "finding_field": finding_field,
    "no_finding": no_finding,
    "no_finding_line": no_finding_line,
    "confirms_asked": confirms_asked,
    "stop": stop,
    "answer_contains": answer_contains,
    "answer_not_contains": answer_not_contains,
    "answer_regex": answer_regex,
    "answer_in_english": answer_in_english,
    "answer_shorter": answer_shorter,
    "no_numbers": no_numbers,
    "gold_quota": gold_quota,
    "gold_absent": gold_absent,
    "pillars_cited": pillars_cited,
    "budget_stop": budget_stop,
    "asks_user": asks_user,
    "critic_clean": critic_clean,
    "unverified_empty": unverified_empty,
    "arg_contains": arg_contains,
    "distinct_args": distinct_args,
    "no_fact": no_fact,
    "commands_ok": commands_ok,
    "retrieved": retrieved,
    "cites_docs": cites_docs,
}


def score_task(run: TaskRun, task: dict) -> TaskScore:
    if not all(CHECKS[c["type"]](run, c) for c in task.get("precondition", [])):
        return TaskScore(status="invalid", failed=["precondition"])
    failed = [c["type"] for c in task["checks"] if not CHECKS[c["type"]](run, c)]
    return TaskScore(status="failed" if failed else "passed", failed=failed)
