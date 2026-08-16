# Auditoria de reconciliação arquitetural — G11

## Arquivos analisados

- `README.md`, `INDEX.md`, `llms.txt` e índices de fabricante/modelo;
- `docs/`, `skills/` e catálogos legados;
- `.harness/`, `HARNESS.md` e Goals relacionados.

## Estruturas concorrentes encontradas

| Estrutura | Uso atual | Decisão |
|---|---|---|
| `docs/<fabricante>/<modelo>/<categoria>/` | Módulos ativos por índices gerados. | Projeção canônica de navegação. |
| `skills/` e catálogos | Conteúdo histórico, comandos, erros e procedimentos. | Fontes rastreáveis; não migrados em massa. |
| manufacturer → category → family → model → software → version → firmware → capability → skill/evidence | Aplicabilidade segura. | Contrato de registries, não árvore física. |

## Resultado

Nenhum arquivo técnico foi movido ou apagado. Este Goal fixa decisões,
limitações e migrações futuras; não implementa registries nem Skill Router.

## Risco documentado

Evidência e confirmação estão distribuídas. Caminhos, nomes ou idade de
equipamento não podem ser usados para inferir compatibilidade.
