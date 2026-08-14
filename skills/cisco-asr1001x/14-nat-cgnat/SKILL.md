---
name: 14-nat-cgnat
description: Interpretar, planejar e validar NAT tradicional, PAT e CGNAT broadband no Cisco ASR1001-X com gates explícitos de bloco público, capacidade, rollback e persistência.
---

# NAT e CGNAT

## Objetivo

Traduzir assinantes com rastreabilidade, capacidade e preservação dos serviços existentes.

## Pré-requisitos

Usar primeiro `network-device-access`. Identificar ASR1001-X, release IOS XE, privilégio e Source of Truth. Começar em READ-ONLY e capturar baseline sanitizado de NAT, interfaces, rotas, pools, ACLs e sessões.

## Comandos candidatos

- [CONFIRMADO em IOS XE 17.09.03a] `show ip nat translations`
- [CONFIRMADO em IOS XE 17.09.03a] `show ip nat statistics`
- [INFERIDO] `show ip nat pool`
- [INFERIDO] `show access-lists`
- [DISCOVERY obrigatório antes de mudança] `ip nat ?`
- [DISCOVERY obrigatório antes de mudança] `ip nat pool ?`
- [DISCOVERY obrigatório antes de mudança] `ip nat inside source ?`

## Planejamento obrigatório

Antes de propor Dynamic PAT/CGNAT, confirmar separadamente:

1. prefixo privado real dos assinantes;
2. interface/template `inside`;
3. interface `outside` e default/upstream;
4. IPv4/bloco público autorizado pelo responsável/upstream;
5. rota de retorno desse bloco;
6. ausência de consumidor prévio do IP público candidato;
7. ACL exclusiva do serviço, evitando reutilizar classificação mais ampla sem justificativa;
8. capacidade/licenciamento/recursos aplicáveis;
9. PATs/NATs estáticos a preservar;
10. sintaxe aceita literalmente na release alvo.

Nunca inferir disponibilidade de um IPv4 público apenas porque ele existe em loopback, responde ping ou participa de PAT de gerenciamento.

## Modelo candidato de Dynamic Port Address CGN

Somente após discovery e autorização, o formato abaixo pode ser usado como candidato:

```text
ip access-list standard <SUBSCRIBER_ONLY_ACL>
 permit <SUBSCRIBER_PREFIX> <WILDCARD>
ip nat pool <PUBLIC_POOL> <FIRST_PUBLIC_IP> <LAST_PUBLIC_IP> netmask <MASK>
ip nat inside source list <SUBSCRIBER_ONLY_ACL> pool <PUBLIC_POOL> overload
```

Todo comando acima é `[HIGH-IMPACT] [DESTRUTIVO]`. Não misturar interface overload, pool overload, BPA ou outro método na mesma mudança sem novo plano.

## Validação temporal

Capturar `show ip nat statistics` e `show ip nat translations` antes e depois de tráfego controlado. Demonstrar:

- criação de traduções para o assinante esperado;
- crescimento de counters em ambos os sentidos;
- ausência de drops/falha de pool/mapping/alocação de porta;
- preservação das traduções/PATs preexistentes.

## Resultado esperado

Mudança pequena, auditável e reversível, sem alterar desnecessariamente PPPoE, rotas, interfaces, `mode cgn` ou serviços de gerenciamento.

## Rollback

Remover apenas o binding criado, depois o pool e por último a ACL, confirmando antes que cada objeto não possui outro consumidor. Não usar `clear ip nat translation *`, reload ou remoção global como rollback normal.

## Persistência

Persistir running-config é gate separado. `write memory`, `copy running-config startup-config` ou equivalente exige autorização explícita após validação funcional. Confirmar startup-config depois do save.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → AUTORIZAR PERSISTÊNCIA → PERSISTIR → DOCUMENTAR. Sanitizar credenciais e dados de assinantes. Dados reais de rede pertencem ao Source of Truth.

## O que NÃO fazer

Não inventar bloco público, não reaproveitar IP de gerenciamento por inferência, não alterar `mode cgn` durante incidente sem plano específico, não limpar traduções globalmente e não salvar antes da homologação.

## Dependências

Usar com `26-nat-troubleshooting`, `30-safe-change`, `31-production-checklist` e `32-pppoe-up-no-navigation`.

## Fonte

- Cisco ASR1001-X / IOS XE; a CLI real prevalece.
- Fluxo de Dynamic Port Address CGN documentado pela Cisco para IOS XE.
- Evidência operacional validada em IOS XE 17.09.03a sem incorporar dados específicos de cliente.
