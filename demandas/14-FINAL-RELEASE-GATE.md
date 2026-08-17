# Demanda — Final Release Gate

**Prioridade sugerida:** P3

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Contexto

O antigo G10 permanece bloqueado e não representa mais toda a arquitetura.

## Objetivo

Criar um release gate final alinhado ao Network Equipment Skill Registry AI-Native.

## Deve validar

- README;
- ARCHITECTURE;
- registries;
- fingerprints;
- Skill Router;
- docs;
- Skills;
- Harness;
- CI;
- security scan;
- anchors;
- links;
- frontmatter;
- indexes;
- deprecation;
- migrations;
- E2E;
- Maker/Checker governance.

## Regra

O release gate deve falhar de forma explícita quando qualquer requisito obrigatório não estiver atendido.

Nunca usar CI verde isoladamente como evidência de maturidade funcional.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
