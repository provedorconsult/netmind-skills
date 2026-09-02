# Skills Buzz em Dokploy

Skills reutilizáveis para operar e diagnosticar uma instalação auto-hospedada do [Buzz](https://github.com/block/buzz) em Dokploy. O Buzz é um relay Nostr com PostgreSQL, Redis e storage S3/MinIO; a documentação oficial separa explicitamente o bundle Compose para VPS do Compose de desenvolvimento. A compatibilidade do Compose, imagem e schema deve ser confirmada no deployment alvo antes de qualquer ação.

## Limites

- O Source of Truth do projeto consumidor define o deployment, Community, domínio, caminho de acesso e mecanismo autorizado de credenciais.
- Estas skills não contêm IPs, domínios, IDs, chaves Nostr, `nsec`, `.env`, credenciais ou dados de uma Community real.
- Dokploy API serve para discovery documentado; não é shell remoto nem autorização para executar SQL arbitrário.
- `READ` é o padrão. Publicar evento de teste requer `TEST`; alterar membership requer `WRITE` explícito. Deploy, reinício, migration e alteração de variáveis não são autorizados por este pacote.

## Quando usar e sequência de diagnóstico

1. Use [Acesso diagnóstico Dokploy → PostgreSQL](dokploy-postgres-diagnostic-access/SKILL.md) para localizar um bloqueio no caminho administrativo ou confirmar a camada de dados em `READ`.
2. Use [Membership de Community](buzz-community-membership/SKILL.md) para distinguir Community/relay de channel membership e, somente com `WRITE` explícito, remediar a camada efetiva confirmada.
3. Use [Validação de runtime de agente](buzz-agent-runtime-validation/SKILL.md) para seguir os gates de autenticação, attestation, canal, menção, processamento, backend e resposta.

Comece em `READ`. Use `TEST` apenas para uma validação funcional controlada e autorizada. Use `WRITE` somente mediante autorização explícita, precheck, rollback e pós-validação. A descoberta de uma falha não autoriza mutação.

## Fontes

- [Buzz — README](https://github.com/block/buzz#readme)
- [Buzz — Compose para VPS](https://github.com/block/buzz/tree/main/deploy/compose)
- [Buzz — Nostr e autenticação](https://github.com/block/buzz/blob/main/NOSTR.md)
