# NetMind Harness Working Memory

## Reconciled history

- G11: `DONE / MERGED` in PR #19, merge commit
  `5ba9d398faf35022ea216c72f9f4c42420371261`.
- G12: `DONE / MERGED` in PR #20, approved head
  `20634b6335df02f832f16930c4fb5f2713117082`, merge commit
  `ed3b157c048c0480a01398c7abdf7821148d830f`.

## Active Goal

`G13` is `READY`. Its canonical source is
`13-backlog-goals-and-legacy-prs-reconciliation.md`; its predecessor is G12.
G01–G10 remain preserved as blocked legacy backlog until G13 audits them.

## Invariants

- Execute one catalog goal at a time and preserve catalog order.
- GitHub PR facts are authoritative; local state is a mirror.
- Only an exact Checker PR comment of `approve` can authorize a merge.
- `request-changes` returns control to the Maker; `blocked` stops the goal.
