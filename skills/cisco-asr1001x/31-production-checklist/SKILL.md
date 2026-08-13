---
name: 31-production-checklist
description: Validar o Cisco ASR1001-X após mudança, separar homologação de persistência e emitir aceite baseado em evidências end-to-end.
---

# Checklist de produção

## Objetivo

Emitir aceite somente quando a causa tratada, os serviços preservados e a persistência autorizada estiverem comprovados.

## Pré-requisitos

Identificar ASR1001-X, release IOS XE, baseline sanitizado, escopo da mudança, rollback e acesso alternativo.

## Checklist pós-mudança

- [ ] Identidade/release permanecem as esperadas.
- [ ] Apenas objetos autorizados mudaram.
- [ ] Interfaces/uplinks críticos estão UP.
- [ ] Rotas/FIB/CEF relevantes estão coerentes.
- [ ] BGP/OSPF permanecem estáveis quando aplicável.
- [ ] PPPoE/IPoE permanece funcional.
- [ ] AAA/RADIUS permanece funcional.
- [ ] NAT/CGNAT cria traduções esperadas e não apresenta novos drops/falhas.
- [ ] ACL/policy/QoS preservam tráfego não envolvido.
- [ ] CPU/memória sem regressão relevante.
- [ ] SSH/gestão e NAT/PAT de gerenciamento permanecem funcionais.
- [ ] Counters antes/depois comprovam forwarding bidirecional.
- [ ] Cliente final validado quando houver acesso.
- [ ] Limitações de teste explicitamente registradas quando não houver acesso ao cliente.
- [ ] Rollback ainda é executável.

## Homologação técnica versus end-to-end

É permitido homologar uma camada específica com evidência suficiente, mas não declarar “serviço end-to-end funcional” sem confirmação do cliente ou teste equivalente. Exemplo: tradução NAT + retorno ao BNG comprovam dataplane NAT, mas não substituem DNS/HTTP/HTTPS no cliente.

## Persistência

Running-config homologado não autoriza automaticamente NVRAM. Persistência exige gate explícito. Após `write memory`/`copy running-config startup-config`:

- [ ] retorno de sucesso registrado;
- [ ] startup-config contém exatamente as linhas aprovadas;
- [ ] objetos preexistentes permanecem intactos;
- [ ] evidência sanitizada publicada no Source of Truth.

## Critério de aceite

Aceitar quando:

1. a causa raiz está corrigida;
2. os counters/estado provam efeito esperado;
3. não há regressão nos objetos preservados;
4. o cliente confirmou o serviço, quando exigido;
5. a persistência, se autorizada, foi validada.

## Critério de rejeição

Rejeitar ou manter pendente diante de novos drops, falha de pool/porta, sessão degradada, diferença inesperada em startup-config, serviço de gestão quebrado ou evidência contraditória.

## Rollback

Acionar plano específico da mudança e repetir este checklist. Não usar clear/reload como primeira resposta.

## Segurança

Sanitizar credenciais, dados pessoais e identificadores sensíveis. Não versionar configuração bruta.

## Dependências

Usar com `30-safe-change` e a skill técnica específica. Para PPPoE UP sem navegação, usar `32-pppoe-up-no-navigation`.

## Fonte

- Cisco ASR1001-X / IOS XE; CLI real prevalece.
- Processo refinado por validação real de CGNAT em IOS XE 17.09.03a, sem incorporar dados específicos de cliente.
