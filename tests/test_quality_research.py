import unittest
from datetime import date

from studio.quality_research import (
    ArchetypeTemplateEvaluation,
    QualitySourceRecord,
    TemplateQualityScores,
)


class QualityResearchContractTests(unittest.TestCase):
    def test_source_record_requires_limitations_and_explicit_reuse(self):
        record = QualitySourceRecord(
            source_id="src_demo_1",
            title="A normative quality standard",
            url="https://example.com/standard",
            source_class="normative",
            evidence_level="gate",
            applicable_archetypes=["all"],
            quality_signal="The publisher defines testable requirements and review guidance.",
            extracts=["Focus and form requirements are testable."],
            limitations=["It does not prove conversion or visual quality."],
            reuse_decision="adopt_as_gate",
            reviewed_by="studio-operator",
            reviewed_on=date(2026, 9, 23),
        )
        self.assertEqual(record.schema_version, "studio.quality-source-record.v1")

    def test_gold_candidate_requires_gates_human_test_and_human_review(self):
        scores = TemplateQualityScores(**{field: 4 for field in TemplateQualityScores.model_fields})
        with self.assertRaises(ValueError):
            ArchetypeTemplateEvaluation(
                evaluation_id="eval_demo_1",
                archetype_id="saas-launch-demand",
                template_ref="templates/saas-home.v1",
                source_ids=["src_one", "src_two"],
                scores=scores,
                normative_gates_passed=True,
                functional_gates_passed=True,
                decision="gold_candidate",
                rationale="Looks strong but the human test has not been completed yet.",
            )
        evaluation = ArchetypeTemplateEvaluation(
            evaluation_id="eval_demo_2",
            archetype_id="saas-launch-demand",
            template_ref="templates/saas-home.v1",
            source_ids=["src_one", "src_two"],
            scores=scores,
            normative_gates_passed=True,
            functional_gates_passed=True,
            human_test_completed=True,
            human_reviewed=True,
            decision="gold_candidate",
            rationale="All gates and the human task test are recorded for review.",
            reviewed_by="studio-operator",
            reviewed_on=date(2026, 9, 23),
        )
        self.assertEqual(evaluation.decision, "gold_candidate")


if __name__ == "__main__":
    unittest.main()
