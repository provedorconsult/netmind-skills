#!/usr/bin/env python3
"""Minimal deterministic Markdown lint for repository documentation (v1.0.0)."""

import argparse
from pathlib import Path


VERSION = "1.0.0"


def lint(path):
    failures = []
    fenced = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.rstrip() != line:
            failures.append(f"{path}:{number}: trailing whitespace")
        if line.lstrip().startswith("```"):
            fenced = not fenced
    if fenced:
        failures.append(f"{path}: unclosed fenced code block")
    return failures


def main():
    parser = argparse.ArgumentParser(description="Lint Markdown deterministically.")
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.path)
    failures = [failure for markdown in sorted(root.rglob("*.md")) if ".git" not in markdown.parts for failure in lint(markdown)]
    for failure in failures:
        print(f"ERROR: {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
