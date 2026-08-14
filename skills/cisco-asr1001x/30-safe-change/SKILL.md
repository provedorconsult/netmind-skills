---
name: 30-safe-change
description: Planejar e controlar mudanças no Cisco ASR1001-X com baseline, gates de autorização, validação, rollback e persistência separada.
---

# Mudança segura

## Objetivo

Impedir alterações improvisadas em produção e separar claramente aplicação, homologação e persistência.

## Pré-requisitos

Usar primeiro `network-device-access`. Identificar ASR1001-X, release IOS XE, privilégio, escopo e Source of Truth. Capturar baseline sanitizado e acesso alternativo antes de qualquer HIGH-IMPACT.

## Gate 1 — Diagnóstico

READ-ONLY. Confirmar causa raiz com configuração, estado operacional e counters. Não propor alteração enquanto a primeira camada falha não estiver identificada.

## Gate 2 — Change Plan

Antes de configurar, documentar:

- equipamento/release;
- causa tratada;
- comandos exatos;
- objetos existentes preservados;
- dependências;
- risco/impacto;
- prechecks e abort conditions;
- validação pós-mudança;
- rollback específico;
- itens ainda parametrizados que impedem execução.

Valores de rede devem vir do Source of Truth ou de confirmação explícita do responsável/upstream; não inferir IP, prefixo, ASN, VLAN ou pool.

## Gate 3 — Aplicação em running-config

Somente após autorização explícita. Alterar a menor unidade possível, validar imediatamente e parar diante de saída inesperada. Não executar comandos adicionais “para aproveitar a janela”.

## Gate 4 — Homologação

Provar que a mudança resolveu a causa e preservou serviços existentes. Usar counters antes/depois, estado de sessão e teste end-to-end quando disponível.

## Gate 5 — Persistência

`write memory`, `copy running-config startup-config` ou equivalente é `[DESTRUTIVO]` e exige autorização específica. Não assumir que autorização para running-config inclui NVRAM.

Após persistir:

1. confirmar retorno `[OK]` ou equivalente;
2. validar startup-config;
3. comparar somente as linhas aprovadas;
4. registrar evidência no Source of Truth.

## Critérios de abort

Abortar se identidade/release divergir, baseline mudar inesperadamente, dependência não estiver confirmada, objeto alvo já possuir consumidor não documentado, rollback ficar inválido ou a CLI rejeitar a sintaxe aprovada.

## Rollback

Escrever antes da mudança, usando comandos específicos e ordem inversa das dependências. Nunca usar reload, clear global ou restauração ampla como rollback normal quando a mudança puder ser removida isoladamente.

## Regras de segurança

Fluxo obrigatório:

`SHOW → ANALISAR → VALIDAR → PROPOR → AUTORIZAR → ALTERAR → VALIDAR → AUTORIZAR PERSISTÊNCIA → PERSISTIR → DOCUMENTAR`.

Sanitizar secrets e dados de assinantes. Configuração bruta não deve ser versionada sem sanitização.

## O que NÃO fazer

Não salvar antes da homologação, não transformar discovery em mudança, não inferir parâmetros de produção, não remover objetos compartilhados sem checar consumidores e não misturar correções de causas diferentes no mesmo gate.

## Dependências

Usar `31-production-checklist` para aceite e a skill técnica específica da mudança.

## Fonte

- Cisco ASR1001-X / IOS XE; CLI real prevalece.
- Processo operacional refinado a partir de mudança CGNAT validada em IOS XE 17.09.03a, sem dados específicos de cliente.
