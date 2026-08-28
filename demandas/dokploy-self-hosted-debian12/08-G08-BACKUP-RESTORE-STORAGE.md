# G08 — Backup, Restore e Storage

## Goal
Definir persistência, backup e recuperação verificável do ambiente Dokploy e aplicações.

## Escopo
Named volumes, bind mounts, banco, volume backup, S3/MinIO, retenção, restore e teste de recuperação.

## Regra
Backup só é `VALIDATED` após restore testado e dados conferidos.

## Acceptance Contract
- Dados persistentes são identificados.
- Estratégia de backup é explícita.
- Restore é testável e possui evidência.
- Limpeza não pode apagar dados sem autorização.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | inventário de volumes | completo |
| T02 | backup | artefato presente |
| T03 | restore | sucesso |
| T04 | validação dos dados | PASS |

## Promotion Criteria
DR documentado e validado em ambiente controlado.
