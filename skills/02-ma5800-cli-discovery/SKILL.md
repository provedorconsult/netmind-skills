---
name: 02-ma5800-cli-discovery
description: Descobrir sintaxe na CLI Huawei MA5800-X7 com `?` antes de sugerir comandos não confirmados ou trabalhar em outra release/contexto.
---

# Descoberta de CLI MA5800

## Objetivo

Ensinar descoberta incremental de sintaxe sem inventar comandos.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Estar no modo correto e usar uma ONT/perfil de teste quando a árvore chegar a uma ação.

## Comandos confirmados

- [CONFIRMADO] `display ont-lineprofile gpon all detail`
- [CONFIRMADO] `display ont-lineprofile gpon all`
- [CONFIRMADO] `display ont-srvprofile gpon all`
- [CONFIRMADO] `display dba-profile all`
- [CONFIRMADO] `display dba-profile all detail`
- [CONFIRMADO] `display service-port all`

## Comandos de descoberta

- [DISCOVERY] `ont-lineprofile gpon profile-id ?`
- [DISCOVERY] `dba-profile add profile-id ?`
- [DISCOVERY] `dba-profile add profile-id 200 profile-name "TESTE" type5 fix ?`
- [DISCOVERY] `dba-profile add profile-id 101 profile-name "DBA-OMCI-2G" type5 fix 128 ?`
- [DISCOVERY] `dba-profile add profile-id 101 profile-name "DBA-OMCI-2G" type5 fix 128 assure ?`
- [DISCOVERY] `dba-profile add profile-id 101 profile-name "DBA-OMCI-2G" type5 fix 128 assure 128 ?`
- [DISCOVERY] `tcont 0 ?`
- [DISCOVERY] `ont add ?`
- [DISCOVERY] `ont add 0 ?`
- [DISCOVERY] `ont add 0 0 sn-auth ?`
- [DISCOVERY] `ont add 0 0 sn-auth 4857544354ABCFB2 ?`
- [DISCOVERY] `ont add 0 0 sn-auth 4857544354ABCFB2 omci ?`
- [DISCOVERY] `ont-port ?`
- [DISCOVERY] `ont-port eth ?`
- [DISCOVERY] `port ?`
- [DISCOVERY] `port vlan ?`
- [DISCOVERY] `port vlan eth ?`
- [DISCOVERY] `port vlan eth 1-4 ?`
- [DISCOVERY] `display ont info summary ?`

## Sintaxe

Acrescentar um token por vez; registrar opções e `<cr>`; nunca transformar uma opção exibida em comando confirmado sem execução bem-sucedida.

## Exemplos

Se `ont add 0 ?` listar `sn-auth`, continuar com `ont add 0 0 sn-auth ?`.

## Resultado esperado

Árvore de tokens da própria release, sem alteração quando a consulta termina em `?`.

## Erros conhecidos

`^` ou rejeição: registrar literalmente como `[ERRO]` e não corrigir por adivinhação.

## Diagnóstico

Confirmar modo, token anterior, faixa apresentada e release.

## Dependências

Matriz global `MA5800-CLI-COMMANDS.md`.

## Riscos

Algumas CLIs podem executar prefixos completos; não pressionar Enter sem `?` em ações.

## Rollback

Nenhum para consultas puras `?`; sair do contexto sem salvar alteração.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não remover `?`, não completar pela memória e não misturar release.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.

