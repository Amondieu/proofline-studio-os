#!/usr/bin/env python3
"""contrast_check.py — token-pair contrast audit for a direction token set.

Parses [data-direction="X"] token blocks from a CSS/HTML file and checks every
text pair against WCAG 2.2: 1.4.3 (4.5:1 normal text, 3:1 large) and
1.4.11 (3:1 non-text UI). Feeds QA test row T-A11Y-102.

Usage:
  python3 tools/contrast_check.py demo/direction-switcher.html
  python3 tools/contrast_check.py demo/direction-switcher.html --json
Exit code 1 if any TEXT pair fails 4.5:1.
"""
from __future__ import annotations
import argparse, json, pathlib, re, sys

# (fg token, bg token, kind, note)
PAIRS = [
    ("--ink-strong", "--bg-base", "text", "headings and body on page background"),
    ("--ink-muted", "--bg-base", "text", "muted paragraphs, meta, labels"),
    ("--ink-muted", "--card-bg", "text", "muted text inside cards"),
    ("--ink-strong", "--card-bg", "text", "headings inside cards"),
    ("--accent-ink", "--accent", "text", "button label on primary button"),
    ("--accent", "--bg-base", "ui", "accent used as BORDER/ICON only — never as body text"),
    ("--signal", "--bg-base", "ui", "focus ring / signal colour, non-text"),
]
GRADIENT_TOKENS = ["--hero-bg"]


def luminance(hex_value: str) -> float:
    h = hex_value.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"not a hex colour: {hex_value}")
    parts = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in parts]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return round((hi + 0.05) / (lo + 0.05), 2)


def parse_tokens(text: str) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for m in re.finditer(r'\[data-direction="([^"]+)"\]\s*\{(.*?)\}', text, re.S):
        name, body = m.group(1), m.group(2)
        tokens = {}
        for t in re.finditer(r"(--[\w-]+)\s*:\s*([^;]+);", body):
            tokens[t.group(1)] = t.group(2).strip()
        out[name] = tokens
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    src = pathlib.Path(a.file).read_text(encoding="utf-8")
    sets = parse_tokens(src)
    if not sets:
        print("no [data-direction] token blocks found")
        return 1
    report, failures = {}, []
    for name, tokens in sets.items():
        rows = []
        for fg, bg, kind, note in PAIRS:
            if fg not in tokens or bg not in tokens:
                continue
            value = tokens[fg]
            if not value.startswith("#"):
                continue  # rgba()/gradient values need manual handling
            r = ratio(value, tokens[bg])
            need = 4.5 if kind == "text" else 3.0
            ok = r >= need
            rows.append(dict(fg=fg, bg=bg, kind=kind, ratio=r, required=need, pass_=ok, note=note))
            if not ok and kind == "text":
                failures.append((name, fg, bg, r))
        manual = [t for t in GRADIENT_TOKENS if t in tokens]
        report[name] = dict(pairs=rows, manual_review=manual)
    if a.json:
        print(json.dumps(report, indent=2))
    else:
        for name, data in report.items():
            print(f"\n[{name}]")
            for row in data["pairs"]:
                mark = "PASS" if row["pass_"] else "FAIL"
                print(f"  {mark} {row['ratio']:>6}:1  {row['fg']} on {row['bg']} "
                      f"({row['kind']}, needs {row['required']}:1) — {row['note']}")
            if data["manual_review"]:
                print(f"  MANUAL  gradients need human verification: {', '.join(data['manual_review'])}")
        print("\nTEXT failures:", len(failures))
        if failures:
            for f in failures:
                print("  FAIL", f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
