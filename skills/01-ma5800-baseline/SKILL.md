---
name: 01-ma5800-baseline
description: Registrar e conferir o baseline real da Huawei MA5800-X7 antes de diagnóstico, provisionamento ou mudança, especialmente na release MA5800V100R018 SPH507.
---

# Baseline MA5800-X7

## Objetivo

Estabelecer identidade, hardware, endereçamento e objetos conhecidos sem alterar a OLT.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Acesso somente leitura; confirmar release e patch; janela apenas se uma etapa posterior alterar configuração.

## Comandos confirmados

- [CONFIRMADO] `display port vlan 0/1/0`
- [CONFIRMADO] `display port vlan 0/8/0`
- [CONFIRMADO] `display current-configuration | include ont-lineprofile`
- [CONFIRMADO] `display current-configuration | include ont-srvprofile`
- [CONFIRMADO] `display service-port all`

## Comandos de descoberta

- [DISCOVERY] Usar `?` no modo atual para qualquer consulta de placa, porta ou versão cuja sintaxe não conste na matriz.

## Sintaxe

Não generalizar F/S/P: PON `0/1/0`, ONT `0`, uplink `0/8/0` são o baseline observado.

## Exemplos

Hardware: 0/1 H907CGHF; 0/8 H901MPLA Active_normal; 0/9 H901MPLA Standby_normal; 0/10-11 H901PILA. VLAN 10 gerência, VLAN 100 clientes.

## Resultado esperado

Release e patch confirmados; `${UPLINK_VLANS}` no uplink; `${PON_VLANS}` na PON; `${MGMT_VLANIF}` com `${MGMT_PREFIX}`; rota via `${MGMT_GATEWAY}`.

## Erros conhecidos

Qualquer divergência de release, estado de board, VLAN ou rota invalida o uso automático do baseline.

## Diagnóstico

Comparar estado lido com o baseline e parar na primeira divergência.

## Dependências

Acesso de gestão pela VLAN 10 e uplink 0/8/0.

## Riscos

Uma conclusão baseada em slot/release errados pode provocar indisponibilidade.

## Rollback

Não aplicável às leituras. Para mudanças posteriores, registrar estado anterior literal.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não alterar VLAN 10, Vlanif10, rota padrão ou profiles default.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
