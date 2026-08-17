# Demanda — Validação E2E AI-Native

**Prioridade sugerida:** P3

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Contexto

O antigo G09 foi superseded porque validava apenas navegação documental.

## Objetivo

Criar validação ponta a ponta da arquitetura funcional.

## Fluxo desejado

`Input sanitizado → Fingerprint → Equipment → Compatibility → Capability → Skill Router → Skill selecionada/bloqueada`

## Cenários mínimos

- Huawei conhecido e compatível;
- Cisco conhecido e compatível;
- equipamento conhecido com versão desconhecida;
- modelo desconhecido;
- capability ausente;
- compatibility `unverified`;
- incompatibilidade explícita;
- evidência insuficiente;
- seleção correta;
- bloqueio correto.

## Métricas possíveis

- número de arquivos consultados;
- decisões tomadas;
- tamanho aproximado de contexto;
- falsos positivos;
- falsos bloqueios;
- determinismo.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
