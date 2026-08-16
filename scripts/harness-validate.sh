#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$root"

python3 - <<'PY'
import json
from pathlib import Path

root = Path('.')
required = [
    '.harness/loops/discover.json', '.harness/loops/maker.json',
    '.harness/loops/checker.json', '.harness/loops/merge-gate.json',
    '.harness/loops/post-merge.json', '.harness/chains/goal.chain.json',
    '.harness/policies/merge-policy.json', '.harness/state/current.json',
    '.harness/sprints/current.json', '.harness/templates/goal-template.json'
]
failures = []
data = {}
for relative in required:
    path = root / relative
    if not path.is_file():
        failures.append(f'missing {relative}')
        continue
    try:
        data[relative] = json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        failures.append(f'invalid JSON {relative}: {exc.msg}')

for relative in required + ['.harness/templates/review-template.md', '.harness/templates/evidence-template.md']:
    path = root / relative
    if path.exists() and any(token in path.read_text(encoding='utf-8').lower() for token in (
        'human-in-the-loop', 'human-review-required', 'manual-approval',
        'approval-required-from-human', 'handoff-to-human', 'wait-for-human'
    )):
        failures.append(f'forbidden approval dependency in {relative}')

policy = data.get('.harness/policies/merge-policy.json', {})
required_policy = policy.get('required', {})
if required_policy.get('checkerComment') != 'approve' or required_policy.get('commentComparison') != 'case-sensitive exact entire comment':
    failures.append('merge policy must require an exact literal approve')
if policy.get('sourceOfTruth') != 'GitHub pull request and its comments; local state only mirrors verified GitHub facts.':
    failures.append('merge policy must make GitHub evidence authoritative')

chain = data.get('.harness/chains/goal.chain.json', {})
states = {'PLANNED', 'READY', 'MAKER_RUNNING', 'VALIDATING', 'PR_OPEN', 'CHECKER_REVIEW', 'CHANGES_REQUESTED', 'BLOCKED', 'MERGE_AUTHORIZED', 'MERGING', 'MERGED', 'POST_MERGE', 'COMPLETE'}
transitions = chain.get('stateTransitions', {})
if set(transitions) != states - {'BLOCKED', 'COMPLETE'}:
    failures.append('state machine is missing a required transition')
for source, targets in transitions.items():
    for target in (targets if isinstance(targets, list) else [targets]):
        if target not in states:
            failures.append(f'impossible state transition {source} -> {target}')
if transitions.get('CHECKER_REVIEW') != ['CHANGES_REQUESTED', 'BLOCKED', 'MERGE_AUTHORIZED']:
    failures.append('Checker transitions are not deterministic')
if not any(step.get('id') == 'approval-gate' and step.get('action') == 'verify-real-github-checker-comment' for step in chain.get('steps', [])):
    failures.append('chain lacks real GitHub approval gate')

maker = data.get('.harness/loops/maker.json', {})
checker = data.get('.harness/loops/checker.json', {})
gate = data.get('.harness/loops/merge-gate.json', {})
if maker.get('role') != 'Codex Maker' or 'merge-pull-request' not in maker.get('forbidden', []):
    failures.append('Maker must be separate and unable to merge')
if checker.get('role') != 'automated Checker' or checker.get('validVerdicts') != ['approve', 'request-changes', 'blocked']:
    failures.append('Checker verdict contract is invalid')
if checker.get('transitions') != {'approve': 'MERGE_AUTHORIZED', 'request-changes': 'CHANGES_REQUESTED', 'blocked': 'BLOCKED'}:
    failures.append('Checker transitions are invalid')
if 'makerPromptRequirement' not in checker or 'separate concise execution prompt' not in checker['makerPromptRequirement']:
    failures.append('Checker must require a separate concise Maker execution prompt')
if 'Maker Execution Prompt' not in (root / '.harness/templates/review-template.md').read_text(encoding='utf-8'):
    failures.append('review template must require the Maker execution prompt')
if not (root / 'scripts/harness-checker-prompt.py').is_file():
    failures.append('Checker prompt generator is missing')
if gate.get('command') != 'python3 scripts/harness-merge-gate.py --repo <owner/repo> --pr <number>':
    failures.append('merge gate must query GitHub PR evidence')

catalog = data.get('.harness/sprints/current.json', {})
goals = catalog.get('goals', [])
expected = [f'G{i:02d}' for i in range(1, 11)]
if [goal.get('id') for goal in goals] != expected:
    failures.append('goal catalog must retain G01 through G10 in order')
for index, goal in enumerate(goals):
    if not (root / goal.get('file', '')).is_file():
        failures.append(f"goal source missing for {goal.get('id')}")
    expected_predecessor = None if index == 0 else expected[index - 1]
    if goal.get('predecessor') != expected_predecessor:
        failures.append(f"invalid predecessor for {goal.get('id')}")
if goals and (goals[0].get('status') != 'PLANNED' or any(goal.get('status') != 'BLOCKED' for goal in goals[1:])):
    failures.append('initial catalog must not execute G01-G10')

current = data.get('.harness/state/current.json', {})
if current.get('goal') != 'G01' or current.get('status') != 'PLANNED' or current.get('merge', {}).get('authorized'):
    failures.append('initial current state is inconsistent')

if failures:
    print('\n'.join(f'ERROR: {failure}' for failure in failures))
    raise SystemExit(1)
print('Harness structural validation passed')
PY
