#!/usr/bin/env python3
"""Validate every Skill and its repository metadata."""

import re
import sys
from pathlib import Path

from quick_validate import safe_load_yaml, validate_agent_manifest, validate_skill
from validate_frontmatter import validate_docs
from validate_operational_safety import validate_operational_safety

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"


def fail(message, failures):
    failures.append(message)
    print(f"ERROR: {message}")


def validate_skills(failures):
    skill_files = sorted(SKILLS_ROOT.glob("**/SKILL.md"))
    if not skill_files:
        fail("No SKILL.md files found", failures)
        return []

    for skill_file in skill_files:
        skill_dir = skill_file.parent
        valid, message = validate_skill(skill_dir)
        if not valid:
            fail(f"{skill_dir.relative_to(ROOT)}: {message}", failures)
            continue

        frontmatter = safe_load_yaml(
            re.match(
                r"^---\n(.*?)\n---",
                skill_file.read_text(encoding="utf-8"),
                re.DOTALL,
            ).group(1)
        )
        expected_name = skill_dir.name
        if frontmatter["name"] != expected_name:
            fail(
                f"{skill_file.relative_to(ROOT)}: name must match directory "
                f"('{expected_name}')",
                failures,
            )

        valid_agent, agent_message = validate_agent_manifest(skill_dir)
        if not valid_agent:
            fail(f"{skill_dir.relative_to(ROOT)}: {agent_message}", failures)

    print(f"Validated {len(skill_files)} SKILL.md files")
    return skill_files


def validate_cisco_skill_index(failures):
    """Keep the Cisco package README index aligned with shipped skill folders."""
    package = SKILLS_ROOT / "cisco-asr1001x"
    readme = package / "README.md"
    if not readme.exists():
        fail("skills/cisco-asr1001x/README.md is missing", failures)
        return

    expected = {path.name for path in package.iterdir() if (path / "SKILL.md").exists()}
    indexed = set(
        re.findall(
            r"\|\s*\d+\s*\|\s*\[[^]]+\]\((\d{2}-[a-z][a-z0-9-]*)/SKILL\.md\)",
            readme.read_text(encoding="utf-8"),
        )
    )
    missing = sorted(expected - indexed)
    stale = sorted(indexed - expected)
    if missing:
        fail(f"skills/cisco-asr1001x/README.md: missing skill index entries: {', '.join(missing)}", failures)
    if stale:
        fail(f"skills/cisco-asr1001x/README.md: stale skill index entries: {', '.join(stale)}", failures)
    print(f"Validated {len(indexed)} Cisco skill index entries")


def validate_cisco_skill_references(failures):
    """Detect references to non-existent numbered Cisco skills in package docs."""
    package = SKILLS_ROOT / "cisco-asr1001x"
    available = {path.name for path in package.iterdir() if (path / "SKILL.md").exists()}
    referenced = set()
    for markdown in package.rglob("*.md"):
        code_spans = re.findall(r"`([^`]+)`", markdown.read_text(encoding="utf-8"))
        for code_span in code_spans:
            referenced.update(re.findall(r"\b\d{2}-[a-z][a-z0-9-]*\b", code_span))
    unknown = sorted(referenced - available)
    if unknown:
        fail(f"skills/cisco-asr1001x: references unknown skill(s): {', '.join(unknown)}", failures)
    print(f"Validated {len(referenced)} numbered Cisco skill reference(s)")


def validate_local_links(failures):
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    checked = 0
    for markdown in sorted(ROOT.glob("**/*.md")):
        if ".git" in markdown.parts:
            continue
        for target in link_pattern.findall(markdown.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#")):
                continue
            clean_target = target.split("#", 1)[0]
            linked = (markdown.parent / clean_target).resolve()
            if not linked.exists():
                fail(
                    f"{markdown.relative_to(ROOT)}: broken local link '{target}'",
                    failures,
                )
            checked += 1
    print(f"Validated {checked} local Markdown links")


def scan_for_sensitive_artifacts(failures):
    patterns = {
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
        "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    }
    checked = 0
    for suffix in ("*.md", "*.yaml", "*.yml"):
        for path in sorted(ROOT.glob(f"**/{suffix}")):
            if ".git" in path.parts:
                continue
            content = path.read_text(encoding="utf-8")
            for label, pattern in patterns.items():
                if pattern.search(content):
                    fail(f"{path.relative_to(ROOT)}: possible {label}", failures)
            checked += 1
    print(f"Scanned {checked} documentation/YAML files for obvious secrets")


def validate_documentation_frontmatter(failures):
    for message in validate_docs(ROOT / "docs"):
        fail(message, failures)


def main():
    failures = []
    validate_skills(failures)
    validate_cisco_skill_index(failures)
    validate_cisco_skill_references(failures)
    validate_local_links(failures)
    scan_for_sensitive_artifacts(failures)
    validate_documentation_frontmatter(failures)
    validate_operational_safety(failures)
    if failures:
        print(f"Validation failed with {len(failures)} error(s)")
        return 1
    print("Repository validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
