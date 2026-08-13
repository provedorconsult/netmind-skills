---
name: 14-nat-cgnat
description: Interpretar e planejar NAT tradicional, PAT e CGNAT broadband no Cisco ASR1001-X considerando restrições da release.
---

# NAT e CGNAT

## Objetivo

Traduzir assinantes com rastreabilidade e capacidade adequada.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show ip nat translations`
- [INFERIDO] `show ip nat statistics`
- [INFERIDO] `show ip nat pool`
- [INFERIDO] `show access-lists`
- [INFERIDO] `ip nat ?`
- [INFERIDO] `ip nat pool <NAME> <START_IP> <END_IP> netmask <MASK>`
- [INFERIDO] `ip nat inside`
- [INFERIDO] `ip nat outside`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Identificar modo NAT, inside/outside, ACL/classificação, pool, overload, capacidade e logging; para investigação correlacionar cliente, IP/porta privada, IP/porta pública e timestamp; validar assimetria/retorno.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Mudar modo CGN com traduções ativas é crítico e release-dependent; logging contém dados pessoais.

## Rollback

Capturar modo, pools, ACLs e bindings; não usar reload; restaurar ordem de classificação, pool e interfaces.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

