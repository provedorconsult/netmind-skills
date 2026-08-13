---
name: 22-boot-config-register
description: Diagnosticar BOOT variable, startup-config, ROMMON e configuration register no Cisco ASR1001-X IOS XE.
---

# Boot e config-register

## Objetivo

Identificar problemas de boot sem usar reload como teste.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show bootvar`
- [INFERIDO] `show version`
- [INFERIDO] `show startup-config`
- [INFERIDO] `show running-config`
- [INFERIDO] `show boot`
- [INFERIDO] `show rom-monitor`
- [INFERIDO] `boot ?`
- [INFERIDO] `config-register 0x2102`
- [INFERIDO] `config-register 0x2142`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Confirmar release e sintaxe; comparar BOOT/CONFIG_FILE/BOOTLDR/register; interpretar 0x2102 como fluxo normal típico e 0x2142 como ignorar startup-config, sempre validar na release.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Boot variable/register errado pode impedir boot ou ignorar configuração; reload é crítico.

## Rollback

Registrar valores anteriores; restaurá-los sem reload; agendar reboot somente com autorização específica.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

