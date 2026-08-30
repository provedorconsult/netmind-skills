# G07 — Skills de Diagnóstico

## Goal
Especificar Skills de diagnóstico conservador para localizar falhas antes de alterar estado.

## Skills candidatas
`dokploy-audit-readonly`, `dokploy-instance-diagnose`, `dokploy-swarm-diagnose`, `dokploy-traefik-diagnose`, `dokploy-postgres-diagnose`, `dokploy-storage-diagnose`, `dokploy-compose-diagnose`, `dokploy-deployment-diagnose`, `dokploy-domain-diagnose`.

## Camadas
`L0 HOST → L1 DOCKER → L2 SWARM → L3 DOKPLOY → L4 TRAEFIK → L5 APPLICATION → L6 DATABASE → L7 DNS/TLS → L8 DEPENDÊNCIA EXTERNA`.

## Acceptance Contract
- Diagnóstico começa por consultas read-only.
- Hipótese é separada de causa confirmada.
- Toda correção exige autorização proporcional.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | UI indisponível | diagnóstico por camadas |
| T02 | 404/502 | Traefik isolado |
| T03 | Postgres falho | dependência identificada |
| T04 | deployment falho | causa baseada em evidência |

## Promotion Criteria
Skills delimitadas, sem automação destrutiva implícita.
