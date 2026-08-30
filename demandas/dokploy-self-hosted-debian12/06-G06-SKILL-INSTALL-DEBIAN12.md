# G06 — Skill Install Debian 12

## Goal
Especificar `dokploy-install-debian12` para provisionamento reproduzível de um host Debian 12.

## Fluxo
`PRECHECK → HOST → DOCKER → SWARM → DOKPLOY → HEALTH → DOMAIN/TLS → BACKUP → TEST DEPLOY`.

## Guardrails
Não sobrescrever Swarm existente, não apagar serviços, não executar ação destrutiva implicitamente e exigir autorização explícita para operações de impacto.

## Acceptance Contract
- Instalação possui preflight e pós-validação.
- Falhas possuem ponto de parada e evidência.
- Procedimento é reproduzível em host controlado.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | Debian 12 limpo | instalação completa |
| T02 | porta conflitante | bloqueio |
| T03 | Swarm existente | bloqueio seguro |
| T04 | pós-instalação | health check PASS |

## Promotion Criteria
Procedimento validado em homologação antes de ser considerado canônico.
