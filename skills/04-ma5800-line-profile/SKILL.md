---
name: 04-ma5800-line-profile
description: Consultar e gerenciar ONT line profiles GPON na MA5800-X7 R018, associando DBA, T-CONT e GEM com validação de dependências.
---

# Line Profile MA5800

## Objetivo

Manter o encadeamento line profile → T-CONT → DBA → GEM verificável.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

DBA existente e compatível; inventário de ONTs/profile bindings.

## Comandos confirmados

- [CONFIRMADO] `display ont-lineprofile gpon all`
- [CONFIRMADO] `display ont-lineprofile gpon profile-id 0` (também 1, 2, 3)
- [CONFIRMADO][DESTRUTIVO] `ont-lineprofile gpon profile-id 100 profile-name "LINE-OMCI-VLAN-100"`
- [CONFIRMADO][DESTRUTIVO] `tcont 0 dba-profile-id 200`
- [CONFIRMADO][DESTRUTIVO] `tcont 0 dba-profile-id 201`

## Comandos de descoberta

- [DISCOVERY] `ont-lineprofile gpon profile-id ?`; [DISCOVERY] `tcont 0 ?`.

## Sintaxe

Entrar no contexto do profile antes de `tcont`. Descobrir a sintaxe de GEM com `?`; o comando de criação de GEM não foi fornecido como confirmado.

## Exemplos

Profile 100 final: Qos PQ, Mapping VLAN, TR069 Disable; T-CONT 0 DBA 201; GEM 1 ETH, encrypt on, cascade off, queue 0.

## Resultado esperado

Consulta do profile 100 mostra exatamente os objetos planejados.

## Erros conhecidos

[ERRO] `Failure: The line profile does not exist`; erro de Max DBA pode surgir ao adicionar ONT.

## Diagnóstico

Listar profiles; conferir DBA referenciado, T-CONT, GEM, mapping e bindings.

## Dependências

DBA 201; GEM 1; ONT 0/1/0.

## Riscos

Mudança em profile vinculado pode atingir múltiplas ONTs.

## Rollback

Capturar detail anterior; preferir novo profile e rebind controlado.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não apagar default 0 (`line-profile_default_0`), que contém T-CONT 0→DBA2 e T-CONT1→DBA0, sem análise.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.

