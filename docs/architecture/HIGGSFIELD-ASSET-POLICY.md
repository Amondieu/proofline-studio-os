# Higgsfield asset policy — controlled creative layer

Status: `proposed / human-gated`

Higgsfield may propose abstract art direction for the WITHKODEX / Proofline
vertical slice. It is not the website authority, source of truth, rights
reviewer, accessibility reviewer, or deployment system.

## Allowed V1 uses

- abstract hero stills and moodboards;
- direction explorations for Precision, Cinematic, and Editorial;
- optional 4–6 second silent loops with a still fallback;
- clearly labelled visuals for studio concepts.

## Prohibited until separately approved

- client data, confidential briefs, personal data, unpublished screenshots, or
  third-party brand material as input;
- generated people represented as clients, staff, testimonials, or proof;
- logos, fake dashboards, fake metrics, compliance badges, or legal claims;
- direct deployment of generated output;
- any production reference before provenance and rights approval.

## Required lifecycle

```text
text-only prompt -> controlled candidates -> visual rubric -> selected candidate
-> provenance record -> rights review -> responsive/performance preparation
-> accessibility review -> human approval -> production reference
```

An asset is not production-approved merely because the provider permits
commercial use of an output. Input rights, likeness, trademark, disclosure,
accessibility, performance, and the concrete usage context remain separate
checks.

## Production gate

An asset may be referenced by a production build only when its record has:

- `rights_review_status: approved`;
- `production_usage: approved`;
- a named human reviewer and timestamp;
- a prompt version and input classification;
- a responsive crop or safe-area review;
- an approved still fallback when motion is involved.

Until then, keep the asset in a private review area or use a placeholder. The
repository must never contain client secrets or confidential source material.

The machine-readable record is
[`schemas/studio/higgsfield-asset-record.v1.json`](../../schemas/studio/higgsfield-asset-record.v1.json).
