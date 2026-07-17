#!/usr/bin/env python3
"""Initialize a non-destructive Chinese stand-up writing workspace."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


FOLDERS = ("ideas", "bits", "sets", "open-mics", "_templates")
TEMPLATES = (
    "idea-card.md",
    "bit-card.md",
    "set-script.md",
    "open-mic-review.md",
)


def initialize(target: Path, force_templates: bool = False) -> tuple[list[Path], list[Path]]:
    target = target.expanduser().resolve()
    if target == Path(target.anchor):
        raise ValueError("Refusing to initialize a filesystem root")

    created: list[Path] = []
    skipped: list[Path] = []
    target.mkdir(parents=True, exist_ok=True)

    for folder in FOLDERS:
        path = target / folder
        if not path.exists():
            path.mkdir()
            created.append(path)

    asset_dir = Path(__file__).resolve().parent.parent / "assets"
    template_dir = target / "_templates"
    for name in TEMPLATES:
        source = asset_dir / name
        destination = template_dir / name
        if destination.exists() and not force_templates:
            skipped.append(destination)
            continue
        shutil.copy2(source, destination)
        created.append(destination)

    return created, skipped


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create folders and reusable templates for Chinese stand-up writing."
    )
    parser.add_argument("target", type=Path, help="Workspace directory to initialize")
    parser.add_argument(
        "--force-templates",
        action="store_true",
        help="Replace existing files in _templates only; never touches writing folders.",
    )
    args = parser.parse_args()

    created, skipped = initialize(args.target, args.force_templates)
    print(f"Workspace ready: {args.target.expanduser().resolve()}")
    print(f"Created or updated: {len(created)}")
    print(f"Preserved existing templates: {len(skipped)}")


if __name__ == "__main__":
    main()
