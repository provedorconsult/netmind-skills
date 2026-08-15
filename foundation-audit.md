# G01 Foundation Audit

## Baseline inspected

- Base commit: `f5f4e41` (G11 merged into `main`).
- No `docs/` tree or root `templates/` directory existed before this Goal.
- Existing GitHub automation is limited to `validate-skills.yml`; this Goal does not add the later indexing or lint workflows.
- Existing technical content remains in its original locations. It is not copied, moved, or edited here.

## Legacy documents identified for later migration

| Source | Evidenced destination family | Treatment in G01 |
| --- | --- | --- |
| `MA5800-CLI-COMMANDS.md` and MA5800 root guides | `docs/huawei/ma5800-x7/` | Preserve in place; scaffold only. |
| `skills/cisco-asr1001x/CISCO-ASR1001X-COMMANDS.md` and package guides | `docs/cisco/asr1001-x/` | Preserve in place; scaffold only. |

## PRD alignment and intentional boundaries

- Every scaffolded model has the five PRD categories: `cli/`, `config/`, `diag/`, `mon/`, and `update/`.
- The category directories contain `.gitkeep` markers solely because Git cannot retain an empty required directory. They carry no technical content and will be replaced by atomic documents in later Goals.
- No files for manufacturer/model combinations without current repository evidence were created. The PRD lists examples such as MikroTik and Fiberhome, but this Goal does not invent model documentation.
- The PRD calls for generated `INDEX.md`, root `INDEX.md`, and `llms.txt`; those artifacts are deliberately deferred to G03, which owns `scripts/build_indexes.py`.
- The PRD describes `lint-markdown.yml` and `generate-indexes.yml`; they are deliberately deferred to G07, the CI Goal.
- The versioned harness state cannot safely store the SHA of the same commit that contains it: changing that field creates a different SHA. Runtime GitHub state reconciliation is intentionally deferred to a future dedicated Goal; G01 does not introduce a false static SHA.
