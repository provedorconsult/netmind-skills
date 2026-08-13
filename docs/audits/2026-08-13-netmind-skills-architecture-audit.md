# Auditoria arquitetural e proposta de evolução do NetMind Skills

**Data:** 2026-08-13  
**Status:** Proposta para debate da equipe e dos agentes  
**Escopo:** arquitetura do repositório, indexação, descoberta, compatibilidade, organização por fabricante/modelo/versão/firmware e consumo por agentes de IA.

## 1. Objetivo

Transformar `netmind-skills` de um conjunto de Skills específicas de equipamentos em um **Network Equipment Skill Registry**: uma biblioteca universal, hierárquica e indexável de conhecimento operacional para equipamentos de rede.

O repositório deve permitir que um agente receba uma identidade parcial ou completa de um equipamento e consiga determinar, com o menor contexto possível:

1. fabricante;
2. categoria do equipamento;
3. família e modelo;
4. sistema operacional/CLI;
5. versão;
6. firmware/patch;
7. capacidades disponíveis;
8. Skills compatíveis;
9. comandos válidados;
10. evidências e limitações;
11. procedimentos de diagnóstico, mudança, validação e rollback.

## 2. Resultado da auditoria

A base atual é tecnicamente promissora e contém conhecimento operacional valioso, especialmente nas Skills Huawei MA5800 e Cisco ASR1001-X. O repositório já possui boas práticas que devem ser preservadas:

- evidência operacional explícita;
- distinção entre conhecimento confirmado e descoberta;
- preocupação com comandos destrutivos;
- uso da CLI real como autoridade operacional;
- Skills separadas por função;
- banco de erros;
- matriz de comandos;
- validação estrutural;
- CI para validação.

O principal problema é arquitetural: o equipamento está excessivamente incorporado no nome e no caminho da Skill. Essa abordagem funciona para poucos equipamentos, mas não escala para dezenas de fabricantes, centenas de modelos e múltiplas versões de software/firmware.

## 3. Decisão arquitetural proposta

Adotar uma arquitetura em múltiplas dimensões:

```text
NetMind Skills
  -> Manufacturer
    -> Category
      -> Family
        -> Model
          -> Software/CLI
            -> Version
              -> Firmware/Patch
                -> Capability
                  -> Skill
                    -> Command / Procedure / Error / Evidence
```

A árvore de diretórios deve representar identidade e compatibilidade; os índices devem representar descoberta e roteamento para agentes.

## 4. Estrutura de diretórios proposta

```text
netmind-skills/
├── README.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
│
├── catalog/
│   ├── manufacturers.yaml
│   ├── platforms.yaml
│   ├── models.yaml
│   ├── versions.yaml
│   ├── capabilities.yaml
│   └── index.yaml
│
├── schemas/
│   ├── skill.schema.yaml
│   ├── device.schema.yaml
│   ├── command.schema.yaml
│   ├── error.schema.yaml
│   └── evidence.schema.yaml
│
├── manufacturers/
│   ├── huawei/
│   │   ├── olt/
│   │   │   └── ma5800/
│   │   │       └── x7/
│   │   │           ├── common/
│   │   │           └── firmware/
│   │   │               └── v100r018/
│   │   │                   └── sph507/
│   │   └── ont/
│   ├── cisco/
│   │   └── router/
│   │       └── asr1000/
│   │           └── asr1001-x/
│   ├── mikrotik/
│   ├── fiberhome/
│   ├── datacom/
│   ├── vsol/
│   ├── zte/
│   ├── nokia/
│   └── juniper/
│
├── capabilities/
│   ├── bgp/
│   ├── ospf/
│   ├── vlan/
│   ├── qinq/
│   ├── pppoe/
│   ├── radius/
│   ├── nat/
│   ├── cgnat/
│   ├── qos/
│   ├── gpon/
│   ├── ont/
│   ├── multicast/
│   └── ipv6/
│
├── commands/
├── errors/
├── operations/
├── agents/
├── indexes/
├── scripts/
└── .github/
```

## 5. Device Fingerprint

Criar uma identidade normalizada para cada equipamento:

```yaml
manufacturer: huawei
category: olt
family: ma5800
model: ma5800-x7
software:
  name: smartax
  version: v100r018
firmware:
  patch: sph507
```

Exemplo Cisco:

```yaml
manufacturer: cisco
category: router
family: asr1000
model: asr1001-x
software:
  name: ios-xe
  version: 17.09.03a
```

O fingerprint deve ser usado pelo agente antes de carregar Skills específicas.

## 6. Índice principal para agentes

Criar `indexes/equipment-index.yaml` como índice de descoberta. O índice deve conter, no mínimo:

- ID canônico do equipamento;
- fabricante;
- categoria;
- família;
- modelo;
- software;
- versão;
- firmware/patch;
- capabilities;
- Skills disponíveis;
- nível de evidência;
- estado de compatibilidade.

Exemplo conceitual:

```yaml
id: huawei-ma5800-x7-v100r018-sph507
manufacturer: huawei
category: olt
family: ma5800
model: ma5800-x7
software:
  name: smartax
  version: v100r018
firmware: sph507
capabilities:
  - vlan
  - gpon
  - ont
  - gem
  - tcont
  - dba
  - service-port
skills:
  baseline: manufacturers/huawei/olt/ma5800/x7/common/baseline
  discovery: manufacturers/huawei/olt/ma5800/x7/common/discovery
compatibility:
  status: exact
  evidence: confirmed
```

## 7. Subindexação

A indexação deve ser hierárquica e incremental:

```text
Nível 0: NetMind
Nível 1: fabricante
Nível 2: categoria
Nível 3: família
Nível 4: modelo
Nível 5: software/CLI
Nível 6: versão
Nível 7: firmware/patch
Nível 8: capability
Nível 9: Skill
Nível 10: comando/procedimento/erro
```

O agente não deve ler todo o repositório para resolver uma tarefa. Deve consultar o índice e carregar somente os nós relevantes.

## 8. Compatibilidade

Compatibilidade deve ser explícita.

```yaml
compatibility:
  exact:
    - huawei.ma5800-x7.v100r018.sph507
  compatible:
    - huawei.ma5800-x7.v100r018
  unverified:
    - huawei.ma5800-x7.v100r019
  incompatible:
    - huawei.ma5800-x8
```

Nenhuma Skill deve ser aplicada automaticamente apenas porque o nome do modelo é semelhante.

## 9. Hierarquia de autoridade

Adotar esta ordem de precedência:

1. CLI real do equipamento;
2. evidência confirmada do mesmo modelo + versão + firmware;
3. resultado de discovery `?` no mesmo contexto;
4. evidência confirmada do mesmo modelo em outra versão;
5. documentação oficial;
6. inferência.

Inferência nunca deve ser apresentada ao agente como comando confirmado.

## 10. Discovery via `?`

O mecanismo de ajuda da CLI deve ser tratado como fonte de conhecimento operacional.

Uma descoberta deve registrar:

```yaml
device:
  manufacturer: huawei
  model: ma5800-x7
  version: v100r018
  patch: sph507
mode: config
input:
  command: dba-profile add profile-id 101 profile-name "..."
  help: "?"
output:
  - fix-bandwidth
  - assure-bandwidth
  - max-bandwidth
status: discovery
```

Isso permite ao agente diferenciar sintaxe comprovada de sintaxe que ainda precisa ser descoberta.

## 11. Command Registry

A atual matriz de comandos deve evoluir para registros estruturados. Cada comando deve conter:

- ID canônico;
- fabricante;
- modelo;
- software;
- versão/firmware;
- modo CLI;
- sintaxe;
- objetivo;
- parâmetros;
- risco;
- pré-requisitos;
- resultado esperado;
- evidência;
- versões compatíveis;
- comandos relacionados;
- rollback, quando aplicável.

Exemplo:

```yaml
id: huawei.ma5800.v100r018.display-version
command: display version
mode: user
purpose:
  - identify-software
  - identify-hardware
risk: read-only
evidence:
  status: confirmed
```

## 12. Error Registry

O banco de erros deve ser normalizado em registros pesquisáveis:

```yaml
id: huawei.ma5800.<error-id>
device:
  model: ma5800-x7
software:
  version: v100r018
command: <command>
error: <literal error>
meaning: <meaning>
probable_causes: []
diagnostic_commands: []
safe_actions: []
unsafe_actions: []
rollback: []
evidence:
  status: confirmed
```

Deve existir também uma área `errors/generic/` para falhas independentes do fabricante.

## 13. Capabilities

Capabilities representam conceitos operacionais e não devem substituir as implementações específicas do fabricante.

Exemplos:

- BGP;
- OSPF;
- VLAN;
- QinQ;
- PPPoE;
- RADIUS;
- NAT/CGNAT;
- QoS;
- GPON;
- ONT;
- IPv6;
- multicast;
- gerenciamento.

Uma capability pode apontar para implementações de vários fabricantes, mas cada implementação continua vinculada ao equipamento e à versão correta.

## 14. Agentes especializados

Criar uma camada explícita para agentes:

```text
agents/
├── equipment-discovery/
├── device-fingerprint/
├── skill-router/
├── cli-discovery/
├── command-selector/
├── diagnostic-engine/
├── troubleshooting/
├── change-planner/
├── rollback-planner/
└── validation/
```

Responsabilidades:

- `equipment-discovery`: identificar fabricante/modelo/software;
- `device-fingerprint`: normalizar identidade;
- `skill-router`: selecionar Skills;
- `cli-discovery`: descobrir sintaxe quando necessário;
- `command-selector`: selecionar comando compatível;
- `diagnostic-engine`: mapear sintoma → evidência → comando → próximo passo;
- `troubleshooting`: executar árvores de diagnóstico;
- `change-planner`: planejar mudanças seguras;
- `rollback-planner`: registrar retorno ao estado anterior;
- `validation`: verificar resultado pós-mudança.

## 15. Segurança operacional

As regras atuais de segurança devem ser mantidas e ampliadas.

Toda ação deve possuir uma classificação de risco, por exemplo:

- `READ_ONLY`;
- `DISCOVERY`;
- `NON_DISRUPTIVE`;
- `CHANGE`;
- `SERVICE_AFFECTING`;
- `DESTRUCTIVE`.

A execução de comandos `DESTRUCTIVE` ou potencialmente indisponibilizantes deve exigir confirmação explícita quando o fluxo do agente assim determinar.

Nenhuma Skill deve armazenar credenciais, segredos, chaves privadas ou dados de clientes.

## 16. Validação CI

O validador existente deve continuar sendo usado, mas passar a verificar também:

- fabricante válido;
- categoria válida;
- modelo válido;
- software/versão;
- firmware/patch;
- capability existente;
- Skill referenciada existente;
- comando referenciado existente;
- erro referenciado existente;
- compatibilidade coerente;
- evidência obrigatória para itens `CONFIRMADO`;
- classificação de risco;
- ausência de segredos.

Também deve existir uma validação de integridade do índice gerado.

## 17. Estratégia de migração

A migração deve preservar o conhecimento existente.

### Fase 1 — Fundação

- criar schemas;
- criar catálogo;
- criar índices;
- criar modelo de fingerprint;
- documentar arquitetura.

### Fase 2 — Huawei MA5800-X7

Migrar as Skills `01-ma5800-*` para:

```text
manufacturers/huawei/olt/ma5800/x7/
```

Preservar evidências e comandos existentes.

### Fase 3 — Cisco ASR1001-X

Migrar o conjunto existente para:

```text
manufacturers/cisco/router/asr1000/asr1001-x/
```

### Fase 4 — Registries

Criar:

- command registry;
- error registry;
- capability registry;
- compatibility matrix.

### Fase 5 — Roteamento de agentes

Implementar descoberta → fingerprint → índice → Skill Router → execução/diagnóstico.

### Fase 6 — Expansão

Adicionar progressivamente MikroTik, FiberHome, Datacom, VSOL, ZTE, Nokia, Juniper e outros fabricantes.

## 18. Prioridades

| Prioridade | Entrega |
|---|---|
| P0 | catálogo de equipamentos |
| P0 | device fingerprint |
| P0 | equipment index |
| P0 | schemas |
| P0 | separação fabricante/modelo/versão/firmware |
| P1 | migração MA5800-X7 |
| P1 | migração ASR1001-X |
| P1 | command registry |
| P1 | error registry |
| P1 | capability registry |
| P1 | compatibility matrix |
| P2 | Skill Router |
| P2 | Device Discovery Agent |
| P2 | geração automática de índices |
| P2 | validação dos índices no CI |
| P3 | expansão para novos fabricantes |
| P3 | busca semântica/vectorização, se necessária |

## 19. Critérios de aceitação da nova arquitetura

A arquitetura será considerada válida quando um agente puder:

1. receber fabricante/modelo/versão/firmware;
2. localizar o fingerprint correspondente;
3. descobrir as capabilities disponíveis;
4. selecionar somente Skills compatíveis;
5. localizar comandos confirmados;
6. diferenciar `CONFIRMADO`, `DISCOVERY`, `INFERIDO` e `DESTRUTIVO`;
7. localizar erros conhecidos;
8. seguir um procedimento de diagnóstico;
9. identificar quando precisa executar `?` para discovery;
10. rejeitar uma Skill incompatível;
11. validar o resultado de uma mudança;
12. obter informações sem carregar todo o repositório no contexto.

## 20. Pontos para debate da equipe

Antes da implementação definitiva, discutir e registrar decisão sobre:

1. árvore física versus índices gerados;
2. YAML versus JSON para catálogos e registros;
3. granularidade de versão e firmware;
4. como representar plataformas com múltiplas famílias de firmware;
5. nomenclatura canônica de fabricante/modelo;
6. se capabilities devem ser taxonomia própria ou apenas tags;
7. formato do Device Fingerprint;
8. política de evidência e expiração de evidência;
9. política para comandos descobertos via `?`;
10. quando uma evidência de outra versão pode ser reutilizada;
11. necessidade futura de busca vetorial;
12. integração com agentes externos ao Codex;
13. política de aprovação para comandos destrutivos;
14. estratégia de migração sem quebrar consumidores existentes.

## 21. Proposta de decisão

A recomendação desta auditoria é **aprovar a arquitetura em camadas e executar a migração incremental**, sem reescrever o conhecimento existente de uma vez.

O repositório deve evoluir para um **registro universal de Skills de equipamentos de rede orientado a agentes**, no qual o contexto mínimo necessário seja carregado sob demanda.

## 22. Relação com a base atual

Esta proposta aproveita diretamente os mecanismos já existentes no repositório, especialmente:

- Skills específicas por função;
- evidência operacional;
- discovery de CLI;
- matriz de comandos;
- banco de erros;
- validação estrutural;
- CI.

A migração deve ser feita por compatibilidade e preservação de conhecimento, não por descarte da base atual.
