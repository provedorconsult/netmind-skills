#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
gate=(python3 "$root/scripts/harness-merge-gate.py" --checker-login 'netmind-checker[bot]' --evidence)

expect_denied() { "${gate[@]}" "$root/tests/harness/$1.json" >/tmp/netmind-harness-gate.out 2>&1 && exit 1 || grep -Fqx "MERGE DENIED: $2" /tmp/netmind-harness-gate.out; }
expect_authorized() { "${gate[@]}" "$root/tests/harness/$1.json" | grep -qx 'MERGE AUTHORIZED'; }

expect_denied ci-green-no-approve 'Checker has no timestamped exact verdict'
expect_denied lgtm 'Checker has no timestamped exact verdict'
expect_denied approved 'Checker has no timestamped exact verdict'
expect_authorized approve
expect_denied approve-obsolete-head 'Checker approval predates current PR HEAD'
expect_denied request-changes-after-approve "latest Checker verdict is 'request-changes'"
expect_denied blocked-after-approve "latest Checker verdict is 'blocked'"
expect_denied draft 'PR is draft or draft status is unknown'
expect_denied ci-failed 'CI is not green'
expect_denied ci-absent 'CI is not green'
expect_denied wrong-checker 'Checker has not executed'
expect_denied approve-extra-text 'Checker has no timestamped exact verdict'
expect_denied closed 'PR is not open'
expect_denied merge-conflict 'PR is not mergeable without conflicts'
python3 "$root/scripts/harness-state-fixtures.py"
echo 'Harness gate tests passed'
