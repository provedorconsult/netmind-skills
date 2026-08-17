# Demanda — Integridade de evidências do Equipment Registry

**Prioridade sugerida:** P0

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Problema identificado

O Equipment Registry contém referências para âncoras antigas do README.

O validador atual confirma a existência do arquivo Markdown, porém não confirma que a âncora informada realmente existe.

Isso permite evidência quebrada com CI verde.

## Impacto

Perda de rastreabilidade e possibilidade de um registro continuar marcado como evidenciado sem existir o ponto de prova citado.

## O Checker deve analisar

- `registries/equipment/v1/equipment-registry.yaml`
- `registries/equipment/v1/SCHEMA.md`
- `scripts/validate_equipment_registry.py`
- `README.md`
- testes do Equipment Registry
- validator de links Markdown

## Resultado esperado da análise

Criar Goal para:

- corrigir referências quebradas existentes;
- validar arquivo + âncora;
- impedir anchors vazios/inexistentes;
- preservar referências versionadas;
- adicionar testes positivos e negativos;
- não inventar nova evidência técnica.

## Atenção

A correção não deve alterar identidade técnica apenas para satisfazer o validador.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
