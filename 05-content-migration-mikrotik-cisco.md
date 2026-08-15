# TASK 05 — Migração Modular MikroTik e Cisco

## Goal

Aplicar o padrão de documentação atômica a conteúdo existente de MikroTik e Cisco, validando a arquitetura em dois ecossistemas adicionais antes da migração geral.

## Fonte de requisitos

Basear-se no PRD:
- RF02;
- RF03;
- RF04;
- RF08;
- RNF01;
- RNF03;
- RNF04.

## Escopo

1. Mapear o conteúdo existente de MikroTik e Cisco.
2. Selecionar conteúdo representativo.
3. Dividir documentos monolíticos quando houver fronteiras claras de funcionalidade.
4. Organizar por fabricante/modelo/versão quando a informação estiver disponível.
5. Adicionar YAML Frontmatter.
6. Preservar sintaxes e comandos originais.
7. Manter documentos atômicos com no máximo 150 linhas, sempre que possível.
8. Atualizar índices automaticamente.

## Regra de fidelidade

Não deduzir versão de RouterOS, IOS/IOS XE, firmware, modelo ou comportamento técnico que não esteja suportado pelo conteúdo existente. Quando o dado não estiver disponível, registrar `N/A` ou ausência conforme o template adotado.

## Critérios de aceite

- Conteúdo não é perdido.
- Frontmatter válido.
- Estrutura de diretórios coerente.
- Índices atualizados.
- Links internos válidos.
- Testes de validação passam.
- PR contém mapa resumido de origem → destino para permitir auditoria do Checker.

# Protocolo Maker / Checker

## Papel do Codex
Atuar exclusivamente como **Maker** nesta tarefa.

## Regra de integração
- O Maker deve implementar apenas o Goal desta tarefa.
- O Maker deve trabalhar em uma branch própria e abrir Pull Request contra `main`.
- O Maker deve executar os testes e validações definidos no arquivo.
- O Maker deve registrar no PR um resumo objetivo do que foi feito e evidências de validação.
- Ao terminar, o Maker deve solicitar explicitamente a revisão do Checker.
- O Maker **não deve fazer merge**, mesmo que os testes estejam verdes.
- O Maker deve aguardar o veredito do Checker em comentário no Pull Request.
- O comentário social `approve` do Checker é a autorização para integração.
- Qualquer outro comentário, inclusive `LGTM`, `looks good`, CI verde ou aprovação informal, **não autoriza merge**.
- Se o Checker solicitar alterações, o Maker deve corrigir na mesma branch/PR, executar novamente as validações e voltar a aguardar novo `approve`.
- Não fechar a PR sem autorização.
- Não alterar escopo de tarefas posteriores para resolver problemas não relacionados.

## Critério de conclusão
A tarefa só é considerada concluída quando:
1. implementação estiver na PR;
2. validações locais/CI estiverem verdes;
3. Checker revisar;
4. Checker publicar o comentário social `approve`.
