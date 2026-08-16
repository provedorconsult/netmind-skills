# Equipment Registry

O Equipment Registry é a fonte versionada da identidade técnica de um
equipamento. Ele não declara capabilities, compatibilidade nem Skills
aplicáveis; esses contratos pertencem a registries e Goals posteriores.

- [Contrato v1](v1/SCHEMA.md)
- [Registros v1](v1/equipment-registry.yaml)

Consulte o Registry a partir de um fingerprint sanitizado. Se um campo não
estiver comprovado, mantenha-o desconhecido e faça discovery seguro ou bloqueie
a operação; nunca deduza identidade pelo caminho de uma Skill.
