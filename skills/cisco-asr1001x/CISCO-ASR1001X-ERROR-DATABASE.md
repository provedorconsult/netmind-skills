# Cisco ASR1001-X Error Database

## Estado

Nenhum erro literal e sanitizado do ASR1001-X foi fornecido. Portanto, este banco não contém erros fictícios. Mensagens de documentação não devem ser apresentadas como retorno real.

## Esquema obrigatório

### <ERRO LITERAL>

- **Status:** [ERRO]
- **Equipamento:** Cisco ASR1001-X
- **IOS XE:** <VERSÃO>
- **Modo/prompt:** <MODO>
- **Comando literal:** <COMANDO_SANITIZADO>
- **Erro literal:** <RETORNO>
- **Causa provável:** <HIPÓTESE>
- **Comandos para diagnóstico:** <DISCOVERY/SHOW>
- **Correção proposta:** <NÃO EXECUTADA>
- **Risco:** <BAIXO|MÉDIO|ALTO|CRÍTICO>
- **Rollback:** <PROCEDIMENTO>
- **Resultado:** <PENDENTE|VALIDADO>

## Regras

Preservar exatamente mensagem, cursor `^`, prompt e linha rejeitada, removendo somente segredos. Não substituir retorno por tradução. Antes de registrar correção, reproduzir apenas se seguro e usar `?` no mesmo modo. Um erro de sintaxe não autoriza tentar variações destrutivas.

