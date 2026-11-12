import copy
import hashlib
import json

import pytest

from apps.evidence_agent.app import run
from controller.config import ROOT
from mini_mos.beliefs.verification import verify_claim

FIXTURE = ROOT / "explorations/belief_formation/B01_correct_source/fixture.json"


def test_correct_source_provenance():
    result = run(FIXTURE)
    source = json.loads(FIXTURE.read_text())["source"]
    assert result["status"] == "fixture_supported"
    assert result["mode"] == "fixture/mock"
    assert result["provenance"]["sha256"] == hashlib.sha256(source["text"].encode()).hexdigest()


@pytest.mark.parametrize("field,value", [
    ("quote", "a fabricated quote"), ("quote", ""), ("quote", None),
    ("source_id", "wrong"), ("answer", "08:00")])
def test_invalid_claim_not_supported(field, value):
    data = json.loads(FIXTURE.read_text())
    claim = copy.deepcopy(data["claim"])
    claim[field] = value
    result = verify_claim(data["source"], claim, data["expected_answer"])
    assert result["status"] == "unverified"
