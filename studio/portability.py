"""Cross-platform project-relative reference rules."""

from __future__ import annotations

import re
from pathlib import Path, PurePosixPath


_DRIVE_ABSOLUTE = re.compile(r"^[A-Za-z]:[\\/]")


class PortablePathError(ValueError):
    """Raised when a contract reference is not portable or project-bounded."""


def normalize_relative_path(reference: str | Path) -> str:
    raw = str(reference)
    if not raw:
        raise PortablePathError("project-relative path must not be empty")
    if _DRIVE_ABSOLUTE.match(raw) or raw.startswith(("/", "\\")):
        raise PortablePathError(f"path must be project-relative: {reference}")
    normalized = raw.replace("\\", "/")
    parts = PurePosixPath(normalized).parts
    if not parts or parts == (".",) or any(part in {"..", ""} for part in parts):
        raise PortablePathError(f"path traversal is not portable: {reference}")
    return "/".join(part for part in parts if part != ".")


def safe_project_path(project_root: str | Path, reference: str | Path) -> tuple[Path, str]:
    root = Path(project_root).resolve()
    normalized = normalize_relative_path(reference)
    candidate = (root / Path(*PurePosixPath(normalized).parts)).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise PortablePathError(f"path escapes project root: {reference}") from exc
    return candidate, normalized
