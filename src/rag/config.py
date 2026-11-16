"""HW 2 settings from config/rag.yaml (spec §5, §6).

A pydantic model, so a typo in the file (an unknown or a missing key) fails at load time instead of
silently falling back to a default somewhere in the code.
"""

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict

Effort = Literal["low", "medium", "high"]


class RagConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    embed_model: str
    rerank_model: str
    candidates: int
    rrf_k: int
    k: int
    context_budget: int
    answer_model: str
    answer_effort: Effort
    answer_max_tokens: int
    judge_model: str
    judge_effort: Effort
    prompt_version: str


def load_config(path: Path = Path("config/rag.yaml")) -> RagConfig:
    return RagConfig.model_validate(yaml.safe_load(path.read_text(encoding="utf-8")))
