# G10 — Golden Host

## Goal
Definir baseline reproduzível de host Debian 12 + Dokploy para provisionamento rápido e seguro.

## Baseline
CPU, RAM, SSD/NVMe, rede, hostname, DNS, firewall, Docker, Swarm, Dokploy, persistência, backup, monitoramento e segurança.

## Acceptance Contract
- Recursos mínimos e recomendados são separados.
- Baseline é reproduzível.
- Pré e pós-check são automatizáveis.
- O host de referência não contém segredos reais.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | provisionar host limpo | baseline aplicado |
| T02 | health check | PASS |
| T03 | deploy de teste | PASS |
| T04 | backup/restore | PASS |

## Promotion Criteria
Baseline validado como referência operacional.
