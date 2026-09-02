---
name: buzz-community-membership
description: Diagnosticar e, somente com autorização WRITE explícita, alterar a membership de uma pubkey de agente na Community Buzz correta com precheck, transação mínima e validação independente.
---

# Membership de Community Buzz

## Objetivo

Diagnosticar membership da identidade pública de um agente na Community correta. Quando uma tarefa autorizar `WRITE` explicitamente, executar uma alteração mínima somente na camada efetiva confirmada no deployment alvo, preservando memberships e roles existentes.

## Contexto obrigatório

Obter exclusivamente do Source of Truth:

- `${COMMUNITY_HOST}` e `${COMMUNITY_ID}`;
- `${AGENT_NAME}`, `${AGENT_PUBKEY}` e `${EXPECTED_ROLE}`;
- `${POSTGRES_READ_PATH}` e `${POSTGRES_WRITE_PATH}` autorizados;
- `${OPERATION_SCOPE}`: `READ` por padrão, `WRITE` somente quando explicitamente concedido.

Nunca solicite, leia ou registre private key, `nsec`, token, senha ou `.env`. Uma pubkey é identificador público, mas ainda deve ser obtida do Source of Truth e incluída em evidência apenas quando necessária.

## Discovery e observação `READ`

1. Confirme que `${COMMUNITY_HOST}` e `${COMMUNITY_ID}` selecionam exatamente uma Community no deployment alvo. No Buzz, a URL/host é parte da seleção da Community; não use uma URL de outro tenant como substituta.
2. Descubra a camada efetiva de membership no schema e release instalados. Não assuma tabela, coluna, role ou constraint a partir de outro deployment. Se `public.relay_members` estiver documentada para o alvo, ainda confirme catálogo, PK/unique e FK antes de interpretar ou escrever.
3. Consulte somente a Community confirmada; registre presença/ausência da `${AGENT_PUBKEY}`, contagem por role e total, sem despejar memberships ou eventos não necessários.
4. Use NIP-11 como healthcheck do relay, não como prova de membership. Em falha NIP-42, compare a pubkey que assinou AUTH com `${AGENT_PUBKEY}`.

## Community Membership ≠ Channel Membership

`relay_members` demonstra membership na Community/relay quando essa for a camada efetiva confirmada no deployment. `channel_members` representa uma autorização diferente. Um agente pode estar presente em `relay_members` e não possuir membership no canal; portanto, `restricted: not a channel member` não deve ser diagnosticado automaticamente como ausência em `relay_members`.

Em `READ`, descubra qual camada rejeitou a operação e não altere membros existentes. A sequência de diagnóstico é:

```text
Community / Relay
  ↓
NIP-42 authentication
  ↓
Channel membership
  ↓
Owner / role policy
  ↓
Mention / subscription
  ↓
Agent processing
  ↓
Backend
  ↓
Response
```

| Evidência observada | Classificação segura |
| --- | --- |
| pubkey ausente da Community/relay efetiva ou `not a relay member` | Community / Relay `FAIL` ou `BLOCKED`, conforme a evidência |
| NIP-42 rejeitado após Community confirmada | NIP-42 `FAIL` ou `BLOCKED` |
| `restricted: not a channel member` | Channel membership `FAIL` ou `BLOCKED`; não inferir ausência em `relay_members` |
| autor membro do canal, mas incompatível com owner/role policy | Owner / role policy `BLOCKED` |
| gates anteriores em PASS sem resposta | continuar em subscription, processamento, backend e resposta |

## Remediação `WRITE` explicitamente autorizada

Antes da alteração, confirme na mesma janela de manutenção:

1. Community única e identidade do deployment validadas.
2. Pubkey alvo ausente (zero memberships) na Community; se estiver presente ou duplicada, aborte e reporte.
3. Contagens e roles anteriores registradas de modo sanitizado.
4. Schema, constraints e campos mínimos exigidos pela release atual confirmados.
5. Impacto, critério de abort, rollback restrito à linha nova e pós-validação independente aprovados.

Execute uma transação curta com o menor conjunto de campos permitido pelo schema confirmado. Não crie Community, não altere owner, roles ou memberships existentes, não relaxe policy do agente e não execute migrations. Em qualquer divergência, faça abort; rollback/remover a nova linha requer a autorização prevista no plano.

## Pós-validação

Faça nova leitura independente e confirme:

- `${AGENT_PUBKEY}` presente exatamente uma vez;
- `${EXPECTED_ROLE}` aplicado;
- total incrementado exatamente em um;
- contagens/fingerprint sanitizado de memberships anteriores preservados;
- constraints, PostgreSQL e relay saudáveis.

Membership válida prova apenas autorização de relay para aquela pubkey; não prova runtime, subscription, processamento ou resposta. Para os gates seguintes, use `$buzz-agent-runtime-validation`.

## Resultado esperado

```text
community: PASS | FAIL | BLOCKED
membership_before: absent | present-once | duplicate | unknown
change: none | inserted-one-member | aborted
membership_after: present-once/expected-role | not-reached
previous_memberships: preserved | not-proven
constraints: PASS | FAIL | BLOCKED
secrets: none-disclosed
```

## Fontes

- [Buzz README — Community por URL e identidade Nostr](https://github.com/block/buzz#what-is-this-really)
- [Buzz Nostr documentation](https://github.com/block/buzz/blob/main/NOSTR.md)
