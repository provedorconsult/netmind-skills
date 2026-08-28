# G13 — Homologação Final

## Goal
Provar em host controlado que o caminho Debian 12 → Dokploy → aplicação → recuperação é reproduzível.

## Fluxo
`Debian 12 → Preflight → Install → Domain/TLS → GitHub → Application → Database → Backup → Restore → Failure Injection → Diagnosis → Recovery`.

## Acceptance Contract
- Instalação reproduzível.
- Deploy validado.
- Backup e restore validados.
- Falhas controladas são diagnosticadas pelas Skills.
- Recuperação possui evidência.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | host limpo | preflight PASS |
| T02 | instalação | Dokploy saudável |
| T03 | aplicação | deploy PASS |
| T04 | backup/restore | PASS |
| T05 | falha controlada | diagnóstico/recovery PASS |

## Promotion Criteria
Todos os Goals necessários validados e documentação/Skills prontas para promoção.
