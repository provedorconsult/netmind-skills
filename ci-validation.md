# Validação contínua de documentação

O workflow `Validate Documentation` roda em Pull Requests e em push para
`main`. Ele é somente leitura: valida frontmatter com o schema de G02, executa
`build_indexes.py --check`, lint Markdown e links internos.

O lint interno versão `1.0.0` verifica whitespace terminal e blocos de código
fechados. O verificador de links versão `1.0.0` valida destinos locais e ignora
links HTTP(S)/mailto para não depender da rede. Ambos evitam dependências
adicionais; PyYAML permanece fixado em `6.0.3`.

Índices devem ser regenerados fora da CI. O `--check` não altera arquivos; uma
divergência falha o workflow.
