# Source-to-Studio adoption map

This repository is a focused derivative of `1AIViralINfluencer`. It keeps the
governance patterns that make a professional studio dependable and removes
domain machinery that belongs to social-media publishing.

## Keep and adapt

| Source capability | Studio treatment | Why |
|---|---|---|
| Nexus-style human authority boundaries | `studio/harness.py`, architecture docs | Automated checks can block and explain, but a human launches. |
| Portable project-relative paths | `studio/portability.py` and audit | Client manifests must travel between Windows, macOS, and CI. |
| Versioned, strict contracts | `schemas/studio/` + Pydantic models | A studio needs repeatable handoffs, not prompt-shaped memory. |
| Evidence/provenance thinking | project fields, asset-rights checks, gate ledger | Claims, assets, decisions, and sign-offs need traceability. |
| Append-only hash chain | `record_human_gate()` | Corrections remain visible instead of rewriting history. |
| Graphify-ready source corpus | `graphify.yaml` + studio ontology | Strategy and standards remain retrievable and reviewable. |
| Human review / compliance gates | Discovery, message, build, and launch gates | Quality is a process and ownership boundary, not a visual style. |

## Exclude from the first studio slice

| Source capability | Decision | Reason |
|---|---|---|
| Mamie/social content pipeline | Exclude | Wrong delivery object; a landing-page project is not a post package. |
| Viral-idea cookbook and persona arena | Exclude | Useful for creator research, not required for client web delivery. |
| Ruflo editorial swarm | Exclude | No autonomous content swarm is needed to run the studio method. |
| Laya calibration and model routing | Exclude | No decision model should silently shape client claims or approvals. |
| Social scheduler, Postiz, n8n, platform adapters | Exclude | Live integrations need separate security, account, and contract reviews. |
| Higgsfield/provider credentials | Exclude | Tools may be used externally as a creative layer; this repo stores no secrets. |
| RTK/SuperCompress | Exclude | Terminal/context optimization is not part of the studio client contract yet. |
| Influencer character and realistic-AI policy bundle | Adapt selectively | Keep disclosure, rights, and no-fabrication principles; remove persona-specific rules. |

## New studio-specific surface

- Six delivery gates with explicit acceptance criteria.
- A project manifest for discovery, message map, selected direction, build QA,
  and launch review.
- Three controlled creative directions: Precision System, Cinematic Authority,
  and Editorial Luxury.
- Fixed-scope offers and a teardown-led funnel.
- A local master site that demonstrates the method without inventing client
  work or performance results.

## Acceptance check

The derivative is considered correctly focused when a new operator can answer,
from this repository alone:

1. What does the studio sell and to whom?
2. What must be true before design and build begin?
3. Which checks block launch?
4. Which actions still require a human?
5. Which source-system capabilities are intentionally not present?
