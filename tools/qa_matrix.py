#!/usr/bin/env python3
"""Map every quality checklist item to an explicit, reviewable test row."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COOKBOOK = ROOT / "docs" / "strategy" / "31-EVIDENCE-BACKED-QUALITY-COOKBOOK.md"
REPORT = ROOT / "research" / "qa-matrix.md"


TESTS = [
    ("T-A11Y-101", "A11Y-001", "Visible focus survives keyboard navigation.", "manual"),
    ("T-A11Y-102", "A11Y-001", "Text and non-text contrast are checked for every direction.", "automated+manual"),
    ("T-A11Y-103", "A11Y-001", "Reduced motion preserves comprehension and interaction.", "manual"),
    ("T-A11Y-104", "A11Y-001", "Zoom, reflow, headings, and reading order remain usable.", "manual"),
    ("T-A11Y-105", "A11Y-001", "Accessible names describe interactive controls.", "manual"),
    ("T-A11Y-106", "A11Y-001", "Keyboard operation reaches the full primary flow.", "manual"),
    ("T-A11Y-201", "A11Y-001", "Focused targets are not hidden behind fixed or sticky UI.", "manual"),
    ("T-A11Y-202", "A11Y-001", "Interactive targets meet the 24px minimum or have a documented equivalent.", "automated+manual"),
    ("T-A11Y-203", "A11Y-001", "Drag interactions provide a non-drag alternative.", "manual"),
    ("T-A11Y-204", "A11Y-001", "Previously supplied information is not redundantly requested.", "manual"),
    ("T-A11Y-205", "A11Y-001", "Help and support mechanisms stay consistent across the flow.", "manual"),
    ("T-FORM-101", "FORM-001", "Labels, errors, success state, and submit path are tested.", "manual"),
    ("T-FORM-102", "FORM-001", "Failure and recovery paths are recorded.", "manual"),
    ("T-FORM-103", "FORM-001", "Spam protection does not block legitimate users.", "manual"),
    ("T-FORM-104", "FORM-001", "Every stored field is justified and minimised.", "manual"),
    ("T-PERF-101", "PERF-001", "LCP meets the project budget and its element is identified.", "automated"),
    ("T-PERF-102", "PERF-001", "CLS meets the project budget after a throttled scroll.", "automated"),
    ("T-PERF-103", "PERF-001", "HTML, CSS, JS, media, and third-party budgets are recorded.", "automated"),
    ("T-PERF-104", "PERF-001", "Fonts and external assets have licence and request evidence.", "automated+manual"),
    ("T-PERF-105", "PERF-001", "INP and animation-property budgets are checked.", "automated+manual"),
    ("T-PROOF-101", "TRUST-001", "Every public claim maps to substantiation or a concept label.", "manual"),
    ("T-AI-101", "AI-001", "AI assets have provenance, rights, and disclosure treatment.", "manual"),
    ("T-LEGAL-101", "SEO-003", "Legal, privacy, and accessibility pages are accurate and reachable.", "manual"),
    ("T-LEGAL-102", "SEO-002", "Structured data does not create invisible or self-serving proof.", "automated+manual"),
    ("T-OPS-101", "OPS-001", "Client ownership of accounts and delivery systems is verified.", "manual"),
    ("T-OPS-102", "OPS-002", "A second person can reproduce the receipt and rollback is rehearsed.", "manual"),
    ("T-OUT-101", "docs/30 §E", "All nine send-gate rows are true for the exact message.", "manual"),
    ("T-OUT-102", "docs/30 §F", "Sequence limits and immediate permanent opt-out suppression hold.", "manual"),
]

CHECKLIST_ITEM_TO_TEST = {
    1: "T-A11Y-202",
    2: "T-A11Y-201",
    3: "T-A11Y-203",
    4: "T-A11Y-205",
    5: "T-A11Y-204",
    6: "T-A11Y-103",
    7: "T-PERF-104",
    8: "T-PERF-102",
    9: "T-PERF-103",
    10: "T-FORM-101",
    11: "T-PROOF-101",
    12: "T-LEGAL-102",
    13: "T-LEGAL-101",
    14: "T-AI-101",
    15: "T-OPS-101",
    16: "T-OPS-102",
}


def parse_checklist() -> dict[int, str]:
    text = COOKBOOK.read_text(encoding="utf-8")
    block = re.search(r"## 5\. Must-pass launch checklist.*?```(.*?)```", text, re.S)
    if not block:
        return {}
    return {
        int(match.group(1)): match.group(2).strip()
        for line in block.group(1).splitlines()
        if (match := re.match(r"\s*\[ \]\s*(\d+)\s+(.*)", line))
    }


def check() -> int:
    checklist = parse_checklist()
    test_ids = {row[0] for row in TESTS}
    problems: list[str] = []
    if set(checklist) != set(range(1, 17)):
        problems.append(f"expected checklist items 1–16, found {sorted(checklist)}")
    for item, test_id in CHECKLIST_ITEM_TO_TEST.items():
        if item not in checklist:
            problems.append(f"checklist item {item} is missing")
        if test_id not in test_ids:
            problems.append(f"checklist item {item} references unknown test {test_id}")
    if len(TESTS) != 28:
        problems.append(f"expected 28 test rows, found {len(TESTS)}")
    if problems:
        print("QA MATRIX: FAIL")
        print("\n".join(f"- {problem}" for problem in problems))
        return 1
    print("checklist items parsed: 16")
    print("items without a test row: none")
    print("rows referencing unknown tests: none")
    print("RESULT: OK")
    return 0


def markdown() -> str:
    lines = [
        "# QA matrix",
        "",
        "Generated from `docs/strategy/31-EVIDENCE-BACKED-QUALITY-COOKBOOK.md`.",
        "A row is evidence for human review; it is not launch authority.",
        "",
        "| Test ID | Card / source | Check | Mode |",
        "|---|---|---|---|",
    ]
    lines.extend(f"| `{test_id}` | `{card}` | {check} | {mode} |" for test_id, card, check, mode in TESTS)
    lines.extend(["", "## Checklist mapping", "", "| Item | Test |", "|---:|---|"])
    lines.extend(f"| {item} | `{test_id}` |" for item, test_id in CHECKLIST_ITEM_TO_TEST.items())
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate the checklist mapping")
    parser.add_argument("--json", action="store_true", help="print the rows as JSON")
    args = parser.parse_args()
    if args.check:
        return check()
    if args.json:
        print(json.dumps([dict(id=a, card=b, check=c, mode=d) for a, b, c, d in TESTS], indent=2))
        return 0
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(markdown(), encoding="utf-8")
    print(f"wrote {REPORT.relative_to(ROOT)} ({len(TESTS)} tests)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
