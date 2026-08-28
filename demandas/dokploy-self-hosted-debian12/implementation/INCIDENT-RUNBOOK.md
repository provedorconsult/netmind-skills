# DOKPLOY-G11 — Incident runbook

## Shared operating contract

For every incident: preserve timestamp/symptom/impact; run only the listed
read-only checks; identify the first explanatory layer; classify cause as fact,
hypothesis, or unknown; obtain authorization before corrective action; validate
with the original symptom check; retain rollback/prevention evidence. Never
copy raw logs, environments, domains, or secrets to this repository.

| ID | Symptom / impact | First check and related Skill | Authorized corrective action / rollback / prevention |
|---|---|---|---|
| INC-001 | UI unavailable / control-plane access lost | L0 capacity/listener, then `dokploy-instance-diagnose` | Action only after cause; rollback is the approved known-good state; monitor health. |
| INC-002 | Port conflict / service cannot bind | listener ownership via `dokploy-preflight` | Change port/firewall only with owner approval; revert prior mapping; reserve ports. |
| INC-003 | Traefik 404 / route not found | `dokploy-traefik-diagnose` routing checks | Correct approved route; restore previous route; validate route contract. |
| INC-004 | Traefik 502 / backend unavailable | `dokploy-traefik-diagnose`, then deployment | Correct backend only after evidence; rollback deployment; keep health checks. |
| INC-005 | PostgreSQL failure / data path unavailable | `dokploy-postgres-diagnose` | Approved recovery only; restore only isolated/approved target; test readiness. |
| INC-006 | Swarm failure / tasks unscheduled | `dokploy-swarm-diagnose` | No cluster recreation; approved repair with known-good state; monitor quorum/capacity. |
| INC-007 | Deployment failure / application unavailable | `dokploy-deployment-diagnose` | Approved deploy correction; rollback known-good artifact; retain immutable version evidence. |
| INC-008 | Build failure / artifact absent | `dokploy-deployment-diagnose` | Fix source/build contract outside production; rollback is no deploy; retain build evidence. |
| INC-009 | DNS failure / name does not resolve | `dokploy-domain-diagnose` | Approved DNS correction; restore prior record; validate resolver propagation. |
| INC-010 | TLS failure / client trust error | `dokploy-domain-diagnose` | Approved certificate/route correction; restore prior valid configuration; monitor expiry. |
| INC-011 | Storage failure / persistent I/O affected | `dokploy-storage-diagnose` | Do not prune; approved storage recovery; validate volume/application integrity. |
| INC-012 | Disk full / writes may fail | `dokploy-storage-diagnose`; current `LIVE-001` | HIGH risk, requires authorization; no blind cleanup; validate space and workloads. |
| INC-013 | Backup failure / recovery unproven | `BACKUP-RESTORE.md` inventory | Approved rerun/configuration fix; retain prior artifacts; require restore proof. |
| INC-014 | Restore failure / recovery unavailable | `BACKUP-RESTORE.md` in isolated target | Stop before production overwrite; preserve failed evidence; remediate backup contract. |
| INC-015 | Upgrade failure / regression | `UPGRADE-ROLLBACK.md` | Authorized known-good rollback; validate all health/data gates; compatibility review. |
| INC-016 | Rollback requested / suspected regression | `UPGRADE-ROLLBACK.md` | Identify known-good and data compatibility; authorized rollback; retain evidence. |

For each row, the listed Skill supplies the evidence/diagnosis path. If its
first check does not prove the cause, escalation is `BLOCKED/UNKNOWN`, not an
automatic fix.
