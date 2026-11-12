"""Read a local JSON fixture and verify a mock claim, without network access."""

import argparse
import json
from pathlib import Path

from mini_mos.beliefs.verification import verify_claim


def run(path):
    fixture = json.loads(Path(path).read_text(encoding="utf-8"))
    return {"mode": "fixture/mock", "case": "B01",
            **verify_claim(fixture["source"], fixture["claim"], fixture["expected_answer"])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.fixture)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "fixture_supported" else 1


if __name__ == "__main__":
    raise SystemExit(main())
