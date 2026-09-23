# Landing Studio Harness

The harness is the reusable delivery layer behind the studio. It is designed
for small, high-quality slices: one client, one primary conversion, one
selected direction, one bounded scope.

## Inputs

- `schemas/studio/project.v1.json` project manifest;
- client discovery brief;
- message-map sign-off;
- selected creative direction and mobile preview review;
- build checklist and a machine-readable QA receipt;
- asset provenance records and detailed human approvals where applicable;
- human launch review and client approval.

## Outputs

`python -m studio validate <manifest>` emits a versioned JSON report with:

- each gate's pass/block state;
- exact blocking reasons;
- explicit read-only and non-authority markers;
- limitations that prevent the report from being mistaken for legal, factual,
  or launch approval.

## What the harness refuses to do

- It does not infer a target audience from a URL.
- It does not write copy from fabricated proof.
- It does not mark client sign-off from a completed field alone.
- It does not treat a visual prototype as a production build.
- It does not accept “AI generated” as proof of asset rights.
- It does not convert a passing checklist into a deployment command.

## Human gate ledger

`studio.record_human_gate()` appends an explicit decision to a local JSONL
ledger. Each record includes the previous record hash and its own hash. This is
an audit aid, not a blockchain and not a substitute for a contract or legal
review. Corrections append a new record with `superseded` rather than rewriting
history.
