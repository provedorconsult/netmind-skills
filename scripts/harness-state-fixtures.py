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
# Cases 7 and 8: legacy backlog remains blocked, and a GitHub-confirmed G13
# merge completes the active sequence without inventing a successor.
first, second = catalog['goals'][:2]
g13 = next(goal for goal in catalog['goals'] if goal['id'] == 'G13')
completed = {goal['id']: goal for goal in catalog['completedGoals']}
g12 = completed['G12']
g13_completed = completed['G13']
assert first['id'] == 'G01' and first['status'] == 'BLOCKED'
assert first['classification'] == 'DONE' and first['mergeStatus'] == 'MERGED'
assert second['id'] == 'G02' and second['status'] == 'BLOCKED'
assert second['predecessor'] == first['id']
assert g12['status'] == 'DONE' and g12['mergeStatus'] == 'MERGED'
assert g12['pullRequest'] == 20
assert g12['mergeCommit'] == 'ed3b157c048c0480a01398c7abdf7821148d830f'
assert catalog['activeGoal'] is None
assert g13['status'] == 'DONE' and g13['mergeStatus'] == 'MERGED'
assert g13['pullRequest'] == 22
assert g13['mergeCommit'] == 'fc88f28038e62d28a0d7381cab5fb20565fa726b'
assert g13['predecessor'] == 'G12'
assert g13_completed['status'] == 'DONE' and g13_completed['mergeStatus'] == 'MERGED'
assert g13_completed['pullRequest'] == g13['pullRequest']
assert g13_completed['mergeCommit'] == g13['mergeCommit']
assert g13_completed['predecessor'] == g13['predecessor']
assert g13_completed['approvedHead'] == '0eecaf65149073a5e4b6dbc919c95b7bf4dd9ffb'
assert current['goal'] is None and current['goalFile'] is None
assert current['status'] == 'COMPLETE' and current['completedGoal'] == 'G13'
assert current['nextGoal'] is None and 'merge' not in current
assert current['checker'] == {'status': 'completed', 'verdict': 'approve', 'comment': 'approve'}
assert {goal['id']: goal for goal in current['completedGoals']}['G13'] == g13_completed
assert chain['nextGoalRule'] == 'Only a GitHub-confirmed MERGED predecessor on main may promote the next catalog goal to READY.'
print("Harness state fixtures passed")
