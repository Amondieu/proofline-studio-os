# Proofline Studio operating model

## Objective

Turn a complex client offer into a clear, high-trust landing-page system that
can be shipped in a fixed window and maintained by the client. The deliverable
is not “an AI website”; it is message clarity, visual credibility, a working
conversion path, and verified launch quality.

## System boundary

```text
Client evidence + brief
          |
          v
Discovery -> Message -> Direction -> Build -> QA -> Human launch decision
     |          |           |          |       |
     +----------+-----------+----------+-------+--> project manifest + evidence
```

The harness sits beside the delivery workflow. It reads the manifest and
returns a deterministic report. It does not write a package, call a provider,
change a client system, deploy a site, or grant legal clearance.

## Authority model

| Actor | Can do | Cannot do |
|---|---|---|
| Harness | Validate shape, completeness, scope, submitted QA, and provenance fields | Approve, publish, deploy, certify lawfulness, verify truth |
| Studio operator | Draft strategy, copy, design, code, QA evidence, and recommendations | Invent proof or transfer client ownership without agreement |
| Client | Confirm offer, claims, assets, direction, and launch approval | Delegate legal responsibility implicitly to the studio |
| Creative tool | Produce candidate references or assets under an approved brief | Establish rights, exclusivity, factuality, or accessibility |

## Gate semantics

1. **Discovery** — the buyer, offer, economics, buying situation, proof, and
   constraints are explicit. Missing proof creates an assumption map and blocks
   final production.
2. **Message** — the message map freezes the target, pain, outcome, mechanism,
   promise, CTA, objections, and section structure before visual production.
3. **Direction** — one creative direction is selected from a controlled system;
   it includes desktop and mobile review.
4. **Build** — the implementation works across required widths, routes CTAs,
   delivers forms, has metadata, and records rights/access/backup checks.
5. **QA** — mobile conversion, technical behavior, trust, legal links,
   accessibility, motion, and consent are reviewed.
6. **Launch** — a named human and the client explicitly approve the reviewed
   state. The current harness reports `readyForHumanLaunchReview`; it never
   returns `readyToLaunch: true`.

## Evidence rule

Every high-consequence statement should have one of four evidence types:

- **demonstrated method** — the studio shows the method or artefact itself;
- **stated standard** — a documented standard with a corresponding receipt;
- **permissioned quote** — verbatim client feedback with permission recorded;
- **labelled concept work** — fictional or exploratory work marked as such.

Unresolved assumptions remain in the project brief and are not evidence. The
studio must never turn an assumption or concept into a testimonial, customer
logo, metric, legal claim, or case-study result.
