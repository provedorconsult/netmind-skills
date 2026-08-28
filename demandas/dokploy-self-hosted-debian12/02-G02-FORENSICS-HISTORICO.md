# G02 — Forensics Histórico

## Goal
Reconstruir procedimentos, incidentes, diagnósticos, causas, soluções e validações relacionados a Dokploy encontrados em G01.

## Fluxo
`REPO → EVIDÊNCIA → SINTOMA → DIAGNÓSTICO → CAUSA → SOLUÇÃO → VALIDAÇÃO → PREVENÇÃO`.

## Classificação
`INSTALLATION`, `DOCKER`, `SWARM`, `TRAEFIK`, `POSTGRES`, `STORAGE`, `NETWORK`, `DNS`, `TLS`, `DEPLOYMENT`, `BACKUP`, `UPGRADE`, `ROLLBACK`, `SECURITY`.

## Acceptance Contract
- Cada incidente possui fonte rastreável.
- Histórico, hipótese e fato confirmado são separados.
- Solução circunstancial não vira padrão sem validação.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | correlacionar incidentes | causa/solução rastreáveis |
| T02 | comparar versões | legacy/current separados |
| T03 | extrair prevenção | candidatos a Skill/runbook |

## Promotion Criteria
Base histórica consolidada e pronta para auditoria do ambiente atual.
