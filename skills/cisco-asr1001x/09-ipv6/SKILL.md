---
name: 09-ipv6
description: Diagnosticar e planejar endereçamento, ND, RA, rotas, CEF e BGP IPv6 no Cisco ASR1001-X.
---

# IPv6 no ASR1001-X

## Objetivo

Validar IPv6 ponta a ponta, incluindo assinantes quando aplicável.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show ipv6 interface brief`
- [INFERIDO] `show ipv6 interface`
- [INFERIDO] `show ipv6 route`
- [INFERIDO] `show ipv6 neighbors`
- [INFERIDO] `show bgp ipv6 unicast`
- [INFERIDO] `ipv6 address <PREFIX>`
- [INFERIDO] `ipv6 enable`
- [INFERIDO] `ipv6 route <PREFIX> <NEXT_HOP>`
- [INFERIDO] `router bgp <ASN>`
- [INFERIDO] `address-family ipv6`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Verificar link-local/global, ND, RA, MTU, rota/CEF, BGP e prefix delegation se suportada pela release/BNG; nunca assumir PD.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

RA indevido pode impactar toda LAN; IPv6 não é traduzido pelo CGNAT IPv4.

## Rollback

Registrar endereços, RA/ND e políticas; reverter só o objeto alterado.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

