# DOKPLOY-G02 — Historical forensics

## Confirmed reusable pattern

| Symptom / risk | Evidence | Diagnosis | Prevention / reusable outcome |
|---|---|---|---|
| Cross-project deployment coupling | `crm10-v3` Dokploy project document, source located by GitHub discovery on 2026-08-28 | Sharing runtime, database volumes, or secrets would violate the documented isolation rule. | Give each project distinct runtime resources and health checks; require backup/restore readiness and explicit deploy authorization. |

## Historical classification

- **CURRENT candidate:** the local `evocrm` Dokploy compose overlay. It proves
  that an overlay exists, not that its values apply to any other host.
- **REFERENCE:** CRM3 planning documentation. It supplies isolation and health
  check principles but is not a validated installation runbook.
- **LEGACY/RELATED:** Easypanel material. It is retained as historical context
  and excluded from Dokploy procedures.
- **UNKNOWN:** no searchable incident ticket or postmortem established a
  confirmed historical root cause for Traefik, PostgreSQL, Swarm, backup, or
  rollback failures.

## Rule adopted

Only the isolation and evidence-before-action pattern is promoted into the
new generic Skills. No environment-specific solution is promoted to canonical
configuration without homologation evidence.
