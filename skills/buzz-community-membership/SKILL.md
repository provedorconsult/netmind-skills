---
name: buzz-community-membership
description: Diagnosticar e alterar com segurança a membership de agentes em uma Community Buzz/Nostr, preservando membros, roles e constraints e sem usar chaves privadas.
---

# Membership de Community Buzz

## Objetivo

Determinar se uma identidade pública de humano ou agente pode autenticar no
relay e, quando a tarefa autorizar `WRITE`, adicionar somente a membership
necessária em `public.relay_members`.

## Quando usar

Use para erros NIP-42 como `restricted: not a relay member`, onboarding de
agente ou auditoria de roles. Não use para criar communities, trocar host do
relay, modificar identidades, mudar `owner-only` ou administrar o runtime do
agente.

## Parâmetros do Source of Truth

- `${COMMUNITY_HOST}` e `${COMMUNITY_ID}`;
- `${AGENT_NAME}` e `${AGENT_PUBKEY}` (somente chave pública);
- `${EXPECTED_ROLE}`; normalmente `member`;
- `${POSTGRES_READ_PATH}` e, somente se autorizado, `${POSTGRES_WRITE_PATH}`;
- `${OPERATION_SCOPE}`: `READ`, `TEST` ou `WRITE`.

Nunca registre `nsec`, private key, token, senha, `.env` ou saída bruta de
ambiente.

## Observação e diagnóstico (READ)

1. Confirme que `${COMMUNITY_HOST}` resolve para exatamente uma Community e
   que o UUID coincide com `${COMMUNITY_ID}`.
2. Consulte `public.relay_members` filtrando por `community_id`.
3. Registre apenas contagem por role e presença/ausência da pubkey alvo.
4. Confira a tabela, PK/unique e FK pelo catálogo PostgreSQL; não suponha o
   contrato a partir de um schema de outra instalação.
5. Consulte NIP-11 como healthcheck do relay. HTTP 200 não prova membership.

Classifique:

- **PASS:** Community, tabela e membership alvo foram lidas com evidência;
- **FAIL:** a pubkey está ausente, duplicada ou tem role incompatível;
- **BLOCKED:** não há caminho autenticado e autorizado até a camada efetiva.

## Interpretação de NIP-42

`Auth failed: restricted: not a relay member` confirma que a identidade que
assinou o AUTH não é aceita como membro. Não conclua que o operador humano é
o agente: cada um pode ter uma pubkey diferente. Antes de mudar dados, confirme
que a pubkey no log do runtime é `${AGENT_PUBKEY}`.

## Remediação mínima (WRITE autorizado)

Execute somente após todas as precondições serem comprovadas na mesma janela
operacional:

1. Community existe exatamente uma vez.
2. `${AGENT_PUBKEY}` possui zero linhas para `${COMMUNITY_ID}`.
3. Contagens e roles atuais foram registradas.
4. PK/unique/FK foram conferidas.
5. Há critério de abort e rollback: remover **somente** a linha recém-criada,
   mediante nova autorização, caso a pós-validação falhe.

Use uma transação curta. Faça lock proporcional somente quando necessário para
evitar concorrência. O `INSERT` deve conter apenas `community_id`, `pubkey` e
`role`, exceto se o schema comprovadamente exigir outro campo. Não edite roles
existentes, não remova membros e não substitua owner.

Abortar sem escrever se a Community, a fingerprint/contagem prévia ou a
ausência da pubkey divergirem.

## Pós-validação

Após `COMMIT`, faça uma leitura independente e confirme:

- `${AGENT_PUBKEY}` existe exatamente uma vez;
- a role é `${EXPECTED_ROLE}`;
- a contagem aumentou exatamente em um;
- roles e fingerprint das linhas anteriores permanecem iguais;
- constraints continuam presentes;
- PostgreSQL e relay estão saudáveis; NIP-11 continua acessível.

Membership aceita o AUTH; ela não prova que o runtime, subscription, backend ou
policy de resposta estejam corretos. Encaminhe essa parte para
`buzz-agent-runtime-validation`.

## Evidência esperada

```text
community: PASS | FAIL | BLOCKED
membership_before: absent | present-once | duplicate
change: none | inserted-one-member
membership_after: present-once/member
previous_memberships: preserved | not-proven
constraints: PASS | FAIL
secrets: none-used
```

## Incidente consolidado

**Causa confirmada:** uma pubkey de agente ausente em `relay_members` causa
falha NIP-42 de membership.

**Não concluir:** que todo erro NIP-42 seja problema de banco, ou que uma
membership resolva lifecycle, subscription, owner policy ou chamada ao modelo.
