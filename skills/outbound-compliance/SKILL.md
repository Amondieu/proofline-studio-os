---
name: outbound-compliance
description: Run the Proofline no-send and human approval checks for a proposed outbound message.
---

# Outbound compliance envelope

Read `docs/strategy/26-OUTREACH-COMPLIANCE-FR-EU.md` and the official CNIL
references linked there. This is an internal control layer, not legal advice.

Check professional relevance, source/collection record, data minimisation,
legal-basis review, suppression, sender identity, privacy information, free
objection route, factual evidence, exact recipient, exact message, and domain
authentication. If any required check is unresolved, mark the draft blocked.

Only a human may create a `SendApproval`. This skill never sends, queues, or
marks a message as sent.
