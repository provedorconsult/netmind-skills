#!/usr/bin/env python3
"""Validate every Skill and its repository metadata."""

import re
import sys
from pathlib import Path

import yaml

from quick_validate import validate_skill
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

        frontmatter = yaml.safe_load(
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

        agent_file = skill_dir / "agents" / "openai.yaml"
        if not agent_file.exists():
            fail(f"{agent_file.relative_to(ROOT)} is missing", failures)
            continue
        try:
            agent_data = yaml.safe_load(agent_file.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            fail(f"{agent_file.relative_to(ROOT)}: invalid YAML: {exc}", failures)
            continue

        interface = (agent_data or {}).get("interface", {})
        for key in ("display_name", "short_description", "default_prompt"):
            if not isinstance(interface.get(key), str) or not interface[key].strip():
                fail(f"{agent_file.relative_to(ROOT)}: missing interface.{key}", failures)
        if f"${expected_name}" not in interface.get("default_prompt", ""):
            fail(
                f"{agent_file.relative_to(ROOT)}: default_prompt must mention "
                f"${expected_name}",
                failures,
            )

    print(f"Validated {len(skill_files)} SKILL.md files")
    return skill_files


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


def main():
    failures = []
    validate_skills(failures)
    validate_local_links(failures)
    scan_for_sensitive_artifacts(failures)
    validate_operational_safety(failures)
    if failures:
        print(f"Validation failed with {len(failures)} error(s)")
        return 1
    print("Repository validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
