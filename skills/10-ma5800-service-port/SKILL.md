---
name: 10-ma5800-service-port
description: Criar e validar service-port GPON na MA5800-X7 R018, ligando ONT/GEM à VLAN de serviço com tag translation.
---

# Service-Port MA5800

## Objetivo

Entregar VLAN 100 do GEM 1 ao domínio L2 da OLT.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

ONT online; GEM 1 existente; em mapping VLAN, GEM mapping compatível com a VLAN/flow; VLAN 100 na PON e uplink; índice 1000 livre.

## Comandos confirmados

- [CONFIRMADO][DESTRUTIVO] `service-port 1000 vlan 100 gpon 0/1/0 ont 0 gemport 1 multi-service user-vlan 100 tag-transform translate`
- [CONFIRMADO] `display service-port 1000`
- [CONFIRMADO] `display service-port all`

## Comandos de descoberta

- [DISCOVERY] Usar `service-port ?` antes de adaptar a outro release/fluxo.

## Sintaxe

Índice, VLAN, F/S/P, ONT, GEM, modo multi-service, user-vlan e translate.

## Exemplos

Resultado: index 1000, VLAN 100, gpon 0/1/0, ONT 0, GEM 1, admin enable, state up.

## Resultado esperado

Service-port `up`, parâmetros iguais ao plano e contadores compatíveis com o tráfego de teste. Estado `up` sem bytes/pacotes não prova forwarding.

## Erros conhecidos

[ERRO] `Failure: No service virtual port can be operated`.

## Diagnóstico

Listar service-ports; conferir índice, ONT, GEM, VLAN, estado da PON e contadores. Com ONT online, service-port `up`/zero tráfego e BNG sem PADI/PADR, voltar ao GEM mapping do line profile antes de alterar VLAN, WAN ou AAA.

## Dependências

ONT → GEM → service-port → VLAN → uplink.

## Riscos

Índice ou VLAN errados podem cruzar clientes/tenants.

## Rollback

Capturar display; descobrir sintaxe de remoção e obter confirmação explícita antes de excluir.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não criar antes de GEM/ONT/VLAN; não apagar automaticamente.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
