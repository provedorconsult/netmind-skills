#!/usr/bin/env python3
"""Validate local Markdown links without fetching external resources (v1.0.0)."""

import argparse
import re
from pathlib import Path


LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")


def main():
    parser = argparse.ArgumentParser(description="Validate local Markdown links.")
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.path)
    failures = []
    for markdown in sorted(root.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        for target in LINK.findall(markdown.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            location = target.split("#", 1)[0]
            if not location:
                continue
            destination = (markdown.parent / location).resolve()
            if not destination.exists():
                failures.append(f"{markdown}:{target}: broken internal link")
    for failure in failures:
        print(f"ERROR: {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
