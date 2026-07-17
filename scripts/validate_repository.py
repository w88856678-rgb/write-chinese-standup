#!/usr/bin/env python3
"""Validate the public write-chinese-standup repository without dependencies."""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "write-chinese-standup"

REQUIRED_FILES = (
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "CHANGELOG.md",
    ROOT / "CONTRIBUTING.md",
    SKILL / "SKILL.md",
    SKILL / "LICENSE",
    SKILL / "agents" / "openai.yaml",
    SKILL / "assets" / "idea-card.md",
    SKILL / "assets" / "bit-card.md",
    SKILL / "assets" / "set-script.md",
    SKILL / "assets" / "open-mic-review.md",
    SKILL / "references" / "craft.md",
    SKILL / "references" / "performance-markup.md",
    SKILL / "references" / "provenance.md",
    SKILL / "scripts" / "init_standup_workspace.py",
    SKILL / "scripts" / "estimate_duration.py",
)


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def validate_required_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))


def validate_skill_frontmatter() -> None:
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    frontmatter = match.group(1)
    name = re.search(r"^name:\s*(.+)$", frontmatter, flags=re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", frontmatter, flags=re.MULTILINE)
    if not name or name.group(1).strip() != "write-chinese-standup":
        fail("SKILL.md name must be write-chinese-standup")
    if not description or len(description.group(1).strip()) < 40:
        fail("SKILL.md description is missing or too short")

    extra_keys = []
    for line in frontmatter.splitlines():
        if line and not line.startswith(" ") and ":" in line:
            key = line.split(":", 1)[0].strip()
            if key not in {"name", "description"}:
                extra_keys.append(key)
    if extra_keys:
        fail("unsupported SKILL.md frontmatter keys: " + ", ".join(extra_keys))


def validate_agent_metadata() -> None:
    text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
    for key in ("display_name:", "short_description:", "default_prompt:"):
        if key not in text:
            fail(f"agents/openai.yaml is missing {key}")
    if "$write-chinese-standup" not in text:
        fail("agents/openai.yaml default_prompt must mention the skill")


def validate_clean_tree() -> None:
    forbidden_names = {".DS_Store", "__pycache__"}
    bad = []
    for path in ROOT.rglob("*"):
        if path.name in forbidden_names or path.name.startswith("._") or path.suffix == ".pyc":
            bad.append(str(path.relative_to(ROOT)))
    if bad:
        fail("generated or macOS files found: " + ", ".join(bad))

    text_suffixes = {".md", ".py", ".yaml", ".yml", ".txt"}
    personal_paths = []
    personal_prefix = "/" + "Users" + "/"
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in text_suffixes:
            text = path.read_text(encoding="utf-8")
            if personal_prefix in text:
                personal_paths.append(str(path.relative_to(ROOT)))
    if personal_paths:
        fail("absolute personal paths found: " + ", ".join(personal_paths))


def validate_python_sources() -> None:
    for path in ROOT.rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        try:
            compile(source, str(path), "exec")
        except SyntaxError as exc:
            fail(f"Python syntax error in {path.relative_to(ROOT)}: {exc}")


def validate_scripts() -> None:
    duration_script = SKILL / "scripts" / "estimate_duration.py"
    workspace_script = SKILL / "scripts" / "init_standup_workspace.py"

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        sample = temp / "sample.md"
        sample.write_text("这是一个测试。// 然后事情变得更奇怪。///", encoding="utf-8")
        duration = subprocess.run(
            [sys.executable, str(duration_script), str(sample), "--json"],
            check=True,
            capture_output=True,
            text=True,
        )
        if '"estimated_minutes"' not in duration.stdout:
            fail("duration estimator did not return JSON output")

        workspace = temp / "workspace"
        subprocess.run(
            [sys.executable, str(workspace_script), str(workspace)],
            check=True,
            capture_output=True,
            text=True,
        )
        for folder in ("ideas", "bits", "sets", "open-mics", "_templates"):
            if not (workspace / folder).is_dir():
                fail(f"workspace initializer did not create {folder}")


def validate_distribution() -> None:
    archive = ROOT / "dist" / "write-chinese-standup.zip"
    if not archive.exists():
        return
    with zipfile.ZipFile(archive) as bundle:
        names = bundle.namelist()
        if not names:
            fail("distribution archive is empty")
        for name in names:
            path = Path(name)
            if path.is_absolute() or ".." in path.parts:
                fail(f"unsafe archive member: {name}")
            if path.parts and path.parts[0] != "write-chinese-standup":
                fail(f"archive member has wrong top-level folder: {name}")
            if any(part == ".DS_Store" or part.startswith("._") for part in path.parts):
                fail(f"macOS metadata found in archive: {name}")


def main() -> None:
    validate_required_files()
    validate_skill_frontmatter()
    validate_agent_metadata()
    validate_clean_tree()
    validate_python_sources()
    validate_scripts()
    validate_distribution()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
