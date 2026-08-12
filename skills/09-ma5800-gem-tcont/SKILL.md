---
name: 09-ma5800-gem-tcont
description: Analisar a relação DBA, T-CONT e GEM em line profiles GPON da MA5800-X7 R018 e evitar comandos de GEM não confirmados.
---

# GEM e T-CONT

## Objetivo

Validar o caminho de transporte GPON antes de criar service-port.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Line profile detail e DBA listados.

## Comandos confirmados

- [CONFIRMADO][DESTRUTIVO] `tcont 0 dba-profile-id 200`; [CONFIRMADO][DESTRUTIVO] `tcont 0 dba-profile-id 201`

## Comandos de descoberta

- [DISCOVERY] `tcont 0 ?`; descobrir toda sintaxe GEM com `?` porque nenhuma criação GEM foi fornecida como confirmada.

## Sintaxe

T-CONT 0 do profile 100 usa DBA 201; GEM Index 1 é ETH, encrypt on, cascade off, queue 0.

## Exemplos

Caminho: ONT → T-CONT 0/DBA 201 → GEM 1 → service-port 1000.

## Resultado esperado

O line profile exibe T-CONT e GEM referenciados pelo service-port.

## Erros conhecidos

Type 4 é incompatível com OMCI neste cenário; DBA Max incompatível pode bloquear ONT add.

## Diagnóstico

Conferir DBA, associação T-CONT, GEM index/service type e capacidade da ONT.

## Dependências

DBA 201, line profile 100, service-port 1000.

## Riscos

Trocar DBA/T-CONT afeta upstream; GEM errado derruba fluxo.

## Rollback

Restaurar associação anterior registrada; validar antes e depois.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não inventar comando `gem add`; não confundir T-CONT com GEM.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.

