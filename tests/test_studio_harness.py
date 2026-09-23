import json
import tempfile
import unittest
from datetime import UTC, datetime
from pathlib import Path

from studio.harness import evaluate_project, record_human_gate
from studio.models import (
    BuildChecklist,
    DesignDirection,
    DiscoveryBrief,
    LaunchReview,
    MessageMap,
    StudioProject,
)
from studio.portability import PortablePathError, normalize_relative_path


def make_project() -> StudioProject:
    return StudioProject(
        project_id="studio_test_ready",
        client_slug="test-client",
        current_stage="launch",
        discovery=DiscoveryBrief(
            company_name="Test Systems",
            market="B2B workflow software",
            offer="A workflow system that reduces manual handoffs for growing teams.",
            average_order_value="€2,000 annual contract",
            target_buyer="Operations leaders at growing B2B teams with repeated manual handoffs.",
            buying_situation="The team has outgrown spreadsheets and needs a reliable workflow.",
            expensive_problem="Manual handoffs create delays and unclear ownership.",
            current_alternatives=["Spreadsheets"],
            buyer_hesitations=["Implementation effort"],
            primary_conversion="Book a workflow audit",
            tone_of_voice=["precise", "calm"],
            proof=["Client supplied case study reference CASE-001"],
        ),
        message_map=MessageMap(
            target_audience="Operations leaders at growing B2B teams.",
            primary_job_to_be_done="Replace fragile manual handoffs with a dependable workflow.",
            core_pain="Important work gets delayed because no one can see ownership.",
            desired_outcome="Teams know what happens next and follow-ups do not disappear.",
            mechanism="The system gives every handoff a clear owner, status, and next action.",
            primary_promise="Make every operational handoff visible and actionable.",
            primary_cta="Book a workflow audit",
            proof=["Client supplied case study reference CASE-001"],
            top_objections=["Setup effort", "Migration risk", "Budget"],
            required_sections=["Hero", "Problem", "Mechanism", "Proof", "Process", "CTA"],
            client_signoff=True,
            signed_off_by="client@example.test",
            signed_off_at=datetime(2026, 9, 23, tzinfo=UTC),
        ),
        design_direction=DesignDirection(
            direction_id="precision",
            label="Precision System",
            intended_audience="B2B software buyers who value clarity and control.",
            visual_principle="A structured signal path makes complex operations legible.",
            palette=["#f6f4ef", "#151515", "#165dff"],
            typography=["Instrument Sans", "Inter"],
            motion_principle="Subtle signal movement; never required for comprehension.",
            mobile_preview_reviewed=True,
            selected_by_client=True,
            selected_by="client@example.test",
            selected_at=datetime(2026, 9, 23, tzinfo=UTC),
        ),
        build=BuildChecklist(
            responsive_viewports=["360", "390", "768", "1024", "1440"],
            navigation_works=True,
            ctas_route_correctly=True,
            form_validation_works=True,
            form_delivery_tested=True,
            calendar_or_secondary_flow_tested=True,
            metadata_present=True,
            open_graph_present=True,
            alt_text_reviewed=True,
            privacy_and_legal_links_present=True,
            analytics_consent_configured=True,
            assets_rights_confirmed=True,
            no_fabricated_claims=True,
            client_admin_access_ready=True,
            backup_export_supplied=True,
        ),
        launch_review=LaunchReview(
            mobile_conversion_pass=True,
            technical_pass=True,
            trust_pass=True,
            legal_pass=True,
            reviewer="studio-operator",
            client_approval=True,
            reviewed_at=datetime(2026, 9, 23, tzinfo=UTC),
        ),
    )


class StudioHarnessTests(unittest.TestCase):
    def test_blocked_manifest_explains_missing_proof_and_unresolved_assumptions(self):
        root = Path(__file__).resolve().parent
        payload = json.loads((root / "fixtures/studio/blocked-project.v1.json").read_text(encoding="utf-8"))
        report = evaluate_project(StudioProject.model_validate(payload))
        self.assertFalse(report["readOnly"] is False)
        self.assertIn("discovery", report["blockedGates"])
        self.assertIn("assumptions remain unresolved", report["gates"][0]["reasons"])
        self.assertFalse(report["readyToLaunch"])

    def test_complete_manifest_is_ready_for_human_review_but_never_authorized(self):
        report = evaluate_project(make_project())
        self.assertEqual(report["blockedGates"], [])
        self.assertTrue(report["readyForHumanLaunchReview"])
        self.assertFalse(report["readyToLaunch"])
        self.assertFalse(report["launchAuthority"])

    def test_human_gate_ledger_is_hash_chained_and_append_only(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state" / "gates.jsonl"
            first = record_human_gate(path, project_id="studio_test_ready", gate_id="message", decision="approved", actor="operator", rationale="Client signed the message map.", recorded_at=datetime(2026, 9, 23, tzinfo=UTC))
            second = record_human_gate(path, project_id="studio_test_ready", gate_id="direction", decision="blocked", actor="operator", rationale="Mobile preview needs another pass.", recorded_at=datetime(2026, 9, 23, 0, 1, tzinfo=UTC))
            self.assertEqual(second["previousHash"], first["recordHash"])
            self.assertEqual(len(path.read_text(encoding="utf-8").splitlines()), 2)

    def test_portable_references_reject_machine_paths(self):
        self.assertEqual(normalize_relative_path(r"docs\strategy\08-LANDING-STUDIO-OS.md"), "docs/strategy/08-LANDING-STUDIO-OS.md")
        for value in (r"C:\client\brief.json", "/etc/passwd", r"..\secret.txt", ""):
            with self.subTest(value=value):
                with self.assertRaises(PortablePathError):
                    normalize_relative_path(value)


if __name__ == "__main__":
    unittest.main()
