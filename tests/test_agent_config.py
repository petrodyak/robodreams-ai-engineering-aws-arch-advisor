"""config/agent.yaml: the HW 3 limits and settings (spec §6, D19)."""

from datetime import date
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from src.agent.config import load_agent_config


def test_load_agent_config_values():
    cfg = load_agent_config()
    assert cfg.model == "claude-haiku-5-5"
    assert cfg.effort == "medium"
    assert (
        cfg.max_tokens_per_call == 8000
    )  # a six-pillar review with thinking was cut at 4000 (F33)
    assert cfg.today == date(2026, 11, 24)
    assert cfg.autonomy == "confirm"
    assert cfg.k == 5
    assert cfg.critic_retries == 1
    assert cfg.history_budget_tokens == 6000
    assert cfg.quota_max_rows == 10
    assert cfg.relevance_threshold == 3.6  # measured in Task 22.4, Step 5
    limits = cfg.limits
    assert limits.max_steps == 12
    assert limits.max_tokens == 200_000
    assert limits.max_usd == 0.05
    assert limits.max_seconds == 240
    assert limits.tool_timeout_s == 10
    assert limits.max_repeats == 2
    assert limits.max_calls_per_tool == {
        "search_corpus": 8,
        "get_architecture": 3,
        "get_service_quota": 4,
    }


def test_config_rejects_unknown_key(tmp_path: Path):
    raw = yaml.safe_load(Path("config/agent.yaml").read_text(encoding="utf-8"))
    raw["temperature"] = 0.2  # D19: no sampling parameters, and no unknown keys at all
    path = tmp_path / "agent.yaml"
    path.write_text(yaml.safe_dump(raw), encoding="utf-8")
    with pytest.raises(ValidationError):
        load_agent_config(path)
