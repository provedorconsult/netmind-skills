# Reconciliation report — Dokploy Self-Hosted / Debian 12

## Context

This implementation branch starts from PR #38's demand head. The demand was
initially `PLANNED`; the current Maker authorization explicitly permits its
implementation and a read-only audit of the authorized Dokploy host.

## Reconciled facts

| Subject | Previous state | Current decision | Evidence |
|---|---|---|---|
| Demand implementation | Explicitly deferred in the original index. | Authorized by the current Maker instruction; retain the old statement as history. | PR #38 head observed during reconciliation; current task authorization. |
| Branch | Local `fix/g19-reconcile-merge-gate` was unrelated. | Dedicated `feature/dokploy-self-hosted-debian12` branch, based on the PR #38 head. | Git branch preflight. |
| Goal identifiers | Harness has its own historic G01–G19 sequence. | Dokploy goals are namespaced as `DOKPLOY-G01` through `DOKPLOY-G13` in implementation evidence. No Harness state is overwritten. | `.harness/state/current.json`; `.harness/sprints/current.json`. |
| Live access | Previously unavailable due to SSH authentication. | SSH as the authorized account and `sudo` elevation were revalidated. | Sanitized access preflight, 2026-08-28. |

## Consequence

This branch is review-ready implementation material, not an authorization to
merge, deploy, restart, prune, change DNS/firewall, upgrade, restore, or alter
the audited host. Each mutable command remains gated by explicit authorization.

## Open governance limitation

The current Harness supports one active catalog goal and its existing G IDs.
It has no registration format for a second namespaced demand sequence. This
implementation therefore documents the mapping rather than creating a parallel
governance mechanism. Checker must select the promotion path before merge.
