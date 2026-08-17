# Demanda — Migração integral Cisco ASR1001-X

**Prioridade sugerida:** P2

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Problema

Existe corpus Cisco amplo, mas a projeção AI-Native ainda não representa todo o conteúdo.

## Objetivo

Mapear o pacote Cisco para a arquitetura atual e futuros registries.

## O Checker deve auditar

- 32 Skills Cisco indexadas;
- PPPoE/BNG;
- AAA/RADIUS;
- NAT/CGNAT;
- routing;
- IPv6;
- troubleshooting;
- backup;
- persistência;
- rollback;
- production validation.

## Regra

Manter versão/contexto explícitos. Não generalizar IOS XE.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
