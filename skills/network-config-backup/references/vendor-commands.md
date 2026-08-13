# Comandos candidatos por plataforma

Estes comandos são candidatos de leitura, não scripts. Confirmar fabricante, modelo, versão, modo CLI e sintaxe com a skill específica e com ajuda contextual antes do uso.

## Huawei MA5800

- Configuração corrente: `[INFERIDO] display current-configuration`.
- Configuração persistida: **PENDENTE DE VALIDAÇÃO** na release real.
- Descoberta: usar `display ?` e `display current-configuration ?` no modo correto.
- `save`, exportação e transferência para servidor são mutáveis e ficam fora da coleta somente de leitura.

## Cisco ASR1001-X / IOS XE

- Configuração corrente: `[INFERIDO] show running-config`.
- Configuração persistida: `[INFERIDO] show startup-config`.
- Baseline de versão: `[INFERIDO] show version`.
- Descoberta: usar `show ?` e `show running-config ?` no modo correto.
- `copy running-config startup-config`, `write memory`, exportação e transferência para servidor são mutáveis e exigem autorização explícita.

## Plataformas sem procedimento

Não inventar sintaxe. Consultar a ajuda contextual somente quando isso for comprovadamente leitura, registrar a lacuna e propor uma extensão parametrizada desta referência ou uma skill específica da plataforma.
