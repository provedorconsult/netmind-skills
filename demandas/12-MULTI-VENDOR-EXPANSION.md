# Demanda — Expansão multi-fabricante

**Prioridade sugerida:** P3

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Objetivo

Preparar expansão funcional além de Huawei e Cisco.

## Fabricantes candidatos

- MikroTik
- ZTE
- FiberHome
- Datacom
- VSOL
- Nokia
- Juniper
- Arista
- Ubiquiti

## Regra principal

Não adicionar fabricante/modelo apenas para preencher roadmap.

Cada inclusão deve depender de:

- fonte técnica;
- modelo real;
- versão;
- evidência;
- Skill reutilizável;
- critérios de compatibilidade.

## O Checker deve decidir

Uma política de onboarding de novos fabricantes antes do primeiro novo vendor.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
