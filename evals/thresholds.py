"""The CI thresholds (spec §8): `config/eval_thresholds.yaml` against a run's metrics.

A key `<metric>_min` fails when the metric is below it, `<metric>_max` when it is above it. A value
equal to the threshold passes: values are compared after rounding to 6 decimals, so a mean such as
15 / 20 is not failed by float noise. A metric that is missing or None fails, because a gate that
cannot be measured has not passed.
"""

from pathlib import Path

import yaml

THRESHOLDS = Path("config/eval_thresholds.yaml")


def load_thresholds(path: Path = THRESHOLDS) -> dict[str, float]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    for key in data:
        if not key.endswith(("_min", "_max")):
            raise ValueError(f"{path}: {key} must end in _min or _max")
    return {k: float(v) for k, v in data.items()}


def check(metrics: dict, thresholds: dict[str, float]) -> list[str]:
    """One message per broken threshold, in the order of `thresholds`."""
    failures = []
    for key, limit in thresholds.items():
        name, kind = key[:-4], key[-3:]
        value = metrics.get(name)
        if value is None:
            failures.append(f"{name} has no value")
        elif kind == "min" and round(value, 6) < limit:
            failures.append(f"{name} {value:.2f} < {limit:.2f}")
        elif kind == "max" and round(value, 6) > limit:
            failures.append(f"{name} {value:.2f} > {limit:.2f}")
    return failures
