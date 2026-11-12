"""Inspect generated Python syntax without importing or running it."""

import argparse
import ast
import json
from pathlib import Path


def inspect_code(code):
    try:
        ast.parse(code)
        error = None
    except SyntaxError as exc:
        error = {"line": exc.lineno, "message": exc.msg}
    return {"syntax_valid": error is None, "syntax_error": error,
            "execution": "blocked_no_sandbox", "unit_tests": "not_run",
            "limitation": "Syntax validity is not a safety or correctness assessment."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(inspect_code(args.source.read_text(encoding="utf-8")), indent=2))


if __name__ == "__main__":
    main()
