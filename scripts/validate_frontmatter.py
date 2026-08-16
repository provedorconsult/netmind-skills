#!/usr/bin/env python3
"""Validate required YAML frontmatter for Markdown documents under docs/."""

import argparse
from pathlib import Path

try:
    import yaml
except ImportError:  # Report the required dependency instead of parsing a subset.
    yaml = None


REQUIRED_FIELDS = {
    "fabricante": str,
    "modelo": list,
    "categoria": str,
    "topicos": list,
    "descricao": str,
    "versao_firmware_testada": str,
    "ultima_atualizacao": str,
}

OPTIONAL_FIELDS = {"status": str}


def error(path, message):
    return f"{path}: {message}"


def frontmatter(path):
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    if not lines or lines[0] != "---":
        return None, "missing YAML frontmatter"
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None, "YAML frontmatter is not closed"
    return "\n".join(lines[1:end]), None


def validate_metadata(path, metadata):
    failures = []
    if not isinstance(metadata, dict):
        return [error(path, "frontmatter must be a YAML mapping")]

    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in metadata:
            failures.append(error(path, f"missing required field '{field}'"))
            continue
        value = metadata[field]
        if not isinstance(value, expected_type):
            failures.append(
                error(path, f"field '{field}' must be {expected_type.__name__}")
            )
            continue
        if isinstance(value, str) and not value.strip():
            failures.append(error(path, f"field '{field}' cannot be empty"))
        if isinstance(value, list):
            if not value:
                failures.append(error(path, f"field '{field}' cannot be empty"))
            elif any(not isinstance(item, str) or not item.strip() for item in value):
                failures.append(
                    error(path, f"field '{field}' must contain non-empty strings")
                )
    for field, expected_type in OPTIONAL_FIELDS.items():
        if field in metadata and not isinstance(metadata[field], expected_type):
            failures.append(error(path, f"field '{field}' must be {expected_type.__name__}"))
        elif field in metadata and not metadata[field].strip():
            failures.append(error(path, f"field '{field}' cannot be empty"))
    return failures


def validate_file(path):
    if yaml is None:
        return [error(path, "PyYAML is required; install PyYAML to validate frontmatter")]
    raw, parsing_error = frontmatter(path)
    if parsing_error:
        return [error(path, parsing_error)]
    try:
        metadata = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        return [error(path, f"invalid YAML frontmatter: {exc.problem or 'parse error'}")]
    return validate_metadata(path, metadata)


def validate_docs(docs_root):
    docs_root = Path(docs_root)
    if not docs_root.exists():
        return [error(docs_root, "docs directory does not exist")]
    failures = []
    for path in sorted(docs_root.rglob("*.md")):
        failures.extend(validate_file(path))
    return failures


def main():
    parser = argparse.ArgumentParser(
        description="Validate YAML frontmatter in Markdown files under docs/."
    )
    parser.add_argument("path", nargs="?", default="docs", help="docs root to validate")
    args = parser.parse_args()
    failures = validate_docs(args.path)
    for failure in failures:
        print(f"ERROR: {failure}")
    if failures:
        print(f"Frontmatter validation failed with {len(failures)} error(s)")
        return 1
    print(f"Frontmatter validation passed for {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
