"""Operator CLI for the read-only studio harness."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .harness import evaluate_project
from .models import StudioProject


def main() -> None:
    parser = argparse.ArgumentParser(prog="python -m studio")
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate", help="validate and evaluate a project manifest")
    validate.add_argument("manifest", type=Path)
    args = parser.parse_args()
    if args.command == "validate":
        project = StudioProject.model_validate_json(args.manifest.read_text(encoding="utf-8"))
        print(json.dumps(evaluate_project(project), indent=2, sort_keys=True))
