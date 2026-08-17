# Demanda — Procedure e Evidence Registries

**Prioridade sugerida:** P2

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Objetivo

Estruturar procedimentos e evidências hoje distribuídos em Skills.

## Procedure Registry deve considerar

- prechecks;
- steps;
- abort conditions;
- validation;
- rollback;
- operational class;
- dependencies.

## Evidence Registry deve considerar

- origem;
- contexto;
- classificação;
- versão;
- data;
- sanitização;
- statement suportado;
- relação com equipment/command/error/procedure.

## O Checker deve decidir

Se Procedure e Evidence devem ser separados desde v1 ou introduzidos em fases distintas.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
