# NetMind Harness Working Memory

## Active Goal

`G01` is running on `feature/g01-foundation-structure`. This work establishes the AI-Native foundation only; it does not migrate technical content or execute G02–G10.

## Invariants

- Execute one catalog goal at a time and preserve catalog order.
- GitHub PR facts are authoritative; local state is a mirror.
- Only an exact Checker PR comment of `approve` can authorize a merge.
- `request-changes` returns control to the Maker; `blocked` stops the goal.
- The G01 audit found no pre-existing `docs/` or root `templates/` directory. The initial scaffold covers only the existing Huawei MA5800-X7 and Cisco ASR1001-X content families.
