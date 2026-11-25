"""`record_finding`: the agent's one side effect, gated in code (spec §8, D13, D23, ADR-0010).

Order of checks, cheapest first, so a refusal or a repeat never reaches the person:

1. arguments: `null` severity / best practice (the strict-mode way to say "unknown"), the id pattern,
   the id occurs in the corpus, the source is a label of this session, the source is a current
   document, the architecture was read in this session;
2. a rejection for this architecture version (Task 24.4);
3. a row that already exists and is open: `already open since <date>`, no question;
4. the guard: `read_only` never writes, `confirm` asks the person, `auto` (tests only) writes;
5. the write: insert, or reopen a resolved row, in one transaction (`Store.insert_or_reopen_finding`).

The pillar is derived from the id, not sent by the model (ADR-0002). The `duplicate` fault commits the
write and then reports a dropped connection; the tool is never retried automatically, and a second
call meets the `UNIQUE` key.
"""

import hashlib
import json
import re
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from src.agent.faults import ConnectionDropped, Fault, faults_for
from src.agent.store import FindingRow, Store
from src.agent.tools import ToolEntry, ToolOutcome

Confirm = Callable[[str, dict], bool]

# spec §8 (amended 25.11): 3-7 letters, so GENSEC01-BP01 and MLCOST04-BP02 pass
BP_PATTERN = re.compile(r"^[A-Z]{3,7}\d{2}-BP\d{2}$")
# the last letters of an id's prefix name its pillar (REL09 → Reliability, GENSEC01 → Security)
PILLARS = {
    "OPS": "Operational Excellence",
    "SEC": "Security",
    "REL": "Reliability",
    "PERF": "Performance Efficiency",
    "COST": "Cost Optimization",
    "SUS": "Sustainability",
}
NOT_CONFIRMED = "NOT DONE: the person did not confirm; do not retry"
READ_ONLY = "NOT DONE: recording is switched off (autonomy read_only); report the finding in the answer"


class RecordFindingArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    architecture_id: str = Field(pattern=r"^[a-z0-9][a-z0-9-]{2,39}$")
    best_practice: str | None
    severity: Literal["high", "medium", "low"] | None
    summary: str = Field(min_length=1, max_length=300)
    source: str


def normalize_bp(raw: str) -> str:
    """` rel09-bp01. ` → `REL09-BP01`: trimmed, trailing punctuation off, upper case."""
    return raw.strip().rstrip(".,;:!?").strip().upper()


def pillar_of(best_practice: str) -> str:
    letters = re.match(r"[A-Z]+", best_practice)
    if letters:
        for suffix, pillar in PILLARS.items():
            if letters.group().endswith(suffix):
                return pillar
    raise ValueError(f"no pillar for {best_practice}")


def canonical_hash(doc: dict) -> str:
    """sha256 of the sorted-key JSON without `updated`: formatting or a new date is the same version."""
    body = {k: v for k, v in doc.items() if k != "updated"}
    text = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode()).hexdigest()


def guard(
    name: str, args: dict, autonomy: str, confirm: Confirm, *, prompt: str | None = None
) -> str | None:
    """The NOT DONE text, or None when the call may run (lesson 11 guard; the check is in code)."""
    if autonomy == "read_only":
        return READ_ONLY
    if autonomy == "auto":
        return None
    return None if confirm(prompt or name, args) else NOT_CONFIRMED


@dataclass
class FindingContext:
    store: Store
    session_id: int
    autonomy: str
    confirm: Confirm
    known_bp: set[str]
    arch_hashes: dict[str, str]  # filled by the get_architecture wrapper (Task 23.3)
    blocked_docs: set[
        str
    ]  # superseded editions and the adversarial overlay (Task 24.2)
    today: date
    faults: list[Fault] = field(default_factory=list)


def _not_done(text: str) -> ToolOutcome:
    return ToolOutcome(text=f"NOT DONE: {text}", is_error=False)


def _error(text: str) -> ToolOutcome:
    return ToolOutcome(text=f"ERROR: {text}", is_error=True)


def make_record_finding(ctx: FindingContext) -> ToolEntry:
    duplicate = any(
        f.kind == "duplicate" for f in faults_for("record_finding", ctx.faults)
    )

    def record_finding(args: RecordFindingArgs) -> ToolOutcome:
        if args.severity is None:
            return _error("severity is missing: ask the user")
        if args.best_practice is None:
            return _error(
                "best_practice is missing: search the corpus for the matching best practice "
                "or ask the user"
            )
        bp = normalize_bp(args.best_practice)
        if not BP_PATTERN.fullmatch(bp):
            return _error(
                f"'{args.best_practice}' is not a Well-Architected best-practice id such as "
                "REL09-BP01"
            )
        if bp not in ctx.known_bp:
            return _not_done(
                f"{bp} does not occur in the corpus: report the gap in the answer, "
                "but it cannot be recorded"
            )
        label = args.source.strip().strip("[]").upper()
        chunk_id = ctx.store.label_map(ctx.session_id).get(label)
        if chunk_id is None:
            return _not_done(f"unknown source label {label} in this session")
        if chunk_id.split("#")[0] in ctx.blocked_docs:
            return _not_done("a finding must rest on a current document")
        arch_hash = ctx.arch_hashes.get(args.architecture_id)
        if arch_hash is None:
            return _not_done("read the architecture with get_architecture first")

        existing = ctx.store.find_finding(args.architecture_id, bp)
        if existing is not None and existing.status == "open":
            if existing.architecture_hash != arch_hash:
                ctx.store.insert_or_reopen_finding(
                    existing.model_copy(update={"architecture_hash": arch_hash})
                )
            return ToolOutcome(
                text=f"already open since {existing.opened_at.isoformat()}",
                is_error=False,
                data={"finding_id": existing.id, "status": "already_open"},
            )

        pillar = pillar_of(bp)
        prompt = f'Record [{args.severity} · {pillar} · {bp}] "{args.summary}"?'
        refused = guard(
            "record_finding",
            args.model_dump(),
            ctx.autonomy,
            ctx.confirm,
            prompt=prompt,
        )
        if refused is not None:
            return ToolOutcome(text=refused, is_error=False)

        outcome = ctx.store.insert_or_reopen_finding(
            FindingRow(
                id=None,
                architecture_id=args.architecture_id,
                pillar=pillar,
                best_practice=bp,
                severity=args.severity,
                summary=args.summary,
                source_chunk_id=chunk_id,
                status="open",
                architecture_hash=arch_hash,
                opened_at=ctx.today,
                resolved_at=None,
            )
        )
        if duplicate:
            raise ConnectionDropped()
        data = {"finding_id": outcome.finding_id, "status": outcome.status}
        if (
            outcome.status == "reopened"
            and existing is not None
            and existing.resolved_at
        ):
            text = f"reopened (was resolved on {existing.resolved_at.isoformat()})"
        else:
            text = (
                f"recorded {bp} ({pillar}, {args.severity}) for {args.architecture_id} "
                f"as finding #{outcome.finding_id}"
            )
        return ToolOutcome(text=text, is_error=False, data=data)

    def run(args: RecordFindingArgs) -> ToolOutcome:
        try:
            return record_finding(args)
        except ConnectionDropped:
            return ToolOutcome(
                text=(
                    "ERROR: connection lost after the write; the result is unknown. "
                    "Do not assume it failed: calling record_finding again is safe and reports "
                    "whether the finding is already recorded"
                ),
                is_error=True,
                faults=["duplicate"],
            )

    return ToolEntry(fn=run, args_model=RecordFindingArgs, read_only=False)
