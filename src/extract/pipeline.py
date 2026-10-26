"""Stage 1 pipeline: one Working Set document -> one Run Record (docs/stage1-data-contract.md).

The provider (src/extract/llm/) only sends messages and returns raw text. Everything that
judges an answer lives here, once, so Claude and Ollama go through identical logic:
validation against the schema with the service check (contract items 2, 9), the one repair
call (item 16), and the Run Record with summed usage, latency and attempts (items 12, 19).

A run appends one line per document to results/runs/jsonl/<run_id>.jsonl and skips documents
that are already in the file, so an interrupted run resumes without paying twice. The run id
names the model, prompt version and sampling, so one file never mixes configurations. After
every record the file is mirrored as results/runs/md/<run_id>.md for reading by a person
(src/extract/report_md.py); the JSONL stays the only thing code reads.
"""

import csv
import json
import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from pydantic import ValidationError

from src.extract.grounding import (
    ALL_CHECKS,
    ENDPOINT_CHECKS,
    QUOTA_CHECKS,
    VALIDATION_VERSION,
    Grounding,
)
from src.extract.llm import (
    LLMCallError,
    LLMClient,
    LLMReply,
    llm_schema_sha,
    short_sha,
)
from src.extract.parts import PARTS_SCOPE, merge, part_rows, spill, split_chapter
from src.extract.report_md import write_markdown
from src.extract.schema import (
    Group,
    PartRecord,
    RunRecord,
    Sampling,
    ServiceDocument,
    Status,
    Usage,
    answer_context,
    worst_status,
)

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw"
MANIFEST = RAW_DIR / "manifest.csv"


@dataclass(frozen=True)
class DocumentSet:
    """A folder of documents with its manifest and its gold files (contract item 20).

    `raw` is the Working Set (30 documents, gold in data/gold/); `holdout` is the Held-out
    Set of step 12 (10 documents never seen while writing prompt v2, gold in
    data/holdout/gold/). The scope suffix is part of a run id over the set.
    """

    name: str
    dir: Path
    gold_dir: Path
    scope: (
        str  # run id suffix: "" for the Working Set, "__holdout" for the Held-out Set
    )

    @property
    def manifest(self) -> Path:
        return self.dir / "manifest.csv"


WORKING_SET = DocumentSet("raw", RAW_DIR, ROOT / "data" / "gold", "")
HOLDOUT_SET = DocumentSet(
    "holdout",
    ROOT / "data" / "holdout",
    ROOT / "data" / "holdout" / "gold",
    "__holdout",
)
DOCUMENT_SETS = {s.name: s for s in (WORKING_SET, HOLDOUT_SET)}
PROMPTS_DIR = ROOT / "prompts"
SAMPLING_CONFIG = ROOT / "config" / "sampling.yaml"
RUNS_DIR = ROOT / "results" / "runs" / "jsonl"  # contract item 12: the source of truth
RUNS_MD_DIR = ROOT / "results" / "runs" / "md"  # its human-readable mirror, derived

# Sections of a prompt file and the placeholders each must contain (prompts/CHANGELOG.md).
PROMPT_SECTIONS = {
    "system": set(),
    "user": {"service", "document"},
    "repair": {"error"},
}
_SECTION_RE = re.compile(r"^=== (\w+) ===$", re.MULTILINE)
_PLACEHOLDER_RE = re.compile(r"\{(\w+)\}")

# The API rejects an empty assistant turn; a refusal or an empty answer still gets its repair.
EMPTY_ANSWER = "(empty answer)"


class NoAnswer(Exception):
    """The provider gave no answer after its retries (contract item 15): no Run Record.

    A transport failure says nothing about the model, so the document is left out of the
    run file and the next run of the same command asks again. `spent` is what the calls
    that did answer cost; it is lost with the document, so the run log shows it.
    """

    def __init__(self, message: str, spent: Usage):
        super().__init__(message)
        self.spent = spent


# ---------------------------------------------------------------- inputs


@dataclass(frozen=True)
class Prompt:
    """One prompt version: prompts/extract_<version>.txt."""

    version: str
    sha: str  # short_sha of the file's bytes: the provenance id written to every record
    system: str
    user: str
    repair: str

    def user_message(self, service: str, document: str) -> str:
        return _fill(self.user, service=service, document=document)

    def repair_message(self, error: str) -> str:
        return _fill(self.repair, error=error)


def _fill(template: str, **values: str) -> str:
    # One pass over the template only: braces or "{service}" inside the document text are
    # data and stay untouched, which str.format/str.replace would not guarantee.
    return _PLACEHOLDER_RE.sub(lambda m: values[m.group(1)], template)


def load_prompt(version: str, prompts_dir: Path = PROMPTS_DIR) -> Prompt:
    path = prompts_dir / f"extract_{version}.txt"
    raw = path.read_bytes()
    parts = _SECTION_RE.split(raw.decode())
    # split() gives [text before the first header, name, body, name, body, ...]
    sections = {name: body.strip() for name, body in zip(parts[1::2], parts[2::2])}
    if set(sections) != set(PROMPT_SECTIONS):
        raise ValueError(
            f"{path.name}: sections {sorted(sections)}, expected {sorted(PROMPT_SECTIONS)}"
        )
    for name, required in PROMPT_SECTIONS.items():
        found = set(_PLACEHOLDER_RE.findall(sections[name]))
        if found != required:
            raise ValueError(
                f"{path.name} [{name}]: placeholders {sorted(found)}, "
                f"expected {sorted(required)}"
            )
    return Prompt(version=version, sha=short_sha(raw), **sections)


def load_sampling(name: str, path: Path = SAMPLING_CONFIG) -> Sampling:
    configs = yaml.safe_load(path.read_text())["sampling"]
    if name not in configs:
        raise ValueError(
            f"unknown sampling {name!r}, expected one of {sorted(configs)}"
        )
    # top_p is left unset in both configurations (contract item 14)
    return Sampling(name=name, top_p=None, **configs[name])


@dataclass(frozen=True)
class Document:
    """One row of data/raw/manifest.csv: a Working Set document and its Target Service."""

    file: str  # the PDF name, e.g. 006-amazon-aurora-dsql.pdf
    service: str
    group: Group
    # in the Golden Set (gold=1); not part of equality, a document is the same either way
    gold: bool = field(default=False, compare=False)

    def text(self, raw_dir: Path = RAW_DIR) -> str:
        return (raw_dir / self.file).with_suffix(".txt").read_text()


def load_manifest(path: Path = MANIFEST) -> list[Document]:
    with open(path, newline="") as f:
        return [
            Document(
                file=r["file"],
                service=r["service"],
                group=Group(r["group"]),
                gold=r["gold"] == "1",
            )
            for r in csv.DictReader(f)
        ]


GOLD_SCOPE = (
    "__gold"  # run id suffix of a run over the Golden Set only (contract item 11)
)


def make_run_id(
    model: str,
    prompt_version: str,
    sampling_name: str,
    *,
    gold: bool = False,
    doc_set: DocumentSet = WORKING_SET,
    validation_version: str = VALIDATION_VERSION,
    parts: bool = False,
) -> str:
    """Contract item 11, e.g. claude__v1__t0, or claude__v1__t05__gold for a run over the
    Golden Set only: the scope is in the name, so a full run never resumes into its file.
    A run over the Held-out Set adds `__holdout` before `__gold`
    (claude__v2__t0__holdout__gold). A validation other than the first adds `__val<N>`
    last (claude__v2__t0__val2): the runs judged by validation "1" keep their names, and
    a re-run under a stricter validation never resumes into them (the provenance guard
    would refuse it anyway). A run in parts (step 13) adds `__parts` right after the
    sampling (claude__v2__t0__parts__val2): it is a configuration, like the prompt, and
    comes before the scopes."""
    run_id = f"{model}__{prompt_version}__{sampling_name}"
    if parts:
        run_id += PARTS_SCOPE
    run_id += doc_set.scope
    if gold:
        run_id += GOLD_SCOPE
    if validation_version != "1":
        run_id += f"__val{validation_version}"
    return run_id


# ---------------------------------------------------------------- one document


def validate_answer(
    reply: LLMReply,
    service: str,
    grounding: Grounding | None = None,
    checks: frozenset[str] = ALL_CHECKS,
) -> tuple[ServiceDocument | None, str | None]:
    """The answer as a Service Document, or the error text the repair call carries.

    Two layers, in order: the schema with the format checks (ADR-0003) — does the answer
    look right — and, with a `grounding`, the chapter itself (ADR-0005) — is every row
    printed in it. A grounding error is reported in the schema's `- path: message` form.
    """
    try:
        doc = ServiceDocument.model_validate_json(
            reply.text, context=answer_context(service)
        )
    except ValidationError as error:
        problems = "\n".join(
            f"- {'.'.join(map(str, e['loc'])) or '(document)'}: {e['msg']}"
            for e in error.errors(include_url=False)
        )
        if reply.stop_reason == "max_tokens":
            # The JSON is cut off; say so, a bare "EOF while parsing" does not explain it.
            problems = "- the answer was cut off at the max_tokens limit\n" + problems
        return None, problems
    if grounding is not None and (errors := grounding.errors(doc, checks)):
        return None, "\n".join(f"- {e}" for e in errors)
    return doc, None


@dataclass
class Attempt:
    """One ask → validate → at most one repair (contract item 16) over one text."""

    calls: list[LLMReply]
    output: ServiceDocument | None
    first_error: str | None  # why the first answer was rejected; None when it passed
    error: (
        str | None
    )  # the record's error text: None (ok), first (repaired), both (failed)

    @property
    def status(self) -> Status:
        if self.output is None:
            return Status.FAILED
        return Status.OK if self.first_error is None else Status.REPAIRED

    @property
    def usage(self) -> Usage:
        return Usage(
            input_tokens=sum(c.usage.input_tokens for c in self.calls),
            output_tokens=sum(c.usage.output_tokens for c in self.calls),
        )

    @property
    def attempts(self) -> int:
        return sum(c.attempts for c in self.calls)

    @property
    def latency_ms(self) -> int:
        return round(sum(c.latency_ms for c in self.calls))


def ask(
    client: LLMClient,
    prompt: Prompt,
    sampling: Sampling,
    service: str,
    text: str,
    grounding: Grounding,
    checks: frozenset[str] = ALL_CHECKS,
    spent_before: Usage | None = None,
) -> Attempt:
    """Ask for `text`, validate, repair at most once; the same loop for a whole document
    and for one part of it (step 13), which differ only in `text` and `checks`."""
    messages = [{"role": "user", "content": prompt.user_message(service, text)}]
    calls: list[LLMReply] = []

    def spent() -> Usage:
        before = spent_before or Usage(input_tokens=0, output_tokens=0)
        return Usage(
            input_tokens=before.input_tokens + sum(c.usage.input_tokens for c in calls),
            output_tokens=before.output_tokens
            + sum(c.usage.output_tokens for c in calls),
        )

    try:
        calls.append(client.complete(prompt.system, messages, sampling))
    except LLMCallError as error:
        raise NoAnswer(f"no answer: {error}", spent()) from error

    output, first_error = validate_answer(calls[0], service, grounding, checks)
    if output is not None:
        return Attempt(calls, output, None, None)
    if calls[0].stop_reason == "max_tokens":
        # Contract item 16, exception: the corrected answer would be as long as the cut one
        # and be cut again, so a repair call only costs money (S3 trial, 21.10).
        return Attempt(calls, None, first_error, f"{first_error}\n--- no repair call")

    repair = messages + [
        {"role": "assistant", "content": calls[0].text.strip() or EMPTY_ANSWER},
        {"role": "user", "content": prompt.repair_message(first_error)},
    ]
    try:
        calls.append(client.complete(prompt.system, repair, sampling))
    except LLMCallError as error:
        raise NoAnswer(f"repair call: no answer: {error}", spent()) from error

    output, second_error = validate_answer(calls[1], service, grounding, checks)
    if output is not None:
        # error keeps the first failure: material for the error analysis in REPORT.md
        return Attempt(calls, output, first_error, first_error)
    return Attempt(
        calls, None, first_error, f"{first_error}\n--- after repair:\n{second_error}"
    )


def extract_document(
    client: LLMClient,
    doc: Document,
    text: str,
    prompt: Prompt,
    sampling: Sampling,
    *,
    parts: bool = False,
) -> RunRecord:
    """One Run Record for `doc`: the whole text in one ask, or (step 13) its endpoints
    part and its quotas part in one ask each, merged by code."""
    grounding = Grounding.of(text, doc.service)  # what the chapter prints (ADR-0005)
    base = {
        "file": doc.file,
        "group": doc.group,
        "model": client.model,
        "prompt_version": prompt.version,
        "prompt_sha": prompt.sha,
        "schema_sha": llm_schema_sha(),
        "validation_version": VALIDATION_VERSION,
        "sampling": sampling,
    }
    if not parts:
        a = ask(client, prompt, sampling, doc.service, text, grounding)
        return RunRecord.model_validate(
            {
                **base,
                "attempts": a.attempts,
                "latency_ms": a.latency_ms,
                "usage": a.usage,
                "status": a.status,
                "output": a.output,
                "error": a.error,
            },
            context=answer_context(doc.service),
        )

    split = split_chapter(text, doc.service)
    attempts: dict[str, Attempt] = {}
    records: list[PartRecord] = []
    spent = Usage(input_tokens=0, output_tokens=0)
    for name, checks in (("endpoints", ENDPOINT_CHECKS), ("quotas", QUOTA_CHECKS)):
        part_text = split.text(name)
        if not part_text:
            continue  # no quotas block printed: the merge says `none` (parts.py)
        a = ask(
            client, prompt, sampling, doc.service, part_text, grounding, checks, spent
        )
        attempts[name] = a
        spent = Usage(
            input_tokens=spent.input_tokens + a.usage.input_tokens,
            output_tokens=spent.output_tokens + a.usage.output_tokens,
        )
        records.append(
            PartRecord(
                name=name,
                words=len(part_text.split()),
                attempts=a.attempts,
                latency_ms=a.latency_ms,
                usage=a.usage,
                status=a.status,
                rows=None if a.output is None else part_rows(name, a.output),
                spill=None if a.output is None else spill(name, a.output),
                error=a.error,
            )
        )
    status = worst_status(r.status for r in records)
    output = None
    if status != Status.FAILED:
        output = merge(
            doc.service,
            attempts["endpoints"].output,
            attempts["quotas"].output if "quotas" in attempts else None,
        )
        # the merged document against the whole chapter, G1–G3: code only, no call
        if leftovers := grounding.errors(output):
            raise ValueError(f"{doc.file}: merged document not grounded: {leftovers}")
    errors = [f"[{r.name}]\n{r.error}" for r in records if r.error is not None]
    return RunRecord.model_validate(
        {
            **base,
            "attempts": sum(r.attempts for r in records),
            "latency_ms": sum(r.latency_ms for r in records),
            "usage": spent,
            "status": status,
            "output": output,
            "error": "\n".join(errors) if errors else None,
            "parts": records,
        },
        context=answer_context(doc.service),
    )


# ---------------------------------------------------------------- one run


def drop_cut_off_tail(path: Path, log: Callable[[str], None]) -> None:
    """Remove what a killed process left after the last complete line (finding F8).

    Every record is appended as one line ending in "\\n", so anything after the last
    "\\n" is an unfinished append: kept, it would glue the next record onto itself.
    """
    if not path.exists():
        return
    data = path.read_bytes()
    keep = data.rfind(b"\n") + 1
    if keep < len(data):
        path.write_bytes(data[:keep])
        log(f"{path.name}: dropped a cut-off last line ({len(data) - keep:,} bytes)")


class ProvenanceMismatch(Exception):
    """A resume would append records made with another prompt or schema (contract item 12).

    A run file is one configuration. When the prompt file or the schema changed since the
    run started, the right move is a new run id, not a second configuration under the old
    one (finding F17); so `run` refuses instead of writing.
    """


Provenance = tuple[str, str, str]  # (prompt_sha, schema_sha, validation_version)


def done_files(path: Path, provenance: Provenance | None = None) -> set[str]:
    """Documents that already have a Run Record in this run's file.

    With `provenance` = (prompt_sha, schema_sha, validation_version) of the run about to
    resume, every stored record must carry the same triple, or `ProvenanceMismatch` is
    raised before any call is made. A line that is not JSON is real damage (only the last line can be cut off, and
    `run` drops that one first), so it raises instead of being skipped silently.
    """
    if not path.exists():
        return set()
    done = set()
    # split("\n"), not splitlines(): that also splits on characters such as U+2028,
    # which may legitimately sit inside a JSON string
    for n, line in enumerate(path.read_text().split("\n"), 1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
            done.add(rec["file"])
            stored = (rec["prompt_sha"], rec["schema_sha"], rec["validation_version"])
        except (ValueError, KeyError) as error:
            raise ValueError(
                f"{path}: line {n} is not a Run Record: {error}"
            ) from error
        if provenance is not None and stored != provenance:
            raise ProvenanceMismatch(
                f"{path.name}: line {n} ({rec['file']}) was made with prompt "
                f"{stored[0]} / schema {stored[1]} / validation {stored[2]}, this run "
                f"has prompt {provenance[0]} / schema {provenance[1]} / validation "
                f"{provenance[2]}: the prompt, schema or validation changed since the "
                "run started — start a new run id, do not resume"
            )
    return done


def missing_files(docs: Iterable[Document], path: Path) -> list[str]:
    """Documents of the run that have no Run Record yet, in manifest order."""
    done = done_files(path)
    return [d.file for d in docs if d.file not in done]


@dataclass(frozen=True)
class RunResult:
    """What one `run` call added: the new Run Records, and the tokens paid for documents
    that ended without one (finding F10), so the cost summary counts them too."""

    records: list[RunRecord]
    lost: Usage


def run(
    client: LLMClient,
    docs: Iterable[Document],
    prompt: Prompt,
    sampling: Sampling,
    out_path: Path,
    *,
    md_path: Path | None = None,
    raw_dir: Path = RAW_DIR,
    parts: bool = False,
    log: Callable[[str], None] = print,
) -> RunResult:
    """Extract every document not yet in `out_path`; return what this call added.

    `md_path` (default: `out_path` with the suffix .md) is rewritten from the whole JSONL
    after every record, so it is complete even when this call adds nothing.
    """
    docs = list(docs)
    md_path = md_path or out_path.with_suffix(".md")
    drop_cut_off_tail(out_path, log)
    done = done_files(out_path, (prompt.sha, llm_schema_sha(), VALIDATION_VERSION))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_markdown(out_path, md_path)  # the mirror of a run that was resumed or cut off
    new: list[RunRecord] = []
    lost = Usage(input_tokens=0, output_tokens=0)
    with out_path.open("a") as f:
        for i, doc in enumerate(docs, 1):
            prefix = f"[{i}/{len(docs)}] {doc.file}"
            if doc.file in done:
                log(f"{prefix}: already in {out_path.name}, skipped")
                continue
            try:
                rec = extract_document(
                    client, doc, doc.text(raw_dir), prompt, sampling, parts=parts
                )
            except NoAnswer as error:
                log(
                    f"{prefix}: {error}; not recorded, the next run retries it "
                    f"(spent in {error.spent.input_tokens:,} / "
                    f"out {error.spent.output_tokens:,} tokens)"
                )
                lost = Usage(
                    input_tokens=lost.input_tokens + error.spent.input_tokens,
                    output_tokens=lost.output_tokens + error.spent.output_tokens,
                )
                continue
            # one line per document, flushed at once: a crash loses at most this document
            f.write(rec.model_dump_json() + "\n")
            f.flush()
            write_markdown(out_path, md_path)
            new.append(rec)
            log(
                f"{prefix}: {rec.status.value}, {rec.attempts} call(s), "
                f"{rec.latency_ms / 1000:.1f} s, "
                f"in {rec.usage.input_tokens:,} / out {rec.usage.output_tokens:,} tokens"
            )
    return RunResult(new, lost)
