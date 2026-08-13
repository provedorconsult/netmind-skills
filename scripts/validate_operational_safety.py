#!/usr/bin/env python3
"""Validate backup filename examples and flag possible specific network data."""

import ipaddress
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKUP_SKILL = ROOT / "skills" / "network-config-backup"

BACKUP_NAME = re.compile(
    r"^[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{2}-\d{2}-\d{4}"
    r"(?:-(?:pre|pos|\d{2}))?\.txt$"
)
PARAMETERIZED_BACKUP_NAME = re.compile(
    r"^\$\{DEVICE_NAME\}-\$\{BACKUP_DATE\}"
    r"(?:-\$\{BACKUP_PHASE\})?\.txt$"
)
TEXT_FILE_TOKEN = re.compile(r"`([^`\s/]+\.txt)`")
IPV4 = re.compile(r"(?<![0-9])(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![0-9])")
LONG_HEX_IDENTIFIER = re.compile(r"(?i)(?<![0-9a-f])[0-9a-f]{12,}(?![0-9a-f])")
URL = re.compile(r"https?://\S+")
NEGATIVE_CONTEXT = ("nunca usar", "inválido", "inválida", "proibido", "rejeitar")
RESERVED_EXAMPLE_NETWORKS = tuple(
    ipaddress.ip_network(network)
    for network in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24")
)


def valid_backup_name(name):
    return bool(BACKUP_NAME.fullmatch(name) or PARAMETERIZED_BACKUP_NAME.fullmatch(name))


def validate_filename_classifier(failures):
    valid = (
        "OLT-LAB-01-12-08-2026.txt",
        "OLT-LAB-01-12-08-2026-pre.txt",
        "OLT-LAB-01-12-08-2026-pos.txt",
        "OLT-LAB-01-12-08-2026-01.txt",
        "${DEVICE_NAME}-${BACKUP_DATE}.txt",
    )
    invalid = ("latest.txt", "backup.txt", "config.txt", "OLT-LAB-01-2026-08-12.txt")
    for name in valid:
        if not valid_backup_name(name):
            failures.append(f"backup filename validator rejected valid fixture: {name}")
    for name in invalid:
        if valid_backup_name(name):
            failures.append(f"backup filename validator accepted invalid fixture: {name}")


def validate_documented_backup_names(failures):
    checked = 0
    for markdown in sorted(BACKUP_SKILL.rglob("*.md")):
        for line_number, line in enumerate(markdown.read_text(encoding="utf-8").splitlines(), 1):
            lowered = line.lower()
            if any(marker in lowered for marker in NEGATIVE_CONTEXT):
                continue
            for name in TEXT_FILE_TOKEN.findall(line):
                checked += 1
                if not valid_backup_name(name):
                    relative = markdown.relative_to(ROOT)
                    failures.append(
                        f"{relative}:{line_number}: invalid primary backup filename '{name}'"
                    )
    print(f"Validated {checked} documented backup filename example(s)")


def iter_documentation():
    for pattern in ("*.md", "*.yaml", "*.yml"):
        for path in sorted(ROOT.rglob(pattern)):
            if ".git" in path.parts or ".github" in path.parts:
                continue
            yield path


def is_placeholder(value):
    return value.startswith(("<", "${")) or value in {"?", "[REDACTED]"}


def scan_possible_specific_data(failures):
    warnings = []
    seen = set()
    for path in iter_documentation():
        relative = path.relative_to(ROOT)
        for line_number, original in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = URL.sub("", original)

            for candidate in IPV4.findall(line):
                try:
                    address = ipaddress.ip_address(candidate)
                except ValueError:
                    continue
                if any(address in network for network in RESERVED_EXAMPLE_NETWORKS):
                    continue
                if address.is_unspecified:
                    continue
                if address.is_private:
                    warnings.append(
                        f"PENDENTE DE REVISÃO {relative}:{line_number}: IPv4 privado"
                    )

            if LONG_HEX_IDENTIFIER.search(line):
                warnings.append(
                    f"PENDENTE DE REVISÃO {relative}:{line_number}: identificador hexadecimal longo"
                )

            for code in re.findall(r"`([^`]+)`", line):
                for expression, label in (
                    (r"\bssh\s+-l\s+(\S+)", "username SSH concreto"),
                    (r"\busername\s+(\S+)", "username concreto"),
                    (r"\bhostname\s+(\S+)", "hostname concreto"),
                ):
                    for value in re.findall(expression, code, flags=re.IGNORECASE):
                        if not is_placeholder(value):
                            warnings.append(
                                f"PENDENTE DE REVISÃO {relative}:{line_number}: {label}"
                            )

                credential = re.search(
                    r"(?i)\b(?:secret|password|community|token|key)\s+(\S+)", code
                )
                if credential and not is_placeholder(credential.group(1)):
                    failures.append(
                        f"{relative}:{line_number}: possible concrete credential in command"
                    )

    for warning in warnings:
        if warning not in seen:
            print(warning)
            seen.add(warning)
    print(f"Flagged {len(seen)} ambiguous specific-data occurrence(s)")


def validate_operational_safety(failures):
    validate_filename_classifier(failures)
    validate_documented_backup_names(failures)
    scan_possible_specific_data(failures)


def main():
    failures = []
    validate_operational_safety(failures)
    for failure in failures:
        print(f"ERROR: {failure}")
    if failures:
        print(f"Operational safety validation failed with {len(failures)} error(s)")
        return 1
    print("Operational safety validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
