---
name: 15-acl
description: Planejar ACL standard, extended, IPv6 e CoPP no Cisco ASR1001-X com análise explícita de fluxo e acesso.
---

# ACL IPv4 e IPv6

## Objetivo

Filtrar tráfego sem bloquear gestão ou serviços legítimos.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show access-lists`
- [INFERIDO] `show ip access-lists`
- [INFERIDO] `show ipv6 access-list`
- [INFERIDO] `ip access-list ?`
- [INFERIDO] `ipv6 access-list ?`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Explicar source, destination, protocol, ports, direction, interface e implicit deny; contar hits; salvar ACL e aplicação; simular regras antes de anexar.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Ordem/implicit deny/direção errados causam blackout; CoPP pode bloquear plano de controle.

## Rollback

Backup da ACL e bindings; restaurar sequência exata; garantir acesso alternativo.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

