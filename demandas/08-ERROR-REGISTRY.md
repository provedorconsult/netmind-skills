# Demanda — Error Registry

**Prioridade sugerida:** P2

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Objetivo

Normalizar erros e respostas conhecidas para diagnóstico reutilizável.

## Campos sugeridos

- id
- equipment_context
- software/version
- command_context
- literal_error
- meaning
- probable_causes
- diagnostic_commands
- safe_actions
- unsafe_actions
- rollback
- evidence

## O Checker deve analisar

- bancos de erro Huawei;
- Cisco error database;
- troubleshooting Skills;
- mensagens literais;
- deduplicação;
- correlação com Command Registry.

## Regra

Erro observado em uma versão não deve ser generalizado para todas.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
