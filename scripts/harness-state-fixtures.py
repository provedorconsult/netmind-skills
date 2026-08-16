#!/usr/bin/env python3
"""Verify required transitions against the shipped harness definitions."""

import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
chain = json.loads((root / '.harness/chains/goal.chain.json').read_text(encoding='utf-8'))
catalog = json.loads((root / '.harness/sprints/current.json').read_text(encoding='utf-8'))

# Case 5: CHECKER_REVIEW -> CHANGES_REQUESTED -> MAKER_RUNNING.
assert chain['stateTransitions']['CHECKER_REVIEW'][0] == 'CHANGES_REQUESTED'
assert chain['stateTransitions']['CHANGES_REQUESTED'] == 'MAKER_RUNNING'
# Case 6: Checker blocked terminates execution.
assert chain['stateTransitions']['CHECKER_REVIEW'][1] == 'BLOCKED'
assert 'BLOCKED' in chain['terminalStates']
# Cases 7 and 8: legacy backlog remains blocked, while a GitHub-confirmed
# G12 merge is the sole basis for promoting G13.
first, second = catalog['goals'][:2]
g13 = next(goal for goal in catalog['goals'] if goal['id'] == 'G13')
completed = {goal['id']: goal for goal in catalog['completedGoals']}
g12 = completed['G12']
assert first['id'] == 'G01' and first['status'] == 'BLOCKED'
assert second['id'] == 'G02' and second['status'] == 'BLOCKED'
assert second['predecessor'] == first['id']
assert g12['status'] == 'DONE' and g12['mergeStatus'] == 'MERGED'
assert g12['pullRequest'] == 20
assert g12['mergeCommit'] == 'ed3b157c048c0480a01398c7abdf7821148d830f'
assert catalog['activeGoal'] == 'G13'
assert g13['status'] == 'READY' and g13['predecessor'] == 'G12'
assert chain['nextGoalRule'] == 'Only a GitHub-confirmed MERGED predecessor on main may promote the next catalog goal to READY.'
print("Harness state fixtures passed")
