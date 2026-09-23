#!/usr/bin/env python3
"""Small, dependency-free contrast audit for the Proofline direction tokens."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PAIRS = [
    ("--text", "--bg", "text", "body and headings on the page background"),
    ("--muted", "--bg", "text", "muted copy on the page background"),
    ("--text", "--surface", "text", "headings inside cards"),
    ("--muted", "--surface", "text", "muted copy inside cards"),
    ("--accent-ink", "--accent", "text", "primary button label"),
    ("--accent", "--bg", "ui", "accent borders, icons, and focus signals"),
]


def luminance(value: str) -> float:
    raw = value.strip().lstrip("#")
    if len(raw) == 3:
        raw = "".join(char * 2 for char in raw)
    if len(raw) != 6:
        raise ValueError(f"not a six-digit hex colour: {value}")
    channels = [int(raw[index:index + 2], 16) / 255 for index in (0, 2, 4)]
    linear = [channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4 for channel in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def ratio(foreground: str, background: str) -> float:
    first, second = luminance(foreground), luminance(background)
    return round((max(first, second) + 0.05) / (min(first, second) + 0.05), 2)


def parse_tokens(text: str) -> dict[str, dict[str, str]]:
    token_sets: dict[str, dict[str, str]] = {"root": {}}
    for match in re.finditer(r"(:root|html\[data-direction=\"([^\"]+)\"\])\s*\{([^{}]*)\}", text, re.S):
        name = match.group(2) or "root"
        token_sets[name] = {
            key: value.strip()
            for key, value in re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", match.group(3))
        }
    root = token_sets.get("root", {})
    for name in list(token_sets):
        if name != "root":
            merged = dict(root)
            merged.update(token_sets[name])
            token_sets[name] = merged
    return token_sets


def audit(path: Path) -> tuple[dict[str, list[dict[str, object]]], list[tuple[str, str, str, float]]]:
    token_sets = parse_tokens(path.read_text(encoding="utf-8"))
    failures: list[tuple[str, str, str, float]] = []
    report: dict[str, list[dict[str, object]]] = {}
    for direction, tokens in token_sets.items():
        rows: list[dict[str, object]] = []
        for foreground, background, kind, note in PAIRS:
            if foreground not in tokens or background not in tokens:
                continue
            if not tokens[foreground].startswith("#") or not tokens[background].startswith("#"):
                continue
            measured = ratio(tokens[foreground], tokens[background])
            required = 4.5 if kind == "text" else 3.0
            passed = measured >= required
            rows.append({"foreground": foreground, "background": background, "kind": kind, "ratio": measured, "required": required, "pass": passed, "note": note})
            if kind == "text" and not passed:
                failures.append((direction, foreground, background, measured))
        report[direction] = rows
    return report, failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report, failures = audit(args.file)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for direction, rows in report.items():
            print(f"\n[{direction}]")
            for row in rows:
                mark = "PASS" if row["pass"] else "FAIL"
                print(f"  {mark} {row['ratio']:>5}:1 {row['foreground']} on {row['background']} ({row['kind']}; needs {row['required']}:1) — {row['note']}")
        print(f"\nTEXT failures: {len(failures)}")
        for failure in failures:
            print("  FAIL", failure)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
