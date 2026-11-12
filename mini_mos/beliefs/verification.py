"""B01 checks exact quotation and fixture answer; cannot establish world truth."""

import hashlib


def verify_claim(source: dict, claim: dict, expected_answer: str) -> dict:
    quote = claim.get("quote")
    linked = claim.get("source_id") == source["source_id"]
    quoted = isinstance(quote, str) and bool(quote.strip()) and quote in source["text"]
    correct = claim.get("answer") == expected_answer
    supported = linked and quoted and correct
    return {"status": "fixture_supported" if supported else "unverified",
            "checks": {"source_link": linked, "exact_quote": quoted, "fixture_answer": correct},
            "provenance": {"source_id": source["source_id"],
                           "sha256": hashlib.sha256(source["text"].encode()).hexdigest(),
                           "quote": quote},
            "limitation": "Exact quote and fixture label do not prove entailment or source truth."}
