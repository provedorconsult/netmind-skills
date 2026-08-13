---
name: 04-ma5800-line-profile
description: Consultar e gerenciar ONT line profiles GPON na MA5800-X7 R018, associando DBA, T-CONT e GEM com validação de dependências.
---

# Line Profile MA5800

## Objetivo

Manter o encadeamento line profile → T-CONT → DBA → GEM → GEM mapping VLAN/flow verificável.

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
- [CONFIRMADO][DESTRUTIVO] na MA5800V100R018/SPH507 de referência: `gem mapping 1 1 vlan 100`, seguido de `commit`.

## Comandos de descoberta

- [DISCOVERY] `ont-lineprofile gpon profile-id ?`; [DISCOVERY] `tcont 0 ?`; [DISCOVERY] `gem ?`; [DISCOVERY] `gem mapping ?`; [DISCOVERY] `undo gem mapping ?`.

## Sintaxe

Entrar no contexto do profile antes de `tcont`. Com `mapping-mode VLAN`, a existência do GEM não é suficiente: o profile deve exibir uma associação explícita entre GEM e VLAN/flow. Na R018 observada, a árvore revelou `gem mapping <GEM_ID> <MAPPING_INDEX> vlan <SERVICE_VLAN>`; redescobrir índice, tipo e VLAN no alvo antes de qualquer mudança.

## Exemplos

Profile parametrizado: Qos PQ, Mapping VLAN, T-CONT → DBA, GEM ETH e `gem mapping <GEM_ID> <MAPPING_INDEX> vlan <SERVICE_VLAN>`.

```text
ont-lineprofile gpon profile-id <LINE_PROFILE_ID>
gem mapping <GEM_ID> <MAPPING_INDEX> vlan <SERVICE_VLAN>
commit
```

Rollback parametrizado, a validar por `?` na release antes da janela:

```text
ont-lineprofile gpon profile-id <LINE_PROFILE_ID>
undo gem mapping <GEM_ID> <MAPPING_INDEX>
commit
```

## Resultado esperado

Consulta do profile mostra T-CONT, GEM e, em mapping VLAN, mapping compatível com a VLAN/flow e o GEM referenciado pelo service-port.

## Erros conhecidos

[ERRO] `Failure: The line profile does not exist`; erro de Max DBA pode surgir ao adicionar ONT.

## Diagnóstico

Listar profiles; conferir DBA referenciado, T-CONT, GEM, mapping, `binding times` e o service-port. A assinatura ONT online + service-port UP/zero tráfego + PPPoE sem PADI no BNG exige verificar GEM mapping antes de camadas posteriores.

## Dependências

DBA 201; GEM 1; ONT 0/1/0.

## Riscos

Mudança em profile vinculado pode atingir múltiplas ONTs. Antes de `commit`, confirmar `binding times`, índice de mapping livre/correto, snapshot sanitizado, critério de abort, acesso alternativo e rollback específico. `commit` aplica a alteração no contexto de profile; `save` global é uma ação distinta e nunca deve ser executada sem autorização explícita.

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
