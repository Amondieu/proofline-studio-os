"""Deterministic readiness audit for the first archetype portfolio site.

The audit measures repository evidence, not business success. It is deliberately
non-authoritative: it can expose gaps and block a launch conversation, but it
cannot approve claims, rights, legal text, or publication.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STATUS_SCORE = {"pass": 1.0, "partial": 0.5, "blocked": 0.0}
RECOMMENDED_ARCHETYPE = "ai-automation-authority"


@dataclass(frozen=True)
class Check:
    id: str
    label: str
    weight: int
    status: str
    evidence: str
    gap: str | None = None

    @property
    def points(self) -> float:
        return self.weight * STATUS_SCORE[self.status]


@dataclass(frozen=True)
class Category:
    id: str
    label: str
    weight: int
    checks: tuple[Check, ...]

    @property
    def score(self) -> int:
        total = sum(check.weight for check in self.checks)
        points = sum(check.points for check in self.checks)
        return round(points / total * 100) if total else 0


def _read(root: Path, relative: str) -> str:
    path = root / relative
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def _exists(root: Path, relative: str) -> bool:
    return (root / relative).is_file()


def _contains(root: Path, relative: str, needle: str) -> bool:
    return needle in _read(root, relative)


def _catalog(root: Path) -> dict[str, Any]:
    return json.loads(_read(root, "config/studio/archetypes.v1.json"))


def _target_record(root: Path, archetype_id: str) -> dict[str, Any] | None:
    return next(
        (
            item
            for item in _catalog(root).get("archetypes", [])
            if item.get("id") == archetype_id
        ),
        None,
    )


def build_audit(root: Path = ROOT, archetype_id: str = RECOMMENDED_ARCHETYPE) -> dict[str, Any]:
    """Build a current audit from committed repository evidence."""

    target = _target_record(root, archetype_id)
    if target is None:
        raise ValueError(f"unknown archetype: {archetype_id}")

    site = _read(root, "site/index.html")
    app = _read(root, "site/app.js")
    styles = _read(root, "site/styles.css")
    evaluation_path = root / "research/archetype-template-evaluations" / f"{archetype_id}.json"
    evaluation = json.loads(evaluation_path.read_text(encoding="utf-8")) if evaluation_path.is_file() else {}
    template_ref = evaluation.get("template_ref", "")
    work_cards = site.count('class="work-card')
    concept_labels = site.count("Studio Concept") + site.count("Independent redesign study")

    categories = (
        Category(
            "strategy_archetype",
            "Strategy & archetype fit",
            20,
            (
                Check(
                    "catalog_entry",
                    "Target archetype is defined in the catalog",
                    20,
                    "pass" if target else "blocked",
                    "config/studio/archetypes.v1.json",
                    None if target else "Add the target archetype to the governed catalog.",
                ),
                Check(
                    "master_template",
                    "Direction-neutral master template exists",
                    25,
                    "pass" if template_ref and _exists(root, template_ref) else "blocked",
                    template_ref or "missing evaluation template_ref",
                    None if template_ref and _exists(root, template_ref) else "Create and register the archetype template.",
                ),
                Check(
                    "candidate_evaluation",
                    "Template evaluation exists with source references",
                    25,
                    "partial" if evaluation.get("decision") == "candidate" and len(evaluation.get("source_ids", [])) >= 2 else "blocked",
                    f"{evaluation_path.relative_to(root)}; decision={evaluation.get('decision', 'missing')}",
                    "Run human task tests and review limitations before promotion beyond candidate.",
                ),
                Check(
                    "public_surface_alignment",
                    "Current portfolio surface names the target archetype and CTA",
                    20,
                    "pass" if archetype_id == "ai-automation-authority" and "AI / Automation Authority" in site and "Request an AI / Automation teardown" in site else "blocked",
                    "site/index.html archetype card and teardown CTA",
                    None if archetype_id == "ai-automation-authority" and "AI / Automation Authority" in site else "Add the target archetype to the public portfolio surface.",
                ),
                Check(
                    "discovery_selection",
                    "A project-specific human archetype selection is recorded",
                    10,
                    "blocked",
                    "No project-specific ClientArchetypeAssessment or selected human gate is recorded for the portfolio site.",
                    "Create the first project brief and record human confirmation of archetype fit.",
                ),
            ),
        ),
        Category(
            "message_conversion",
            "Message & conversion path",
            15,
            (
                Check(
                    "hero_offer_audience",
                    "Hero states offer, audience context, and outcome",
                    25,
                    "pass" if "Premium landing pages" in site and "AI, SaaS, and service offers" in site else "blocked",
                    "site/index.html hero and meta description",
                    "Rewrite the hero around the selected archetype and buyer job.",
                ),
                Check(
                    "primary_cta",
                    "Primary CTA is visible and repeated consistently",
                    20,
                    "pass" if site.count("#teardown") >= 4 else "partial",
                    f"site/index.html contains {site.count('#teardown')} teardown routes",
                    "Keep one dominant action and verify every route in a live test.",
                ),
                Check(
                    "conversion_architecture",
                    "Offer and funnel are documented outside the page",
                    20,
                    "pass" if _exists(root, "docs/strategy/09-MASTER-SITE-CONCEPT.md") and _exists(root, "docs/operations/MESSAGE-MAP.md") else "blocked",
                    "master-site concept and message-map documents",
                    "Document the archetype-specific message map and objection path.",
                ),
                Check(
                    "form_delivery",
                    "Form delivery is real and tested",
                    25,
                    "blocked" if "no data was sent" in site or "no data is sent" in site else "partial",
                    "site/index.html explicitly labels the form as a local demo",
                    "Add a reviewed production endpoint or an approved handoff route with recovery states.",
                ),
                Check(
                    "message_signoff",
                    "Message has human/client sign-off",
                    10,
                    "blocked",
                    "No project-specific sign-off record is present.",
                    "Record the human message decision in the first project gate log.",
                ),
            ),
        ),
        Category(
            "portfolio_proof",
            "Portfolio proof & evidence honesty",
            15,
            (
                Check(
                    "work_surface",
                    "Portfolio work surface contains multiple inspectable examples",
                    25,
                    "pass" if work_cards >= 3 else "partial",
                    f"site/index.html contains {work_cards} work cards",
                    "Add a relevant first archetype case walkthrough when it exists.",
                ),
                Check(
                    "concept_labels",
                    "Non-client work is explicitly labelled",
                    25,
                    "pass" if concept_labels >= 3 else "partial",
                    f"site/index.html contains {concept_labels} concept/redesign labels",
                    "Keep every non-client example labelled at the artifact level.",
                ),
                Check(
                    "case_evidence",
                    "A permissioned, outcome-backed case study exists",
                    20,
                    "blocked",
                    "Current work is concept or independent redesign material; no commissioned client result is recorded.",
                    "Add one permissioned case with role, scope, evidence, and limitations; do not invent results.",
                ),
                Check(
                    "rights_register",
                    "Rights and claim policy exists for future portfolio assets",
                    15,
                    "partial" if _exists(root, "templates/studio/asset-provenance-log.csv") and _exists(root, "docs/strategy/18-TRUST-AND-PROOF-STANDARDS.md") else "blocked",
                    "asset provenance template and trust/proof standards",
                    "Create a site-specific asset and claim register before adding external or client work.",
                ),
                Check(
                    "portfolio_truth_rule",
                    "Portfolio truth rule is documented",
                    15,
                    "pass" if "Portfolio truth rule" in _read(root, "docs/strategy/09-MASTER-SITE-CONCEPT.md") else "blocked",
                    "docs/strategy/09-MASTER-SITE-CONCEPT.md",
                    "Document how concept, redesign, and commissioned work are distinguished.",
                ),
            ),
        ),
        Category(
            "design_build",
            "Design system & build basis",
            15,
            (
                Check(
                    "directions",
                    "Three governed creative directions exist",
                    25,
                    "pass" if len(json.loads(_read(root, "config/studio/directions.v1.json")).get("directions", [])) == 3 else "partial",
                    "config/studio/directions.v1.json",
                    "Keep direction changes separate from message and conversion architecture.",
                ),
                Check(
                    "direction_switcher",
                    "Direction switcher is implemented and stateful",
                    20,
                    "pass" if "data-direction-choice" in site and "localStorage" in app else "blocked",
                    "site/index.html and site/app.js",
                    "Implement a tested switcher without changing the core CTA path.",
                ),
                Check(
                    "semantic_site_shell",
                    "Semantic, keyboard-oriented site shell exists",
                    20,
                    "pass" if "<main id=\"main\">" in site and "skip-link" in site and 'aria-label="Primary navigation"' in site else "partial",
                    "site/index.html semantic landmarks and skip link",
                    "Complete a keyboard sweep through the actual first-archetype page.",
                ),
                Check(
                    "responsive_css",
                    "Responsive and reduced-motion rules exist",
                    20,
                    "pass" if "@media" in styles and "prefers-reduced-motion" in styles else "partial",
                    "site/styles.css",
                    "Attach viewport-specific screenshots or a reproducible browser QA receipt.",
                ),
                Check(
                    "archetype_page_scope",
                    "The public surface is already dedicated to the selected archetype",
                    15,
                    "partial" if "AI / Automation Authority" in site else "blocked",
                    "Current site is a studio master site with multiple archetype cards.",
                    "Build the focused AI/automation portfolio page while preserving the master site as the studio index.",
                ),
            ),
        ),
        Category(
            "qa_evidence",
            "QA, accessibility & performance evidence",
            15,
            (
                Check(
                    "contract_tests",
                    "Contracts and unit tests exist",
                    25,
                    "pass" if _exists(root, "scripts/validate_studio_contracts.py") and _exists(root, "tests/test_archetype_evaluations.py") else "blocked",
                    "contract validator and archetype evaluation tests",
                    "Keep the first page wired to the same contract/test loop.",
                ),
                Check(
                    "qa_matrix",
                    "QA matrix and contrast tooling exist",
                    20,
                    "pass" if _exists(root, "tools/qa_matrix.py") and _exists(root, "tools/contrast_check.py") else "blocked",
                    "tools/qa_matrix.py and tools/contrast_check.py",
                    "Record the first-archetype run results with the page artifact.",
                ),
                Check(
                    "portable_graph",
                    "Portability and Graphify checks exist",
                    15,
                    "pass" if _exists(root, "scripts/portable_audit.py") and _exists(root, "graphify.yaml") else "blocked",
                    "portable audit and Graphify profile configuration",
                    "Run both checks after adding the focused page and its assets.",
                ),
                Check(
                    "manual_browser_evidence",
                    "Current page has committed manual browser evidence",
                    25,
                    "partial" if _exists(root, "LLMarena/NewLLM/quality-run-2026-09-23.md") else "blocked",
                    "LLMarena/NewLLM quality run is preserved, but not a focused-page receipt",
                    "Create a project-specific receipt for keyboard, mobile, reduced motion, form, and direction behavior.",
                ),
                Check(
                    "performance_receipt",
                    "Page-specific performance receipt exists",
                    15,
                    "blocked",
                    "No committed page-specific LCP/INP/CLS receipt is present for the first archetype page.",
                    "Measure the focused page on constrained mobile conditions and attach the result.",
                ),
            ),
        ),
        Category(
            "operations_trust_legal",
            "Operations, trust & legal production basis",
            10,
            (
                Check(
                    "business_registration",
                    "Austria business-registration gate is cleared",
                    20,
                    "blocked",
                    "legal/BUSINESS-REGISTRATION-GATE.v1.md is documented but remains explicitly blocked until human confirmation.",
                    "Confirm the actual service mix and Gewerbewortlaut with the responsible Austrian contact before paid work.",
                ),
                Check(
                    "legal_routes",
                    "Privacy, legal notice, and accessibility routes are real",
                    20,
                    "blocked" if "Privacy · Legal · Cookie settings" in site else "partial",
                    "Footer currently displays non-linked placeholder labels.",
                    "Add reviewed, jurisdiction-appropriate routes before any public production launch.",
                ),
                Check(
                    "analytics_consent",
                    "Analytics and consent behavior is configured",
                    15,
                    "blocked",
                    "No analytics provider or consent implementation is part of this foundation slice.",
                    "Add a separately reviewed adapter and consent record; do not add tracking by default.",
                ),
                Check(
                    "hosting_ownership",
                    "Hosting, domain, and account ownership are recorded",
                    15,
                    "blocked",
                    "Repository intentionally keeps hosting, DNS, and credentials outside the foundation slice.",
                    "Record an approved hosting/ownership handoff for the eventual portfolio deployment.",
                ),
                Check(
                    "asset_policy",
                    "Asset, AI, and claim boundaries are documented",
                    15,
                    "pass" if _exists(root, "docs/strategy/18-TRUST-AND-PROOF-STANDARDS.md") and _exists(root, "templates/studio/asset-provenance-log.csv") else "partial",
                    "trust/proof standards and asset provenance template",
                    "Fill the register for every actual image, font, icon, and claim used.",
                ),
                Check(
                    "handover_basis",
                    "Build and launch handover checklists exist",
                    15,
                    "pass" if _exists(root, "docs/operations/BUILD-CHECKLIST.md") and _exists(root, "docs/operations/LAUNCH-REVIEW.md") else "blocked",
                    "build checklist and launch review",
                    "Complete them for the focused page rather than relying on templates alone.",
                ),
            ),
        ),
        Category(
            "human_gates",
            "Human decisions & launch gates",
            10,
            (
                Check(
                    "discovery_gate",
                    "Discovery gate is signed for this site",
                    20,
                    "blocked",
                    "No project-specific human gate ledger entry exists for the first archetype site.",
                    "Record discovery assumptions, evidence owner, and human decision.",
                ),
                Check(
                    "message_gate",
                    "Message gate is signed for this site",
                    20,
                    "blocked",
                    "No project-specific message approval is recorded.",
                    "Approve the first-archetype message map and proof boundary.",
                ),
                Check(
                    "direction_gate",
                    "Direction gate is signed for this site",
                    20,
                    "blocked",
                    "The master site demonstrates directions but does not record a selected project direction.",
                    "Select and record one direction for the focused portfolio page.",
                ),
                Check(
                    "launch_review",
                    "Launch review and human approval exist",
                    25,
                    "blocked",
                    "Current site is explicitly a concept/proof-of-work site, not an approved production launch.",
                    "Run the launch review only after form, legal, rights, ownership, and rollback evidence exist.",
                ),
                Check(
                    "concept_boundary",
                    "The current public surface is honest about its status",
                    15,
                    "pass" if "not a live client intake" in site and "not commissioned client work" in site else "partial",
                    "site/index.html concept labels and local-demo note",
                    "Preserve the concept boundary until production gates are genuinely complete.",
                ),
            ),
        ),
    )

    category_payload: list[dict[str, Any]] = []
    for category in categories:
        category_payload.append(
            {
                "id": category.id,
                "label": category.label,
                "weight": category.weight,
                "score": category.score,
                "weightedPoints": round(category.weight * category.score / 100, 2),
                "checks": [asdict(check) | {"points": round(check.points, 2)} for check in category.checks],
            }
        )

    overall = round(sum(item["weightedPoints"] for item in category_payload))
    blocked = [
        {
            "checkId": check.id,
            "category": category.id,
            "label": check.label,
            "gap": check.gap,
        }
        for category in categories
        for check in category.checks
        if check.status == "blocked"
    ]
    return {
        "schemaVersion": "studio.readiness-audit.v1",
        "auditId": f"readiness_first_archetype_{date.today().isoformat()}",
        "generatedOn": date.today().isoformat(),
        "targetArchetypeId": archetype_id,
        "targetArchetypeName": target["name"],
        "portfolioMode": True,
        "overallBasisCompletenessPercent": overall,
        "categoryScores": category_payload,
        "hardBlockers": blocked,
        "productionStatus": "blocked_until_gates_complete",
        "recommendation": "Build the focused AI/automation portfolio page next, then attach project-specific Discovery, message, direction, QA, form, rights, legal, and launch evidence.",
        "limitations": [
            "The percentage measures repository evidence and implementation basis, not conversion performance or business success.",
            "A concept or redesign can demonstrate method but cannot establish client results, rights, or universal quality.",
            "Automated checks can expose gaps and block; they cannot approve a launch or legal sufficiency.",
        ],
    }


def render_markdown(audit: dict[str, Any]) -> str:
    lines = [
        f"# First archetype portfolio readiness audit — {audit['generatedOn']}",
        "",
        f"**Target:** `{audit['targetArchetypeId']}` — {audit['targetArchetypeName']}",
        "",
        f"## Current position: {audit['overallBasisCompletenessPercent']}% basis completeness",
        "",
        "This is a deterministic repository audit for the first focused archetype website that also serves as Proofline Studio portfolio work. It is not a launch approval. The recommended first target is AI / Automation Authority because the current master site already leads with that system and its assessment CTA.",
        "",
        "| Area | Weight | Score | Weighted points |",
        "|---|---:|---:|---:|",
    ]
    for category in audit["categoryScores"]:
        lines.append(
            f"| {category['label']} | {category['weight']}% | {category['score']}% | {category['weightedPoints']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- **Portfolio basis:** sufficiently structured to build the focused first archetype page as an honest concept/proof-of-work artifact.",
            "- **Production launch:** blocked. The local demo form, placeholder legal routes, missing project-specific human gates, and missing page-specific performance/ownership evidence are intentional open gates.",
            "- **Proof boundary:** current concepts demonstrate method and design thinking; they are not commissioned case studies or conversion results.",
            "",
            "## Blockers and next actions",
            "",
        ]
    )
    for blocker in audit["hardBlockers"]:
        lines.append(f"- **{blocker['label']}** — {blocker['gap']}")
    lines.extend(
        [
            "",
            "## Re-run",
            "",
            "```powershell",
            "python tools/readiness_audit.py --archetype ai-automation-authority --write-report",
            "```",
            "",
            "The report remains advisory; human decisions still control source promotion, claims, rights, legal text, design direction, and launch.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archetype", default=RECOMMENDED_ARCHETYPE)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    audit = build_audit(archetype_id=args.archetype)
    markdown = render_markdown(audit)
    if args.write_report:
        reports = ROOT / "reports"
        reports.mkdir(exist_ok=True)
        stem = f"first-archetype-readiness-{audit['generatedOn']}"
        (reports / f"{stem}.json").write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
        (reports / f"{stem}.md").write_text(markdown, encoding="utf-8")
        print(f"Wrote {reports / f'{stem}.md'}")
        print(f"Wrote {reports / f'{stem}.json'}")
    else:
        print(markdown)
    print(f"READINESS BASIS: {audit['overallBasisCompletenessPercent']}%")
    print(f"PRODUCTION STATUS: {audit['productionStatus']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
