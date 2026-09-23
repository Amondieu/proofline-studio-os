# 20 — Archetype selection rubric

## Intake fields

Capture these fields before recommending a blueprint:

```yaml
business_type: ""
primary_offer: ""
ideal_buyer: ""
buying_trigger: ""
primary_job_to_be_done: ""
primary_conversion: ""
deal_value: ""
sales_cycle: ""
proof_available: []
highest_buyer_risk: ""
content_complexity: medium
visual_intensity: medium
privacy_or_regulatory_risk: low
recommended_archetype: null
recommended_design_direction: null
recommended_offer_tier: null
required_human_review: []
```

The JTBD should describe a situation, an action, and an outcome. A useful
working form is: “When [situation], I want to [verb + object], so I can
[outcome].” It is a prompt for better discovery, not a claim that one sentence
captures the whole buyer.

Reference: [Stackmatix — Jobs to be Done](https://www.stackmatix.com/blog/jobs-to-be-done).

## Scoring dimensions

Score each candidate from 0–5, then record the evidence behind the score.

| Dimension | Question |
| --- | --- |
| Buyer job | Does the archetype match what the buyer is trying to decide or do? |
| Risk shape | Does it address the most expensive hesitation? |
| Conversion fit | Does its primary action match the real next step? |
| Proof fit | Can the client supply the evidence the blueprint requires? |
| Delivery fit | Can Proofline deliver the sections, interactions, and QA scope? |
| Offer fit | Does the recommended tier match complexity, value, and sales cycle? |
| Direction fit | Does the visual starting point serve the decision rather than decorate it? |
| Governance fit | Are privacy, rights, accessibility, and legal boundaries reviewable? |

Store the total and a short rationale in `candidate_scores`. The helper in
`studio/archetypes.py` returns `high` confidence only with a clear lead, and
returns `low` confidence for a close result or a single unchallenged score.

## Human review rules

Human review is required for:

- the primary job and buying trigger;
- the buyer risk and the promised next step;
- proof ownership, consent, and factuality;
- privacy, regulatory, accessibility, and legal constraints;
- the final archetype, direction, offer tier, and launch scope.

An assessment may recommend `ai-automation-authority` while the project is
still in Discovery. It may not mark the project approved, launch-ready, or
client-confirmed unless a person records that decision in the relevant gate.

## Tie and no-fit handling

- Tie: keep both candidates, set confidence to `low`, and ask a focused
  Discovery question.
- Close scores: do not force a visual direction; run a message test first.
- Missing proof: retain the archetype as a hypothesis and add a proof backlog.
- High privacy or regulatory risk: prefer the most conservative applicable
  blueprint and expand human review; do not infer compliance.
- No reasonable fit: leave the recommendation empty and document why.

## Acceptance check

An assessment is structurally complete when it has intake fields, at least one
candidate with rationale, required human review items, an assessor, and a date.
It is substantively complete only after the client confirms the situation and
the studio freezes the message and direction gates.
