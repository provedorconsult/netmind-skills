# Demanda — Command Registry

**Prioridade sugerida:** P2

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Objetivo

Normalizar comandos hoje distribuídos em Skills, matrizes e documentos.

## Campos sugeridos

- id
- manufacturer
- model
- software
- version
- firmware
- mode
- command
- parameters
- purpose
- operational_class
- preconditions
- expected_result
- evidence
- compatibility
- rollback
- related_commands

## O Checker deve analisar

- o que já existe em `COMMAND-MATRIX.md`;
- catálogos Huawei;
- catálogos Cisco;
- duplicidade;
- sintaxe confirmada versus inferida;
- versionamento;
- como evitar explosão de registros.

## Regra

Registry não deve promover comando inferido a confirmado.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
