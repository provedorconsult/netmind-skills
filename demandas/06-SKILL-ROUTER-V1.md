# Demanda — Skill Router v1

**Prioridade sugerida:** P1

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Objetivo

Implementar seleção conservadora de Skills com base em fingerprint + registries.

## Fluxo alvo

`Target → Fingerprint → Equipment → Compatibility → Capability → Skill Router → Skill`

## Regras esperadas

- nunca escolher Skill apenas pelo nome do diretório;
- bloquear quando compatibilidade não for suficiente;
- exigir capability adequada;
- preferir `exact`;
- permitir `compatible` somente dentro de regras explícitas;
- retornar motivo da seleção;
- retornar motivo do bloqueio;
- não executar comandos.

## O Checker deve definir

- input;
- output;
- formato de decisão;
- relação com índices;
- fallback;
- comportamento para `unknown`;
- testes de roteamento.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
