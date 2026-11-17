"""The eval runner's prompt override (evals/run.py): a prompt version is measured before the config
switches to it (plan Task 19.4)."""

from evals.run import parse_args
from src.rag.config import load_config


def test_prompt_override_changes_only_the_prompt_version():
    command, cfg = parse_args(["answers", "--prompt", "v2"])

    assert command == "answers"
    assert cfg.prompt_version == "v2"
    assert cfg.k == 5  # everything else comes from config/rag.yaml


def test_no_override_keeps_the_config():
    _, cfg = parse_args(["score"])

    assert cfg == load_config()
