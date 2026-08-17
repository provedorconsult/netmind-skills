# Demanda — Compatibility Registry v1

**Prioridade sugerida:** P1

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Objetivo da demanda

Criar uma camada explícita de aplicabilidade entre Equipment Registry e Skills.

## Estados mínimos esperados

- `exact`
- `compatible`
- `unverified`
- `incompatible`

## Problema atual

Hoje a presença de uma Skill ou documento em um caminho pode ser interpretada incorretamente como compatibilidade.

## O Checker deve decidir

- schema;
- IDs;
- relação com Equipment Registry;
- relação com versões/firmware;
- evidência obrigatória;
- regras para `unverified`;
- como representar incompatibilidade;
- precedência entre evidências conflitantes.

## Guardrail

Sem evidência suficiente, o estado padrão deve ser `unverified`.

Nunca inferir compatibilidade apenas por fabricante, família ou semelhança de modelo.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
