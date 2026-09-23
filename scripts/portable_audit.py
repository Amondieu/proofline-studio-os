"""Check the focused repo for unsafe absolute project references."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRIVE = re.compile(r"(?<![A-Za-z0-9_-])[A-Za-z]:[\\/]")


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    # LLMarena is a preserved research archive. Its report intentionally uses
    # URL-like route examples and is not an operational project manifest.
    ignored = {".git", ".venv", "node_modules", ".graphify", "__pycache__", "LLMarena"}
    for path in root.rglob("*"):
        if not path.is_file() or any(part in ignored for part in path.parts) or "tests" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue
        for line_number, line in enumerate(text.splitlines(), 1):
            if DRIVE.search(line) or line.lstrip().startswith(("/", "\\\\")):
                errors.append(f"{path.relative_to(root)}:{line_number}")
    return errors


if __name__ == "__main__":
    problems = audit()
    if problems:
        print("PORTABILITY AUDIT: FAIL")
        print("\n".join(f"- absolute reference: {item}" for item in problems))
        sys.exit(1)
    print("PORTABILITY AUDIT: PASS")
