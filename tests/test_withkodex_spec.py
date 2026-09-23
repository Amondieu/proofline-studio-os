import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC_DIR = ROOT / "specs/170-withkodex-proofline-integration"


class WithkodexProoflineSpecTests(unittest.TestCase):
    def test_spec_bundle_is_complete_and_proposed(self) -> None:
        expected = {"spec.md", "plan.md", "tasks.md", "acceptance.md", "traceability.json", "qa-receipt.md"}
        self.assertEqual(expected, {path.name for path in SPEC_DIR.iterdir() if path.is_file()})
        traceability = json.loads((SPEC_DIR / "traceability.json").read_text(encoding="utf-8"))
        self.assertEqual("proposed", traceability["status"])
        self.assertEqual(9, len(traceability["requirements"]))

    def test_integration_preserves_business_gate_and_external_boundary(self) -> None:
        spec = (SPEC_DIR / "spec.md").read_text(encoding="utf-8")
        self.assertIn("withkodex.com/proofline", spec)
        self.assertIn("G-BIZ-001", spec)
        self.assertIn("external WITHKODEX website", spec)
        self.assertIn("does not", spec)


if __name__ == "__main__":
    unittest.main()
