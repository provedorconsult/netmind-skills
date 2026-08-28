# DOKPLOY-G04 — Canonical architecture

## Canonical model

```text
Debian 12 → Docker Engine → Docker Swarm → Dokploy
                                      ├─ PostgreSQL
                                      ├─ ingress/proxy
                                      ├─ applications
                                      └─ persistent storage
```

## Component contract

| Component | Responsibility | Persistence / dependency |
|---|---|---|
| Debian 12 | supported host baseline | capacity, updates, firewall and host identity are managed deliberately |
| Docker | runtime | Docker data must be capacity-monitored; no blind prune |
| Swarm | scheduling | do not initialize/recreate an existing cluster |
| Dokploy | deployment control plane | health is validated separately from SSH reachability |
| PostgreSQL | application data | named persistent storage plus tested restore |
| Ingress/proxy | HTTP(S) routing | DNS/TLS and backend health are separate layers |
| Applications | isolated workloads | project-specific volumes, secrets and health checks |

## State separation

- **CURRENT:** the audited host is Debian 12 with Docker and active Swarm;
  filtered service evidence indicates Dokploy and PostgreSQL matches.
- **LEGACY/REFERENCE:** CRM3 planning and non-Dokploy deployment documents.
- **CANONICAL:** the component contract above, conditional on controlled-host
  homologation; it does not prescribe current-host values, ports, domains,
  networks, or volume names.

## Non-negotiable controls

DNS, TLS, external GitHub integration, observability, backup destination and
retention are explicit deployment inputs. They remain `UNKNOWN` for the
audited host until scoped evidence is safely collected.
