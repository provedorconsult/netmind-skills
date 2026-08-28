# G05 — Skill Preflight

## Goal
Especificar `dokploy-preflight` para bloquear instalação quando o host não atende aos pré-requisitos.

## Verificações
Debian 12, CPU, RAM, disco, IP, hostname, DNS, portas, Docker, Swarm, firewall, serviços existentes e conflitos de rede.

## Resultado
`READY` ou `BLOCKED`, com evidência e motivo.

## Acceptance Contract
- Nenhuma instalação prossegue diante de bloqueio crítico.
- Checks são determinísticos e read-only.
- Saída permite auditoria.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | host elegível | READY |
| T02 | porta ocupada | BLOCKED |
| T03 | Swarm existente | BLOCKED/estratégia explícita |
| T04 | recurso insuficiente | BLOCKED |

## Promotion Criteria
Contrato da Skill pronto para implementação sem ambiguidade.
