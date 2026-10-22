"""The Golden Set files (data/gold/, contract item 10) and the helper that narrows their check.

The gold files are the reference for every accuracy metric, so they must load with the same
schema and checks as a model answer, and exactly the gold=1 rows of the manifest must have
one. The hostname parser of scripts/check_gold.py is pinned on small layout-mode samples.
"""

import pytest

from scripts.check_gold import printed_hostnames, target_chapter
from scripts.make_gold_drafts import GOLD_DIR, gold_documents, gold_path
from src.extract.schema import ServiceDocument, stored_context

GOLD = gold_documents()


def test_exactly_the_gold_rows_of_the_manifest_have_a_file():
    assert len(GOLD) == 10
    files = {p.name for p in GOLD_DIR.glob("*.json")}
    assert files == {gold_path(f).name for f in GOLD}


@pytest.mark.parametrize("file", sorted(GOLD))
def test_gold_file_is_a_valid_service_document_of_its_service(file):
    doc = GOLD[file]
    text = gold_path(file).read_text()
    # the schema, the format checks (ADR-0003) and the service check (contract item 2)
    gold = ServiceDocument.model_validate_json(
        text, context=stored_context(doc.service)
    )
    assert gold.endpoints, "every gold document has an endpoints table"
    # derived by code, so not stored: a hand-corrected hostname cannot leave it stale
    assert "endpoint_type" not in text


# ---------------------------------------------------------------- the check helper

TABLE = """\
 Region Name            Region                 Endpoint                                       Protocol

 US East (N.            us-east-1              bedrock-agentcore-control.us-                  HTTPS
 Virginia)                                     east-1.amazonaws.com

 Asia Pacific            ap-southeast-1         bedrock-agentcore-control. ap-                 HTTPS
 (Singapore)                                    southeast-1.amazonaws.com
"""


def test_a_hostname_wrapped_over_lines_is_rejoined():
    assert printed_hostnames(TABLE) == [
        "bedrock-agentcore-control.us-east-1.amazonaws.com",
        "bedrock-agentcore-control.ap-southeast-1.amazonaws.com",
    ]


def test_a_templated_hostname_is_read_as_printed():
    table = """\
 Region Name            Region                 Endpoint                                      Protocol

 US East (Ohio)         us-east-2             gatewayId      .gateway.bedrock-a             HTTPS
                                              gentcore.us-east-2.amazonaws.com
"""
    assert printed_hostnames(table) == [
        "gatewayId.gateway.bedrock-agentcore.us-east-2.amazonaws.com"
    ]


def test_page_furniture_and_prose_do_not_become_hostnames():
    text = (
        TABLE
        + "Bedrock AgentCore                                         Version 1.0 724\n"
        + "The following table provides a list of Region-specific endpoints that the\n"
        + " US East (Ohio)   us-east-2   not-in-a-table.us-east-2.amazonaws.com   HTTPS\n"
    )
    assert len(printed_hostnames(text)) == 2


def test_target_chapter_leaves_out_the_neighbouring_chapters():
    text = (
        "AWS Network Security Manager endpoints and quotas\nnsm.us-east-1.amazonaws.com\n"
        "Amazon OpenSearch Service endpoints and quotas\nes.us-east-1.amazonaws.com\n"
        "Amazon OpenSearch Serverless endpoints and quotas\naoss.us-east-1.amazonaws.com\n"
    )
    chapter = target_chapter(text, "Amazon OpenSearch Service")
    assert "es.us-east-1" in chapter
    assert "nsm." not in chapter and "aoss." not in chapter
