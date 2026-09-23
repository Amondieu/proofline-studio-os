import unittest

from tools.readiness_audit import build_audit


class ReadinessAuditTests(unittest.TestCase):
    def test_recommended_first_archetype_has_a_reproducible_basis_score(self) -> None:
        audit = build_audit()

        self.assertEqual("ai-automation-authority", audit["targetArchetypeId"])
        self.assertGreaterEqual(audit["overallBasisCompletenessPercent"], 0)
        self.assertLessEqual(audit["overallBasisCompletenessPercent"], 100)
        self.assertEqual(7, len(audit["categoryScores"]))
        self.assertEqual("blocked_until_gates_complete", audit["productionStatus"])
        self.assertTrue(audit["hardBlockers"])

    def test_audit_is_not_allowed_to_call_the_site_launch_ready(self) -> None:
        audit = build_audit()

        self.assertNotEqual("ready_to_launch", audit["productionStatus"])
        blocker_ids = {item["checkId"] for item in audit["hardBlockers"]}
        self.assertIn("form_delivery", blocker_ids)
        self.assertIn("business_registration", blocker_ids)
        self.assertIn("launch_review", blocker_ids)


if __name__ == "__main__":
    unittest.main()
