#!/usr/bin/env python3
"""Verify required transitions against the shipped harness definitions."""

import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
chain = json.loads((root / '.harness/chains/goal.chain.json').read_text(encoding='utf-8'))
catalog = json.loads((root / '.harness/sprints/current.json').read_text(encoding='utf-8'))
current = json.loads((root / '.harness/state/current.json').read_text(encoding='utf-8'))

# Case 5: CHECKER_REVIEW -> CHANGES_REQUESTED -> MAKER_RUNNING.
assert chain['stateTransitions']['CHECKER_REVIEW'][0] == 'CHANGES_REQUESTED'
assert chain['stateTransitions']['CHANGES_REQUESTED'] == 'MAKER_RUNNING'
# Case 6: Checker blocked terminates execution.
assert chain['stateTransitions']['CHECKER_REVIEW'][1] == 'BLOCKED'
assert 'BLOCKED' in chain['terminalStates']
# Cases 7 and 8: legacy backlog remains blocked, G13/G14 are complete, and
# G15 is explicitly promoted as the next READY goal with predecessor G14.
first, second = catalog['goals'][:2]
g13 = next(goal for goal in catalog['goals'] if goal['id'] == 'G13')
g14 = next(goal for goal in catalog['goals'] if goal['id'] == 'G14')
g15 = next(goal for goal in catalog['goals'] if goal['id'] == 'G15')
completed = {goal['id']: goal for goal in catalog['completedGoals']}
g12 = completed['G12']
g14_completed = completed['G14']
assert first['id'] == 'G01' and first['status'] == 'BLOCKED'
assert first['classification'] == 'DONE' and first['mergeStatus'] == 'MERGED'
assert second['id'] == 'G02' and second['status'] == 'BLOCKED'
assert second['predecessor'] == first['id']
assert g12['status'] == 'DONE' and g12['mergeStatus'] == 'MERGED'
assert g12['pullRequest'] == 20
assert g12['mergeCommit'] == 'ed3b157c048c0480a01398c7abdf7821148d830f'
assert catalog['activeGoal'] == 'G15'
assert g13['status'] == 'DONE' and g13['mergeStatus'] == 'MERGED'
assert g13['pullRequest'] == 22
assert g13['mergeCommit'] == 'fc88f28038e62d28a0d7381cab5fb20565fa726b'
assert g13['predecessor'] == 'G12'
assert g14['status'] == 'DONE' and g14['mergeStatus'] == 'MERGED'
assert g14['pullRequest'] == 23
assert g14['mergeCommit'] == 'd6cf4f684317810d915a89bd9e03524564e8afa9'
assert g14['predecessor'] == 'G13'
assert g14_completed == g14
assert g15['status'] == 'READY'
assert g15['file'] == '15-readme-institucional-ai-native.md'
assert g15['predecessor'] == 'G14'
assert g15['status'] == 'READY'
assert current['goal'] == 'G15' and current['goalFile'] == g15['file']
assert current['status'] == 'READY' and current['completedGoal'] == 'G14'
assert current['predecessor'] == 'G14' and current['nextGoal'] == 'G15'
assert 'merge' not in current
assert current['checker'] == {'status': 'authorized', 'verdict': 'goal-authorized', 'comment': 'G15 promoted by Harness/Checker'}
assert {goal['id']: goal for goal in current['completedGoals']}['G14'] == g14_completed
assert chain['nextGoalRule'] == 'Only a GitHub-confirmed MERGED predecessor on main may promote the next catalog goal to READY.'
print("Harness state fixtures passed")
