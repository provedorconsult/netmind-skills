# Classificação de comandos

Aplicar exatamente uma classificação primária a cada comando citado no fluxo de backup.

## `[CONFIRMADO]`

Validado no contexto claramente documentado de fabricante, modelo, versão, modo CLI e resultado. A confirmação não se transfere automaticamente para outro equipamento ou release.

## `[INFERIDO]`

Tecnicamente plausível por documentação ou experiência, mas ainda requer descoberta e validação no alvo. Não promover por conhecimento prévio.

## `[PENDENTE DE VALIDAÇÃO]`

Sintaxe, efeito, modo, segurança ou critério de sucesso insuficientemente conhecidos. Não utilizar até concluir a investigação.

## `[PROIBIDO]`

Não executar no fluxo automático. Inclui persistência, escrita, exportação mutável, restauração, reload, reset e qualquer comando destrutivo ou de alto impacto.

Um comando `[PROIBIDO]` somente pode aparecer em procedimento de mudança separado, com autorização explícita, backup, impacto, validação e rollback; nunca é promovido implicitamente pela skill de backup.
