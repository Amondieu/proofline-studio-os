import unittest
from datetime import date

from studio.cookbook import (
    AntiPatternRecord,
    EvidenceLevel,
    EvidenceRef,
    PatternRecord,
    PatternScores,
    calculate_pattern_readiness,
)


def evidence() -> list[EvidenceRef]:
    return [
        EvidenceRef(
            source_id="W3C-WCAG22",
            title="Web Content Accessibility Guidelines 2.2",
            url="https://www.w3.org/TR/WCAG22/",
            level=EvidenceLevel.authoritative,
            note="Normative accessibility criteria inform the interaction checks.",
        )
    ]


class CookbookContractTests(unittest.TestCase):
    def test_readiness_formula_matches_declared_weights(self):
        scores = PatternScores(
            clarity_impact=10,
            conversion_plausibility=8,
            trust_impact=9,
            mobile_suitability=9,
            accessibility_safety=10,
            performance_safety=9,
            implementation_cost=8,
            maintenance_burden=8,
            legal_safety=10,
            studio_fit=10,
        )
        self.assertEqual(calculate_pattern_readiness(scores), 9.12)

    def test_pattern_and_anti_pattern_contracts_require_evidence(self):
        scores = PatternScores(**{field: 8 for field in PatternScores.model_fields})
        pattern = PatternRecord(
            pattern_id="HERO-001",
            name="Outcome-first hero",
            category="positioning",
            status="pilot",
            problem_solves="Makes the offer and next action legible quickly.",
            use_only_when=["The audience and offer are specific."],
            do_not_use_when=["The CTA destination is unresolved."],
            target_client_fit=["B2B AI", "SaaS"],
            user_conversion_hypothesis="Clearer first-screen meaning should reduce avoidable decoding.",
            evidence_level="authoritative",
            evidence=evidence(),
            implementation=["Use semantic HTML text and one primary CTA."],
            accessibility_requirements=["Keyboard reachable and visibly focused CTA."],
            performance_budget=["Do not lazy-load the LCP visual."],
            trust_legal_requirements=["Use only supplied or labelled proof."],
            low_cost_version="Text, one static visual, and a direct CTA.",
            premium_version="A direction-specific composition with the same message hierarchy.",
            test_method="Run a five-second comprehension test with target-like reviewers.",
            success_signal="Two of three reviewers identify the offer, audience, and action.",
            failure_signal="Reviewers describe the visual but not the offer.",
            next_controlled_test="Test a shorter headline against the current version.",
            scores=scores,
            readiness_score=calculate_pattern_readiness(scores),
            cookbook_tags=["hero", "clarity", "mobile"],
            reviewed_by="studio-operator",
            reviewed_on=date(2026, 9, 23),
        )
        self.assertEqual(pattern.schema_version, "studio.pattern-record.v1")
        anti_pattern = AntiPatternRecord(
            anti_pattern_id="FORM-AP-001",
            name="Silent form failure",
            category="forms",
            why_it_is_tempting="Omitting states keeps the mockup visually minimal.",
            why_it_fails="People cannot recover from errors or know whether the lead arrived.",
            harm_type=["conversion", "accessibility"],
            early_warning_signal="Only the happy path exists in the prototype.",
            detection_method="Submit empty, invalid, spam, valid, and delivery-failure cases.",
            severity="blocker",
            replacement_pattern="FORM-001",
            exception="None.",
            launch_rule="block_launch",
            evidence=evidence(),
        )
        self.assertEqual(anti_pattern.launch_rule, "block_launch")


if __name__ == "__main__":
    unittest.main()
