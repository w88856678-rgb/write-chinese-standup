#!/usr/bin/env python3
"""Build a reproducible installable ZIP from the skill sources."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "write-chinese-standup"
ARCHIVE = ROOT / "dist" / "write-chinese-standup.zip"


def main() -> None:
    ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(ARCHIVE, "w", compression=ZIP_DEFLATED) as bundle:
        for path in sorted(SKILL.rglob("*")):
            if not path.is_file():
                continue
            if any(part.startswith(".") or part == "__pycache__" for part in path.relative_to(SKILL).parts):
                continue
            if path.suffix == ".pyc":
                continue
            member = ZipInfo(path.relative_to(SKILL.parent).as_posix(), (1980, 1, 1, 0, 0, 0))
            member.create_system = 3
            member.external_attr = 0o100644 << 16
            member.compress_type = ZIP_DEFLATED
            bundle.writestr(member, path.read_bytes())
    print(f"Built {ARCHIVE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
