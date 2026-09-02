---
name: buzz-agent-runtime-validation
description: Validar de forma escalonada o runtime, a autenticação NIP-42, a assinatura e a resposta de um agente Buzz, separando evidências READ de um único teste controlado autorizado.
---

# Validação de runtime de agente Buzz

## Objetivo

Encontrar a primeira quebra comprovada na cadeia de execução de um agente Buzz, sem transformar conectividade do relay, membership ou logs antigos em prova de resposta funcional.

```text
runtime → relay → Community membership → NIP-42 → owner attestation → channel membership → subscription → mention → processing → backend → response
```

## Contexto obrigatório

Resolva no Source of Truth:

- `${AGENT_NAME}` e `${AGENT_PUBKEY}`;
- `${RELAY_URL}`, `${COMMUNITY_ID}` e `${CHANNEL_ID}`;
- `${SUBSCRIPTION_MODE}` e `${RESPONSE_POLICY}`;
- `${OWNER_PUBKEY}`, somente se exposta por configuração pública/read-only;
- `${OWNER_ATTESTATION_MODE}`: `NIP-OA`, mecanismo equivalente ou `NOT_ENABLED`, confirmado por configuração pública/read-only;
- `${DESKTOP_LAUNCHER}` ou mecanismo oficial do runtime;
- `${TEST_AUTHOR_PUBKEY}` apenas para um teste `TEST` explicitamente autorizado.

Nunca solicite, leia, exiba ou registre private key, `nsec`, token, senha ou `.env`. A existência de uma identidade humana autorizada não comprova membership da identidade do agente.

## Diagnóstico `READ`

1. Localize e use apenas o launcher oficial configurado para o agente. Não inicie `buzz-acp`, `buzz-cli` ou um harness diretamente como substituto do runtime configurado.
2. Colete PID, PPID, filhos, duração, exit code, stdout/stderr sanitizados, logs de Desktop/agente e artefatos de crash disponíveis. Confirme executável, permissões, `HOME`, `PATH`, `DISPLAY`, `XDG_RUNTIME_DIR` e D-Bus sem expor secrets.
3. Confirme em sequência conexão ao relay, Community membership, NIP-42, owner attestation quando habilitada, channel membership, subscription do canal/modo e recebimento de menção. Pare no primeiro gate `FAIL` ou `BLOCKED`.
4. Trate encerramento limpo sem stderr, crash ou sinal como observação de ciclo de vida, não como causa raiz comprovada.
5. Mantenha timestamps por tentativa. Log anterior a uma correção é evidência histórica, não prova de falha atual.

## Gates

| Gate | PASS comprovado | FAIL ou BLOCKED |
| --- | --- | --- |
| Runtime | processo ativo e startup concluído | launcher encerra ou não cria PID |
| Community / relay | pubkey presente na Community correta | `not a relay member`, ausência ou camada não confirmada |
| NIP-42 | conexão/AUTH aceita | `auth failed` após alcançar a camada de relay |
| Owner attestation | credencial NIP-OA aceita como caminho alternativo de admissão, ou `NOT_REQUIRED` após membership direta aceita | credencial rejeitada, ou caminho necessário não comprovado |
| Channel membership | pubkey autorizada no canal confirmado | `restricted: not a channel member`, ausência ou camada não confirmada |
| Subscription | assinatura autorizada do canal/modo | nenhuma SUB/REQ autorizada |
| Mention | evento controlado recebido | nenhum evento após teste válido |
| Processing | sessão/prompt iniciado | rejeição antes do prompt |
| Backend | chamada/completion observável | erro de harness/modelo |
| Response | evento publicado pela `${AGENT_PUBKEY}` | resposta ausente ou publicação rejeitada |

Uma falha `not a relay member` indica que a pubkey que assinou o AUTH não foi aceita na Community/relay; compare-a com `${AGENT_PUBKEY}`. Uma falha `restricted: not a channel member` deve ser classificada no gate de canal, não como ausência automática em `relay_members`. Nenhuma dessas mensagens, isoladamente, prova falha de relay, modelo ou backend.

## NIP-OA / owner attestation

Quando `${OWNER_ATTESTATION_MODE}` indicar `BUZZ_ALLOW_NIP_OA_AUTH` ou mecanismo equivalente, trate owner attestation como gate independente e alternativo à membership direta quando a release alvo assim o documentar. NIP-42 aceito prova somente a autenticação no relay; membership na Community prova somente a camada de relay; nenhum dos dois prova que a attestation do owner foi apresentada ou aceita.

- Membership direta aceita: `NOT_REQUIRED — OWNER ATTESTATION`; não inferir que a attestation foi usada.
- Agente sem membership direta e attestation aceita como caminho autorizado: `PASS — OWNER ATTESTATION`.
- Attestation apresentada e rejeitada: `FAIL — OWNER ATTESTATION`.
- Caminho de attestation necessário, mas configuração/evidência não disponível em `READ`: `BLOCKED — OWNER ATTESTATION`.
- Mecanismo confirmado como não habilitado: `NOT_ENABLED — OWNER ATTESTATION`; não inferir que uma policy `owner-only` deixou de existir.

## Política `owner-only`

Prove runtime, AUTH, subscription e recebimento da menção antes de comparar `${TEST_AUTHOR_PUBKEY}` com `${OWNER_PUBKEY}`.

- Menção recebida, autor membro do canal, mas diferente do owner e sem resposta: `BLOCKED — OWNER POLICY`.
- Autor não é membro da Community/relay: `FAIL` ou **BLOCKED — COMMUNITY MEMBERSHIP**, conforme a evidência.
- Autor é membro da Community, mas não do canal: `FAIL` ou **BLOCKED — CHANNEL MEMBERSHIP**, conforme a evidência.
- Owner não disponível por meio público/read-only: `BLOCKED — OWNER IDENTITY NOT EXPOSED`.

Nunca relaxe policy para obter resposta no teste.

## Teste único `TEST`

Somente após `runtime`, **Community membership**, `NIP-42`, **owner attestation** quando aplicável, **channel membership** e `subscription` em `PASS`, e com autorização explícita:

1. Publique uma única menção controlada no canal confirmado.
2. Registre timestamp, canal, pubkey autora e ID do evento, sem material secreto.
3. Acompanhe recebimento, processamento, backend e publicação.
4. Recupere o evento de resposta e confirme `${AGENT_PUBKEY}` como pubkey autora.
5. Não repita publicação para compensar evidência incompleta; classifique o gate como `BLOCKED` e devolva a limitação.

## Resultado esperado

```text
runtime: PASS | FAIL | BLOCKED
nip42: PASS | FAIL | BLOCKED
owner_attestation: PASS | FAIL | BLOCKED | NOT_REQUIRED | NOT_ENABLED
channel_membership: PASS | FAIL | BLOCKED
subscription: PASS | FAIL | BLOCKED
mention: PASS | FAIL | BLOCKED
processing: PASS | FAIL | BLOCKED
backend: PASS | FAIL | BLOCKED
response: PASS | FAIL | BLOCKED
owner_policy: PASS | BLOCKED | NOT_REACHED
evidence: sanitized | insufficient
```

## Fontes

- [Buzz README — agentes, relay e NIP-42](https://github.com/block/buzz#architecture)
- [Buzz Nostr documentation](https://github.com/block/buzz/blob/main/NOSTR.md)
