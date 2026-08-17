# Demanda — Device Fingerprint v1

**Prioridade sugerida:** P1

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Objetivo

Formalizar fingerprint estruturado e sanitizado para descrever o equipamento alvo antes da seleção de Skills.

## Campos mínimos

- manufacturer
- category
- family
- model
- software_cli
- version
- firmware
- patch
- observed_capabilities
- evidence_reference

## Requisitos conceituais

- não conter credenciais;
- não conter dados de cliente desnecessários;
- permitir `unknown`;
- registrar origem da descoberta;
- distinguir observado de inferido;
- não fazer network scanning;
- permitir coleta parcial.

## O Checker deve decidir

Se o fingerprint será:

- documento/schema;
- formato YAML/JSON;
- artefato temporário;
- input do Skill Router;
- ou combinação desses modelos.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
