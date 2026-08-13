---
name: 17-ma5800-rollback
description: Preparar e executar rollback controlado de mudanças MA5800-X7, restaurando objetos na ordem inversa e validando dependências.
---

# Rollback MA5800

## Objetivo

Retornar ao último estado conhecido sem ampliar impacto.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Snapshot textual anterior, comandos reversos validados por `?`, critérios de abort e autorização.

## Comandos confirmados

- [CONFIRMADO] Displays deste pacote para validar estado; nenhum comando genérico de undo/delete é inferido.

## Comandos de descoberta

- [DISCOVERY] Descobrir no contexto exato a sintaxe de `undo`/`delete` antes da janela.

## Sintaxe

Ordem inversa típica: serviço → binding → profiles novos; preservar objetos compartilhados/default.

Para mapping de GEM, o rollback deve apontar exclusivamente para o GEM e mapping-index criados. Descobrir antes, no contexto exato, a forma `undo gem mapping <GEM_ID> <MAPPING_INDEX>` e validar que o índice corresponde à VLAN/flow recém-adicionado; não usar `save` global sem autorização explícita.

## Exemplos

Se service-port novo falhar, removê-lo somente após confirmar índice e sintaxe; depois avaliar ONT/profile.

## Resultado esperado

Estado igual ao baseline, gestão acessível e serviço anterior restaurado.

## Erros conhecidos

Se reversão for rejeitada, parar e reconsultar objeto/referências.

## Diagnóstico

Comparar displays antes/depois; não repetir cegamente.

## Dependências

Backout testado, acesso alternativo e inventário de bindings.

## Riscos

Rollback destrutivo pode ser pior que a mudança se IDs forem compartilhados.

## Rollback

O próprio procedimento é o rollback; manter plano de escalonamento.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não usar comandos não confirmados nem apagar profile default.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
