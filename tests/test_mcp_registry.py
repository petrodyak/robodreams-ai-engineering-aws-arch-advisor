"""The architecture registry behind the MCP server (spec §9, D11; src/mcp_server/registry.py)."""

import json
import shutil
from pathlib import Path

import pytest

from src.mcp_server.registry import (
    REGISTRY,
    Architecture,
    InvalidArchitecture,
    list_team,
    load_architecture,
    owner_of,
    resolve_path,
    team_dir,
)

SCHEMA_FILE = REGISTRY / "architecture.schema.json"


def _files() -> list[Path]:
    return sorted(REGISTRY.glob("*/*.json"))


def test_registry_has_the_planned_architectures():
    assert {p.stem for p in _files()} >= {
        "lakehouse-iceberg",
        "streaming-ingest",
        "payments-core",
    }


def test_registry_files_validate():
    for path in _files():
        arch = load_architecture(path)
        assert arch.team == path.parent.name, path
        assert arch.id == path.stem, path


def test_schema_file_is_current():
    expected = json.dumps(Architecture.model_json_schema(), indent=2) + "\n"
    assert SCHEMA_FILE.read_text(encoding="utf-8") == expected


@pytest.mark.parametrize(
    "bad", ["../payments/payments-core", "a/../../x", "ab", "Lakehouse", "x" * 41, ""]
)
def test_path_traversal_rejected(bad):
    with pytest.raises(ValueError):
        resolve_path(REGISTRY, "data-platform", bad)


def test_resolve_path_stays_in_team_folder():
    path = resolve_path(REGISTRY, "data-platform", "lakehouse-iceberg")
    assert path.parent == team_dir(REGISTRY, "data-platform")
    with pytest.raises(ValueError):
        team_dir(REGISTRY, "../payments")


def test_owner_of_other_team():
    assert owner_of(REGISTRY, "payments-core") == "payments"
    assert owner_of(REGISTRY, "lakehouse-iceberg") == "data-platform"
    assert owner_of(REGISTRY, "no-such-arch") is None


def test_owner_of_reads_no_file(monkeypatch):
    def spy(*_args, **_kwargs):
        raise AssertionError("owner_of must not open a file")

    monkeypatch.setattr(Path, "read_text", spy)
    monkeypatch.setattr(Path, "open", spy)
    assert owner_of(REGISTRY, "payments-core") == "payments"


def test_architecture_ids_unique_across_teams():
    stems = [p.stem for p in _files()]
    assert len(stems) == len(set(stems))


def test_list_team_only_lists_its_own_folder():
    rows, broken = list_team(REGISTRY, "data-platform")
    assert {r["architecture_id"] for r in rows} == {
        "lakehouse-iceberg",
        "streaming-ingest",
    }
    assert all(set(r) == {"architecture_id", "name", "updated"} for r in rows)
    assert broken == []


def test_broken_file_named(tmp_path: Path):
    # Review Focus 1: Petro edits an architecture by hand and breaks it
    root = tmp_path / "architectures"
    shutil.copytree(REGISTRY, root)
    path = root / "data-platform" / "streaming-ingest.json"
    doc = json.loads(path.read_text(encoding="utf-8"))
    del doc["components"][0]["service"]
    path.write_text(json.dumps(doc), encoding="utf-8")

    with pytest.raises(InvalidArchitecture) as error:
        load_architecture(path)
    assert error.value.field == "components.0.service"
    assert error.value.file == "streaming-ingest.json"
    assert "components.0.service" in str(error.value)

    rows, broken = list_team(root, "data-platform")
    assert [r["architecture_id"] for r in rows] == ["lakehouse-iceberg"]
    assert broken == ["streaming-ingest.json"]


def test_not_json_is_invalid(tmp_path: Path):
    path = tmp_path / "x-arch.json"
    path.write_text("{not json", encoding="utf-8")
    with pytest.raises(InvalidArchitecture):
        load_architecture(path)


def test_lakehouse_has_the_planned_gaps():
    # architectures/README.md lists these; the review tasks rely on them
    arch = load_architecture(
        resolve_path(REGISTRY, "data-platform", "lakehouse-iceberg")
    )
    services = {c.service for c in arch.components}
    assert {
        "Amazon S3 Tables",
        "AWS Glue",
        "Amazon Athena",
        "AWS Lake Formation",
    } <= services
    s3 = next(c for c in arch.components if c.service == "Amazon S3 Tables")
    assert s3.settings["backup"] == "none"
    glue = next(c for c in arch.components if c.service == "AWS Glue")
    assert glue.settings["concurrent_jobs"] * glue.settings["dpus_per_job"] > 500
    assert arch.region == "eu-central-1"


# --- step 23 review fixes (25.11) ----------------------------------------------------------


def test_list_team_skips_links_out_of_the_folder(tmp_path: Path):
    # review Important 1: a symlink in a team folder must not list another team's architecture
    root = tmp_path / "architectures"
    shutil.copytree(REGISTRY, root)
    (root / "data-platform" / "mirror.json").symlink_to(
        root / "payments" / "payments-core.json"
    )
    rows, broken = list_team(root, "data-platform")
    assert "payments-core" not in {r["architecture_id"] for r in rows}
    assert "mirror.json" in broken


def test_id_must_match_file_name(tmp_path: Path):
    # review Important 2: a hand-copied file that keeps the old id
    root = tmp_path / "architectures"
    shutil.copytree(REGISTRY, root)
    folder = root / "data-platform"
    shutil.copy(folder / "streaming-ingest.json", folder / "copy-of-stream.json")
    with pytest.raises(InvalidArchitecture) as error:
        load_architecture(folder / "copy-of-stream.json")
    assert error.value.field == "id"
    rows, broken = list_team(root, "data-platform")
    assert [r["architecture_id"] for r in rows].count("streaming-ingest") == 1
    assert "copy-of-stream.json" in broken


def test_team_must_match_folder(tmp_path: Path):
    root = tmp_path / "architectures"
    shutil.copytree(REGISTRY, root)
    planted = root / "data-platform" / "payments-core.json"
    shutil.copy(root / "payments" / "payments-core.json", planted)
    with pytest.raises(InvalidArchitecture) as error:
        load_architecture(planted)
    assert error.value.field == "team"
