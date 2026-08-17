# Demanda — Redução de ruído no secret/specific-data scan

**Prioridade sugerida:** P2

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Problema

A CI sinaliza hashes Git legítimos do Harness como ocorrências ambíguas de identificadores hexadecimais longos.

O build passa, mas o ruído pode esconder alertas reais.

## Objetivo

Reduzir falso positivo sem enfraquecer detecção de secrets/dados específicos.

## O Checker deve analisar

- `validate_operational_safety.py`;
- campos Git conhecidos;
- arquivos de state;
- working-memory;
- PR/merge SHA;
- allowlist contextual.

## Regra

Não criar allowlist genérica para qualquer hexadecimal longo.
A exceção deve ser contextual e limitada a campos de rastreabilidade Git.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
