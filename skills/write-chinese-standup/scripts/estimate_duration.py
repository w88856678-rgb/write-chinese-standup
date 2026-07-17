#!/usr/bin/env python3
"""Estimate spoken duration for a marked-up Chinese stand-up script."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


HAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
LATIN_WORD_RE = re.compile(r"\b[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*\b")
CUE_RE = re.compile(r"\[[^\]\n]+\]")


def estimate(text: str, cpm: float, wpm: float) -> dict[str, float | int]:
    uncued = CUE_RE.sub("", text)
    long_holds = uncued.count("///")
    without_long = uncued.replace("///", "")
    beats = without_long.count("//")
    without_beats = without_long.replace("//", "")
    short_pauses = without_beats.count("/")
    clean = without_beats.replace("/", "")

    han_chars = len(HAN_RE.findall(clean))
    latin_words = len(LATIN_WORD_RE.findall(clean))
    speech_seconds = han_chars / cpm * 60 + latin_words / wpm * 60
    marked_pause_seconds = long_holds * 1.4 + beats * 0.65 + short_pauses * 0.3
    total_seconds = speech_seconds + marked_pause_seconds

    return {
        "han_characters": han_chars,
        "latin_words": latin_words,
        "short_pauses": short_pauses,
        "beat_pauses": beats,
        "laugh_holds": long_holds,
        "estimated_seconds": round(total_seconds, 1),
        "estimated_minutes": round(total_seconds / 60, 2),
        "likely_range_minutes": [
            round(total_seconds / 60 * 0.9, 2),
            round(total_seconds / 60 * 1.25, 2),
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("script", type=Path, help="UTF-8 text or Markdown script")
    parser.add_argument("--cpm", type=float, default=210.0, help="Chinese characters per minute")
    parser.add_argument("--wpm", type=float, default=145.0, help="Latin words per minute")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    if args.cpm <= 0 or args.wpm <= 0:
        parser.error("--cpm and --wpm must be positive")
    result = estimate(args.script.read_text(encoding="utf-8"), args.cpm, args.wpm)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print(f"Estimated duration: {result['estimated_minutes']} minutes")
    low, high = result["likely_range_minutes"]
    print(f"Likely live range: {low}–{high} minutes")
    print(
        "Counted "
        f"{result['han_characters']} Chinese characters, "
        f"{result['latin_words']} Latin words, "
        f"and {result['laugh_holds']} laugh holds."
    )


if __name__ == "__main__":
    main()
