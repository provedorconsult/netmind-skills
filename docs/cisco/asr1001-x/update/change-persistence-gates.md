---
fabricante: cisco
modelo: [asr1001-x]
categoria: update
topicos: [change, persistence, rollback, authorization]
descricao: "Gates de aplicação, homologação, persistência e rollback no ASR1001-X."
versao_firmware_testada: "IOS XE 17.09.03a"
ultima_atualizacao: "2026-08-15"
---

# Gates para mudança e persistência

Fonte legada: `skills/cisco-asr1001x/30-safe-change/SKILL.md`. O processo foi
refinado a partir de mudança CGNAT validada em IOS XE 17.09.03a, sem dados de
cliente.

## Sequência obrigatória

```text
SHOW → ANALISAR → VALIDAR → PROPOR → AUTORIZAR → ALTERAR → VALIDAR
→ AUTORIZAR PERSISTÊNCIA → PERSISTIR → DOCUMENTAR
```

Antes de configurar, registrar equipamento/release, causa, comandos exatos,
objetos preservados, dependências, impacto, prechecks, abort, validação e
rollback. Valores de IP, prefixo, ASN, VLAN e pool vêm do Source of Truth ou
de confirmação explícita; nunca de inferência.

## Aplicação, homologação e persistência

Alterar somente após autorização explícita, na menor unidade possível, e parar
diante de saída inesperada. Homologar com counters, estado de sessão e teste
end-to-end quando disponível.

`write memory`, `copy running-config startup-config` ou equivalente é
`[DESTRUTIVO]` e requer autorização própria. Após persistir, confirmar retorno,
validar startup-config, comparar somente linhas aprovadas e registrar evidência.

## Abort e rollback

Abortar se identidade/release divergir, baseline mudar, dependência não estiver
confirmada, houver consumidor desconhecido, rollback ficar inválido ou a CLI
rejeitar a sintaxe. O rollback deve ser específico e em ordem inversa; nunca
usar reload, clear global ou restauração ampla como rotina.
