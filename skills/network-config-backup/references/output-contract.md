# Contrato de saída

Produzir uma estrutura equivalente após cada tentativa, inclusive em falha. Não incluir endereço de gerenciamento, credenciais ou saída bruta sensível.

```yaml
status: success
device: ${DEVICE_NAME}
backup_file: ${PATH}
evidence: ${EVIDENCE_PATH}
sanitized: true
validation_result:
  validated: true
  complete: true
  truncated: false
  end_marker_found: true
previous_backup: ${PREVIOUS_OR_NULL}
diff_result:
  compared: true
  diff_detected: true
  summary: ${SANITIZED_DIFF_SUMMARY}
warnings: []
```

## Regras

- `status`: usar `success`, `failed` ou `partial`. Somente `success` autoriza propor versionamento.
- `backup_file`: apontar para o arquivo sanitizado e validado; usar `null` em falha anterior à criação.
- `evidence`: apontar para evidência sanitizada da tentativa.
- `sanitized`: usar `true` somente depois da varredura e revisão manual.
- `validation_result.validated`: exigir todos os critérios aplicáveis.
- `validation_result.complete`: exigir início, fim e prompt esperados.
- `validation_result.truncated`: usar `true` diante de timeout, paginação remanescente, desconexão, limite de buffer ou marcador final ausente.
- `previous_backup`: usar caminho relativo ou `null`.
- `diff_result.compared`: usar `false` quando não houver backup anterior e explicar em `warnings`.
- `warnings`: registrar limitações, divergências e itens `PENDENTE DE VALIDAÇÃO` sem secrets.
