---
name: 21-ssh
description: Configurar e diagnosticar SSH, usuários, AAA e linhas VTY no Cisco ASR1001-X sem perder o único acesso remoto.
---

# Acesso SSH

## Objetivo

Preservar acesso administrativo cifrado e auditável.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show ip ssh`
- [INFERIDO] `show users`
- [INFERIDO] `show running-config | section line vty`
- [INFERIDO] `ip ssh ?`
- [INFERIDO] `username <USERNAME> secret <SECRET>`
- [INFERIDO] `line vty ?`
- [INFERIDO] `transport input ssh`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Verificar versão SSH, chaves sem exibi-las, AAA/method list, ACL/VRF e VTY; abrir sessão de teste antes de encerrar a atual.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Mudança de AAA/VTY/ACL pode causar lockout.

## Rollback

Manter sessão atual e acesso alternativo; restaurar VTY/AAA/ACL.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

