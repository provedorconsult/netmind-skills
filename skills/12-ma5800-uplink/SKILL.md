---
name: 12-ma5800-uplink
description: Validar o uplink 0/8/0, suas VLANs e a continuidade até o BNG sem alterar gestão ou assumir comandos não observados.
---

# Uplink MA5800

## Objetivo

Confirmar que VLAN 100 sai da OLT e VLAN 10 mantém gestão.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Acesso alternativo/out-of-band para qualquer mudança; coordenação com BNG.

## Comandos confirmados

- [CONFIRMADO] `display port vlan 0/8/0`; [CONFIRMADO][DESTRUTIVO] `port vlan 10 0/8 0`; [CONFIRMADO][DESTRUTIVO] `port vlan 100 0/8 0`

## Comandos de descoberta

- [DISCOVERY] Descobrir comandos de estado físico da H901MPLA com `?`; nenhum foi fornecido como confirmado.

## Sintaxe

Uplink observado: slot 0/8 H901MPLA Active_normal, porta 0, VLANs 1/10/100, native 1.

## Exemplos

Correlacionar VLAN 100 no 0/8/0 com subinterface/bridge correspondente no ASR1001-X.

## Resultado esperado

Placa normal e VLANs presentes; continuidade validada também no BNG.

## Erros conhecidos

Sem erro literal de uplink fornecido; registrar qualquer retorno novo antes de agir.

## Diagnóstico

Board → porta → VLAN → enlace remoto → BNG.

## Dependências

H901MPLA, VLANs, cabeamento e ASR1001-X.

## Riscos

Mudança remota pode perder gestão e clientes.

## Rollback

Exigir plano out-of-band e estado anterior; não improvisar.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não alterar rota padrão via `${MGMT_GATEWAY}` ou `${MGMT_VLANIF}`.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
