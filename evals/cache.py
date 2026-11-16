"""The eval cache: paid answers are stored in Git and replayed (ADR-0008).

- The key is sha256 over the model, the effort and the sha256 of the system text, the user message
  and the schema. The system text stands for the prompt version and the user message for the
  question + context, so any change to either is a miss and a new paid call.
- `evals/cache/answers.jsonl` is append only, one `{"key": ..., "value": ...}` per line; on load
  the last line for a key wins.
- `live=False` (CI) never calls Claude: a miss raises StaleCacheError with what to do.
- The cost guard: a run stops before its (max_misses + 1)-th new call (spec §8: 30).
"""

import hashlib
import json
from pathlib import Path

from src.rag.llm import LLMResult

STALE = "cache is stale: run make eval locally and commit evals/cache/"
MAX_MISSES = 30


class StaleCacheError(RuntimeError):
    pass


class CostGuardError(RuntimeError):
    pass


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def cache_key(model: str, effort: str, system: str, user: str, schema: dict) -> str:
    canonical = json.dumps(
        {
            "model": model,
            "effort": effort,
            "system": _sha(system),
            "user": _sha(user),
            "schema": _sha(json.dumps(schema, sort_keys=True)),
        },
        sort_keys=True,
    )
    return _sha(canonical)


class EvalCache:
    """The JSONL cache file of one run; `.misses` counts this run's new calls."""

    def __init__(self, path: Path, *, live: bool, max_misses: int = MAX_MISSES):
        self.path = path
        self.live = live
        self.max_misses = max_misses
        self.misses = 0
        self._data: dict[str, dict] = {}
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                if line:
                    entry = json.loads(line)
                    self._data[entry["key"]] = entry["value"]

    def get(self, key: str) -> dict | None:
        return self._data.get(key)

    def put(self, key: str, value: dict) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"key": key, "value": value}, sort_keys=True) + "\n")
        self._data[key] = value

    def allow_miss(self) -> None:
        """Called before a new paid call: refuses it in CI and above the cost guard."""
        if not self.live:
            raise StaleCacheError(STALE)
        if self.misses >= self.max_misses:
            raise CostGuardError(
                f"cost guard: {self.max_misses} new calls in this run already"
            )
        self.misses += 1


class CachedLLM:
    """ClaudeJSON behind the cache: the same `complete_json` signature and attributes."""

    def __init__(self, llm, cache: EvalCache):
        self.llm = llm
        self.cache = cache
        self.model = llm.model
        self.effort = llm.effort

    def complete_json(self, system: str, user: str, schema: dict) -> LLMResult:
        key = cache_key(self.model, self.effort, system, user, schema)
        if (hit := self.cache.get(key)) is not None:
            return LLMResult.model_validate(hit)
        self.cache.allow_miss()
        result = self.llm.complete_json(system, user, schema)
        self.cache.put(key, result.model_dump())
        return result
