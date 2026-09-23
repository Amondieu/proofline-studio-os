# 19 — Business archetypes

<!-- v0.1 · 2026-09-23 · owner: founder · status: V1 pilot -->

## Why this layer exists

Proofline Studio does not need five industry templates. It needs a small set of
conversion blueprints for recurring buyer situations: what the buyer is trying
to decide, what makes the decision feel risky, what evidence can reduce that
risk, and what the first appropriate action is.

An archetype is therefore a category of observable buying and decision
patterns. It is not a persona, an industry label, a brand voice, or an
automatic diagnosis. The client remains the source of truth for their offer,
proof, constraints, and desired outcome.

This distinction follows the useful difference described by Nielsen Norman
Group: archetypes describe categories of users, while personas humanize those
categories. Proofline keeps the category as an operating aid and performs the
humanization in Discovery rather than pretending that a template knows the
client.

Reference: [NN/g — Archetypes vs. Personas](https://www.nngroup.com/videos/archetypes-vs-personas/).

## V1 pilot catalog

| Archetype | Observable job | Primary first action | Direction | Tier |
| --- | --- | --- | --- | --- |
| AI / Automation Authority System | Make a costly workflow and technical mechanism credible | Workflow assessment | Precision | Authority Landing Sprint |
| SaaS Launch & Demand System | Turn a product use case into a launch-ready buying path | Product demo | Cinematic | Launch System |
| Expert Authority System | Make a point of view and fit legible | Fit-call application | Editorial | Authority Landing Sprint |
| Creative Portfolio & Inquiry System | Curate relevant proof and attract better-fit briefs | Project brief | Cinematic | Launch System |
| High-Trust Lead Engine | Reduce uncertainty before a sensitive inquiry | Confidential consultation | Editorial | Authority Landing Sprint |

The first public surface leads with the first two because they best match the
current Proofline concept and available studio proof. The other three remain
usable in Discovery and internal sales qualification. The optional future
`Category-Creation Launch System` stays outside the V1 catalog until there is
enough evidence and a repeatable delivery boundary.

## Operating rule

1. Discovery captures the client situation in `ClientArchetypeAssessment`.
2. A human or reviewed assessment step records candidate scores and a
   recommendation.
3. The recommendation informs message, direction, offer tier, and QA scope.
4. The client confirms or rejects the fit during Discovery.
5. The selected archetype is never evidence for a claim about conversion.

The archetype can be changed without changing the client’s source facts. A
project may also remain unclassified when the evidence is weak.

## Required boundaries

- No archetype invents proof, credentials, metrics, testimonials, rights, or
  legal language.
- `recommended_*` fields are advisory and do not replace `selected_by_client`
  or human gate records.
- A high-risk or regulated project gets explicit privacy, ownership, legal, and
  accessibility review before a launch decision.
- The archetype does not determine the visual direction by itself. It provides
  a starting hypothesis that the buyer, offer, evidence, and brand constraints
  must confirm.

## Repository sources

- `config/studio/archetypes.v1.json` — structured V1 catalog.
- `studio/archetypes.py` — recommendation helper and contract exports.
- `schemas/archetype-record.schema.json` — blueprint contract.
- `schemas/client-archetype-assessment.schema.json` — client assessment contract.
- `docs/strategy/20-ARCHETYPE-SELECTION-RUBRIC.md` — fit and confidence rules.
- `docs/strategy/21-ARCHETYPE-CONVERSION-BLUEPRINTS.md` — detailed blueprint cards.
- `docs/strategy/22-ARCHETYPE-SALES-PLAYBOOK.md` — public positioning and qualification.
