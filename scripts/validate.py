#!/usr/bin/env python3
"""Validate the distributable skill without depending on a local Codex install."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    sys.exit("ERROR: install development dependencies: pip install -r requirements-dev.txt")


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "__pycache__", "outputs", "tmp", "raw"}
REQUIRED = (
    "SKILL.md", "references/intake.md",
    "references/output.md", "references/source-notes.md", "README.md",
    "LICENSE", "CONTRIBUTING.md", "evals/scenarios.md",
)
LANGUAGE_PAIRS = (
    ("SKILL.md", "SKILL.en.md"),
    ("README.md", "README.en.md"),
    ("CONTRIBUTING.md", "CONTRIBUTING.en.md"),
    ("references/intake.md", "references/intake.en.md"),
    ("references/output.md", "references/output.en.md"),
    ("references/source-notes.md", "references/source-notes.en.md"),
    ("evals/scenarios.md", "evals/scenarios.en.md"),
)
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".txt", ".py"}
LOCAL_PATH = re.compile(r"/(?:Users|home)/[A-Za-z0-9_.-]+/|[A-Za-z]:\\Users\\")
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")


def validate(root: Path) -> list[str]:
    errors = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")
    for pair in LANGUAGE_PAIRS:
        for relative in pair:
            if not (root / relative).is_file():
                errors.append(f"missing bilingual counterpart: {relative}")

    def load_yaml(path: Path):
        try:
            value = yaml.safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(value, dict):
                raise ValueError("expected a mapping")
            return value
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            return {}

    skill = root / "SKILL.md"
    if skill.is_file():
        content = skill.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
        if not match:
            errors.append("SKILL.md: missing YAML frontmatter")
        else:
            try:
                metadata = yaml.safe_load(match.group(1))
                if not isinstance(metadata, dict):
                    raise ValueError("expected a mapping")
                if metadata.get("name") != "tech-plan":
                    errors.append("SKILL.md: name must be tech-plan")
                description = metadata.get("description")
                if not isinstance(description, str) or not description.strip():
                    errors.append("SKILL.md: description must be a nonempty string")
            except (ValueError, yaml.YAMLError) as exc:
                errors.append(f"SKILL.md: invalid frontmatter: {exc}")

    metadata_path = root / "agents/openai.yaml"
    if metadata_path.is_file():
        metadata = load_yaml(metadata_path)
        interface = metadata.get("interface")
        if not isinstance(interface, dict):
            errors.append("agents/openai.yaml: interface must be a mapping")
        else:
            for field in ("display_name", "short_description", "default_prompt"):
                if not isinstance(interface.get(field), str) or not interface[field].strip():
                    errors.append(f"agents/openai.yaml: missing interface.{field}")
            prompt = interface.get("default_prompt", "")
            if isinstance(prompt, str) and "$tech-plan" not in prompt:
                errors.append("agents/openai.yaml: default_prompt must mention $tech-plan")

    # Prune local and generated directories before visiting their contents.
    import os
    for directory, dirs, names in os.walk(root):
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
        for name in names:
            path = Path(directory) / name
            relative = path.relative_to(root)
            if path.is_symlink():
                errors.append(f"{relative}: distribution must not rely on symlinks")
                continue
            if path.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".zip"}:
                errors.append(f"{relative}: unexpected binary/source artifact")
            if path.suffix not in TEXT_SUFFIXES:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                errors.append(f"{relative}: cannot read UTF-8 text: {exc}")
                continue
            if LOCAL_PATH.search(text):
                errors.append(f"{relative}: contains a personal absolute path")
            if path.suffix != ".md":
                continue
            for target in LINK.findall(text):
                target = target.strip().strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                resolved = (path.parent / unquote(parsed.path)).resolve()
                if not resolved.is_relative_to(root.resolve()):
                    errors.append(f"{relative}: link escapes repository: {target}")
                elif not resolved.exists():
                    errors.append(f"{relative}: broken local link: {target}")
    return errors


if __name__ == "__main__":
    problems = validate(ROOT)
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}", file=sys.stderr)
        sys.exit(1)
    print("OK: skill metadata, bilingual files, local links and distribution hygiene")
