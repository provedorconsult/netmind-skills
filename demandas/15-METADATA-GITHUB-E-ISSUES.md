# Demanda — Metadata GitHub e estratégia de Issues

**Prioridade sugerida:** P1

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Problema identificado

A descrição do repositório no GitHub ainda está centrada em Huawei MA5800-X7, enquanto o README posiciona o projeto como multi-fabricante AI-Native.

Também deve ser confirmada a estratégia para Issues.

## O Checker deve analisar

- descrição do repositório;
- topics;
- visibilidade;
- Issues habilitadas/desabilitadas;
- relação entre Issues e Goals;
- política de contribuição.

## Resultado esperado

Definir se:

1. Issues serão usadas como intake/backlog; ou
2. Goals Git-native continuarão sendo a única fila oficial.

A descrição e os topics devem refletir a identidade atual.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
