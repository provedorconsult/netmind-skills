# Checker Review

- Goal:
- PR:
- Branch / commit:
- Diff and scope checked:
- Implementation checked:
- Tests and CI checked:
- Security checked:
- Evidence checked:
- Goal conformity checked:

## Verdict

Publish exactly one comment on the GitHub PR: `approve`, `request-changes`, or `blocked`.

`approve` authorizes the merge gate but does not execute the merge. After `MERGE_AUTHORIZED`, the Maker re-checks the real PR state and executes the merge. The Checker must never merge the PR.
