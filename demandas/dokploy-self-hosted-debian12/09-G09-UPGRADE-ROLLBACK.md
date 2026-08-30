# G09 — Upgrade e Rollback

## Goal
Definir ciclo de vida seguro para atualizar Dokploy e recuperar falhas.

## Fluxo
`AUDIT → BACKUP → VERSION CHECK → COMPATIBILITY → UPGRADE → HEALTH → VALIDATION → ROLLBACK`.

## Acceptance Contract
- Versão atual é registrada antes da mudança.
- Backup precede upgrade.
- Critério de abort e rollback é explícito.
- Upgrade não é automático sem autorização.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | versão suportada | caminho normal |
| T02 | falha pós-upgrade | rollback definido |
| T03 | backup pré-upgrade | restaurável |

## Promotion Criteria
Procedimento testado em ambiente controlado.
