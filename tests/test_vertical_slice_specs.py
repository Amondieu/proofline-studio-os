import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class VerticalSliceSpecTests(unittest.TestCase):
    def test_each_vertical_slice_feature_has_required_spec_kit_artifacts(self) -> None:
        required = {
            "100-withkodex-portfolio-master-site-v1",
            "110-proofline-route-v1",
            "120-ai-automation-authority-v1",
            "130-teardown-interest-intake-v1",
        }
        for feature in required:
            directory = ROOT / "specs" / feature
            for filename in ("spec.md", "plan.md", "tasks.md", "acceptance.md", "traceability.json", "qa-receipt.md", "converge.md"):
                self.assertTrue((directory / filename).is_file(), f"missing {feature}/{filename}")
            traceability = json.loads((directory / "traceability.json").read_text(encoding="utf-8"))
            self.assertEqual("studio.spec-traceability.v1", traceability["schemaVersion"])
            self.assertEqual(feature, traceability["featureId"])
            self.assertTrue(traceability["requirements"])

    def test_creative_layer_has_prompt_and_provenance_boundaries(self) -> None:
        prompt_schema = ROOT / "prompts" / "schemas" / "prompt-record.schema.json"
        asset_schema = ROOT / "schemas" / "studio" / "higgsfield-asset-record.v1.json"
        self.assertTrue(prompt_schema.is_file())
        self.assertTrue(asset_schema.is_file())
        self.assertIn("Higgsfield", (ROOT / "docs/architecture/HIGGSFIELD-ASSET-POLICY.md").read_text(encoding="utf-8"))
        for prompt in (
            "precision-system-hero.v1.md",
            "cinematic-authority-hero.v1.md",
            "editorial-luxury-hero.v1.md",
            "motion-loop-constraints.v1.md",
        ):
            self.assertTrue((ROOT / "prompts/higgsfield" / prompt).is_file())


if __name__ == "__main__":
    unittest.main()
