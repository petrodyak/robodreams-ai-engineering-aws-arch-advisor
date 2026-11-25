"""HW 3 agent settings from config/agent.yaml (spec §6, §10, §11, D19).

A pydantic model with `extra="forbid"` and no defaults, as `src/rag/config.py`: a typo or a missing
key fails at load time instead of silently falling back to a value somewhere in the code. A sampling
parameter such as `temperature` is therefore refused too (D19).
"""

from datetime import date
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict

Effort = Literal["low", "medium", "high"]
Autonomy = Literal["read_only", "confirm", "auto"]


class Limits(BaseModel):
    """Per-request limits; each one that trips becomes the request's stop reason (spec §6)."""

    model_config = ConfigDict(extra="forbid")

    max_steps: int
    max_tokens: int
    max_usd: float
    max_seconds: float
    tool_timeout_s: float
    max_repeats: int
    max_calls_per_tool: dict[str, int]


class AgentConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    model: str
    effort: Effort
    max_tokens_per_call: int
    today: date
    autonomy: Autonomy
    prompt_version: str
    tools_version: str
    k: int
    relevance_threshold: float | None
    quota_max_rows: int
    critic_retries: int
    history_budget_tokens: int
    db_path: Path
    traces_dir: Path
    limits: Limits


def load_agent_config(path: Path = Path("config/agent.yaml")) -> AgentConfig:
    return AgentConfig.model_validate(yaml.safe_load(path.read_text(encoding="utf-8")))
