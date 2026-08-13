---
name: network-config-backup
description: Coletar, sanitizar, validar, nomear, comparar e documentar backups textuais de configuração de equipamentos de rede inventariados. Usar antes e depois de mudanças, em coletas periódicas, em preparação de rollback ou ao validar um arquivo antes de versioná-lo.
---

# Backup seguro de configuração

## Princípios

- Tratar o inventário do Source of Truth como autoridade para identidade, fabricante e modelo.
- Nunca inferir equipamentos ou valores reais a partir desta skill.
- Manter todos os alvos e valores como parâmetros.
- Executar somente leitura por padrão. Classificar persistência, exportação para servidor, escrita e alteração de configuração como mutáveis.
- Parar antes de qualquer comando mutável sem autorização explícita, impacto conhecido e rollback.
- Nunca sobrescrever backup existente nem registrar segredos em Git, logs, Issues ou Pull Requests.

## Parâmetros obrigatórios

Resolver no Source of Truth antes de acessar o equipamento:

- `${DEVICE_NAME}`: nome canônico;
- `${DEVICE_CATEGORY}`: `olt`, `routers`, `switches`, `radios`, `servers` ou `other`;
- `${DEVICE_VENDOR}` e `${DEVICE_MODEL}`;
- `${DEVICE_HOST}`: endereço autorizado, sem copiá-lo para evidências públicas;
- `${BACKUP_DATE}`: `DD-MM-AAAA`;
- `${BACKUP_PHASE}`: vazio, `pre`, `pos` ou sequência aprovada;
- `${BACKUP_ROOT}`: raiz de backups do Source of Truth.
- `${READ_TIMEOUT_SECONDS}`: limite autorizado para a coleta;
- `${PAGINATION_MODE}`: desabilitada por sintaxe validada ou avanço manual controlado;
- `${EXPECTED_END_MARKER}`: prompt ou marcador final validado para a plataforma.

Se identidade, fabricante ou modelo não estiverem confirmados, limitar-se a observações seguras e registrar `PENDENTE DE VALIDAÇÃO`. Não criar o backup sob nome arbitrário.

## Fluxo

1. **Observar:** confirmar alvo, sessão, prompt, data, acesso somente leitura e espaço de destino.
2. **Selecionar procedimento:** ler integralmente a skill do fabricante/modelo, a [classificação de comandos](references/command-classification.md) e os [comandos por plataforma](references/vendor-commands.md).
3. **Precheck:** preencher o [checklist de readiness](references/preflight-checklist.md), confirmar que o destino não existe e definir timeout, paginação e marcador final.
4. **Coletar:** executar o comando de exibição confirmado ou descoberto na CLI. Não executar `save`, `write`, `copy`, export, reload ou equivalente como parte implícita da coleta.
5. **Preservar bruto fora do Git:** manter a saída original somente em armazenamento protegido quando contiver segredos.
6. **Sanitizar:** criar uma cópia destinada ao versionamento e mascarar credenciais, hashes, chaves, comunidades, tokens e dados proibidos pela política do Source of Truth.
7. **Validar:** conferir completude, identidade, nome, data, conteúdo, sanitização, ausência de sobrescrita e o [contrato de saída](references/output-contract.md).
8. **Comparar:** confrontar com o backup anterior e destacar mudanças inesperadas.
9. **Documentar:** registrar comando, horário, resultado, limitações, arquivo anterior e novo arquivo, sem segredos.
10. **Pós-check:** confirmar que a sessão permaneceu somente leitura e que nenhum estado do equipamento mudou.

## Caminho e nome

Usar:

```text
${BACKUP_ROOT}/${DEVICE_CATEGORY}/${DEVICE_NAME}/${DEVICE_NAME}-${BACKUP_DATE}.txt
```

Para duas coletas ligadas a uma mudança, acrescentar `-pre` e `-pos`. Para coletas independentes no mesmo dia, usar `-01`, `-02` e seguintes. Nunca usar `latest.txt`, timestamp Unix ou nome genérico como arquivo principal.

Exemplos sintéticos válidos para a validação estática: `OLT-LAB-01-12-08-2026.txt`, `OLT-LAB-01-12-08-2026-pre.txt`, `OLT-LAB-01-12-08-2026-pos.txt` e `OLT-LAB-01-12-08-2026-01.txt`. Eles não representam equipamentos reais.

## Timeout, paginação e truncamento

- Definir `${READ_TIMEOUT_SECONDS}` antes da coleta; nunca aguardar indefinidamente.
- Desabilitar paginação somente com comando classificado para a plataforma e validado no contexto. Caso contrário, avançar manualmente sem enviar texto que possa ser interpretado como comando.
- Invalidar a coleta se houver prompt de paginação remanescente, timeout, desconexão, limite de buffer, mensagem de erro ou ausência de `${EXPECTED_END_MARKER}`.
- Não concatenar silenciosamente tentativas parciais. Recomeçar a coleta em novo arquivo quando a causa estiver resolvida.

## Sanitização

Revisar, no mínimo:

- senhas e secrets, inclusive hashes e valores cifrados;
- chaves SSH, certificados e material criptográfico;
- comunidades SNMP;
- secrets de RADIUS, TACACS+, BGP e PPP;
- tokens e credenciais embutidos em URLs;
- usuários ou identificadores pessoais quando não forem necessários ao backup versionado.

Usar marcadores inequívocos como `<REDACTED_SECRET>`. Não substituir endereçamento, VLANs ou interfaces reais quando forem parte necessária do Source of Truth autorizado. Se a sanitização destruir a utilidade operacional do backup, não versionar o arquivo e solicitar armazenamento protegido aprovado.

## Validação e comparação

Antes de versionar, confirmar:

- arquivo não vazio e sem mensagem de erro ou truncamento;
- início e fim esperados da configuração;
- equipamento, categoria, data e sufixo corretos;
- ausência de arquivo anterior sobrescrito;
- varredura de segredos revisada manualmente;
- diff com a coleta anterior, quando existente;
- mudanças relevantes em interfaces, VLANs, IPs, rotas, uplinks, PONs, serviços, ACLs, autenticação e gerenciamento destacadas.

Não normalizar automaticamente divergências nem editar a configuração coletada para fazê-la coincidir com o estado pretendido.

## Falhas e rollback

- Em timeout, paginação incompleta, desconexão ou erro de CLI, marcar a coleta como inválida e preservar o backup anterior.
- Se um comando inesperadamente mudar estado, parar, registrar o retorno literal sanitizado e seguir a skill de rollback da plataforma. Não improvisar reversão.
- O rollback normal desta skill é descartar somente a nova cópia incompleta ou insegura; nunca apagar o backup anterior.
- Não usar reboot, reset ou restauração integral de configuração como rollback automático.

## Resultado esperado

Entregar `backup_file`, `evidence`, `validation_result`, `diff_result` e `warnings` conforme o [contrato de saída](references/output-contract.md). O backup deve estar completo, sanitizado, não sobrescrito e associado ao equipamento inventariado. Se qualquer requisito falhar, não publicar o arquivo e registrar a pendência.
