# G04 — Arquitetura Canônica

## Goal
Consolidar uma arquitetura Dokploy Self-Hosted sobre Debian 12 baseada em evidência atual e separar `CURRENT`, `LEGACY` e `CANONICAL`.

## Escopo
Host, Docker Engine, Swarm, Dokploy, PostgreSQL, Traefik, redes, volumes, portas, DNS/TLS, GitHub, aplicações, bancos, backup, observabilidade e segurança.

## Acceptance Contract
- Cada componente possui função e dependência documentadas.
- Nenhum comportamento legacy é tratado como canônico sem validação.
- Persistência e limites operacionais são explícitos.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | comparar audit com arquitetura | divergências listadas |
| T02 | separar legacy/current | classificação inequívoca |
| T03 | validar dependências | fluxo completo |

## Promotion Criteria
Baseline arquitetural aprovado para orientar os Goals de implementação.
