# Política de depreciação de documentação

Um equipamento só é deprecado quando o repositório traz evidência explícita de
que ele é legado ou descontinuado. Idade, versão, ausência de manutenção e
opinião técnica não constituem evidência.

Quando confirmado, seu documento AI-Native deve ficar em:

```text
docs/_deprecated/<fabricante>/<modelo>/<categoria>/<modulo>.md
```

O frontmatter preserva os campos obrigatórios e inclui `status: deprecated`.
O conteúdo histórico não é apagado: a auditoria registra origem, destino,
evidência e links atualizados.

Documentos sob `docs/_deprecated/` são excluídos dos índices operacionais
`INDEX.md` e de `llms.txt`. Agentes só devem consultá-los para contexto
histórico ou equipamento explicitamente deprecado, confirmando o status antes
do uso. O construtor valida esse status; documentos ativos não o recebem por
padrão.
