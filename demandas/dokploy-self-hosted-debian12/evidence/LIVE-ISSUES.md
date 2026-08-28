# Live issues — Dokploy audit

## LIVE-001 — Root filesystem exhausted

- **Severity:** HIGH
- **Evidence:** Read-only `df` reported the root filesystem at 100% use, zero
  available MiB, and 10% inode use on 2026-08-28T16:57:51Z.
- **Root cause:** UNKNOWN. A bounded Docker-data aggregate exceeded 20 seconds
  and the journal aggregate was unreadable during a follow-up read-only
  collection. No deletion-oriented inspection was attempted.
- **Risk:** Full root storage can prevent writes, deployments, logging, and
  Docker operations. Blind cleanup risks volume/image loss and outage.
- **Recommended fix:** `REQUIRES AUTHORIZATION`. First take a pre-change
  snapshot and collect bounded, read-only size aggregates. Then select a
  reversible, approved remediation with an application owner.
- **Rollback:** Preserve any moved/deleted artifact according to its recovery
  plan; no generic rollback exists for a blind prune.
- **Validation:** Recheck free capacity, workload health, and the affected
  application after any authorized change.
