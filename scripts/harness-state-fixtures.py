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
# Cases 7 and 8: legacy backlog remains blocked, G13 through G17 are complete,
# and no successor is promoted without a formal decision.
first, second = catalog['goals'][:2]
g13 = next(goal for goal in catalog['goals'] if goal['id'] == 'G13')
g14 = next(goal for goal in catalog['goals'] if goal['id'] == 'G14')
g15 = next(goal for goal in catalog['goals'] if goal['id'] == 'G15')
g16 = next(goal for goal in catalog['goals'] if goal['id'] == 'G16')
g17 = next(goal for goal in catalog['goals'] if goal['id'] == 'G17')
completed = {goal['id']: goal for goal in catalog['completedGoals']}
g12 = completed['G12']
g14_completed = completed['G14']
g15_completed = completed['G15']
g16_completed = completed['G16']
g17_completed = completed['G17']
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
assert g14['status'] == 'DONE' and g14['mergeStatus'] == 'MERGED'
assert g14['pullRequest'] == 23
assert g14['mergeCommit'] == 'd6cf4f684317810d915a89bd9e03524564e8afa9'
assert g14['predecessor'] == 'G13'
assert g14_completed == g14
assert g15['file'] == '15-readme-institucional-ai-native.md'
assert g15['predecessor'] == 'G14'
assert g15['status'] == 'DONE' and g15['mergeStatus'] == 'MERGED'
assert g15['pullRequest'] == 25
assert g15['mergeCommit'] == 'afafd885c5f7e852a4f85356cd9327b9440758d1'
assert g15['approvedHead'] == '23c43d1d7b89ffd4f7294c81b6407e5119458589'
assert g15_completed == {key: value for key, value in g15.items() if key != 'file'}
assert g16['predecessor'] == 'G15'
assert g16['status'] == 'DONE' and g16['mergeStatus'] == 'MERGED'
assert g16['pullRequest'] == 28
assert g16['mergeCommit'] == '6ad640b6cae88a0b2b0b459ae8f81c6e7ce026c6'
assert g16['approvedHead'] == '7b871b31519a6623cd0cecef65ac89bc084f1255'
assert g16_completed == g16
assert g17['predecessor'] == 'G16'
assert g17['status'] == 'DONE' and g17['mergeStatus'] == 'MERGED'
assert g17['pullRequest'] == 31
assert g17['mergeCommit'] == '4117de936136dce7cfdff0a851829c4fc6a3f7c1'
assert g17['approvedHead'] == '1ddc124ed2c7aa05caf0d5de7c3df019bd12a30e'
assert g17_completed == g17
assert current['goal'] is None and current['goalFile'] is None
assert current['status'] == 'COMPLETE' and current['completedGoal'] == 'G17'
assert current['predecessor'] is None and current['nextGoal'] is None
assert 'merge' not in current
assert current['checker'] == {'status': 'completed', 'verdict': 'approve', 'comment': 'approve'}
assert {goal['id']: goal for goal in current['completedGoals']}['G14'] == g14_completed
assert {goal['id']: goal for goal in current['completedGoals']}['G15'] == g15_completed
assert {goal['id']: goal for goal in current['completedGoals']}['G16'] == g16_completed
assert {goal['id']: goal for goal in current['completedGoals']}['G17'] == g17_completed
assert chain['nextGoalRule'] == 'Only a GitHub-confirmed MERGED predecessor on main may promote the next catalog goal to READY.'
print("Harness state fixtures passed")
