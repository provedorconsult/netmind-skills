# NetMind Harness Working Memory

## Active Goal

`G01` is planned only. This G11 implementation does not execute backlog goals.

## Invariants

- Execute one catalog goal at a time and preserve catalog order.
- GitHub PR facts are authoritative; local state is a mirror.
- Only an exact Checker PR comment of `approve` can authorize a merge.
- `request-changes` returns control to the Maker; `blocked` stops the goal.
