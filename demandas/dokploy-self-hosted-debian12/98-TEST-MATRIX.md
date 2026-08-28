# Test Matrix — Dokploy Self-Hosted

| Área | Cobertura |
|---|---|
| Discovery | repositórios, arquivos, commits, PRs/issues |
| Forensics | sintomas, causas, soluções, versões |
| Audit | host, Docker, Swarm, Dokploy, Traefik, Postgres, storage |
| Install | Debian 12, preflight, pós-check |
| Diagnose | camadas L0–L8 |
| Compose | env, volumes, networks, health |
| Backup | execução, existência, integridade |
| Restore | recuperação e conferência |
| Upgrade | pré-check, validação, rollback |
| Security | secrets, portas, autorização |
| Harness | Goal, PR, CI, Checker, approve |
| Homologation | instalação e falhas controladas |

Cada teste futuro deve registrar `ID`, `precondition`, `action`, `expected result`, `evidence` e `PASS/FAIL`.
