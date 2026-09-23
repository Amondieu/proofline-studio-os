# Versioned prompt system

These prompts are planning and creative-direction inputs, not autonomous
authority. They are versioned so that a change in output can be traced to a
changed hypothesis, source constraint, or evaluation rubric.

## Provider boundaries

- **LLMArena:** research, information architecture, copy alternatives,
  architecture plans, task decomposition, and critique artifacts only.
- **Higgsfield:** abstract, text-only creative concepts and optional silent
  motion drafts only.
- **Repository and human review:** source of truth for code, claims, rights,
  accessibility, performance, privacy, and launch.

Do not upload client data, personal data, confidential documents, unpublished
screenshots, or unapproved brand material to external creative tools.

## Evaluation loop

```text
hypothesis -> controlled candidates -> rubric -> select/revise/reject
-> provenance -> rights review -> responsive/performance QA -> human approval
```

The prompt record structure is
[`schemas/prompt-record.schema.json`](schemas/prompt-record.schema.json).
Provider-specific asset decisions use
[`schemas/studio/higgsfield-asset-record.v1.json`](../schemas/studio/higgsfield-asset-record.v1.json).
