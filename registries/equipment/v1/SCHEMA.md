# Equipment Registry — contrato v1

## Finalidade e limites

Este formato versionado registra somente identidade técnica comprovada:

```text
manufacturer → family → model → software/CLI → version → firmware/patch → evidence
```

Ele não declara capability, compatibilidade, comando, procedimento, erro ou
Skill aplicável. Um consumidor não pode concluir esses fatos a partir deste
Registry nem do caminho de uma Skill.

## Estrutura

`equipment-registry.yaml` é um mapa YAML UTF-8 com os campos obrigatórios:

| Campo | Tipo | Regra |
|---|---|---|
| `format` | string | Deve ser `netmind-equipment-registry`. |
| `format_version` | string | Versão do contrato; v1 é `1.0`. |
| `records` | lista não vazia | Registros de identidade. |
| `records[].id` | string | ID canônico único de equipamento. |
| `manufacturer`, `family`, `model`, `software_cli`, `version`, `firmware_patch` | objeto | Cada um contém `id` e `value`. |
| `evidence` | lista não vazia | Evidência rastreável que sustenta os valores conhecidos do registro. |
| `evidence[].classification` | enum | `CONFIRMADO`, `DISCOVERY`, `INFERIDO` ou `VERSÃO DIFERENTE`. |
| `evidence[].reference` | string | Caminho relativo ao repositório e âncora Markdown, por exemplo `README.md#equipamento-e-baseline`. |
| `evidence[].statement` | string | Declaração curta e sanitizada do fato sustentado. |

Os objetos de identidade têm exatamente:

| Campo | Tipo | Regra |
|---|---|---|
| `id` | string ou `null` | ID canônico do valor; `null` quando o valor é desconhecido. |
| `value` | string não vazia ou `null` | Valor literal comprovado; `null` quando desconhecido. |

`id` e `value` devem ser ambos conhecidos ou ambos `null`. O campo
`firmware_patch` é obrigatório no formato, mas pode ser desconhecido. Campos
desconhecidos não recebem texto substituto, estimativa ou ID sintético.

## Identificadores canônicos e normalização

IDs usam minúsculas ASCII e hífens; segmentos são separados por `:`. Valores
são preservados como observados na evidência, inclusive maiúsculas e pontuação.

```text
manufacturer:<manufacturer>
family:<manufacturer>:<family>
model:<manufacturer>:<family>:<model>
software:<manufacturer>:<software>
version:<manufacturer>:<software-ou-unknown>:<version>
firmware:<manufacturer>:<software-ou-unknown>:<version>:<patch>
equipment:<manufacturer>:<family>:<model>
```

Na normalização de segmentos, converta para minúsculas, substitua sequências de
caracteres fora de `a-z` e `0-9` por um único `-`, e remova hífens das pontas.
Não normalizar um valor observado para mudar seu significado. O identificador
de versão/firmware usa `unknown` apenas quando o software/CLI é desconhecido e
o próprio valor de versão ou patch é comprovado; isso não afirma qual software
o equipamento executa.

## Unicidade e preenchimento

- `records[].id`, IDs de manufacturer, family, model, software, version e
  firmware conhecidos devem ser únicos no arquivo.
- Um `model` deve pertencer ao manufacturer e à family informados no seu ID;
  o mesmo vale para os níveis seguintes quando conhecidos.
- A lista `evidence` deve conter ao menos uma referência local existente e não
  pode repetir a mesma combinação de classificação e referência.
- `CONFIRMADO` representa fato observado/executado com sucesso no contexto
  citado; `DISCOVERY` representa consulta literal aceita; `INFERIDO` é fonte
  ainda não confirmada; `VERSÃO DIFERENTE` é fonte de release não validada no
  contexto do registro.
- As classificações qualificam a evidência, não promovem capability ou
  compatibilidade. Um valor sem evidência é desconhecido (`null`).

## Expansão

Para adicionar fabricante ou modelo, mantenha `format_version: "1.0"`, inclua
um novo registro completo, use IDs canônicos sem colisão e uma evidência local
rastreável para cada fato conhecido. Execute o validador antes de propor a
mudança. Alterações incompatíveis de estrutura exigem uma nova versão em outro
diretório (por exemplo, `v2/`); não altere silenciosamente o contrato v1.

Não adicione compatibilidade, capability ou referências de Skill como atalho de
evidência. Quando a fonte não comprovar um campo, deixe o par `id`/`value` como
`null` até haver discovery ou evidência apropriada.
