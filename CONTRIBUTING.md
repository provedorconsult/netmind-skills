# Contribuindo

## Fluxo de documentação

1. Atualize `main` e crie uma branch própria.
2. Faça uma mudança focada, preservando fontes históricas e sem inserir
   credenciais ou dados de cliente.
3. Para módulos, use a estrutura fabricante → modelo → categoria e YAML
   Frontmatter válido. Use nomes kebab-case e documentos atômicos.
4. Gere índices com `python scripts/build_indexes.py --build` quando a mudança
   alterar módulos; versione os artefatos derivados.
5. Valide antes da PR:

```bash
git diff --check
bash scripts/harness-validate.sh
python scripts/validate_repository.py
python scripts/build_indexes.py --check
python scripts/lint_markdown.py .
python scripts/validate_markdown_links.py .
```

6. Revise o diff, faça commit, push e abra PR contra `main`.
7. Aguarde a CI e solicite a revisão do Checker.

## Maker e Checker

O Maker implementa, valida, abre a PR e solicita o Checker. O Checker revisa
escopo, implementação, testes, CI e evidências e publica `approve`,
`request-changes` ou `blocked`.

CI verde **não** autoriza merge. Somente o comentário social literal
`approve` do Checker autoriza a integração. `LGTM`, `Approved`, `APPROVE`,
`looks good` e `CI passed` não são autorização. Após `approve`, integrar a PR
e executar a validação pós-merge antes de iniciar o Goal seguinte.

## Templates

Use os templates de Issue existentes para propor modelo ou relatar atualização.
O template de PR exige Goal, escopo, validação e evidências. Não declare uma
categoria operacional fora de `cli`, `config`, `diag`, `mon` e `update`.
