#!/usr/bin/env python3
"""Audit a generated prompt for exact-line repetition and approximate token cost.

Usage:
  python prompt_audit.py current.txt
  python prompt_audit.py current.txt previous.txt

No external dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

MIN_LINE_LEN = 18


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def normalize_line(line: str) -> str:
    line = re.sub(r"[`*_>#\-]+", " ", line.lower())
    return re.sub(r"\s+", " ", line).strip(" .:;")


def meaningful_lines(text: str) -> set[str]:
    result: set[str] = set()
    for raw in text.splitlines():
        line = normalize_line(raw)
        if len(line) >= MIN_LINE_LEN:
            result.add(line)
    return result


def approximate_tokens(text: str) -> int:
    # Practical rough estimate for mixed English/Arabic prompts.
    chars = len(text)
    words = len(re.findall(r"\S+", text))
    return max(round(chars / 4), round(words * 1.35))


def internal_duplicates(text: str) -> list[str]:
    seen: set[str] = set()
    duplicates: list[str] = []
    for raw in text.splitlines():
        line = normalize_line(raw)
        if len(line) < MIN_LINE_LEN:
            continue
        if line in seen and line not in duplicates:
            duplicates.append(line)
        seen.add(line)
    return duplicates


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print("Usage: python prompt_audit.py current.txt [previous.txt]")
        return 2

    current = read(sys.argv[1])
    current_lines = meaningful_lines(current)
    duplicates = internal_duplicates(current)

    print(f"Approximate tokens: {approximate_tokens(current)}")
    print(f"Meaningful lines: {len(current_lines)}")
    print(f"Internal duplicate lines: {len(duplicates)}")

    for line in duplicates[:20]:
        print(f"  DUPLICATE: {line}")

    if len(sys.argv) == 3:
        previous = read(sys.argv[2])
        overlap = sorted(current_lines & meaningful_lines(previous))
        denominator = max(1, len(current_lines))
        ratio = len(overlap) / denominator
        print(f"Exact-line overlap with previous: {len(overlap)} ({ratio:.1%})")
        for line in overlap[:20]:
            print(f"  REPEATED: {line}")

    forbidden = [
        r"create (an? )?(implementation )?plan",
        r"create (an? )?roadmap",
        r"think step by step",
        r"status[-_ ]?2\.md",
    ]
    hits: list[str] = []
    for raw in current.splitlines():
        line = raw.strip()
        lower = line.lower()
        negated = any(phrase in lower for phrase in (
            "do not create", "don't create", "must not create",
            "never create", "without creating", "no plan", "no roadmap",
        ))
        for pattern in forbidden:
            if re.search(pattern, line, re.I) and not negated:
                hits.append(f"{pattern} :: {line}")

    print(f"Forbidden-pattern hits: {len(hits)}")
    for hit in hits:
        print(f"  FORBIDDEN: {hit}")

    return 1 if duplicates or hits else 0


if __name__ == "__main__":
    raise SystemExit(main())
