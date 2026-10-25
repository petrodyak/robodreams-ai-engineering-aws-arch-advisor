"""Stage 1 metrics: every run file -> results/metrics.csv (contract items 13, 17-19).

One row per run x Group plus a total row per run. Three families of numbers:

- validity: `% ok` (valid on the first answer) and `% ok + repaired`, with the denominator
  taken from the manifest, not from the run file (item 18): a document the run never
  recorded (no answer, item 15) counts as failed and is also reported as `no_answer`;
- latency p50 / p95 over the recorded documents (wall clock per document, item 19) and the
  cost per 1,000 documents from `usage` and list prices (Claude) or $0 plus the summed
  wall clock as the compute note (local model);
- accuracy against the Golden Set (item 17): Endpoint Rows matched by `endpoint`, Quota Rows
  by `name`, as key precision / recall, then per-field accuracy on the matched rows.
  `description` is compared case-insensitively, everything else exactly (whitespace was
  already collapsed by the schema). A gold document without an output (`failed` or no
  answer) is scored as an empty extraction: no rows predicted, every gold row missing.
  Group and total numbers are micro-averages (sums over rows, then one ratio), so a
  254-row document weighs 254 rows, not one document.

`python -m src.extract.metrics` (`make metrics`) rewrites the CSV from every file in
results/runs/jsonl/ and prints a one-line-per-run summary.
"""

import csv
import re
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path

from src.extract.llm.claude import cost_usd
from src.extract.pipeline import (
    GOLD_SCOPE,
    HOLDOUT_SET,
    ROOT,
    RUNS_DIR,
    WORKING_SET,
    Document,
    DocumentSet,
    load_manifest,
)
from src.extract.report_md import load_records
from src.extract.schema import (
    EndpointRow,
    Group,
    QuotaRow,
    RunRecord,
    ServiceDocument,
    Status,
    stored_context,
)

GOLD_DIR = ROOT / "data" / "gold"
METRICS_FILE = ROOT / "results" / "metrics.csv"
TOTAL = "total"  # the `group` value of a run's total row (item 13)
CLAUDE_MODEL = "claude"  # the only paid model (short name in run ids)

# <model>__<prompt_version>__<sampling_name>[__gold] (contract item 11)
RUN_ID_RE = re.compile(
    r"^(?P<model>[^_]+(?:_[^_]+)*)__(?P<prompt>v\d+)__(?P<sampling>\w+?)"
    r"(?P<holdout>__holdout)?(?P<gold>__gold)?(?:__val(?P<val>\d+))?$"
)

# Endpoint and quota fields scored on matched rows (item 17). `endpoint_type` is computed
# from the hostname and `endpoint` / `name` are the keys, so neither is scored.
ENDPOINT_FIELDS = ("region_name", "region_code", "protocol")
QUOTA_FIELDS = ("default", "adjustable", "description")
CASE_INSENSITIVE = {"description"}

COLUMNS = [
    "run_id", "model", "prompt_version", "prompt_sha", "schema_sha", "validation_version",
    "sampling", "scope", "group",
    "n_docs", "ok", "repaired", "failed", "no_answer", "pct_ok", "pct_ok_or_repaired",
    "latency_p50_ms", "latency_p95_ms", "cost_per_1000_usd", "wallclock_s",
    "gold_docs", "gold_scored", "quota_table_format_acc",
    "ep_precision", "ep_recall", "ep_region_name_acc", "ep_region_code_acc", "ep_protocol_acc",
    "q_precision", "q_recall", "q_default_acc", "q_adjustable_acc", "q_description_acc",
]  # fmt: skip


# ---------------------------------------------------------------- run id and scope


@dataclass(frozen=True)
class RunId:
    model: str
    prompt_version: str
    sampling: str
    gold: bool  # the __gold scope suffix: only the Golden Set documents were run
    validation: str = "1"  # the __val<N> suffix; "1" when absent (contract item 11)
    doc_set: DocumentSet = WORKING_SET  # the __holdout suffix (contract item 20)

    @property
    def scope(self) -> str:
        scope = "gold" if self.gold else "full"
        return scope if self.doc_set is WORKING_SET else f"{self.doc_set.name}-{scope}"


def parse_run_id(run_id: str) -> RunId:
    m = RUN_ID_RE.match(run_id)
    if m is None:
        raise ValueError(
            f"not a run id like claude__v1__t0 or claude__v1__t05__gold: {run_id!r}"
        )
    return RunId(
        m["model"],
        m["prompt"],
        m["sampling"],
        m["gold"] == GOLD_SCOPE,
        m["val"] or "1",
        HOLDOUT_SET if m["holdout"] else WORKING_SET,
    )


def run_scope(run: RunId, docs: Iterable[Document]) -> list[Document]:
    """The documents the run was meant to cover: the denominator of validity (item 18)."""
    return [d for d in docs if d.gold or not run.gold]


def run_provenance(run_id: str, records: list[RunRecord]) -> tuple[str, str, str]:
    """The one (prompt_sha, schema_sha, validation_version) of a run (contract item 12).

    A run file is one prompt, one schema and one validation by definition: its records
    are compared as one configuration. A resumed run after an edit to any of them would
    mix two configurations under one run id (finding F17) — that is an error, not a row.
    """
    triples = {(r.prompt_sha, r.schema_sha, r.validation_version) for r in records}
    if len(triples) > 1:
        raise ValueError(
            f"{run_id}: records with different provenance in one run file: "
            f"{sorted(triples)} — the prompt, schema or validation changed under the run"
        )
    return triples.pop() if triples else ("", "", "")


# ---------------------------------------------------------------- accuracy (item 17)


@dataclass
class Tally:
    """Row-level counts that add up across documents (micro-average)."""

    gold: int = 0  # gold keys
    predicted: int = 0  # predicted keys
    matched: int = 0  # keys in both
    field_total: Counter = field(default_factory=Counter)  # per field: matched rows
    field_correct: Counter = field(default_factory=Counter)

    def add(self, other: "Tally") -> None:
        self.gold += other.gold
        self.predicted += other.predicted
        self.matched += other.matched
        self.field_total.update(other.field_total)
        self.field_correct.update(other.field_correct)

    @property
    def precision(self) -> float | None:
        return _ratio(self.matched, self.predicted)

    @property
    def recall(self) -> float | None:
        return _ratio(self.matched, self.gold)

    def field_accuracy(self, name: str) -> float | None:
        return _ratio(self.field_correct[name], self.field_total[name])


@dataclass
class DocAccuracy:
    """One document against its gold file."""

    endpoints: Tally
    quotas: Tally
    format_correct: bool


def _ratio(num: int, den: int) -> float | None:
    return num / den if den else None


def _value(row: EndpointRow | QuotaRow, name: str) -> object:
    v = getattr(row, name)
    return v.lower() if name in CASE_INSENSITIVE and isinstance(v, str) else v


def match_rows(gold: list, predicted: list, key: str, fields: tuple[str, ...]) -> Tally:
    """Match rows by `key`, then score `fields` on the matched rows (item 17).

    Keys are compared as sets: a hostname printed twice is one row (item 6), so a model
    repeating a row is neither rewarded nor punished for the duplicate.
    """
    gold_by_key = {getattr(r, key): r for r in gold}
    pred_by_key = {getattr(r, key): r for r in predicted}
    matched = gold_by_key.keys() & pred_by_key.keys()
    tally = Tally(
        gold=len(gold_by_key), predicted=len(pred_by_key), matched=len(matched)
    )
    for k in matched:
        g, p = gold_by_key[k], pred_by_key[k]
        for name in fields:
            tally.field_total[name] += 1
            if _value(g, name) == _value(p, name):
                tally.field_correct[name] += 1
    return tally


def score_document(
    gold: ServiceDocument, output: ServiceDocument | None
) -> DocAccuracy:
    """Score one output against its gold file; `None` (failed, no answer) is an empty
    extraction: nothing predicted, every gold row missing, the format wrong."""
    if output is None:
        return DocAccuracy(
            endpoints=Tally(gold=len({r.endpoint for r in gold.endpoints})),
            quotas=Tally(gold=len({r.name for r in gold.quotas})),
            format_correct=False,
        )
    return DocAccuracy(
        endpoints=match_rows(
            gold.endpoints, output.endpoints, "endpoint", ENDPOINT_FIELDS
        ),
        quotas=match_rows(gold.quotas, output.quotas, "name", QUOTA_FIELDS),
        format_correct=gold.quota_table_format == output.quota_table_format,
    )


def load_gold(file: str, gold_dir: Path = GOLD_DIR) -> ServiceDocument:
    path = (gold_dir / file).with_suffix(".json")
    # the service was checked against the manifest when the file was written (tests/test_gold.py)
    return ServiceDocument.model_validate_json(
        path.read_text(), context=stored_context(None)
    )


# ---------------------------------------------------------------- validity, latency, cost


def percentile(values: list[int], p: float) -> float:
    """The p-th percentile (0..100) with linear interpolation between the two nearest
    ranks, the default of numpy and spreadsheets; `values` must not be empty."""
    if not values:
        raise ValueError("percentile of no values")
    xs = sorted(values)
    pos = (len(xs) - 1) * p / 100
    lo = int(pos)
    hi = min(lo + 1, len(xs) - 1)
    return xs[lo] + (xs[hi] - xs[lo]) * (pos - lo)


@dataclass
class GroupMetrics:
    """One row of metrics.csv: a run restricted to the documents of one group (or all)."""

    run_id: str
    run: RunId
    group: str
    docs: list[Document]  # the denominator (item 18)
    records: list[RunRecord]
    provenance: tuple[str, str, str] = (
        "",
        "",
        "",
    )  # prompt_sha, schema_sha, validation_version
    gold_docs: int = 0
    gold_scored: int = 0  # gold documents with an output
    format_correct: int = 0
    endpoints: Tally = field(default_factory=Tally)
    quotas: Tally = field(default_factory=Tally)

    @property
    def statuses(self) -> Counter:
        return Counter(r.status for r in self.records)

    @property
    def no_answer(self) -> int:
        return len(self.docs) - len(self.records)

    def row(self) -> dict[str, object]:
        n = len(self.docs)
        s = self.statuses
        ok, repaired = s[Status.OK], s[Status.REPAIRED]
        latencies = [r.latency_ms for r in self.records]
        tokens_in = sum(r.usage.input_tokens for r in self.records)
        tokens_out = sum(r.usage.output_tokens for r in self.records)
        cost = (
            cost_usd(tokens_in, tokens_out) if self.run.model == CLAUDE_MODEL else 0.0
        )
        ep, q = self.endpoints, self.quotas
        return {
            "run_id": self.run_id,
            "model": self.run.model,
            "prompt_version": self.run.prompt_version,
            "prompt_sha": self.provenance[0],
            "schema_sha": self.provenance[1],
            "validation_version": self.provenance[2],
            "sampling": self.run.sampling,
            "scope": self.run.scope,
            "group": self.group,
            "n_docs": n,
            "ok": ok,
            "repaired": repaired,
            # failed records plus the documents without a record (item 18)
            "failed": s[Status.FAILED] + self.no_answer,
            "no_answer": self.no_answer,
            "pct_ok": _pct(ok, n),
            "pct_ok_or_repaired": _pct(ok + repaired, n),
            "latency_p50_ms": round(percentile(latencies, 50)) if latencies else None,
            "latency_p95_ms": round(percentile(latencies, 95)) if latencies else None,
            # per 1,000 documents, from the recorded documents (tokens of a document that
            # ended without a record are in the run log only, finding F10)
            "cost_per_1000_usd": _round(cost / len(self.records) * 1000, 2)
            if self.records
            else None,
            # the compute note of the local model (item 19): documents ran one after another,
            # so the summed per-document wall clock is the run's wall clock
            "wallclock_s": round(sum(latencies) / 1000),
            "gold_docs": self.gold_docs,
            "gold_scored": self.gold_scored,
            "quota_table_format_acc": _pct(self.format_correct, self.gold_docs),
            "ep_precision": _pct100(ep.precision),
            "ep_recall": _pct100(ep.recall),
            "ep_region_name_acc": _pct100(ep.field_accuracy("region_name")),
            "ep_region_code_acc": _pct100(ep.field_accuracy("region_code")),
            "ep_protocol_acc": _pct100(ep.field_accuracy("protocol")),
            "q_precision": _pct100(q.precision),
            "q_recall": _pct100(q.recall),
            "q_default_acc": _pct100(q.field_accuracy("default")),
            "q_adjustable_acc": _pct100(q.field_accuracy("adjustable")),
            "q_description_acc": _pct100(q.field_accuracy("description")),
        }


def _pct(num: int, den: int) -> float | None:
    return _pct100(_ratio(num, den))


def _pct100(ratio: float | None) -> float | None:
    return None if ratio is None else _round(ratio * 100, 1)


def _round(v: float, digits: int) -> float:
    return round(v + 0.0, digits)  # +0.0 turns a -0.0 into 0.0


# ---------------------------------------------------------------- one run


def run_metrics(
    run_id: str,
    records: list[RunRecord],
    docs: list[Document],
    gold_dir: Path = GOLD_DIR,
) -> list[GroupMetrics]:
    """Rows for one run: one per Group that has documents in the run's scope, then total."""
    run = parse_run_id(run_id)
    scope = run_scope(run, docs)
    provenance = run_provenance(run_id, records)
    if records and provenance[2] != run.validation:
        raise ValueError(
            f"{run_id}: the run id says validation {run.validation!r}, the records say "
            f"{provenance[2]!r}"
        )
    by_file = {r.file: r for r in records}
    unknown = set(by_file) - {d.file for d in scope}
    if unknown:
        raise ValueError(
            f"{run_id}: records for documents outside the run's scope: {sorted(unknown)}"
        )

    accuracy: dict[str, DocAccuracy] = {}
    for d in scope:
        if d.gold:
            rec = by_file.get(d.file)
            output = rec.output if rec is not None else None
            accuracy[d.file] = score_document(load_gold(d.file, gold_dir), output)

    rows = []
    groups = [g.value for g in Group] + [TOTAL]
    for group in groups:
        group_docs = [d for d in scope if group == TOTAL or d.group.value == group]
        if not group_docs:
            continue
        gm = GroupMetrics(
            run_id=run_id,
            run=run,
            group=group,
            docs=group_docs,
            records=[by_file[d.file] for d in group_docs if d.file in by_file],
            provenance=provenance,
        )
        for d in group_docs:
            if d.file not in accuracy:
                continue
            acc = accuracy[d.file]
            rec = by_file.get(d.file)
            gm.gold_docs += 1
            gm.gold_scored += rec is not None and rec.output is not None
            gm.format_correct += acc.format_correct
            gm.endpoints.add(acc.endpoints)
            gm.quotas.add(acc.quotas)
        rows.append(gm)
    return rows


# ---------------------------------------------------------------- all runs -> CSV


def all_metrics(
    runs_dir: Path = RUNS_DIR,
    docs: list[Document] | None = None,
    gold_dir: Path | None = None,
) -> list[GroupMetrics]:
    """Every run file, each against the manifest and gold files of its own document set
    (the `__holdout` suffix, contract item 20); `docs` / `gold_dir` override both (tests)."""
    rows: list[GroupMetrics] = []
    for path in sorted(runs_dir.glob("*.jsonl")):
        doc_set = parse_run_id(path.stem).doc_set
        set_docs = docs if docs is not None else load_manifest(doc_set.manifest)
        set_gold = gold_dir if gold_dir is not None else doc_set.gold_dir
        rows.extend(run_metrics(path.stem, load_records(path), set_docs, set_gold))
    return rows


def write_csv(rows: Iterable[GroupMetrics], path: Path = METRICS_FILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        for gm in rows:
            writer.writerow({k: ("" if v is None else v) for k, v in gm.row().items()})


def summary(rows: Iterable[GroupMetrics]) -> str:
    """The total row of every run as a Markdown table, for the terminal and the chat."""
    header = [
        "run", "docs", "ok %", "ok+rep %", "no ans", "p50 s", "p95 s", "$/1000",
        "ep P/R %", "q P/R %", "fmt %",
    ]  # fmt: skip
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for gm in rows:
        if gm.group != TOTAL:
            continue
        r = gm.row()
        lines.append(
            "| "
            + " | ".join(
                [
                    r["run_id"],
                    str(r["n_docs"]),
                    _s(r["pct_ok"]),
                    _s(r["pct_ok_or_repaired"]),
                    str(r["no_answer"]),
                    _s(
                        None
                        if r["latency_p50_ms"] is None
                        else r["latency_p50_ms"] / 1000
                    ),
                    _s(
                        None
                        if r["latency_p95_ms"] is None
                        else r["latency_p95_ms"] / 1000
                    ),
                    _s(r["cost_per_1000_usd"]),
                    f"{_s(r['ep_precision'])} / {_s(r['ep_recall'])}",
                    f"{_s(r['q_precision'])} / {_s(r['q_recall'])}",
                    _s(r["quota_table_format_acc"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def _s(v: object) -> str:
    if v is None:
        return "—"
    return f"{v:.1f}" if isinstance(v, float) else str(v)


def main() -> None:
    rows = all_metrics()
    write_csv(rows)
    print(f"{METRICS_FILE.relative_to(ROOT)}: {len(rows)} row(s)")
    print(summary(rows))


if __name__ == "__main__":
    main()
