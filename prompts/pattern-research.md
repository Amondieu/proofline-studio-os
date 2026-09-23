# Pattern Research pass

Use this prompt in a separate research pass. It complements the broader Studio
OS research; it does not replace the repository's human gates.

```text
You are researching a reusable pattern and anti-pattern cookbook for Proofline
Studio, a human-governed landing-page studio serving B2B AI/automation,
micro-SaaS, and premium digital services.

Do not collect pretty inspiration. Extract reusable, testable principles from
official standards and documentation, credible UX research, maintained design
systems, explicit licences, and public websites used only as observational
examples.

For every candidate, separate:
- source fact;
- Proofline inference;
- implementation recommendation;
- uncertainty and missing evidence.

Use the four source levels: authoritative, strong practitioner, observational,
and inference. Never use an observational site as proof of causal conversion
impact, and never copy its expression, code, screenshots, copy, logo, asset, or
trade dress.

For each pattern answer: problem, buyer context, audience fit, required inputs,
mechanism, hypothesis, accessibility risk, performance risk, trust/legal risk,
when not to use, low-cost version, premium version, low-traffic test, success
signal, failure signal, and launch gate.

For each anti-pattern answer: temptation, failure mode, harm type, early warning,
detection, severity, replacement, exception, and launch rule.

Return records compatible with:
- schemas/pattern-record.schema.json
- schemas/anti-pattern-record.schema.json
- schemas/experiment-record.schema.json

Do not promote a pattern to approved. Mark it pilot until a local proof of
concept, QA receipt, and named human decision exist. Do not claim legal
compliance, conversion guarantees, or causality from one public example.
```

The output should be copied into the evidence log first, then reviewed into a
card. It should not be pasted directly into a client deliverable.
