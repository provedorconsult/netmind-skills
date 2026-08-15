---
fabricante: cisco
modelo: [asr1001-x]
categoria: mon
topicos: [cpu, memory, platform, monitoring]
descricao: "Observação de CPU, memória e recursos de plataforma no ASR1001-X."
versao_firmware_testada: "N/A"
ultima_atualizacao: "2026-08-15"
---

# Observação de CPU e memória

Fonte legada: `skills/cisco-asr1001x/23-cpu-memory/SKILL.md`. A fonte não
informa versão real do equipamento; os comandos permanecem `[INFERIDO]` até
serem aceitos na CLI do alvo.

## Consultas candidatas

```text
show processes cpu
show processes cpu sorted
show processes memory
show memory statistics
show platform resources
```

## Interpretação

Registrar janela e uptime; correlacionar processo com BGP, NAT, QoS, PPPoE,
CEF ou ataque. Quando a release oferecer comandos, comparar control plane e
data plane. Diferenciar pico transitório, saturação sustentada, leak e pressão
de forwarding usando estado e contadores.

## Limites

Comandos detalhados ou debug podem elevar carga; não executar debug sem plano.
Este módulo é somente leitura: não matar processo nem usar reload.
