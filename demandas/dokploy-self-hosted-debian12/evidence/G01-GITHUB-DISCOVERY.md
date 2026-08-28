# DOKPLOY-G01 — GitHub discovery evidence

## Method

Read-only GitHub organization inventory and code search were run on
2026-08-28 for `dokploy`, `docker compose`, `docker swarm`, `traefik`,
`minio`, `rollback deployment`, and `incident runbook`. A textual match is
classified as reference evidence, not proof of a running integration.

## Findings

| Repository | Path / immutable evidence | Classification | Current relevance |
|---|---|---|---|
| `provedorconsult/netmind-skills` | PR #38, observed head | CANONICAL demand | Formal contract and safety boundary for this work. |
| `provedorconsult/crm10-v3` | `docs/pre-development/crm3/02-infraestrutura/01-DOKPLOY-CRM3.md`, GitHub code search on 2026-08-28 | REFERENCE | Defines isolated Dokploy project resources, health endpoints, and deploy gates. It does not prove the current host state. |
| `provedorconsult/crm10-v3` | `skills/deploy-verify/SKILL.md`, GitHub code search on 2026-08-28 | REFERENCE | Deploy validation pattern; no generic Dokploy lifecycle Skill was found in this repository. |
| `provedorconsult/evocrm` | `deploy/dokploy/docker-compose.dokploy.yml` observed in the authorized local checkout | CURRENT candidate | Compose overlay exists. Its configuration is not copied because it may contain operational references. |
| `provedorconsult/myollama` | `scripts/setup-debian12.sh`, GitHub code search on 2026-08-28 | RELATED | Debian 12 setup reference; not evidence for Dokploy use. |
| `provedorconsult/agente-pc` | `docs/deploy-easypanel.md`, GitHub code search on 2026-08-28 | LEGACY/RELATED | Another platform; explicitly not a Dokploy procedure. |

## Search coverage and gaps

- `dokploy`: direct matches were concentrated in `crm10-v3`; those paths were
  reviewed as references, not promoted to canonical procedure.
- `traefik`, `docker swarm`, `rollback deployment`, and `incident runbook`:
  no direct searchable code results in the organization at execution time.
- `minio`: results were predominantly planning/reference material in
  `crm10-v3`; no running MinIO service is inferred.
- All other organization repositories were retained in the organization
  inventory. With no matching result in the scoped searches, they are
  `NO-EVIDENCE`, not discarded candidates.

## Safety

No secrets, hostnames, addresses, compose environments, or raw logs were
copied. GitHub discovery is read-only and does not establish deployment
authorization.
