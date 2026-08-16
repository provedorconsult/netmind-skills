"""G08 coverage for repository entrypoint and contribution guidance."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")


class EntrypointDocumentationTests(unittest.TestCase):
    def test_readme_explains_ai_native_navigation(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for required in ("llms.txt", "INDEX.md", "fabricante → modelo → categoria", "YAML Frontmatter", "kebab-case", "150 linhas"):
            self.assertIn(required, readme)

    def test_contributing_documents_real_validation_and_gate(self):
        contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        for command in ("harness-validate.sh", "validate_repository.py", "build_indexes.py --check", "lint_markdown.py", "validate_markdown_links.py"):
            self.assertIn(command, contributing)
        self.assertIn("CI verde **não** autoriza merge", contributing)
        self.assertIn("comentário social literal\n`approve`", contributing)

    def test_entrypoint_links_are_local_and_valid(self):
        for filename in ("README.md", "CONTRIBUTING.md"):
            document = ROOT / filename
            for target in LINK.findall(document.read_text(encoding="utf-8")):
                if target.startswith(("http://", "https://", "#")):
                    continue
                self.assertTrue((document.parent / target).exists(), f"{filename}: {target}")


if __name__ == "__main__":
    unittest.main()
