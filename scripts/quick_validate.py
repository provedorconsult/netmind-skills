#!/usr/bin/env python3
"""Structural validator mirrored from the Codex Skill Creator."""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # Keep the repository validators runnable without extra packages.
    yaml = None

MAX_SKILL_NAME_LENGTH = 64
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}


def safe_load_yaml(content):
    """Load the small mapping-only YAML subset used by skill metadata.

    PyYAML is used when installed. The fallback deliberately supports only
    nested mappings and scalar values, which is sufficient for frontmatter and
    `agents/openai.yaml` manifests in this repository.
    """
    if yaml is not None:
        return yaml.safe_load(content)

    root = {}
    stack = [(-1, root)]
    for line_number, raw_line in enumerate(content.splitlines(), 1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        match = re.fullmatch(r"\s*([^:#][^:]*):(?:\s*(.*))?", raw_line)
        if not match:
            raise ValueError(f"unsupported YAML syntax at line {line_number}")
        key, raw_value = match.groups()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        if not stack:
            raise ValueError(f"invalid YAML indentation at line {line_number}")
        target = stack[-1][1]
        if raw_value is None or not raw_value.strip():
            value = {}
            target[key.strip()] = value
            stack.append((indent, value))
            continue
        value = raw_value.strip()
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        target[key.strip()] = value
    return root


def validate_skill(skill_path):
    skill_path = Path(skill_path)
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    try:
        frontmatter = safe_load_yaml(match.group(1))
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except (ValueError, getattr(yaml, "YAMLError", ValueError)) as exc:
        return False, f"Invalid YAML in frontmatter: {exc}"

    unexpected = set(frontmatter) - ALLOWED_FRONTMATTER
    if unexpected:
        return False, f"Unexpected frontmatter keys: {', '.join(sorted(unexpected))}"

    if "name" not in frontmatter or "description" not in frontmatter:
        return False, "Frontmatter requires name and description"

    name = frontmatter["name"]
    if not isinstance(name, str):
        return False, "Name must be a string"
    name = name.strip()
    if not re.match(r"^[a-z0-9-]+$", name):
        return False, f"Name '{name}' must use lowercase hyphen-case"
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return False, f"Name '{name}' has invalid hyphen placement"
    if len(name) > MAX_SKILL_NAME_LENGTH:
        return False, f"Name is longer than {MAX_SKILL_NAME_LENGTH} characters"

    description = frontmatter["description"]
    if not isinstance(description, str):
        return False, "Description must be a string"
    description = description.strip()
    if not description:
        return False, "Description cannot be empty"
    if "<" in description or ">" in description:
        return False, "Description cannot contain angle brackets"
    if len(description) > 1024:
        return False, "Description is longer than 1024 characters"

    return True, "Skill is valid"


def validate_agent_manifest(skill_path):
    """Validate the minimal Codex UI metadata required for a skill directory."""
    skill_path = Path(skill_path)
    skill_name = skill_path.name
    agent_file = skill_path / "agents" / "openai.yaml"
    if not agent_file.exists():
        return False, "agents/openai.yaml is missing"

    try:
        agent_data = safe_load_yaml(agent_file.read_text(encoding="utf-8"))
    except (ValueError, getattr(yaml, "YAMLError", ValueError)) as exc:
        return False, f"invalid agents/openai.yaml: {exc}"

    interface = (agent_data or {}).get("interface", {})
    for key in ("display_name", "short_description", "default_prompt"):
        value = interface.get(key)
        if not isinstance(value, str) or not value.strip():
            return False, f"agents/openai.yaml: missing interface.{key}"
    if f"${skill_name}" not in interface["default_prompt"]:
        return False, f"agents/openai.yaml: default_prompt must mention ${skill_name}"
    return True, "Agent manifest is valid"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)
    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
