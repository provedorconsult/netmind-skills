---
name: buzz-agent-runtime-validation
description: Validar e diagnosticar a cadeia funcional de agentes Buzz, do launcher e NIP-42 à subscription, menção, processamento, owner policy e publicação verificável de resposta.
---

# Validação de runtime de agente Buzz

## Objetivo

Localizar a primeira quebra na cadeia:

```text
runtime → relay → NIP-42 → subscription → mention → processing → backend → response
```

Cada gate precisa de evidência independente. Nunca atribua uma resposta ao
agente apenas pelo texto exibido: confirme a pubkey autora do evento.

## Parâmetros

- `${AGENT_NAME}`, `${AGENT_PUBKEY}` e `${AGENT_LOG}`;
- `${RELAY_URL}`, `${CHANNEL_ID}` e `${SUBSCRIPTION_MODE}`;
- `${RESPONSE_POLICY}` e `${OWNER_PUBKEY}` quando a configuração expuser esse
  dado publicamente;
- `${DESKTOP_LAUNCHER}` oficial e `${BACKEND_HARNESS}`;
- `${TEST_AUTHOR_PUBKEY}` para um teste `TEST` autorizado.

Não leia ou peça nsec/private key. Não altere policy, harness, backend ou
membership durante um ciclo estritamente diagnóstico.

## Observação: runtime e launcher

1. Descubra o launcher oficial no arquivo `.desktop`, serviço de usuário ou
   documentação do produto. Use exatamente esse mecanismo; não execute
   `buzz-acp` ou o harness diretamente como substituto.
2. Observe PID, PPID, processo-filhos, tempo de vida, exit code, stdout/stderr,
   log do Desktop e artefatos de crash.
3. Verifique executáveis referenciados na configuração, permissões dos
   diretórios de runtime, socket/PID esperado, HOME, PATH, DISPLAY,
   XDG_RUNTIME_DIR e D-Bus.
4. Compare somente presença e diferenças relevantes de ambiente; nunca imprima
   valores secretos.

Um encerramento limpo do launcher sem evidência de crash é uma observação, não
uma causa. Registre como `runtime lifecycle issue observed; exact shutdown
cause not conclusively established` até haver prova adicional.

## Diagnóstico por gate

| Gate | PASS | FAIL | Próxima ação segura |
| --- | --- | --- | --- |
| Runtime | processo ativo e startup sem erro terminal | launcher/harness encerra | coletar exit, PID, PPID e logs |
| NIP-42 | conexão/AUTH aceito | `not a relay member`, `restricted` ou `auth failed` | confirmar pubkey e membership |
| Subscription | `subscribed` para relay/canal e modo esperado | conexão sem SUB ou REQ rejeitado | inspecionar acesso ao canal |
| Mention | evento de menção recebido | nenhum evento após teste controlado | confirmar autor, canal e destinatário |
| Processing | sessão/prompt iniciado | rejeição antes do prompt | coletar erro do runtime |
| Backend | chamada/completion observada | erro de modelo/harness | validar estado do backend sem expor credenciais |
| Response | EVENT publicado pela `${AGENT_PUBKEY}` | resposta ausente/publicação rejeitada | correlacionar log e evento |

Logs anteriores a uma correção são evidência histórica; não os trate como falha
atual. Marque timestamps e separe cada tentativa.

## Owner-only

Se `${RESPONSE_POLICY}` for `owner-only`, primeiro prove runtime, AUTH,
subscription e recebimento da menção. Depois compare `${TEST_AUTHOR_PUBKEY}`
com `${OWNER_PUBKEY}` apenas se ambos estiverem disponíveis por configuração
pública/read-only.

- Autor diferente do owner, menção recebida e sem resposta: `BLOCKED — OWNER POLICY`.
- Owner desconhecido: `BLOCKED — OWNER IDENTITY NOT EXPOSED`.

Não relaxe a policy para fazer o teste passar.

## Teste funcional único (TEST autorizado)

Somente com runtime, NIP-42 e subscription em PASS:

1. publique uma única menção controlada no canal confirmado;
2. registre timestamp, canal, autor e ID do evento;
3. observe logs até processamento, backend e publicação;
4. recupere o evento de resposta e valide sua pubkey autora;
5. não repita o teste para compensar evidência incompleta.

## Resultado

```text
runtime: PASS | FAIL | BLOCKED
nip42: PASS | FAIL | BLOCKED
subscription: PASS | FAIL | BLOCKED
mention: PASS | FAIL | BLOCKED
processing: PASS | FAIL | BLOCKED
response: PASS | FAIL | BLOCKED
owner_policy: PASS | BLOCKED | NOT_REACHED
```

## Incidente consolidado

**Causas confirmadas possíveis:** membership ausente bloqueia NIP-42; runtime
ativo conectado pode assinar o canal sem ainda responder à policy.

**Hipótese não confirmada:** launcher/Desktop que encerra com código zero, sem
crash ou stderr, não prova a causa do shutdown. Não invente uma causa para esse
comportamento transitório.
