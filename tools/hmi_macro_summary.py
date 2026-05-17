#!/usr/bin/env python3
"""Summarize HMI macro text files.

This helper is intentionally conservative: it does not execute macros. It only
counts lines, non-empty lines, and likely command-like statements.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def summarize(path: Path) -> str:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    non_empty = [line for line in lines if line.strip()]
    command_like = [line for line in non_empty if not line.lstrip().startswith(("#", "//", ";"))]
    return f"{path.name:24} lines={len(lines):4d} non_empty={len(non_empty):4d} command_like={len(command_like):4d}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize HMI macro text files.")
    parser.add_argument("paths", nargs="*", type=Path, default=list(Path.cwd().glob("*.txt")))
    args = parser.parse_args()

    if not args.paths:
        print("No macro text files found.")
        return 1

    for path in args.paths:
        if path.exists():
            print(summarize(path))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())