# Matriz resumida das demandas

| Arquivo | Demanda | Prioridade | Dependência principal |
|---|---|---:|---|
| 01 | Harden Harness Merge Gate | P0 | nenhuma |
| 02 | Evidence Integrity | P0 | nenhuma |
| 03 | Compatibility Registry | P1 | Equipment Registry |
| 04 | Capability Registry | P1 | Equipment + Compatibility |
| 05 | Device Fingerprint | P1 | Equipment |
| 06 | Skill Router | P1 | 03 + 04 + 05 |
| 07 | Command Registry | P2 | arquitetura/compatibilidade |
| 08 | Error Registry | P2 | Command Registry recomendado |
| 09 | Procedure/Evidence | P2 | registries base |
| 10 | Huawei Full Migration | P2 | registries base |
| 11 | Cisco Full Migration | P2 | registries base |
| 12 | Multi-vendor Expansion | P3 | onboarding policy + registries |
| 13 | E2E AI-Native | P3 | Router funcional |
| 14 | Final Release Gate | P3 | todas obrigatórias |
| 15 | Metadata/Issues | P1 | nenhuma |
| 16 | Secret Scan Noise | P2 | nenhuma |
