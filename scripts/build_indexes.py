#!/usr/bin/env python3
"""Build or verify deterministic AI-native documentation indexes.

Generated navigation artifacts use ``categoria: index``. This is metadata for
indexes only; operational modules remain limited to ``CATEGORIES``.
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

CATEGORIES = ("cli", "config", "diag", "mon", "update")


def frontmatter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("YAML frontmatter is not closed") from exc
    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML frontmatter: {exc.problem or 'parse error'}") from exc
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return data


def metadata(documents_root):
    records = []
    for path in sorted(documents_root.rglob("*.md")):
        if path.name == "INDEX.md":
            continue
        relative = path.relative_to(documents_root)
        deprecated = relative.parts[0] == "_deprecated"
        if len(relative.parts) < (5 if deprecated else 3):
            raise ValueError(f"{path}: expected docs/<fabricante>/<modelo>/...")
        try:
            data = frontmatter(path)
        except ValueError as exc:
            raise ValueError(f"{path}: {exc}") from exc
        required = ("fabricante", "modelo", "categoria", "topicos", "descricao")
        missing = [field for field in required if field not in data]
        if missing:
            raise ValueError(f"{path}: missing required field '{missing[0]}'")
        if data["categoria"] not in CATEGORIES:
            raise ValueError(f"{path}: categoria must be one of {', '.join(CATEGORIES)}")
        models = data["modelo"]
        if not isinstance(models, list) or not models:
            raise ValueError(f"{path}: modelo must be a non-empty list")
        if deprecated:
            if data.get("status") != "deprecated":
                raise ValueError(f"{path}: deprecated documents must set status: deprecated")
            continue
        records.append((relative.parts[0], relative.parts[1], data, path))
    return records


def model_index(vendor, model, records, root):
    lines = ["---", f"fabricante: {vendor}", f"modelo: [{model}]", "categoria: index", "topicos: [indice]", f'descricao: "Índice de {vendor} {model}."', 'versao_firmware_testada: "N/A"', 'ultima_atualizacao: "generated"', "---", "", f"# {vendor} {model}", "", "Este é um artefato de navegação; `index` não é categoria operacional.", ""]
    for category in CATEGORIES:
        lines += [f"## {category}", ""]
        items = [item for item in records if item[2]["categoria"] == category]
        if items:
            for _, _, data, path in sorted(items, key=lambda item: str(item[3])):
                link = path.relative_to(root / "docs" / vendor / model).as_posix()
                lines.append(f"- [{path.stem}]({link}) — {data['descricao']}")
        else:
            lines.append("- Nenhum módulo publicado.")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def vendor_index(vendor, models):
    lines = ["---", f"fabricante: {vendor}", "modelo: [N/A]", "categoria: index", "topicos: [indice]", f'descricao: "Índice de modelos {vendor}."', 'versao_firmware_testada: "N/A"', 'ultima_atualizacao: "generated"', "---", "", f"# {vendor}", "", "Este é um artefato de navegação; `index` não é categoria operacional.", ""]
    lines += [f"- [{model}]({model}/INDEX.md)" for model in sorted(models)]
    return "\n".join(lines).rstrip() + "\n"


def artifacts(root):
    docs = root / "docs"
    records = metadata(docs)
    pairs = {(path.parents[2].name, path.parents[1].name) for path in docs.rglob(".gitkeep")}
    pairs.update((vendor, model) for vendor, model, _, _ in records)
    by_pair = {(vendor, model): [] for vendor, model in pairs}
    for record in records:
        by_pair[(record[0], record[1])].append(record)
    output = {}
    for (vendor, model), items in sorted(by_pair.items()):
        output[docs / vendor / model / "INDEX.md"] = model_index(vendor, model, items, root)
    vendors = {}
    for vendor, model in by_pair:
        vendors.setdefault(vendor, []).append(model)
    for vendor, models in sorted(vendors.items()):
        output[docs / vendor / "INDEX.md"] = vendor_index(vendor, models)
    root_lines = ["# NetMind Skills Index", "", "## Fabricantes", ""]
    root_lines += [f"- [{vendor}](docs/{vendor}/INDEX.md)" for vendor in sorted(vendors)]
    output[root / "INDEX.md"] = "\n".join(root_lines) + "\n"
    llms = ["# NetMind Skills", "", "Documentação operacional AI-Native para equipamentos de rede.", "", "## Fabricantes", ""]
    llms += [f"- [{vendor}](docs/{vendor}/INDEX.md)" for vendor in sorted(vendors)]
    llms += ["", "## Acesso rápido por tarefa", "", "- Consulte o índice do fabricante e depois o índice do modelo para selecionar um módulo atômico."]
    output[root / "llms.txt"] = "\n".join(llms) + "\n"
    return output


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--build", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--root", default=Path(__file__).resolve().parents[1], type=Path)
    args = parser.parse_args()
    if yaml is None:
        print("ERROR: PyYAML is required to build indexes", file=sys.stderr)
        return 1
    try:
        output = artifacts(args.root)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    stale = [path for path, content in output.items() if not path.exists() or path.read_text(encoding="utf-8") != content]
    if args.check and stale:
        for path in stale:
            print(f"OUT OF DATE: {path.relative_to(args.root)}")
        return 1
    if args.build:
        for path, content in output.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    print(f"Indexes {'built' if args.build else 'verified'}: {len(output)} artifact(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
