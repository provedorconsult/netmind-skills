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
for verdict in approve request-changes blocked; do
  prompt=(python3 "$root/scripts/harness-checker-prompt.py" --goal G01 --pr 1 --head abc123 --verdict "$verdict")
  if [[ "$verdict" != approve ]]; then
    prompt+=(--details 'Corrigir o bloqueio e repetir a validação.')
  fi
  output=$("${prompt[@]}")
  grep -q '^MAKER EXECUTION PROMPT$' <<<"$output"
  grep -q '^Goal: G01$' <<<"$output"
  grep -q '^PR: #1$' <<<"$output"
  grep -q '^HEAD: abc123$' <<<"$output"
  grep -q "^Verdict: $verdict$" <<<"$output"
  grep -q '^Action: ' <<<"$output"
done
echo 'Harness gate tests passed'
