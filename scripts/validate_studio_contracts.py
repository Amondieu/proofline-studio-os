"""Dependency-light structural checks for the focused studio repo."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    schema_dir = root / "schemas" / "studio"
    schema_files = sorted(schema_dir.glob("*.json")) + sorted((root / "schemas").glob("*.json"))
    if not schema_files:
        errors.append("no studio schemas found")
    for path in schema_files:
        try:
            schema = _load(path)
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(root)}: invalid JSON: {exc}")
            continue
        for field in ("$schema", "$id", "title", "type"):
            if field not in schema:
                errors.append(f"{path.relative_to(root)}: missing {field}")
        if schema.get("type") != "object":
            errors.append(f"{path.relative_to(root)}: root must be an object")

    for relative in (
        "config/studio/studio-profile.v1.json",
        "config/studio/directions.v1.json",
        "config/studio/offer-catalog.v1.json",
        "config/studio/qa-policy.v1.json",
        "config/studio/evidence-policy.v1.json",
        "config/studio/cookbook-policy.v1.json",
    ):
        path = root / relative
        try:
            data = _load(path)
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            errors.append(f"{relative}: {exc}")
            continue
        if not data.get("schemaVersion"):
            errors.append(f"{relative}: missing schemaVersion")

    manifest = root / "tests" / "fixtures" / "studio" / "blocked-project.v1.json"
    try:
        from studio.models import StudioProject

        StudioProject.model_validate(_load(manifest))
    except Exception as exc:  # intentionally surfaces the exact contract error
        errors.append(f"{manifest.relative_to(root)}: {exc}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("STUDIO CONTRACTS: FAIL")
        print("\n".join(f"- {problem}" for problem in problems))
        sys.exit(1)
    count = len(list((ROOT / "schemas/studio").glob("*.json"))) + len(list((ROOT / "schemas").glob("*.json")))
    print(f"STUDIO CONTRACTS: PASS ({count} schemas)")
