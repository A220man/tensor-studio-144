#!/usr/bin/env python3
"""Validate marketplace.json against JSON schema."""

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Error: jsonschema package not installed. Run: pip install jsonschema", file=sys.stderr)
    sys.exit(1)


def validate_marketplace(marketplace_path: Path, schema_path: Path) -> bool:
    """Validate marketplace.json against schema."""
    try:
        with open(schema_path) as f:
            schema = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in schema file: {e}", file=sys.stderr)
        return False
    except OSError as e:
        print(f"Error: Cannot read schema file: {e}", file=sys.stderr)
        return False

    try:
        with open(marketplace_path) as f:
            marketplace = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in marketplace file at line {e.lineno}, column {e.colno}: {e.msg}", file=sys.stderr)
        return False
    except OSError as e:
        print(f"Error: Cannot read marketplace file: {e}", file=sys.stderr)
        return False

    try:
        jsonschema.validate(instance=marketplace, schema=schema)
        print(f"✓ {marketplace_path} is valid")
        return True
    except jsonschema.ValidationError as e:
        print(f"✗ Validation error in {marketplace_path}:", file=sys.stderr)
        print(f"  Path: {' -> '.join(str(p) for p in e.path)}", file=sys.stderr)
        print(f"  Message: {e.message}", file=sys.stderr)
        if e.validator_value is not None:
            print(f"  Expected: {e.validator_value}", file=sys.stderr)
        return False
    except jsonschema.SchemaError as e:
        print(f"Error: Invalid schema: {e}", file=sys.stderr)
        return False


def main():
    marketplace_path = Path("marketplace.json")
    schema_path = Path("schemas/marketplace-schema.json")

    if not marketplace_path.exists():
        print(f"Error: {marketplace_path} not found", file=sys.stderr)
        return 1

    if not schema_path.exists():
        print(f"Error: {schema_path} not found", file=sys.stderr)
        return 1

    if validate_marketplace(marketplace_path, schema_path):
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
