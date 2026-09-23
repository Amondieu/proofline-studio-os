import csv
import json
import unittest
from pathlib import Path

from studio.quality_research import ArchetypeTemplateEvaluation


ROOT = Path(__file__).resolve().parents[1]


class ArchetypeEvaluationCoverageTests(unittest.TestCase):
    def test_every_catalog_archetype_has_a_candidate_evaluation(self) -> None:
        catalog = json.loads(
            (ROOT / "config/studio/archetypes.v1.json").read_text(encoding="utf-8")
        )
        expected_ids = {item["id"] for item in catalog["archetypes"]}
        paths = sorted((ROOT / "research/archetype-template-evaluations").glob("*.json"))
        evaluations = [
            ArchetypeTemplateEvaluation.model_validate(
                json.loads(path.read_text(encoding="utf-8"))
            )
            for path in paths
        ]

        self.assertEqual(expected_ids, {evaluation.archetype_id for evaluation in evaluations})
        self.assertEqual(len(expected_ids), len(evaluations))
        for evaluation in evaluations:
            self.assertEqual("candidate", evaluation.decision)
            self.assertFalse(evaluation.human_reviewed)
            self.assertFalse(evaluation.human_test_completed)
            self.assertTrue((ROOT / evaluation.template_ref).is_file())

    def test_evaluations_reference_registered_sources(self) -> None:
        with (ROOT / "research/archetype-source-register.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            source_ids = {row["source_id"] for row in csv.DictReader(handle)}

        for path in (ROOT / "research/archetype-template-evaluations").glob("*.json"):
            evaluation = ArchetypeTemplateEvaluation.model_validate(
                json.loads(path.read_text(encoding="utf-8"))
            )
            self.assertTrue(set(evaluation.source_ids).issubset(source_ids))


if __name__ == "__main__":
    unittest.main()
