import unittest
from datetime import date

from studio.archetypes import ArchetypeRecord, ArchetypeScore, ClientArchetypeAssessment, recommend_archetype


class ArchetypeContractTests(unittest.TestCase):
    def test_recommendation_downgrades_close_scores(self):
        scores = [
            ArchetypeScore(archetype_id="ai-automation-authority", score=84, rationale="The buyer must trust a technical workflow mechanism."),
            ArchetypeScore(archetype_id="saas-launch-demand", score=82, rationale="A productized offer also has a plausible launch path."),
        ]
        self.assertEqual(recommend_archetype(scores), ("ai-automation-authority", "low"))

    def test_archetype_and_assessment_are_advisory_records(self):
        record = ArchetypeRecord(
            archetype_id="ai-automation-authority",
            name="AI / Automation Authority System",
            ideal_client=["AI consultancy"],
            primary_jtbd="When a workflow is costly and hard to judge, make the mechanism credible so the buyer can request an assessment.",
            buyer_hesitations=["Will this work with our systems?"],
            primary_conversion="Request a workflow assessment",
            primary_kpi="Qualified assessment requests",
            hero_principle="Name the workflow, mechanism, and next diagnostic step.",
            proof_requirements=["Documented method"],
            core_sections=["Hero", "Diagnosis", "Mechanism", "Proof", "Engagement", "CTA"],
            recommended_design_direction="precision",
            motion_rule="Use restrained motion to explain the system.",
            prohibited_patterns=["AI hype"],
            recommended_offer_tier="authority-sprint",
            qualification_signals=["Named workflow"],
            required_gates=["discovery", "message", "direction", "build", "qa", "launch"],
        )
        assessment = ClientArchetypeAssessment(
            project_id="studio_demo_project",
            business_type="AI consultancy",
            primary_offer="Workflow automation advisory and implementation.",
            ideal_buyer="Operations leaders with an expensive manual workflow.",
            buying_trigger="A growing workflow is slowing the team and needs review.",
            primary_job_to_be_done="When a workflow becomes expensive, I want a credible assessment so I can choose a safe next step.",
            primary_conversion="Request a workflow assessment",
            deal_value="€10k–30k",
            sales_cycle="30–60 days",
            proof_available=["Method document"],
            highest_buyer_risk="The buyer fears disruption to a core operation.",
            content_complexity="high",
            visual_intensity="medium",
            privacy_or_regulatory_risk="high",
            candidate_scores=[ArchetypeScore(archetype_id=record.archetype_id, score=86, rationale="The job and risk match the blueprint.")],
            recommended_archetype=record.archetype_id,
            recommended_design_direction="precision",
            recommended_offer_tier="authority-sprint",
            required_human_review=["Confirm workflow evidence and privacy boundary."],
            rationale="The recommendation is a fit hypothesis pending Discovery.",
            assessed_by="studio-operator",
            assessed_on=date(2026, 9, 23),
        )
        self.assertEqual(record.status, "pilot")
        self.assertFalse(assessment.human_confirmed)
        with self.assertRaises(ValueError):
            ClientArchetypeAssessment.model_validate({**assessment.model_dump(), "human_confirmed": True})


if __name__ == "__main__":
    unittest.main()
