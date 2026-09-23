import unittest
from datetime import date, datetime

from studio.outbound import (
    ProspectScore,
    ReplyRecord,
    SendApproval,
    SuppressionRecord,
    calculate_prospect_score,
)


class OutboundContractTests(unittest.TestCase):
    def test_score_calculation_and_threshold_are_explicit(self):
        score = calculate_prospect_score(
            icp_fit=19,
            visible_conversion_leak=17,
            current_trigger=12,
            offer_economics=13,
            decision_maker=8,
            evidence_confidence=8,
            compliance_fit=8,
        )
        self.assertEqual(score.total, 85)
        with self.assertRaises(ValueError):
            ProspectScore(
                icp_fit=20,
                visible_conversion_leak=20,
                current_trigger=15,
                offer_economics=15,
                decision_maker=10,
                evidence_confidence=10,
                compliance_fit=10,
                total=99,
            )

    def test_opt_out_requires_suppression(self):
        with self.assertRaises(ValueError):
            ReplyRecord(
                reply_id="reply_demo_1",
                prospect_id="pr_2026_0001",
                received_at=datetime(2026, 9, 23, 10, 0),
                classification="opt_out",
                summary="Recipient asked not to receive more messages.",
                next_action="Stop outreach.",
                suppression_applied=False,
            )
        record = ReplyRecord(
            reply_id="reply_demo_1",
            prospect_id="pr_2026_0001",
            received_at=datetime(2026, 9, 23, 10, 0),
            classification="opt_out",
            summary="Recipient asked not to receive more messages.",
            next_action="Stop outreach.",
            suppression_applied=True,
        )
        self.assertTrue(record.suppression_applied)

    def test_send_approval_records_exact_message_hash(self):
        approval = SendApproval(
            approval_id="send_demo_1",
            draft_id="draft_demo_1",
            exact_recipient="founder@example.com",
            message_sha256="a" * 64,
            decision="approved",
            checklist=[f"check-{index}" for index in range(8)],
            approved_by="studio-operator",
            approved_on=datetime(2026, 9, 23, 10, 0),
        )
        self.assertEqual(approval.decision, "approved")

    def test_suppression_records_are_minimal_and_lifetime_is_explicit(self):
        permanent = SuppressionRecord(
            suppression_id="sup_demo_1",
            identifier="person@example.com",
            scope="person",
            suppressed_at=datetime(2026, 9, 23, 10, 0),
            reason="opt_out",
            source="reply",
        )
        self.assertTrue(permanent.permanent)
        with self.assertRaises(ValueError):
            SuppressionRecord(
                suppression_id="sup_demo_2",
                identifier="example.com",
                scope="domain",
                suppressed_at=datetime(2026, 9, 23, 10, 0),
                reason="opt_out",
                source="reply",
                permanent=False,
                expires_on=date(2026, 12, 23),
            )


if __name__ == "__main__":
    unittest.main()
