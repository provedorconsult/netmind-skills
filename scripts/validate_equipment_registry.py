#!/usr/bin/env python3
"""Validate the versioned Equipment Registry without inferring identity."""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "registries/equipment/v1/equipment-registry.yaml"
ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?::[a-z0-9]+(?:-[a-z0-9]+)*)+$")
CLASSIFICATIONS = {"CONFIRMADO", "DISCOVERY", "INFERIDO", "VERSÃO DIFERENTE"}
IDENTITY_FIELDS = ("manufacturer", "family", "model", "software_cli", "version", "firmware_patch")


def fail(errors, message):
    errors.append(message)


def validate_identity(errors, record_number, field, value):
    prefix = f"record {record_number} {field}"
    if not isinstance(value, dict) or set(value) != {"id", "value"}:
        fail(errors, f"{prefix}: must contain exactly id and value")
        return
    identifier, literal = value["id"], value["value"]
    if (identifier is None) != (literal is None):
        fail(errors, f"{prefix}: id and value must both be known or both be null")
    if identifier is not None and (not isinstance(identifier, str) or not ID.fullmatch(identifier)):
        fail(errors, f"{prefix}: invalid canonical id")
    if literal is not None and (not isinstance(literal, str) or not literal.strip()):
        fail(errors, f"{prefix}: value must be a non-empty string or null")


def validate_hierarchy(errors, number, record):
    manufacturer = record["manufacturer"]["id"]
    family = record["family"]["id"]
    model = record["model"]["id"]
    if manufacturer is None or family is None or model is None:
        return
    manufacturer_segment = manufacturer.removeprefix("manufacturer:")
    family_segment = family.rsplit(":", 1)[-1]
    model_segment = model.rsplit(":", 1)[-1]
    expected = {
        "manufacturer": "manufacturer:",
        "family": f"family:{manufacturer_segment}:",
        "model": f"model:{manufacturer_segment}:{family_segment}:",
        "software_cli": f"software:{manufacturer_segment}:",
        "version": f"version:{manufacturer_segment}:",
        "firmware_patch": f"firmware:{manufacturer_segment}:",
    }
    for field, prefix in expected.items():
        identifier = record[field]["id"]
        if identifier is not None and not identifier.startswith(prefix):
            fail(errors, f"record {number} {field}: id does not match its identity hierarchy")
    if record["id"] != f"equipment:{manufacturer_segment}:{family_segment}:{model_segment}":
        fail(errors, f"record {number}: id does not match manufacturer, family and model")


def validate(path):
    if yaml is None:
        return ["PyYAML is required to validate the Equipment Registry"]
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return [f"cannot parse {path}: {exc}"]
    errors = []
    if not isinstance(data, dict) or set(data) != {"format", "format_version", "records"}:
        return ["root: must contain exactly format, format_version and records"]
    if data["format"] != "netmind-equipment-registry" or data["format_version"] != "1.0":
        fail(errors, "root: unsupported format or format_version")
    records = data["records"]
    if not isinstance(records, list) or not records:
        return errors + ["root: records must be a non-empty list"]
    seen = set()
    for number, record in enumerate(records, 1):
        if not isinstance(record, dict) or set(record) != {"id", *IDENTITY_FIELDS, "evidence"}:
            fail(errors, f"record {number}: has missing or unknown fields")
            continue
        record_id = record["id"]
        if not isinstance(record_id, str) or not ID.fullmatch(record_id):
            fail(errors, f"record {number}: invalid canonical id")
        elif record_id in seen:
            fail(errors, f"record {number}: duplicate id {record_id}")
        else:
            seen.add(record_id)
        for field in IDENTITY_FIELDS:
            validate_identity(errors, number, field, record[field])
        if all(isinstance(record[field], dict) and set(record[field]) == {"id", "value"} for field in IDENTITY_FIELDS):
            validate_hierarchy(errors, number, record)
        evidence = record["evidence"]
        if not isinstance(evidence, list) or not evidence:
            fail(errors, f"record {number}: evidence must be a non-empty list")
            continue
        references = set()
        for item in evidence:
            if not isinstance(item, dict) or set(item) != {"classification", "reference", "statement"}:
                fail(errors, f"record {number}: invalid evidence item")
                continue
            classification = item["classification"]
            reference = item["reference"]
            statement = item["statement"]
            if classification not in CLASSIFICATIONS:
                fail(errors, f"record {number}: invalid evidence classification")
            if not isinstance(reference, str) or "#" not in reference:
                fail(errors, f"record {number}: evidence reference must include a Markdown anchor")
            else:
                relative, _ = reference.split("#", 1)
                if not relative or not (ROOT / relative).is_file():
                    fail(errors, f"record {number}: evidence reference does not exist: {reference}")
            if not isinstance(statement, str) or not statement.strip():
                fail(errors, f"record {number}: evidence statement must be non-empty")
            key = (classification, reference)
            if key in references:
                fail(errors, f"record {number}: duplicate evidence reference")
            references.add(key)
    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate Equipment Registry v1")
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args()
    errors = validate(args.path)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print(f"Equipment Registry validation passed: {args.path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
