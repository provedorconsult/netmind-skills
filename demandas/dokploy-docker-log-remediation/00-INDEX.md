# Demanda — Dokploy Docker JSON Log Remediation

## Objetivo

Resolver de modo controlado o incidente `LIVE-001`: logs JSON de containers
foram confirmados como causa primária da exaustão do filesystem raiz. A fonte é
a PR #41, HEAD observado `f73ba66`: ~56.880 MiB em 71 logs, maior ~52.014 MiB,
root em 100%, sem deleted-open files; journal/volumes/APT não são a causa
primária.

## Limite

Esta demanda planeja e, em Goals futuros, controla remediação autorizada. Ela
não autoriza `prune`, remoção de volume/imagem/container, `rm -rf`, reinício,
DNS, firewall, upgrade ou rollback genérico.

## Sequência

`DOKPLOY-LOG-G01 → G02 → G03 → G04 → G05 → G06 → G07 → G08 → G09`.
Os IDs são namespaced para não colidir com o Harness existente.

## Gate

`READ → preservar evidência → classificar risco → autorização explícita →
ação controlada → validação`. Diagnóstico não implica limpeza.
