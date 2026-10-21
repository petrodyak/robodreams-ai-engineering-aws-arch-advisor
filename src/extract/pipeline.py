"""Stage 1 pipeline: one Working Set document -> one Run Record (docs/stage1-data-contract.md).

The provider (src/extract/llm/) only sends messages and returns raw text. Everything that
judges an answer lives here, once, so Claude and Ollama go through identical logic:
validation against the schema with the service check (contract items 2, 9), the one repair
call (item 16), and the Run Record with summed usage, latency and attempts (items 12, 19).

A run appends one line per document to results/runs/<run_id>.jsonl and skips documents that
are already in the file, so an interrupted run resumes without paying twice. The run id names
the model, prompt version and sampling, so one file never mixes configurations.
"""

import csv
import json
import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path

import yaml
from pydantic import ValidationError

from src.extract.llm import LLMCallError, LLMClient, LLMReply
from src.extract.schema import (
    Group,
    RunRecord,
    Sampling,
    ServiceDocument,
    Status,
    Usage,
    answer_context,
)

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw"
MANIFEST = RAW_DIR / "manifest.csv"
PROMPTS_DIR = ROOT / "prompts"
SAMPLING_CONFIG = ROOT / "config" / "sampling.yaml"
RUNS_DIR = ROOT / "results" / "runs"

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


# ---------------------------------------------------------------- inputs


@dataclass(frozen=True)
class Prompt:
    """One prompt version: prompts/extract_<version>.txt."""

    version: str
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
    parts = _SECTION_RE.split(path.read_text())
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
    return Prompt(version=version, **sections)


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

    def text(self, raw_dir: Path = RAW_DIR) -> str:
        return (raw_dir / self.file).with_suffix(".txt").read_text()


def load_manifest(path: Path = MANIFEST) -> list[Document]:
    with open(path, newline="") as f:
        return [
            Document(file=r["file"], service=r["service"], group=Group(r["group"]))
            for r in csv.DictReader(f)
        ]


def make_run_id(model: str, prompt_version: str, sampling_name: str) -> str:
    """Contract item 11, e.g. claude__v1__t0."""
    return f"{model}__{prompt_version}__{sampling_name}"


# ---------------------------------------------------------------- one document


def validate_answer(
    reply: LLMReply, service: str
) -> tuple[ServiceDocument | None, str | None]:
    """The answer as a Service Document, or the error text the repair call carries."""
    try:
        doc = ServiceDocument.model_validate_json(
            reply.text, context=answer_context(service)
        )
        return doc, None
    except ValidationError as error:
        problems = "\n".join(
            f"- {'.'.join(map(str, e['loc'])) or '(document)'}: {e['msg']}"
            for e in error.errors(include_url=False)
        )
        if reply.stop_reason == "max_tokens":
            # The JSON is cut off; say so, a bare "EOF while parsing" does not explain it.
            problems = "- the answer was cut off at the max_tokens limit\n" + problems
        return None, problems


def extract_document(
    client: LLMClient,
    doc: Document,
    text: str,
    prompt: Prompt,
    sampling: Sampling,
) -> RunRecord:
    """Ask, validate, repair at most once (contract item 16), and record what happened."""
    messages = [{"role": "user", "content": prompt.user_message(doc.service, text)}]
    calls: list[LLMReply] = []

    def record(
        status: Status,
        output: ServiceDocument | None,
        error: str | None,
        *,
        extra_attempts: int = 0,
        extra_latency_ms: int = 0,
    ) -> RunRecord:
        # Sums over every call for the document, the repair included (items 12, 19).
        return RunRecord.model_validate(
            {
                "file": doc.file,
                "group": doc.group,
                "model": client.model,
                "prompt_version": prompt.version,
                "sampling": sampling,
                "attempts": sum(c.attempts for c in calls) + extra_attempts,
                "latency_ms": sum(c.latency_ms for c in calls) + extra_latency_ms,
                "usage": Usage(
                    input_tokens=sum(c.usage.input_tokens for c in calls),
                    output_tokens=sum(c.usage.output_tokens for c in calls),
                ),
                "status": status,
                "output": output,
                "error": error,
            },
            context=answer_context(doc.service),
        )

    try:
        calls.append(client.complete(prompt.system, messages, sampling))
    except LLMCallError as error:
        return record(
            Status.FAILED,
            None,
            f"no answer: {error}",
            extra_attempts=error.attempts,
            extra_latency_ms=error.latency_ms,
        )

    output, first_error = validate_answer(calls[0], doc.service)
    if output is not None:
        return record(Status.OK, output, None)
    if calls[0].stop_reason == "max_tokens":
        # Contract item 16, exception: the corrected answer would be as long as the cut one
        # and be cut again, so a repair call only costs money (S3 trial, 21.10).
        return record(Status.FAILED, None, f"{first_error}\n--- no repair call")

    repair = messages + [
        {"role": "assistant", "content": calls[0].text.strip() or EMPTY_ANSWER},
        {"role": "user", "content": prompt.repair_message(first_error)},
    ]
    try:
        calls.append(client.complete(prompt.system, repair, sampling))
    except LLMCallError as error:
        return record(
            Status.FAILED,
            None,
            f"{first_error}\n--- repair call: no answer: {error}",
            extra_attempts=error.attempts,
            extra_latency_ms=error.latency_ms,
        )

    output, second_error = validate_answer(calls[1], doc.service)
    if output is not None:
        # error keeps the first failure: material for the error analysis in REPORT.md
        return record(Status.REPAIRED, output, first_error)
    return record(
        Status.FAILED, None, f"{first_error}\n--- after repair:\n{second_error}"
    )


# ---------------------------------------------------------------- one run


def done_files(path: Path) -> set[str]:
    """Documents that already have a Run Record in this run's file."""
    if not path.exists():
        return set()
    with path.open() as f:
        return {json.loads(line)["file"] for line in f if line.strip()}


def run(
    client: LLMClient,
    docs: Iterable[Document],
    prompt: Prompt,
    sampling: Sampling,
    out_path: Path,
    *,
    raw_dir: Path = RAW_DIR,
    log: Callable[[str], None] = print,
) -> list[RunRecord]:
    """Extract every document not yet in `out_path`; return the new Run Records."""
    docs = list(docs)
    done = done_files(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    new: list[RunRecord] = []
    with out_path.open("a") as f:
        for i, doc in enumerate(docs, 1):
            prefix = f"[{i}/{len(docs)}] {doc.file}"
            if doc.file in done:
                log(f"{prefix}: already in {out_path.name}, skipped")
                continue
            rec = extract_document(client, doc, doc.text(raw_dir), prompt, sampling)
            # one line per document, flushed at once: a crash loses at most this document
            f.write(rec.model_dump_json() + "\n")
            f.flush()
            new.append(rec)
            log(
                f"{prefix}: {rec.status.value}, {rec.attempts} call(s), "
                f"{rec.latency_ms / 1000:.1f} s, "
                f"in {rec.usage.input_tokens:,} / out {rec.usage.output_tokens:,} tokens"
            )
    return new
