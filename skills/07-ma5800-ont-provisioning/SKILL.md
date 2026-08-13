---
name: 07-ma5800-ont-provisioning
description: Provisionar ONT por SN na MA5800-X7 R018 usando line/service profiles validados e diagnóstico prévio de compatibilidade DBA.
---

# Provisionamento de ONT

## Objetivo

Adicionar a EG8145X6-10 de bancada com encadeamento GPON correto e separar autorização da ONT da configuração posterior de WAN.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Autofind e SN confirmados; profiles 100 consultados; DBA compatível; ONT-ID livre; rollback preparado.

## Comandos confirmados

- [CONFIRMADO][DESTRUTIVO] `ont add 0 0 sn-auth 4857544354ABCFB2 omci ont-lineprofile-id 100 ont-srvprofile-id 100 desc "EG8145X6-10-TESTE"`

## Comandos de descoberta

- [DISCOVERY] `ont add ?`; `ont add 0 ?`; `ont add 0 0 sn-auth ?`; `ont add 0 0 sn-auth 4857544354ABCFB2 ?`; `ont add 0 0 sn-auth 4857544354ABCFB2 omci ?`.

## Sintaxe

No contexto GPON 0/1: port 0, ONT-ID 0, sn-auth, OMCI e IDs dos profiles.

## Exemplos

Saída observada: `Number of ONTs that can be added: 1, success: 1`; PortID 0, ONTID 0.

## Resultado esperado

ONT 0 adicionada e depois online em `display ont info summary 0/1/0`. Isso não prova que a WAN PPPoE esteja criada ou autenticada.

## Erros conhecidos

[ERRO] `Failure: The maximum bandwidth of the referenced DBA profile exceeds the limitation`.

## Diagnóstico

Investigar DBA Max, capacidade/ont-type, line profile, T-CONT, GEM e referências. Não alterar Max às cegas.

## Dependências

Autofind; DBA; line profile; service profile; PON. A configuração route/PPPoE pertence à etapa posterior `20-ma5800-ont-wan-pppoe`.

## Riscos

SN/porta/profile errados podem interromper ou sequestrar o serviço de outra ONT.

## Rollback

Planejar remoção da ONT e de service-port somente após consultar dependências; sintaxe de delete deve ser descoberta.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não guardar senha; não usar SN de produção como exemplo executável; não modificar ONT online sem necessidade.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
