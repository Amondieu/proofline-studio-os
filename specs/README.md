# Spec-driven vertical slice

The WITHKODEX portfolio work is intentionally decomposed into independently
reviewable features:

```text
100 Master Site
  └── 110 Proofline Route
        ├── 120 AI / Automation Authority
        └── 130 Interest-Only Teardown
```

Each feature has `spec.md → plan.md → tasks.md → implement → converge`, with
acceptance, traceability, and QA evidence kept beside the feature. The current
bundles are planning-only; their unchecked tasks are not a claim that the
external site has been implemented.

This follows the current GitHub Spec Kit core workflow. For production-grade
features, add clarification, checklist, and cross-artifact analysis gates where
the human review needs them. The repository Constitution remains the authority
for human gates and launch safety.

Reference: [GitHub Spec Kit](https://github.com/github/spec-kit).
