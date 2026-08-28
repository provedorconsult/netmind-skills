# G01 — Discovery GitHub

## Goal
Mapear os repositórios `provedorconsult` que usam, documentam ou integram Dokploy e preservar evidência rastreável.

## Escopo
Pesquisar repositórios, arquivos, commits, PRs e documentação por `dokploy`, `docker compose`, `swarm`, `traefik`, `deployment`, `backup`, `rollback`, `incident` e termos equivalentes.

## Entregáveis
- inventário de repositórios;
- inventário de evidências;
- referência de commit/arquivo/PR/issue;
- classificação `DOKPLOY-DIRECT`, `DOKPLOY-COMPOSE`, `DOKPLOY-DOC`, `DOKPLOY-SKILL`, `DOKPLOY-HISTORY`, `DOKPLOY-RELATED`, `NO-EVIDENCE`.

## Acceptance Contract
- AC01: nenhum repositório candidato é descartado sem justificativa.
- AC02: cada evidência possui origem rastreável.
- AC03: segredos e dados sensíveis não são copiados.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | busca global por Dokploy | resultados classificados |
| T02 | busca por Docker/Swarm/Traefik | candidatos correlacionados |
| T03 | revisão dos candidatos | evidências rastreáveis |

## Promotion Criteria
Inventário revisado, lacunas explicitadas e pronto para G02.

## Codex
Somente pesquisa e documentação. Não alterar infraestrutura.
