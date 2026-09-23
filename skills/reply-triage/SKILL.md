---
name: reply-triage
description: Classify outbound replies, apply suppression on opt-out, and record minimal human-owned next actions.
---

# Reply triage envelope

Read `docs/strategy/29-REPLY-HANDLING-AND-LEARNING.md` and
`config/studio/outbound-policy.v1.json` first.

Use the installed upstream `revops` and `analytics` references for operational
labels only. Preserve opt-outs, do not re-contact suppressed prospects, and do
not copy full inbox content into the repository. A reply never authorizes a
project, offer, or launch decision.

Output a `ReplyRecord`; an `opt_out` must set `suppression_applied=true`.
