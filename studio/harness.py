"""Read-only gate evaluation and explicit human gate recording.

The evaluator is intentionally conservative. It can show exactly why a project
is blocked, but no evaluation result grants launch authority.
"""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .models import StudioProject


REQUIRED_VIEWPORTS = {"360", "390", "768", "1024", "1440"}
REQUIRED_BUILD_CHECKS = (
    "navigation_works",
    "ctas_route_correctly",
    "form_validation_works",
    "form_delivery_tested",
    "calendar_or_secondary_flow_tested",
    "metadata_present",
    "open_graph_present",
    "alt_text_reviewed",
    "privacy_and_legal_links_present",
    "analytics_consent_configured",
    "assets_rights_confirmed",
    "no_fabricated_claims",
    "client_admin_access_ready",
    "backup_export_supplied",
)


def _result(gate_id: str, passed: bool, reasons: list[str] | None = None) -> dict[str, Any]:
    return {"gateId": gate_id, "passed": passed, "reasons": reasons or []}


def evaluate_project(project: StudioProject) -> dict[str, Any]:
    """Return a deterministic, non-authoritative project readiness report."""

    discovery_reasons: list[str] = []
    if not project.discovery.proof:
        discovery_reasons.append("no client-approved proof is recorded")
    if project.discovery.assumption_map:
        discovery_reasons.append("assumptions remain unresolved")
    discovery = _result("discovery", not discovery_reasons, discovery_reasons)

    message_reasons: list[str] = []
    if project.message_map is None:
        message_reasons.append("message map is missing")
    else:
        if not project.message_map.client_signoff:
            message_reasons.append("client message sign-off is missing")
        if project.message_map.assumptions_to_confirm:
            message_reasons.append("message assumptions remain unresolved")
    message = _result("message", not message_reasons, message_reasons)

    direction_reasons: list[str] = []
    if project.design_direction is None:
        direction_reasons.append("design direction is missing")
    else:
        if not project.design_direction.selected_by_client:
            direction_reasons.append("client has not selected a direction")
        if not project.design_direction.mobile_preview_reviewed:
            direction_reasons.append("mobile direction preview is not reviewed")
    direction = _result("direction", not direction_reasons, direction_reasons)

    build_reasons: list[str] = []
    if project.build is None:
        build_reasons.append("build checklist is missing")
    else:
        missing_viewports = REQUIRED_VIEWPORTS.difference(project.build.responsive_viewports)
        if missing_viewports:
            build_reasons.append("missing responsive checks: " + ", ".join(sorted(missing_viewports)))
        for field in REQUIRED_BUILD_CHECKS:
            if not getattr(project.build, field):
                build_reasons.append(f"build check is incomplete: {field}")
    build = _result("build", not build_reasons, build_reasons)

    launch_reasons: list[str] = []
    review = project.launch_review
    if review is None:
        launch_reasons.append("launch review is missing")
    else:
        for field, label in (
            ("mobile_conversion_pass", "mobile conversion test"),
            ("technical_pass", "technical test"),
            ("trust_pass", "trust test"),
            ("legal_pass", "legal test"),
        ):
            if not getattr(review, field):
                launch_reasons.append(f"{label} has not passed")
        if not review.reviewer:
            launch_reasons.append("human reviewer is missing")
        if not review.client_approval:
            launch_reasons.append("client launch approval is missing")
    launch = _result("launch", not launch_reasons, launch_reasons)

    gates = [discovery, message, direction, build, launch]
    blocked = [gate["gateId"] for gate in gates if not gate["passed"]]
    return {
        "schemaVersion": "studio.harness-report.v1",
        "projectId": project.project_id,
        "readOnly": True,
        "authoritative": False,
        "launchAuthority": False,
        "gates": gates,
        "blockedGates": blocked,
        "readyForHumanLaunchReview": not blocked,
        "readyToLaunch": False,
        "limitations": [
            "The report checks submitted evidence only; it does not verify truth or rights.",
            "A passing report cannot publish, deploy, approve, or change client systems.",
            "Legal sufficiency remains a human/client responsibility.",
        ],
    }


def record_human_gate(
    ledger_path: str | Path,
    *,
    project_id: str,
    gate_id: str,
    decision: str,
    actor: str,
    rationale: str,
    recorded_at: datetime | None = None,
) -> dict[str, Any]:
    """Append one explicit human decision to a hash-chained local ledger."""

    if not actor.strip():
        raise ValueError("human actor is required")
    if not rationale.strip():
        raise ValueError("rationale is required")
    if decision not in {"approved", "blocked", "superseded"}:
        raise ValueError("decision must be approved, blocked, or superseded")
    path = Path(ledger_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    previous_hash = "sha256:" + "0" * 64
    if path.exists():
        lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if lines:
            previous = json.loads(lines[-1])
            previous_hash = previous["recordHash"]
    payload = {
        "schemaVersion": "studio.human-gate-record.v1",
        "projectId": project_id,
        "gateId": gate_id,
        "decision": decision,
        "actor": actor,
        "rationale": rationale,
        "recordedAt": (recorded_at or datetime.now(UTC)).isoformat(),
        "previousHash": previous_hash,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["recordHash"] = "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, sort_keys=True) + "\n")
    return payload
