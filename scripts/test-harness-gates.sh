#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
gate=(python3 "$root/scripts/harness-merge-gate.py" --checker-login 'netmind-checker[bot]' --evidence)

expect_denied() { "${gate[@]}" "$root/tests/harness/$1.json" >/tmp/netmind-harness-gate.out 2>&1 && exit 1 || grep -qx 'MERGE DENIED: no exact Checker comment '\''approve'\''' /tmp/netmind-harness-gate.out || grep -q '^MERGE DENIED:' /tmp/netmind-harness-gate.out; }
expect_authorized() { "${gate[@]}" "$root/tests/harness/$1.json" | grep -qx 'MERGE AUTHORIZED'; }

expect_denied ci-green-no-approve
expect_denied lgtm
expect_denied approved
expect_authorized approve
python3 "$root/scripts/harness-state-fixtures.py"
echo 'Harness gate tests passed'
