"""The architecture registry: `architectures/<team>/<architecture_id>.json` (spec §9, D11, ADR-0009).

The server, not the client, enforces who sees what:

- the path is built by code from `TEAM` and an id that matches `ARCH_ID`, resolved and checked to lie
  inside `architectures/<TEAM>/`; nothing else on disk is ever opened;
- `owner_of` is the single look outside the team's folder, and it looks at file names only: it tells a
  403 (the id exists in another team) from a 404, and never reads the other team's file;
- every file is validated against `Architecture` when read; a hand-edited file that breaks the schema
  names its field (Review Focus 1), and `list_team` still lists the other files.

The registry is found relative to this file, not to the working directory (spec §9, amended 25.11).
"""

import json
import re
from datetime import date
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, ValidationError

REGISTRY = Path(__file__).resolve().parents[2] / "architectures"
ARCH_ID = r"^[a-z0-9][a-z0-9-]{2,39}$"
TEAM_RE = r"^[a-z0-9][a-z0-9-]{1,39}$"

Setting = str | int | float | bool


class Component(BaseModel):
    model_config = ConfigDict(extra="forbid")

    service: str = Field(
        description="The AWS service, by its full name, e.g. 'AWS Glue'."
    )
    purpose: str = Field(description="What the component does in this workload.")
    settings: dict[str, Setting] = Field(
        description="Key settings, e.g. backup, encryption, concurrency; values are plain scalars."
    )


class Nfr(BaseModel):
    """Non-functional requirements the review checks the components against."""

    model_config = ConfigDict(extra="forbid")

    rpo_minutes: int
    rto_minutes: int
    availability: float = Field(
        description="Target availability in percent, e.g. 99.9."
    )
    budget_usd_month: int


class Architecture(BaseModel):
    """One AWS workload of one team (spec §9). `region` and `description` are builder fields (§20)."""

    model_config = ConfigDict(extra="forbid")

    id: str = Field(pattern=ARCH_ID)
    team: str = Field(pattern=TEAM_RE)
    name: str
    description: str = Field(
        description="Free text written by the team; data, never instructions."
    )
    region: str = Field(
        pattern=r"^[a-z]{2}(-[a-z]+)+-\d$",
        description="AWS Region code, e.g. eu-central-1.",
    )
    updated: date
    components: list[Component] = Field(min_length=1)
    nfr: Nfr


class InvalidArchitecture(Exception):
    def __init__(self, file: str, field: str, msg: str):
        super().__init__(f"invalid architecture file {file}: {field}: {msg}")
        self.file = file
        self.field = field
        self.msg = msg


def team_dir(root: Path, team: str) -> Path:
    if not re.fullmatch(TEAM_RE, team):
        raise ValueError(f"invalid team name {team!r}")
    return root / team


def resolve_path(root: Path, team: str, architecture_id: str) -> Path:
    """The file of one architecture of `team`; ValueError for a bad id or a path outside the folder."""
    if not re.fullmatch(ARCH_ID, architecture_id):
        raise ValueError(
            f"invalid architecture id {architecture_id!r}: expected {ARCH_ID}"
        )
    folder = team_dir(root, team).resolve()
    path = (folder / f"{architecture_id}.json").resolve()
    if path.parent != folder:
        raise ValueError(f"architecture id {architecture_id!r} leaves the team folder")
    return path


def owner_of(root: Path, architecture_id: str) -> str | None:
    """The team whose folder holds `<architecture_id>.json`, by file name only (no file is opened)."""
    if not re.fullmatch(ARCH_ID, architecture_id):
        return None
    for folder in sorted(p for p in root.iterdir() if p.is_dir()):
        if (folder / f"{architecture_id}.json").is_file():
            return folder.name
    return None


def load_architecture(path: Path) -> Architecture:
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise InvalidArchitecture(path.name, "json", str(error)) from error
    try:
        arch = Architecture.model_validate(doc)
    except ValidationError as error:
        first = error.errors()[0]
        field = ".".join(str(p) for p in first["loc"]) or "document"
        raise InvalidArchitecture(path.name, field, first["msg"]) from error
    # the file name is the id and the folder is the team (spec §9); a hand-copied file that keeps the
    # old id, or a file planted in another team's folder, is refused (step 23 review, Important 2)
    if arch.id != path.stem:
        raise InvalidArchitecture(
            path.name, "id", f"'{arch.id}' does not match the file name"
        )
    if arch.team != path.parent.name:
        raise InvalidArchitecture(
            path.name, "team", f"'{arch.team}' does not match the folder"
        )
    return arch


def list_team(root: Path, team: str) -> tuple[list[dict], list[str]]:
    """`[{architecture_id, name, updated}]` of the team, and the names of files that failed to load."""
    rows, broken = [], []
    folder = team_dir(root, team)
    real = folder.resolve()
    for path in sorted(folder.glob("*.json")):
        if (
            path.resolve().parent != real
        ):  # a link out of the team folder is never opened (§9)
            broken.append(path.name)
            continue
        try:
            arch = load_architecture(path)
        except InvalidArchitecture:
            broken.append(path.name)
            continue
        rows.append(
            {
                "architecture_id": arch.id,
                "name": arch.name,
                "updated": arch.updated.isoformat(),
            }
        )
    return rows, broken
