# Notion Client Portal V1

<!-- v0.1 · 2026-09-23 · owner: founder · status: build later -->

This is the implementation specification for the first Notion client portal.
It turns the integration boundary in
[`docs/architecture/NOTION-CANVA-INTEGRATION.md`](../architecture/NOTION-CANVA-INTEGRATION.md)
into a small, testable workspace pattern. It is not a live Notion export or
connector configuration.

## Product promise

The client should always be able to answer three questions:

1. What is the current phase?
2. What is my one next action?
3. Which deliverables and decisions are approved?

The portal is a controlled delivery funnel:

`Kickoff → Inputs → Message approval → Direction selection → Preview → QA → Launch approval → Handover`

It is not a file dump and it does not expose internal prompts, margins,
research notes, leads, repository internals, or risk analysis.

## Workspace layers

| Layer | Audience | V1 role |
| --- | --- | --- |
| Studio HQ | Studio only | Pipeline, internal research, margins, pattern library, internal QA |
| Clients | Studio/team only | Company, contact, contract, rights, and access metadata |
| Projects | Studio/team plus filtered client view | Phase, package, links, milestones, health, next action |
| Client Portal | The client and studio | Brief, open decisions, assets, preview, feedback, handover |

The client sees only their own project page and filtered linked views. Start
with `View + Comment`; grant Edit only after a deliberate permissions review.

## Four V1 databases

### `Clients`

```text
Client name
Primary contact
Email
Company URL
Time zone
Project relation
Portal access status
Contract status
Privacy / asset rights status
Notes (internal only)
```

### `Projects`

```text
Project name
Client
Project ID
Archetype
Package
Primary conversion
Design direction
Current phase
Start date
Target launch date
Preview URL
Production URL
Repository URL (internal)
Primary approver
Revision round
Project health
Next client action
```

Standard phase values:

```text
01 — Onboarding
02 — Discovery
03 — Message approval
04 — Creative direction approval
05 — Build
06 — Client review
07 — QA
08 — Launch approval
09 — Live / handover
10 — Closed
```

The ten client-facing phases map to the canonical six studio gates. They are a
communication view, not a replacement for `Discovery → Message → Direction →
Build → QA → Launch` in the repository.

### `Decisions & Approvals`

```text
Project
Decision category
Decision requested
Options presented
Studio recommendation
Client decision
Status
Approver
Due date
Approved date
Scope impact
Evidence / URL
```

Decision categories:

`Scope · Copy · Creative direction · Brand asset · Technical integration · Legal / claims · Launch · Handover`

Statuses:

`Pending client input · Pending studio review · Approved · Approved with listed changes · Rejected · Out of scope · Escalate`

An explicit status, approver, date, and evidence link is required. “Looks good”
in a comment is not a binding approval.

### `Assets & Deliverables`

```text
Project
Asset / deliverable name
Type
Owner
Source
Rights confirmed?
AI-generated?
Real person / likeness involved?
License / release link
Status
Client review needed?
Final download / URL
Expiry date, if relevant
```

This view mirrors repository `AssetRecord` data. Missing rights, unclear
likeness permission, or an unverified claim stays blocked; it does not become a
client-facing deliverable because a file exists in Notion.

## Master portal template

Each project gets a page from one master template:

```md
# [Client] × Proofline Studio

## Your project outcome
[One measurable primary conversion]

## Current phase
[Current phase]

## What we are doing now
[Maximum three concrete actions]

## Your next action
> [One decision or asset request, with a deadline]
>
> [Open approval decision]

## Timeline
| Milestone | Owner | Status | Date |
|---|---|---|---|
| Discovery complete | Studio + Client | Pending | [Date] |
| Message map approved | Client | Pending | [Date] |
| Design direction selected | Client | Pending | [Date] |
| Build preview | Studio | Pending | [Date] |
| QA and launch approval | Client + Studio | Pending | [Date] |

## Decisions requiring your approval
[Filtered Decisions & Approvals view]

## Required assets
[Filtered Assets & Deliverables view]

## Preview and feedback
Preview link: [Staging URL]

### Feedback rules
1. Add feedback to the relevant section or decision record.
2. Choose: factual correction, copy, visual, or functionality.
3. Send one consolidated feedback round by the stated deadline.
4. New features or sections become a separate scope decision.
5. “Approved” applies only to the recorded decision.

## Final deliverables
[Filtered view: Final or Delivered only]

## Launch and handover
[Activated after launch]
- Production URL:
- Domain owner:
- Hosting owner:
- Form destination:
- Analytics owner:
- Source-code / export location:
- Final QA receipt:
- Maintenance and support window:
```

The **Your next action** block must remain singular. If five client actions are
needed, the studio resolves them into one ordered request or creates a decision
record with dependencies.

## Portal workflow

### Before sale

Keep a private prospect page with URL, archetype hypothesis, three observable
conversion leaks, offer tier, teardown link, and next outreach action. Do not
give a prospect the full client portal before engagement.

### Onboarding

Expose the agreement link, start and target dates, required inputs, brief form,
asset upload route, and the next ten-day sequence.

### Message gate

The client reviews target audience, core promise, primary CTA, proof claims,
and offer scope. No design work begins while message approval is unresolved.

### Direction gate

Show at most Precision System, Cinematic Authority, and Editorial Luxury. The
client selects one direction or records a specific change request. “Mix all
three” is a new studio decision and must be scoped.

### Preview and QA

Show the preview URL, tested items, client test items, one feedback window, and
one explicit action:

`Approve for launch · Approve with listed corrections · Request in-scope changes · Raise out-of-scope request`

### Handover

The final packet links the production URL, ownership contacts, form destination,
analytics owner, repository/export, brand assets, AI provenance, final QA
receipt, maintenance window, and update request path.

## Access and safety acceptance

- Studio Admin: full internal access.
- Studio Collaborator: project-scoped maintenance only.
- Client Approver: own project, comment, upload, and explicit decisions.
- Client Viewer: own project, status, and final deliverables only.
- No public unprotected project pages.
- No passwords, API keys, OAuth tokens, or unnecessary personal data.
- Access changes are recorded for sensitive projects.
- Access is removed or reduced after handover according to the agreement.

## Pilot acceptance test

Use the Proofline master site as a dummy client and verify:

1. a client sees only one project;
2. internal notes and repository URLs remain hidden from the client view;
3. the singular next action is obvious on desktop and mobile;
4. an approval has status, approver, date, and evidence;
5. feedback can be consolidated per revision round;
6. launch and handover fields remain pending until the corresponding gate;
7. removing portal access does not remove repository records or receipts.

Only after this pilot should a real client portal template be created.
