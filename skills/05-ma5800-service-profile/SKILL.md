---
name: 05-ma5800-service-profile
description: Consultar e configurar ONT service profiles GPON e VLANs das portas Ethernet na MA5800-X7 R018 com sintaxe comprovada.
---

# Service Profile MA5800

## Objetivo

Aplicar VLAN 100 às ETH 1–4 da ONT pelo service profile e distinguir esse mapeamento do profile de WAN roteada ainda não descoberto.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

VLAN 100 existente; profile ID livre; confirmar capacidade física da ONT.

## Comandos confirmados

- [CONFIRMADO] `display ont-srvprofile gpon all`
- [CONFIRMADO] `display current-configuration | include ont-srvprofile`
- [CONFIRMADO][DESTRUTIVO] `ont-srvprofile gpon profile-id 100 profile-name "SRV-OMCI-VLAN-100"`
- [CONFIRMADO][DESTRUTIVO] `port vlan eth 1 translation 100 user-vlan 100` (repetido com 2, 3 e 4)

## Comandos de descoberta

- [DISCOVERY] `ont-port ?`; `ont-port eth ?`; `port ?`; `port vlan ?`; `port vlan eth ?`; `port vlan eth 1-4 ?`.

## Sintaxe

A forma confirmada é por porta individual. O discovery `port vlan eth 1-4 100 ?` exibiu `<cr>`, `TLS`, `priority`, `prival`, mas não foi confirmado como ação.

## Exemplos

Configurar cada ETH 1–4 com translation 100/user-vlan 100 e consultar o profile.

## Resultado esperado

Profile 100 mostra as quatro portas ETH na VLAN 100. Isso confirma o mapeamento Ethernet, não confirma WAN route, PPPoE, NAT ou DHCP.

## Erros conhecidos

[ERRO] `port vlan eth 1-4 vlanid100` foi rejeitado.

## Diagnóstico

Voltar ao contexto do service profile e descobrir o próximo token com `?`.

## Dependências

VLAN 100, ONT com quatro ETH, ONT binding. Para route/PPPoE, carregar também `20-ma5800-ont-wan-pppoe`.

## Riscos

Mapeamento incorreto pode isolar LAN ou misturar serviços.

## Rollback

Registrar mapeamento anterior e obter via `?` a sintaxe de remoção/reversão antes da janela.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não assumir que faixa 1-4 aceita a mesma sintaxe da configuração por porta nem que este service profile, sozinho, transforma a ONT em roteador.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
