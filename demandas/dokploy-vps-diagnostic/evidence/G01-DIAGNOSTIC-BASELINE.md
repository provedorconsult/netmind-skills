# DOKPLOY-VPS-G01 — Diagnostic baseline

**Execution status:** `BLOCKED`

## Scope and authorization

The current task authorizes only `READ_ONLY` diagnosis of the confirmed Dokploy
VPS. No cleanup, restart, deployment, prune, delete, upgrade, rollback, or
other production mutation was attempted.

## Source evidence preserved

- Dokploy Self-Hosted / Debian 12 implementation: PR #39, observed HEAD
  `926002e`.
- Forensic-demand definition: PR #40.
- Initial incident: `LIVE-001`, root filesystem capacity exhaustion, with
  cause previously `UNKNOWN`.

## Access preflight — 2026-08-28

| Check | Result |
|---|---|
| Local configuration shape | Five connection variables present; values not recorded. |
| Trusted host-key entry | Present. |
| Transport reachability | `UNREACHABLE_OR_FILTERED`. |
| SSH marker authentication | Not reached because transport failed. |
| VPS mutation | None. |

## Decision

`DOKPLOY-VPS-G01` cannot produce a live baseline while the confirmed target is
unreachable. The single permitted post-failure objective check was completed;
no repeated authentication, address discovery, alternate-target selection, or
network change was attempted.

## Required external resolution

Restore or confirm the authorized management path for the existing target,
then resume from G01. Do not provide credentials in chat. G02–G12 remain
`NOT_EXECUTED`; their evidence must not be inferred from the earlier audit.
