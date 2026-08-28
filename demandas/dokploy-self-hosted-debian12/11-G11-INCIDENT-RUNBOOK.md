# G11 — Incident Runbook

## Goal
Criar runbooks de diagnóstico rápido para falhas recorrentes.

## Incidentes
UI indisponível, portas, Traefik 404/502, PostgreSQL, Swarm, deployment/build, DNS/TLS, storage, disco cheio, backup, restore, upgrade e rollback.

## Contrato por incidente
`Sintoma → impacto → primeiro diagnóstico → comandos read-only → hipóteses → evidência → correção autorizável → validação → rollback → prevenção`.

## Acceptance Contract
- Todo incidente possui caminho inicial determinístico.
- Comandos read-only são separados das ações de mudança.
- Toda ação de impacto possui autorização e validação.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | UI down | diagnóstico reproduzível |
| T02 | 404/502 | camada causadora isolada |
| T03 | disco cheio | dados preservados |
| T04 | falha de upgrade | recuperação definida |

## Promotion Criteria
Runbooks prontos para teste controlado.
