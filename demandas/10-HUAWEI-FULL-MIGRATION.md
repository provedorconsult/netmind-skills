# Demanda — Migração integral Huawei MA5800-X7

**Prioridade sugerida:** P2

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Problema

A estrutura AI-Native Huawei existe, mas a migração do corpus operacional é parcial.

## Objetivo

Mapear Skills e conteúdo legado Huawei para módulos/registries sem perda de evidência.

## O Checker deve auditar

- quais Skills já possuem equivalente em `docs/`;
- quais estão apenas em `skills/`;
- comandos duplicados;
- erros;
- rollback;
- troubleshooting;
- ONT provisioning;
- PPPoE;
- GEM/T-CONT;
- VLAN;
- uplink;
- profiles;
- backup;
- safe change.

## Regra

Migração não significa reescrever tudo.

Preservar histórico e fonte original quando ela continuar sendo autoridade.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
