---
fabricante: huawei
modelo: [ma5800-x7]
categoria: update
topicos: [rollback, change, abort, validation]
descricao: "Prechecks e ordem de rollback para mudanças autorizadas na MA5800-X7."
versao_firmware_testada: "MA5800V100R018 / SPH507"
ultima_atualizacao: "2026-08-15"
---

# Prechecks de rollback

Fonte legada: `ROLLBACK-CHECKLIST.md`. Este procedimento se aplica somente a
uma mudança autorizada e não fornece sintaxe de remoção.

## Antes da janela

- Definir critério de abort.
- Capturar displays e parâmetros completos do estado anterior.
- Mapear referências e Binding times.
- Confirmar que nenhum objeto é default ou compartilhado.
- Validar sintaxe reversa com `?`.
- Obter autorização explícita para comandos `[DESTRUTIVO]`.
- Garantir acesso de gestão ou out-of-band.

## Reversão e parada

Reverter na ordem inversa da criação. Para o baseline de bancada informado,
remover WAN route/PPPoE somente com sintaxe validada e restaurar o baseline
bridge da ONT. Parar ao primeiro erro de rollback e reconsultar o estado.

## Pós-validação

Validar ONT, service-port, VLAN, uplink, PPPoE e gestão. Registrar resultado e
objetos residuais. Nunca improvisar `delete` ou `undo`.
