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
if gate.get('command') != 'python3 scripts/harness-merge-gate.py --repo <owner/repo> --pr <number>':
    failures.append('merge gate must query GitHub PR evidence')

catalog = data.get('.harness/sprints/current.json', {})
goals = catalog.get('goals', [])
legacy_expected = [f'G{i:02d}' for i in range(1, 11)]
expected = legacy_expected + ['G13', 'G14', 'G15']
if [goal.get('id') for goal in goals] != expected:
    failures.append('goal catalog must retain G01-G10 and promote G13, G14 and G15 in order')
predecessors = {**{goal: (None if goal == 'G01' else f'G{i-1:02d}') for i, goal in enumerate(legacy_expected, start=1)},
               'G13': 'G12', 'G14': 'G13', 'G15': 'G14'}
for goal in goals:
    goal_id = goal.get('id')
    goal_file = goal.get('file')
    if goal_file and not (root / goal_file).is_file():
        failures.append(f'goal source missing for {goal_id}')
    if goal.get('predecessor') != predecessors.get(goal_id):
        failures.append(f'invalid predecessor for {goal_id}')
if catalog.get('activeGoal') != 'G15':
    failures.append('activeGoal must be G15')
if any(goal.get('status') != 'BLOCKED' for goal in goals[:10]):
    failures.append('legacy backlog must remain BLOCKED')
classifications = {goal.get('id'): goal.get('classification') for goal in goals}
if any(classifications.get(goal) != 'DONE' for goal in legacy_expected[:7]):
    failures.append('G01-G07 must retain DONE historical classifications')
if classifications.get('G08') != 'SUPERSEDED' or classifications.get('G09') != 'SUPERSEDED' or classifications.get('G10') != 'BLOCKED':
    failures.append('legacy G08-G10 classifications are inconsistent')
if not (root / 'G13-RECONCILIATION.md').is_file():
    failures.append('G13 reconciliation report is missing')
if catalog.get('goals', [])[-2].get('status') != 'DONE' or catalog.get('goals', [])[-1].get('status') != 'READY':
    failures.append('catalog must record G14 as DONE and G15 as READY')
completed = {goal.get('id'): goal for goal in catalog.get('completedGoals', [])}
g12 = completed.get('G12', {})
if g12.get('status') != 'DONE' or g12.get('mergeStatus') != 'MERGED' or g12.get('pullRequest') != 20 or g12.get('mergeCommit') != 'ed3b157c048c0480a01398c7abdf7821148d830f':
    failures.append('catalog must record G12 as DONE/MERGED with PR #20 merge evidence')
g14 = completed.get('G14', {})
if g14.get('status') != 'DONE' or g14.get('mergeStatus') != 'MERGED' or g14.get('pullRequest') != 23 or g14.get('mergeCommit') != 'd6cf4f684317810d915a89bd9e03524564e8afa9' or g14.get('predecessor') != 'G13':
    failures.append('catalog must record G14 as DONE/MERGED with PR #23 merge evidence')

current = data.get('.harness/state/current.json', {})
if current.get('goal') != 'G15' or current.get('goalFile') != '15-readme-institucional-ai-native.md' or current.get('status') != 'READY' or current.get('predecessor') != 'G14' or current.get('completedGoal') != 'G14' or current.get('nextGoal') != 'G15':
    failures.append('current state must promote G15 as READY with predecessor G14')
current_completed = {goal.get('id'): goal for goal in current.get('completedGoals', [])}
if current_completed.get('G12', {}).get('mergeCommit') != 'ed3b157c048c0480a01398c7abdf7821148d830f':
    failures.append('current state must retain G12 merge evidence')
if current_completed.get('G14', {}).get('mergeCommit') != 'd6cf4f684317810d915a89bd9e03524564e8afa9':
    failures.append('current state must retain G14 merge evidence')
if current.get('checker') != {'status': 'authorized', 'verdict': 'goal-authorized', 'comment': 'G15 promoted by Harness/Checker'}:
    failures.append('current state must record G15 promotion authorization')

if failures:
    print('\n'.join(f'ERROR: {failure}' for failure in failures))
    raise SystemExit(1)
print('Harness structural validation passed')
PY
