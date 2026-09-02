# NetMind Skills

> **Network Equipment Skill Registry AI-Native** para conhecimento operacional seguro, reutilizável e multi-fabricante.

O NetMind Skills organiza conhecimento técnico para que agentes de IA e operadores encontrem procedimentos, comandos, diagnósticos e evidências sem transformar suposição em ação sobre equipamentos de rede.

## Finalidade

Este repositório é uma biblioteca operacional de conhecimento: ajuda a identificar o contexto técnico disponível, navegar para a documentação aplicável e preservar os limites de evidência e autorização de cada ação.

Ele **não é**:

- um inventário de clientes, topologias ou equipamentos em produção;
- um cofre de credenciais, arquivos `.env` ou backups reais;
- uma ferramenta de descoberta por varredura de rede;
- uma autorização implícita para alterar um equipamento;
- um manual completo de um único fabricante;
- um Skill Router ou conjunto completo de registries já implementados.

Huawei MA5800-X7, Cisco ASR1001-X e ZTE ZXA10 C650 são a cobertura técnica atual. Eles são exemplos da biblioteca, não sua identidade: o projeto permanece multi-fabricante.

## Como um agente deve navegar

1. Receba o alvo e o escopo autorizado do **Source of Truth** do projeto consumidor. Não deduza destino, IP ou credencial.
2. Comece em [llms.txt](llms.txt) ou no [índice principal](INDEX.md), escolha o fabricante e o modelo, e abra o módulo atômico aplicável.
3. Confirme fingerprint, versão, contexto de CLI e evidência antes de usar qualquer comando. Se faltar contexto, faça `DISCOVERY` seguro ou bloqueie a operação.
4. Use a Skill e os catálogos correspondentes; respeite a classe operacional concedida pela tarefa.
5. Registre apenas evidência sanitizada e valide o resultado, sem elevar inferência a fato confirmado.

O caminho conceitual é:

```text
Target
  → Device Fingerprint
  → Equipment Registry
  → Compatibility Registry
  → Capability Registry
  → Skill Router
  → Skill / Command / Procedure / Error
  → Validation / Evidence
```

Esse é um modelo de navegação e evolução, não uma declaração de que todos os componentes existem hoje.

## Estado da arquitetura

| Estado | Componentes |
|---|---|
| **IMPLEMENTADO** | [Índices AI-Native](llms.txt), módulos em `docs/`, [Equipment Registry](registries/equipment/INDEX.md), Skills e catálogos históricos, Harness, validadores e testes de repositório. |
| **EM EVOLUÇÃO** | Normalização incremental de comandos, erros, procedimentos e evidências hoje distribuídos em Skills, módulos e catálogos. |
| **PLANEJADO** | Coleta estruturada de Device Fingerprint, Compatibility Registry, Capability Registry, Evidence Registry e Skill Router conservador. |

A [arquitetura canônica](ARCHITECTURE.md) descreve os contratos e seus limites. Ela não substitui a estrutura atual nem cria registries por documentação.

## Estrutura atual

| Diretório ou arquivo | Função atual |
|---|---|
| [`docs/`](docs/) | Módulos navegáveis por fabricante, modelo e categoria: `cli`, `config`, `diag`, `mon` e `update`. |
| [`registries/equipment/`](registries/equipment/INDEX.md) | Identidade técnica versionada e evidenciada; não comprova capability, compatibilidade ou Skill aplicável. |
| [`skills/`](skills/) | Skills parametrizadas, catálogos e conhecimento histórico de plataforma. |
| [`llms.txt`](llms.txt) e [`INDEX.md`](INDEX.md) | Pontos de entrada gerados para navegação de agentes e pessoas. |
| [`.harness/`](.harness/) | Estado e governança Git-native dos Goals; não é um registry de equipamento. |
| [`scripts/`](scripts/) | Builders e validadores determinísticos do repositório. |
| [`tests/`](tests/) | Cobertura automatizada dos contratos e validadores do repositório. |

O registry existente é o **Equipment Registry**. Seus registros e contrato v1 estão em [`registries/equipment/v1/`](registries/equipment/v1/). Compatibilidade e capabilities devem continuar desconhecidas quando não houver fonte comprovada.

## Cobertura atual

| Plataforma | Navegação principal | Contexto e limites |
|---|---|---|
| Huawei MA5800-X7 | [Índice Huawei](docs/huawei/ma5800-x7/INDEX.md) e [Skills MA5800](skills/01-ma5800-baseline/SKILL.md) | A evidência disponível depende do contexto registrado; confirme release, patch e CLI antes de agir. |
| Cisco ASR1001-X | [Índice Cisco](docs/cisco/asr1001-x/INDEX.md) e [Skills Cisco](skills/cisco-asr1001x/README.md) | A aplicabilidade é contextual; não generalize comandos para outro IOS XE, modo ou plataforma. |
| ZTE ZXA10 C650 | [Índice ZTE](docs/zte/zxa10-c650/INDEX.md) e [Skill de baseline](skills/21-zte-c650-baseline/SKILL.md) | Evidência observada somente para ZXA10 Software V1.1.2; a equivalência operacional autorizada não generaliza comandos para outra release ou chassis. |

Para rotas de consulta, configuração, diagnóstico, monitoramento ou update, selecione primeiro o modelo e depois o módulo. A presença de um arquivo no caminho não prova que ele seja compatível com o alvo.

## Bibliotecas relacionadas

- [SoftMind Skills](https://github.com/provedorconsult/softmind-skills) — operações de softwares, bancos de dados, containers e plataformas auto-hospedadas.

## Evidência técnica e classe operacional

Evidência responde **o que é comprovado**. Classe operacional responde **o que a tarefa permite fazer**. São dimensões diferentes.

| Evidência técnica | Significado |
|---|---|
| `CONFIRMADO` | Sintaxe ou resultado observado com sucesso no contexto indicado. |
| `DISCOVERY` | Consulta segura, ajuda contextual ou descoberta ainda não promovida a comando confirmado. |
| `INFERIDO` | Derivado de documentação ou contexto incompleto; requer validação. |
| `ERRO` | Comando rejeitado ou retorno literal observado. |
| `VERSÃO DIFERENTE` | Evidência de outro release, firmware ou contexto; não é confirmação para o alvo. |

| Classe operacional | Regra |
|---|---|
| `READ` | Consulta de status, configuração exibida ou contadores. |
| `DISCOVERY` | Ajuda contextual e inspeção de sintaxe sem alteração de estado. |
| `TEST` | Teste controlado, conforme tarefa e Skill. |
| `WRITE` | Criação ou alteração: exige autorização e guardrails. |
| `PERSIST` | Persistência global, tratada como ação própria quando aplicável. |
| `HIGH-IMPACT` | Ações de impacto material — por exemplo reload/reset, gestão, routing, AAA, firewall ou ACL/NAT de produção — exigem autorização explícita e plano proporcional. |

Ordem de autoridade: CLI real do alvo; evidência do mesmo modelo e versão; discovery no alvo; documentação oficial compatível; evidência de outra versão; inferência. **Nunca promova inferência a comando confirmado.**

## Acesso, segurança e Source of Truth

A abertura de uma sessão autenticada é uma capacidade básica; o guardrail incide sobre o comando executado após a conexão. O [Source of Truth](ACCESS-GUARDRAILS.md) do projeto consumidor define alvo, topologia, endereços, janela e mecanismo autorizado de credenciais.

Antes de `WRITE`, `PERSIST` ou `HIGH-IMPACT`, valide alvo, contexto, versão, sintaxe, estado anterior, impacto, dependências, rollback, abort e pós-validação. Em falha de autenticação, host key inesperada ou identidade divergente, pare e devolva evidência sanitizada. Nunca substitua um alvo confirmado por varredura ou adivinhação.

Não armazene neste repositório credenciais, tokens, `.env`, dados de clientes, backups brutos, configurações reais ou topologias sensíveis. Exemplos devem usar dados sanitizados e redes reservadas.

### Exemplo conceitual sanitizado

```text
Tarefa autorizada: READ
Target: fornecido pelo Source of Truth
Fingerprint: fabricante/modelo/versão ainda parcialmente desconhecidos

Agente → abre o índice do fabricante/modelo
       → usa DISCOVERY não mutável para confirmar contexto de CLI
       → seleciona módulo compatível apenas após evidência
       → executa consulta READ e registra retorno sanitizado
```

O agente não escolhe um comando `WRITE` a partir de `INFERIDO`, nem trata a sessão como autorização de mudança.

## Harness: Maker e Checker

Mudanças no repositório seguem o fluxo:

```text
Goal → Maker → PR → CI → Checker → approve → merge
```

O Maker trabalha somente no Goal ativo e abre uma PR isolada. A CI valida automações, mas **CI verde não autoriza merge**. A integração só é autorizada pelo comentário social literal `approve`, emitido pelo Checker no HEAD efetivamente revisado. Consulte o [Harness](HARNESS.md) e o estado em [`.harness/`](.harness/).

## Estado atual e roadmap

Hoje, a navegação por índices, os módulos Huawei e Cisco, as Skills legadas e o Equipment Registry fornecem a base operacional. A arquitetura preserva essas fontes enquanto a normalização avança de modo incremental e auditável.

Os próximos passos arquiteturais — registries de compatibilidade, capability e evidência, além do Skill Router — permanecem planejados. Eles exigem Goals próprios, dados comprovados e revisão; não são funcionalidades disponíveis nem devem ser simulados por convenção de diretórios.

## Quick Start

1. Leia [este README](README.md), [llms.txt](llms.txt) e [a arquitetura](ARCHITECTURE.md).
2. Abra o [Equipment Registry](registries/equipment/INDEX.md) se houver fingerprint sanitizado disponível.
3. Navegue pelo [índice Huawei](docs/huawei/INDEX.md) ou [índice Cisco](docs/cisco/INDEX.md), depois pelo modelo e módulo.
4. Leia a Skill e seus limites de evidência antes de formar qualquer comando.
5. Para acesso autorizado, siga os [guardrails de acesso](ACCESS-GUARDRAILS.md); para mudanças, obtenha a classe operacional apropriada e aplique o procedimento seguro.

## Validação estática local

Os validadores usam somente a dependência de desenvolvimento fixada em
[`requirements-dev.txt`](requirements-dev.txt), na mesma versão da CI. Prepare
um ambiente descartável fora do runtime do projeto e execute as verificações
estáticas:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --disable-pip-version-check -r requirements-dev.txt

python scripts/validate_frontmatter.py docs
python scripts/validate_equipment_registry.py
python scripts/build_indexes.py --check
python scripts/lint_markdown.py .
python scripts/validate_markdown_links.py .
python scripts/validate_repository.py
bash scripts/harness-validate.sh
```

Não execute localmente suítes de teste, containers, deploys, migrações ou
acesso a equipamentos. As suítes dinâmicas, incluindo o merge gate do Harness,
permanecem sob responsabilidade da CI/VPS.

## Documentação complementar

- [Arquitetura canônica](ARCHITECTURE.md)
- [Índice AI-Native](llms.txt)
- [Equipment Registry](registries/equipment/INDEX.md)
- [Guardrails de acesso](ACCESS-GUARDRAILS.md)
- [Huawei MA5800-X7](docs/huawei/ma5800-x7/INDEX.md)
- [Cisco ASR1001-X](docs/cisco/asr1001-x/INDEX.md)
- [ZTE ZXA10 C650](docs/zte/zxa10-c650/INDEX.md)
- [Skills Cisco](skills/cisco-asr1001x/README.md)
- [Matriz de comandos Huawei](COMMAND-MATRIX.md)
- [Harness Git-native](HARNESS.md)
