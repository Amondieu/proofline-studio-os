"""Operator CLI for the read-only studio harness."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .harness import evaluate_project
from .laya import LayaAdvisoryEngine, LayaModel, LayaPackageAdapter, LayaRequest, LayaUnavailableError
from .models import StudioProject


def main() -> None:
    parser = argparse.ArgumentParser(prog="python -m studio")
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate", help="validate and evaluate a project manifest")
    validate.add_argument("manifest", type=Path)
    laya_run = subparsers.add_parser(
        "laya-run",
        help="run an optional Laya advisory request; output never authorizes an action",
    )
    laya_run.add_argument("request", type=Path, help="path to a studio.laya-request.v1 JSON file")
    laya_run.add_argument("--device", default=None, help="optional torch device passed to Laya")
    laya_run.add_argument("--max-loaded", type=int, default=1)
    laya_run.add_argument("--preload", action="store_true")
    laya_run.add_argument("--abstain-below", type=float, default=0.75)
    args = parser.parse_args()
    if args.command == "validate":
        project = StudioProject.model_validate_json(args.manifest.read_text(encoding="utf-8"))
        print(json.dumps(evaluate_project(project), indent=2, sort_keys=True))
    elif args.command == "laya-run":
        request = LayaRequest.model_validate_json(args.request.read_text(encoding="utf-8"))
        try:
            adapter = LayaPackageAdapter(
                model=request.requested_model or LayaModel.english,
                device=args.device,
                max_loaded=args.max_loaded,
                preload=args.preload,
            )
        except LayaUnavailableError as exc:
            parser.error(str(exc))
        decision = LayaAdvisoryEngine(adapter, abstain_below=args.abstain_below).advise(request)
        print(decision.model_dump_json(indent=2))
