import unittest
from datetime import UTC, datetime
from pathlib import Path

from studio.laya import (
    CalibrationStatus,
    LayaAdvisoryEngine,
    LayaDecision,
    LayaEvaluationRecord,
    LayaModel,
    LayaRequest,
    LayaTask,
    sanitize_state,
)


class FakeLayaAdapter:
    provider = "fake-laya"
    model = LayaModel.multilingual
    calibration_status = CalibrationStatus.unknown

    def __init__(self, confidence: float = 0.91) -> None:
        self.confidence = confidence
        self.last_request = None

    def predict(self, request: LayaRequest) -> dict:
        self.last_request = request
        return {
            "answers": {
                request.question_id: {
                    "type": "choice",
                    "choice": "qualified",
                    "probabilities": {"qualified": self.confidence, "review": 1 - self.confidence},
                    "confidence": self.confidence,
                }
            },
            "routing": {"model": "multilingual", "reason": "fake test route"},
        }


def make_request(**overrides) -> LayaRequest:
    values = {
        "request_id": "laya_req_demo_1",
        "task": LayaTask.prospect_triage,
        "question_id": "triage",
        "state": {"company": "Example GmbH", "contactEmail": "person@example.com", "nested": {"apiKey": "secret"}},
        "questions": {"triage": {"type": "choice", "options": ["qualified", "review"]}},
        "language": "de",
        "evidence_refs": ["docs/strategy/26-OUTBOUND-SCORING.md"],
    }
    values.update(overrides)
    return LayaRequest(**values)


class LayaAdvisoryTests(unittest.TestCase):
    def test_high_confidence_result_is_still_advisory_and_hashed(self):
        adapter = FakeLayaAdapter()
        decision = LayaAdvisoryEngine(adapter).advise(make_request())

        self.assertEqual(decision.selected_option, "qualified")
        self.assertFalse(decision.abstained)
        self.assertTrue(decision.needs_human_review)
        self.assertFalse(decision.action_authorized)
        self.assertEqual(len(decision.input_sha256), 64)
        self.assertNotIn("contactEmail", adapter.last_request.state)
        self.assertNotIn("apiKey", adapter.last_request.state["nested"])

    def test_low_confidence_result_abstains(self):
        decision = LayaAdvisoryEngine(FakeLayaAdapter(confidence=0.61), abstain_below=0.75).advise(make_request())

        self.assertTrue(decision.abstained)
        self.assertIsNone(decision.selected_option)
        self.assertIn("threshold", decision.abstention_reason)

    def test_sensitive_request_is_rejected_before_adapter(self):
        adapter = FakeLayaAdapter()
        with self.assertRaises(ValueError):
            LayaAdvisoryEngine(adapter).advise(make_request(contains_sensitive_data=True))
        self.assertIsNone(adapter.last_request)

    def test_request_requires_question_id_to_exist(self):
        with self.assertRaises(ValueError):
            make_request(question_id="missing")

    def test_decision_cannot_cross_authority_boundary(self):
        with self.assertRaises(ValueError):
            LayaDecision(
                decision_id="laya_dec_demo_1",
                request_id="laya_req_demo_1",
                task=LayaTask.prospect_triage,
                model=LayaModel.english,
                provider="fake-laya",
                input_sha256="a" * 64,
                probabilities={"qualified": 1.0},
                confidence=1.0,
                routing_reason="test",
                action_authorized=True,
            )

    def test_human_evaluation_is_explicit(self):
        evaluation = LayaEvaluationRecord(
            evaluation_id="laya_eval_demo_1",
            decision_id="laya_dec_demo_1",
            human_option="qualified",
            agrees_with_model=True,
            reviewer="studio-operator",
            reviewed_at=datetime.now(UTC),
            calibration_bucket="0.90-1.00",
        )
        self.assertTrue(evaluation.agrees_with_model)

    def test_sanitizer_handles_nested_sensitive_keys(self):
        clean, redacted = sanitize_state({"access_token": "x", "person": {"professionalEmail": "x@example.com", "ok": True}})
        self.assertEqual(clean, {"person": {"ok": True}})
        self.assertEqual(sorted(redacted), ["access_token", "person.professionalEmail"])

    def test_example_request_fixture_is_contract_valid(self):
        fixture = Path(__file__).parent / "fixtures" / "laya" / "advisory-request.v1.json"
        request = LayaRequest.model_validate_json(fixture.read_text(encoding="utf-8"))
        self.assertEqual(request.requested_model, LayaModel.typed_decisions)


if __name__ == "__main__":
    unittest.main()
