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

After reviewing the current HEAD and its green CI, publish exactly one comment on the GitHub PR: `approve`, `request-changes`, or `blocked`. A new HEAD requires another review and a new verdict. `approve` authorizes the merge gate but does not execute the merge; only the Maker may merge after a fresh `MERGE_AUTHORIZED` result. The Checker must never merge the PR.
