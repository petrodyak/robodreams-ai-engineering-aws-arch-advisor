"""Stage 1 schema: Service Document and Run Record (docs/stage1-data-contract.md).

ServiceDocument (+ EndpointRow, QuotaRow) is one class for three uses (contract item 1):
the model's answer, a Golden Set file (data/gold/<name>.json) and the input to metrics.
Its validation JSON Schema, `ServiceDocument.model_json_schema()`, is what both providers
receive. Format checks live in validators, not in the schema (ADR-0003): the schema stays
identical for Claude and Ollama, and a failed check becomes the text of the one repair call.

RunRecord is one line of results/runs/<run_id>.jsonl (contract item 12); the model never
sees it. The gold and record formats are read by RAG (stage 2) and the agent (stage 3):
change them only together with `schema_version`.

Validation needs a context, so that a caller cannot skip a check by forgetting it:
- a model answer:  `ServiceDocument.model_validate_json(raw, context=answer_context(name))`
- a stored file:   `....model_validate(data, context=stored_context(name or None))`
`None` as the name skips the service check on purpose (e.g. a file loaded only for metrics).
A RunRecord needs the same context, even when its `output` is an already validated
instance: Pydantic re-runs ServiceDocument's after-validator on it.
"""

import re
from enum import StrEnum
from typing import Annotated, Any, Literal, Self

from pydantic import (
    AfterValidator,
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    ValidationInfo,
    computed_field,
    field_validator,
    model_validator,
)

# Contract item 9 / ADR-0003. Matched with fullmatch, so no anchors are needed.
REGION_CODE_RE = re.compile(r"[a-z]{2}(-gov)?-[a-z]+-\d+")
# DNS labels (letters, digits, inner hyphens), at least two of them; no scheme, no spaces.
HOSTNAME_RE = re.compile(
    r"[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?(\.[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?)+"
)
# Domains of the Working Set plus the China variant; a new one is a known limit (README).
AWS_DOMAINS = ("amazonaws.com", "amazonaws.com.cn", "api.aws", "on.aws")
# Dual-stack (IPv4 + IPv6) endpoints live on these domains or carry a "dualstack" label.
DUAL_STACK_DOMAINS = ("api.aws", "on.aws")


def collapse_whitespace(s: str) -> str:
    """The only normalisation of extracted text (contract item 9)."""
    return " ".join(s.split())


# Every extracted string field uses this type, so line wraps and column padding from the
# PDF text never reach a comparison with the Golden Set.
NormStr = Annotated[str, AfterValidator(collapse_whitespace)]


def answer_context(service: str) -> dict[str, Any]:
    """Context for validating a model answer for the Target Service `service`."""
    return {"service": service, "stored": False}


def stored_context(service: str | None) -> dict[str, Any]:
    """Context for loading a gold or results file, which carries the computed endpoint_type."""
    return {"service": service, "stored": True}


def _on_domain(host: str, domains: tuple[str, ...]) -> bool:
    # A dot boundary, so "notamazonaws.com" is not taken for a subdomain of amazonaws.com.
    return host.lower().endswith(tuple("." + d for d in domains))


class Protocol(StrEnum):
    """The Protocol column exactly as printed."""

    HTTPS = "HTTPS"
    HTTP = "HTTP"
    HTTP_AND_HTTPS = "HTTP and HTTPS"


class EndpointType(StrEnum):
    """Derived from the hostname by code; not extracted and not scored (contract item 6)."""

    FIPS = "fips"
    DUAL_STACK = "dual_stack"
    FIPS_DUAL_STACK = "fips_dual_stack"
    IPV4 = "ipv4"
    GLOBAL = "global"


class QuotaTableFormat(StrEnum):
    STANDARD = "standard"  # Name | Default | Adjustable | Description (ADR-0001)
    NON_STANDARD = "non_standard"  # a quotas table in any other layout: not extracted
    NONE = "none"  # no quotas table for the Target Service


class Group(StrEnum):
    """The `group` column of data/raw/manifest.csv."""

    SHORT = "short"
    MEDIUM = "medium"
    EDGE = "edge"


class Status(StrEnum):
    OK = "ok"  # valid on the first answer
    REPAIRED = "repaired"  # invalid first, valid after the one repair call (item 16)
    FAILED = "failed"  # still invalid after the repair call, or no answer at all


# ---------------------------------------------------------------- Service Document


class EndpointRow(BaseModel):
    """One row of the endpoints table: one hostname, exactly the printed columns."""

    model_config = ConfigDict(extra="forbid")

    region_name: NormStr = Field(
        description='Region Name column as printed, e.g. "US East (Ohio)"'
    )
    region_code: NormStr = Field(
        description='Region column: an AWS Region code such as "us-east-2", '
        "rejoined if a line wrap split it"
    )
    endpoint: NormStr = Field(
        description='Endpoint column: one hostname without the scheme, e.g. "dsql.us-east-2.api.aws"'
    )
    protocol: Protocol = Field(description="Protocol column as printed")

    @model_validator(mode="before")
    @classmethod
    def _drop_stored_endpoint_type(cls, data: Any, info: ValidationInfo) -> Any:
        # Gold and results files store the computed endpoint_type. Drop it only when loading
        # such a file: in a model answer the key is an invented field, and extra="forbid"
        # must reject it like any other.
        stored = (info.context or {}).get("stored", False)
        if stored and isinstance(data, dict) and "endpoint_type" in data:
            data = {k: v for k, v in data.items() if k != "endpoint_type"}
        return data

    @field_validator("region_code")
    @classmethod
    def _check_region_code(cls, v: str) -> str:
        if not REGION_CODE_RE.fullmatch(v):
            raise ValueError(f"not an AWS Region code like us-east-2: {v!r}")
        return v

    @field_validator("endpoint")
    @classmethod
    def _check_endpoint(cls, v: str) -> str:
        if not HOSTNAME_RE.fullmatch(v):
            raise ValueError(f"not a single hostname (broken by a line wrap?): {v!r}")
        if not _on_domain(v, AWS_DOMAINS):
            raise ValueError(f"not a hostname on an AWS domain {AWS_DOMAINS}: {v!r}")
        return v

    @computed_field
    @property
    def endpoint_type(self) -> EndpointType:
        host = self.endpoint.lower()
        if self.region_code not in host:
            return EndpointType.GLOBAL
        fips = "fips" in host
        dual_stack = "dualstack" in host.split(".") or _on_domain(
            host, DUAL_STACK_DOMAINS
        )
        if fips and dual_stack:
            return EndpointType.FIPS_DUAL_STACK
        if fips:
            return EndpointType.FIPS
        if dual_stack:
            return EndpointType.DUAL_STACK
        return EndpointType.IPV4


class QuotaRow(BaseModel):
    """One row of a Standard Quota Table (ADR-0001), values as printed (ADR-0002)."""

    model_config = ConfigDict(extra="forbid")

    name: NormStr = Field(description="Name column as printed")
    default: NormStr = Field(
        description="Default column as printed, not converted to a number. "
        'Keep "Each supported Region: 10,000" verbatim. A cell with a value per Region '
        'becomes "us-east-1: 20,000; us-east-2: 6,000": Region codes, separator "; ", '
        "in table order"
    )
    # strict: a JSON true/false only. Lax mode would turn "Yes" or 1 into True and hide
    # that a model ignored the schema type from the validity metric.
    adjustable: bool = Field(
        strict=True, description="Adjustable column: Yes is true, No is false"
    )
    description: NormStr = Field(
        description="Description column as printed, footnote markers included"
    )


class ServiceDocument(BaseModel):
    """Endpoints and quotas of the one Target Service of a Working Set document.

    Validation without a context fails (see the module docstring): the service check
    (contract item 2) is the Neighbour Tail detector and must not be lost silently.
    """

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["1"] = Field(description='Always "1"')
    service: NormStr = Field(
        description="The Target Service name given in the prompt, unchanged"
    )
    quota_table_format: QuotaTableFormat = Field(
        description="standard: the quotas table has exactly the columns Name, Default, "
        "Adjustable, Description; non_standard: a quotas table in any other layout; "
        "none: no quotas table for the target service"
    )
    endpoints: list[EndpointRow] = Field(
        description="Every row of the target service's endpoints table, one per hostname"
    )
    quotas: list[QuotaRow] = Field(
        description="Rows of the target service's quotas table; "
        "empty unless quota_table_format is standard"
    )

    @model_validator(mode="after")
    def _check_consistency(self, info: ValidationInfo) -> Self:
        if self.quotas and self.quota_table_format != QuotaTableFormat.STANDARD:
            raise ValueError(
                "quotas must be empty when quota_table_format is "
                f"{self.quota_table_format.value!r}: only Standard Quota Table rows "
                "are extracted"
            )
        if info.context is None or "service" not in info.context:
            raise ValueError(
                "validate with context=answer_context(<service>) or "
                "stored_context(<service or None>): the service check needs the name"
            )
        expected = info.context["service"]
        if expected is not None and self.service != collapse_whitespace(expected):
            raise ValueError(
                f"service is {self.service!r}, expected the target service "
                f"{expected!r}: rows from a neighbouring service?"
            )
        return self


# ---------------------------------------------------------------- Run Record


class Sampling(BaseModel):
    """The Sampling Configuration of the run, copied from config/sampling.yaml so that
    every record is self-contained even if the config changes later."""

    model_config = ConfigDict(extra="forbid")

    name: str  # the <sampling_name> part of the run id: t0, t05
    temperature: float
    top_p: float | None  # left unset in both configurations (contract item 14)


class Usage(BaseModel):
    """Tokens summed over every call for the document, the repair call included."""

    model_config = ConfigDict(extra="forbid")

    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)


def _round_ms(v: Any) -> Any:
    # Timers give float milliseconds (perf_counter() * 1000); store whole milliseconds.
    return round(v) if isinstance(v, float) else v


# status -> (has output, has error). For "repaired", error keeps the first failure,
# which is the material for the error analysis in REPORT.md.
_STATUS_RULES = {
    Status.OK: (True, False),
    Status.REPAIRED: (True, True),
    Status.FAILED: (False, True),
}


class RunRecord(BaseModel):
    """One line of results/runs/<run_id>.jsonl (contract item 12)."""

    model_config = ConfigDict(extra="forbid")

    file: str  # the `file` column of data/raw/manifest.csv
    group: Group
    model: str  # the full model id, e.g. claude-haiku-4-5, qwen2.5:7b
    prompt_version: str  # v1, v2
    sampling: Sampling
    attempts: int = Field(ge=1)  # API calls: transport retries and the repair included
    # wall clock for the whole document (item 19)
    latency_ms: Annotated[int, BeforeValidator(_round_ms)] = Field(ge=0)
    usage: Usage
    status: Status
    output: ServiceDocument | None
    error: str | None

    @model_validator(mode="after")
    def _status_matches_output_and_error(self) -> Self:
        want_output, want_error = _STATUS_RULES[self.status]
        if (self.output is not None, self.error is not None) != (
            want_output,
            want_error,
        ):
            raise ValueError(
                f"status {self.status.value!r} needs output "
                f"{'set' if want_output else 'null'} and error "
                f"{'set' if want_error else 'null'}"
            )
        return self
