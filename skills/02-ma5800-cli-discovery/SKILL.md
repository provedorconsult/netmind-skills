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

- [PENDENTE DE VALIDAÇÃO] `display current-configuration ?` para enumerar somente as opções oferecidas pela CLI observada; não executar filtros nesta etapa
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
- [DISCOVERY] `ont add ${PON_PORT} ${ONT_ID} sn-auth ${ONT_SERIAL} ?`
- [DISCOVERY] `ont add ${PON_PORT} ${ONT_ID} sn-auth ${ONT_SERIAL} omci ?`
- [DISCOVERY] `ont-port ?`
- [DISCOVERY] `ont-port eth ?`
- [DISCOVERY] `port ?`
- [DISCOVERY] `port vlan ?`
- [DISCOVERY] `port vlan eth ?`
- [DISCOVERY] `port vlan eth 1-4 ?`
- [DISCOVERY] `display ont info summary ?`

## Sintaxe

Acrescentar um token por vez; registrar opções e `<cr>`; nunca transformar uma opção exibida em comando confirmado sem execução bem-sucedida.

## Discovery de backup global

1. Confirmar MA5800-X7, MA5800V100R018C00/SPH507, user view e autorização específica para discovery.
2. Executar somente o candidato literal `display current-configuration ?`; não completar uma opção nem remover `?`.
3. Registrar de forma sanitizada as opções, filtros, `<cr>`, paginação, mensagens de erro e retorno ao prompt.
4. Se a ajuda paginar, usar apenas avanço manual já validado no contexto; interromper diante de comportamento ambíguo.
5. Manter toda opção apenas exibida como `[DISCOVERY]`. Não executar filtro nem promover sintaxe a `[CONFIRMADO]` sem nova evidência real.
6. Considerar uma futura coleta completa somente se a própria CLI enumerar todos os domínios exigidos e cada saída tiver início, fim e prompt verificáveis, sem erro, timeout, paginação residual, desconexão ou truncamento.
7. Se a cobertura não for comprovadamente exaustiva, registrar `[PENDENTE DE VALIDAÇÃO]` e não publicar conteúdo parcial como backup.

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

Não remover `?`, não completar pela memória, não misturar release e não usar `save`, escrita, cópia, exportação, reload, reboot ou restore no fluxo automático.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
