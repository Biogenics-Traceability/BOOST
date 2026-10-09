#!/usr/bin/env python3
"""Validate every entity example instance against its own JSON Schema.

Each drafts/current/schema/<entity>/ directory holds validation_schema.json
(with the schema under the "schema" key) and one or more *example*.json files.
Every example must be a valid instance of its entity's schema, including
string formats (date, date-time, uri, email). Exits non-zero on any failure.

  python3 .github/scripts/validate-examples.py            # from the repo root
"""
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:  # pragma: no cover
    print("jsonschema is required: pip install jsonschema")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "drafts" / "current" / "schema"


def main() -> int:
    examples = sorted(SCHEMA_DIR.glob("*/*example*.json"))
    if not examples:
        print(f"No example files found under {SCHEMA_DIR}")
        return 1
    failures = 0
    for path in examples:
        schema_path = path.parent / "validation_schema.json"
        if not schema_path.exists():
            print(f"SKIP  {path.relative_to(ROOT)} (no validation_schema.json)")
            continue
        schema = json.loads(schema_path.read_text())["schema"]
        instance = json.loads(path.read_text())
        validator = jsonschema.Draft7Validator(schema, format_checker=jsonschema.FormatChecker())
        errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
        if errors:
            failures += 1
            print(f"FAIL  {path.relative_to(ROOT)}")
            for err in errors:
                where = "/".join(str(p) for p in err.absolute_path) or "<root>"
                print(f"      {where}: {err.message[:160]}")
        else:
            print(f"ok    {path.relative_to(ROOT)}")
    print(f"\n{len(examples) - failures} of {len(examples)} example files validate")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
