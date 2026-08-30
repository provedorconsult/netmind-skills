# G03 — Auditoria Dokploy Atual

## Goal
Definir e futuramente executar auditoria exclusivamente read-only do Dokploy atualmente utilizado.

## Escopo
Host, Debian, kernel, CPU/RAM/disco, rede, Docker, Swarm, services, networks, volumes, Dokploy, PostgreSQL, Traefik, domínios, TLS, backups, integrações e segurança.

## Safety Contract
Não reiniciar, atualizar, remover, prune, recriar, alterar DNS/firewall ou modificar configuração.

## Entregáveis
Snapshot sanitizado, comandos executados, timestamps, versão e evidências brutas sem credenciais.

## Acceptance Contract
- AC01: toda coleta é read-only.
- AC02: estado real fica reproduzível por evidência.
- AC03: segredos não são persistidos.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | host | baseline completo |
| T02 | Docker/Swarm | estado documentado |
| T03 | Dokploy/Traefik/Postgres | saúde documentada |
| T04 | storage/backup | persistência documentada |

## Promotion Criteria
Snapshot completo, sanitizado e revisado.
