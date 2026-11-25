"""Service quotas from the HW 1 golden set (`data/gold/*.json`) for `get_service_quota` (spec §5, D12).

The gold files hold the quota tables of ten services, checked by hand against the AWS General
Reference PDF on 22.10.2026 (`data/gold/README.md`). `default` is returned as the source wrote it (often
per Region): the model reads the row for the architecture's Region, the code does not parse it
(ADR-0002). Three services have no standard quota table in the source (ADR-0001).
"""

import json
from datetime import date
from pathlib import Path

GOLD_DIR = Path(__file__).resolve().parents[2] / "data" / "gold"
GOLD_AS_OF = date(2026, 10, 22)
MAX_ROWS = 10
SOURCE = (
    "AWS General Reference, service endpoints and quotas (HW 1 golden set, data/gold/)"
)

GOLD_SERVICES: tuple[str, ...] = (
    "Amazon Aurora",
    "Amazon Aurora DSQL",
    "Amazon Bedrock AgentCore",
    "Amazon Kinesis Data Streams",
    "Amazon OpenSearch Service",
    "Amazon Simple Queue Service",
    "AWS DataSync",
    "AWS Glue",
    "AWS Glue DataBrew",
    "AWS Lake Formation",
)


def _gold() -> dict[str, dict]:
    by_service = {}
    for path in sorted(GOLD_DIR.glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        by_service[doc["service"]] = doc
    return by_service


def quotas(service: str, quota_name: str | None, max_rows: int = MAX_ROWS) -> dict:
    """`{service, as_of, quotas, more, source, note}`; ValueError for a service outside the ten."""
    if service not in GOLD_SERVICES:
        raise ValueError(
            f"unknown service {service!r}: expected one of {', '.join(GOLD_SERVICES)}"
        )
    doc = _gold()[service]
    rows = [
        {k: q[k] for k in ("name", "default", "adjustable", "description")}
        for q in doc["quotas"]
    ]
    if quota_name:
        needle = quota_name.lower()
        rows = [r for r in rows if needle in r["name"].lower()]
    result = {
        "service": service,
        "as_of": GOLD_AS_OF.isoformat(),
        "quotas": rows[:max_rows],
        "more": max(0, len(rows) - max_rows),
        "source": SOURCE,
    }
    if not doc["quotas"]:
        result["note"] = (
            f"the source has no standard quota table for {service} (ADR-0001): "
            "the quota is not available here"
        )
    elif not rows:
        result["note"] = (
            f"no quota name contains {quota_name!r}: try other words or quota_name null"
        )
    elif result["more"]:
        result["note"] = f"{result['more']} more rows: narrow quota_name to see them"
    return result
