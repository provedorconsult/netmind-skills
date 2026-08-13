---
name: 11-ma5800-vlan
description: Consultar e validar VLANs de cliente e gestão na PON e uplink da MA5800-X7 R018 preservando a conectividade administrativa.
---

# VLAN MA5800

## Objetivo

Garantir continuidade L2 da VLAN 100 sem tocar a VLAN 10.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Plano: VLAN 10 gestão, VLAN 100 clientes; uplink 0/8/0.

## Comandos confirmados

- [CONFIRMADO] `display port vlan 0/1/0`
- [CONFIRMADO] `display port vlan 0/8/0`
- [CONFIRMADO][DESTRUTIVO] `vlan 10 smart`; `vlan 100 smart`
- [CONFIRMADO][DESTRUTIVO] `vlan desc 10 description "gerencia"`
- [CONFIRMADO][DESTRUTIVO] `port vlan 10 0/8 0`; `port vlan 100 0/8 0`

## Comandos de descoberta

- [DISCOVERY] Usar `?` antes de qualquer variação de associação/remoção.

## Sintaxe

PON 0/1/0 observada com VLAN 100. Uplink 0/8/0 com 1,10,100 e native VLAN 1.

## Exemplos

Validar VLAN 100 em ambos os lados antes de investigar BNG.

## Resultado esperado

VLAN 100 presente na PON e no uplink; gestão intacta.

## Erros conhecidos

Ausência em um lado interrompe o caminho; não há erro literal específico fornecido.

## Diagnóstico

Seguir PON → VLAN → uplink; parar no primeiro ponto ausente.

## Dependências

Service-port 1000 e uplink 0/8/0.

## Riscos

Alterar VLAN 10/native VLAN/rota pode perder gestão.

## Rollback

Registrar memberships e native VLAN; só executar reversão cuja sintaxe foi descoberta.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não alterar VLAN 10, Vlanif10 ou native VLAN 1 sem autorização.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.

