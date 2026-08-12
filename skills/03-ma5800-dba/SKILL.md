---
name: 03-ma5800-dba
description: Consultar, criar, validar e diagnosticar DBA profiles na MA5800-X7 R018, incluindo limites OMCI, bind-times e inconsistências de IDs.
---

# DBA Profiles MA5800

## Objetivo

Tratar DBA com evidência do equipamento e compatibilidade OMCI.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Executar `display dba-profile all`; escolher ID após consulta; conhecer capacidade da ONT e referências.

## Comandos confirmados

- [CONFIRMADO] `display dba-profile all`
- [CONFIRMADO] `display dba-profile profile-id 100` (também 101, 102, 200 e 201)
- [CONFIRMADO][DESTRUTIVO] `dba-profile add profile-id 101 profile-name "DBA-OMCI-2G" type5 fix 128 assure 128 max 2000000`
- [CONFIRMADO][DESTRUTIVO] `dba-profile add profile-id 102 profile-name "DBA-OMCI-2G" type5 fix 1000 assure 1000 max 2000000`
- [CONFIRMADO][DESTRUTIVO] `dba-profile add profile-id 103 profile-name "DBA-OMCI-2G" type5 fix 2048 assure 2048 max 2048000`
- [CONFIRMADO][DESTRUTIVO] `dba-profile add profile-id 200 profile-name "TESTE" type5 fix 2048 assure 2048 max 2048000`

## Comandos de descoberta

- [DISCOVERY] `dba-profile add profile-id ?` e progressões registradas na Skill de discovery.

## Sintaxe

Type 5 observado: `fix <kbps> assure <kbps> max <kbps>`. Validar faixa com `?` na release alvo.

## Exemplos

Perfil 200 final observado: DBA-VLAN100-2G-OMCI, Type 5, 2048/2048/2048000, best-effort. Perfil 201: DBA-OMCI-GPON-1G, 2048/2048/1024000, bind-times 1.

## Resultado esperado

Perfil consultável e valores iguais ao plano; profile 101 foi observado com 128/128/2000000, embora abaixo do mínimo tenha sido rejeitado em outro contexto.

## Erros conhecidos

[ERRO] `Failure: OMCI must not use type4 DBA-profile`; [ERRO] `Failure: The bandwidth of OMCI can't be less than 1Mbps`; inconsistência 102: `already existed` seguida de `does not exist`.

## Diagnóstico

Não assumir existência pelo erro. Reconsultar lista, ID, bind-times, T-CONT e limite da ONT.

## Dependências

Line profile, T-CONT OMCI, capacidade da ONT.

## Riscos

Max incompatível impede `ont add`; alterar DBA vinculado afeta assinantes.

## Rollback

Criar novo perfil compatível e reverter associação antes de considerar exclusão; nunca apagar automaticamente.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não usar Type 4 no T-CONT OMCI; não reduzir DBA sem diagnóstico; não reutilizar ID por suposição.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.

