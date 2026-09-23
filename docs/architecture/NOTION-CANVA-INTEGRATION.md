# Notion + Canva integration boundary

<!-- v0.1 · 2026-09-23 · owner: founder · status: planned, not connected -->

This document records the intended future role of Notion and Canva in
Proofline Studio. It is an architecture decision and implementation backlog,
not an active connector specification. No OAuth connection, API adapter,
webhook, export job, or external data sync is included in this slice.

## Decision in one sentence

GitHub remains the technical and evidentiary source of truth; Notion becomes a
human-readable operations and client-handover layer; Canva becomes a visual
sales and creative-production layer.

Neither Notion nor Canva may replace the repository, the typed contracts, the
design-system authority, the QA harness, the asset-rights log, or the human
launch gates.

## System ownership

| Concern | System of record | Later client-facing output |
| --- | --- | --- |
| Website code and component logic | GitHub repository | Client access or agreed export |
| Design tokens and direction rules | Repository, with a reviewed presentation copy | Direction board and approved summary |
| Contracts, cookbooks, and adoption map | Repository | Relevant excerpts or links |
| Website assets and usage rights | Repository asset records and rights log | Export package and usage notes |
| QA evidence and launch receipt | Repository | Handover receipt and preview links |
| Project status, decisions, feedback, and handover guidance | Notion later | Client portal |
| Pitch, teardown, direction board, and simple brand templates | Canva later | PDF, presentation, or controlled edit link |
| Secrets, passwords, API keys, OAuth tokens | Client password manager / approved secret store | Never copied into Notion or Canva |
| Sensitive CRM exports and unnecessary personal data | Client CRM or agreed data room | No duplicate by default |

## Role of Notion

Notion is the future operations and communication surface. It should make the
current phase, the next client action, the approved decisions, and the final
handover understandable without exposing implementation complexity.

### Planned Notion databases

Start with five databases, not an ERP:

1. **Prospects** — company, contact, URL, archetype hypothesis, pain
   hypothesis, tier, audit status, call status, next action, confidence.
2. **Projects** — client, `project_id`, archetype, package, primary conversion,
   direction, phase, preview URL, production URL, repository URL, owner,
   delivery date, revision round, launch status, risk level.
3. **Decisions & Approvals** — project, decision type, options, recommendation,
   client decision, date, approver, evidence link, scope impact, status.
4. **Assets & Rights** — project, asset ID, source, owner, licence, commercial
   use status, AI/likeness flags, release link, usage, approval, expiry.
5. **Pattern Library** — pattern ID, category, status, archetypes, problem,
   evidence level, accessibility risk, performance cost, implementation link,
   test result, approver, last review.

### Client portal template

Every future client portal should expose:

- project outcome and primary conversion;
- current phase: `Discovery / Message / Direction / Build / QA / Launch`;
- maximum three current-week items;
- one clearly labelled **Your next action**;
- approved decisions as a linked view;
- requested assets with owner and deadline;
- preview URL and known limitations;
- feedback rules and revision-round boundary;
- final handover, hidden or marked pending until delivery.

“Looks good” in a comment is not a formal approval. A future adapter may
display Notion decisions, but the binding approval must map to an explicit
`ApprovalRecord`, gate record, or client sign-off field in the repository.

### Notion exclusions

Do not store production secrets, API credentials, passwords, OAuth tokens,
unnecessary sensitive personal data, sole-source code, unreviewed AI assets, or
legally binding approval only as a free-text comment. Public or unclear
workspace permissions must not expose confidential client material.

## Role of Canva

Canva is the future fast, visible, client-ready layer for presentations and
simple editable assets. It is not the place where Proofline websites are
built, versioned, tested, or made accessible.

### Proofline Canva kit to build later

- three direction groups: Precision System, Cinematic Authority, Editorial
  Luxury;
- dark/light wordmarks, monogram, favicon/avatar;
- direction palettes and approved type pairings;
- `01-3-Point-Teardown`;
- `02-Authority-Sprint-Proposal`;
- `03-Creative-Direction-Board`;
- `04-Case-Study-Carousel`;
- `05-Client-Launch-Kit`.

The first useful production asset is the three-point teardown. The direction
board comes next because it gives the client a concrete, reviewable choice
before Build.

### Canva exclusions

Do not use Canva as the final responsive website source, design-token authority,
UI-state or form-validation environment, accessibility test environment, or
performance-sensitive asset pipeline. Do not promise exclusive brand assets or
rights transfers without a separate rights review. Do not upload confidential
client material until data-processing, usage, and client-permission questions
are resolved.

## Future adapter mapping

The future adapters should link external records to canonical repository IDs;
they must not create a second identity system.

| Repository record | External field/link later | Sync direction |
| --- | --- | --- |
| `StudioProject.project_id` | Notion Project ID / page URL | Repository creates link; Notion may show status |
| `ClientArchetypeAssessment` | Notion archetype + confidence + review questions | Notion captures inputs; human confirms in project record |
| `MessageMap` | Notion copy-approval view | Repository remains canonical; Notion exposes review state |
| `DesignDirection` | Canva board URL + exported reviewed artifact | Canva presents; repository stores selected direction and reference |
| `AssetRecord` | Notion Assets & Rights row | Repository rights record is authoritative |
| `ApprovalRecord` / human-gate ledger | Notion decision row and evidence link | Explicit human action only; comments are not enough |
| `QAReceipt` | Notion QA checklist and final receipt link | Repository evidence is authoritative |
| Launch receipt | Notion handover page | Repository receipt remains immutable source |

External records should carry a repository-relative ID and a source URL. A
missing link, failed permission check, or rights ambiguity must block the
relevant handoff rather than silently creating a copy.

## Planned implementation phases

### Phase 0 — documented boundary (now)

- Keep all operational and technical authority in the repository.
- Keep external-tool ideas in this document and the migration map.
- Do not install or configure a connector.

### Phase 1 — Notion client portal pilot

- Build the four V1 client databases (`Clients`, `Projects`, `Decisions &
  Approvals`, `Assets & Deliverables`) and one client portal template. The
  internal `Prospects` and `Pattern Library` views remain Studio HQ concerns.
- Run it against the Proofline master site as a dummy client.
- Test phase/status mapping, one-next-action discipline, feedback rounds, and
  handover links.
- Confirm that no secrets or unnecessary personal data enter the workspace.

### Phase 2 — Canva sales/creative pilot

- Create the Proofline Brand Kit with the three directions.
- Build and test `01-3-Point-Landing-Page-Teardown`.
- Build `03-Creative-Direction-Board` with explicit approval choices.
- Add a rights review field to every client-editable asset package.

### Phase 3 — reviewed adapters

- Specify least-privilege permissions and data retention.
- Map records to canonical repository IDs.
- Add export/link receipts and failure handling.
- Require human review before any status or approval is written back.
- Pilot with one internal project before a real client.

The executable specifications are:

- `docs/operations/NOTION-CLIENT-PORTAL-V1.md`
- `docs/operations/CANVA-SALES-TEMPLATES-V1.md`

## Acceptance gates before any connector

- Scope and data map reviewed by the founder.
- Workspace permissions and client visibility tested.
- Secrets and sensitive-data exclusion tested.
- Asset rights and Canva content decisions recorded.
- Notion decision statuses map to explicit repository decisions.
- Canva exports retain source, version, and rights references.
- QA, launch authority, and human sign-off remain repository-owned.
- Disconnect/export/recovery procedure documented.

## Reference links to revalidate at implementation time

The following links were supplied as research context and should be checked
again before building an adapter because vendor features, terms, and licensing
can change:

- [Notion project documentation](https://www.notion.com/use-case/project-management/project-documentation)
- [Canva creative operating system](https://www.canva.com/newsroom/news/creative-operating-system/)
- [Canva Brand Kit best practices](https://www.canva.com/help/brand-kit-best-practices/)
- [Canva Brand Kit usage](https://www.canva.com/help/brand-kit-usage/)

This repository’s existing authority boundary remains controlling if a vendor
feature conflicts with it.
