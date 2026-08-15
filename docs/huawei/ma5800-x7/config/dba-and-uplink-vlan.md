---
fabricante: huawei
modelo: [ma5800-x7]
categoria: config
topicos: [dba, vlan, uplink, guardrails]
descricao: "Evidência de configuração de DBA e VLAN de uplink com guardrails obrigatórios."
versao_firmware_testada: "MA5800V100R018 / SPH507"
ultima_atualizacao: "2026-08-15"
---

# DBA e VLAN de uplink

Fonte legada: `MA5800-CLI-COMMANDS.md`, `COMMAND-MATRIX.md` e
`ACCESS-GUARDRAILS.md`. Os exemplos são evidência; não devem ser executados
como bloco nem com valores copiados para outro alvo.

## Guardrails antes de escrever

1. Confirmar alvo, release, contexto e autorização `WRITE` vigente.
2. Capturar o estado anterior com `display dba-profile all` e as consultas de
   VLAN/porta aplicáveis.
3. Descobrir tokens ainda não confirmados com `?`.
4. Identificar referências, Binding times, impacto e rollback.
5. Não alterar gestão, rota ou objetos compartilhados sem autorização de alto
   impacto.

## Evidência confirmada e destrutiva

```text
dba-profile add profile-id 101 profile-name "DBA-OMCI-2G" type5 fix 128 assure 128 max 2000000
vlan 100 smart
port vlan 100 0/8 0
```

Os três comandos são `[CONFIRMADO][DESTRUTIVO]`. O primeiro criou o profile
101 na sessão de origem; os demais fazem parte do baseline observado para VLAN
de cliente e uplink. Revalidar IDs, nomes, VLAN e porta no alvo autorizado.

## Descoberta segura

```text
dba-profile add profile-id ?
dba-profile add profile-id 200 profile-name "TESTE" type5 fix ?
```

Essas consultas são `[DISCOVERY]` e existem para confirmar a árvore de sintaxe
antes de qualquer escrita. Elas não transformam parâmetros descobertos em
valores aprovados.

## Abort e pós-validação

Abortar ao primeiro erro, preservar a saída e reconsultar o estado. A mensagem
`Failure: The DBA-profile has already existed` não prova que o objeto seja
consultável; conferir a listagem antes de continuar.
