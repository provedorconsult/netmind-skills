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
# Cases 7 and 8: catalog ordering is fixed, while post-merge alone decides
# whether a successor stays blocked or becomes ready.
first, second = catalog['goals'][:2]
assert first['id'] == 'G01' and second['id'] == 'G02'
assert second['predecessor'] == first['id']
assert chain['nextGoalRule'] == 'Only a GitHub-confirmed MERGED predecessor on main may promote the next catalog goal to READY.'


def successor_status(predecessor_merged):
    return 'NEXT GOAL READY' if predecessor_merged else 'NEXT GOAL BLOCKED'


assert successor_status(False) == 'NEXT GOAL BLOCKED'
assert successor_status(True) == 'NEXT GOAL READY'
print("Harness state fixtures passed")
