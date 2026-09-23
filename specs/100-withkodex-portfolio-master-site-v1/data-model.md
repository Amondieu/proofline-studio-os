# Data model — Feature 100

## Route record

Each route records `path`, `visitor_job`, `primary_cta`, `status`, `owner`,
`source_ids`, `required_evidence`, and `human_gate`.

## Content record

Each claim records `claim_id`, `text`, `claim_type`, `evidence_ref`,
`qualification`, `reviewer`, and `status`. Outcome, client, metric, legal, and
compliance claims require evidence or remain blocked.

## Asset record

Higgsfield candidates use `schemas/studio/higgsfield-asset-record.v1.json`.
Existing non-provider assets use `schemas/studio/asset-record.v1.json`. A
production reference requires a human-approved record in addition to vendor
terms.

## Form record

The master site references the interest-only model in
`specs/130-teardown-interest-intake-v1/data-model.md`; it must not define a
second provider or retention policy.
