# Proofline Studio working rules

## Purpose

Proofline Studio is a human-governed operating system for producing and
launching professional websites and conversion landing pages. The repository
contains the studio's method, reusable contracts, QA harness, and a public
proof-of-work site. It is not an autonomous publishing system.

## Authority boundaries

- The harness may validate completeness, provenance, scope, and QA evidence.
- Automated checks may block a project, never approve a project for launch.
- A human must sign off discovery, message, design direction, and launch review.
- Client claims, testimonials, logos, metrics, rights, consent, and legal text
  are never invented by an agent or inferred from a template.
- Creative tools may propose assets; they do not establish rights, exclusivity,
  factuality, accessibility, or production readiness.
- Hosting, DNS, analytics, CRM, calendar, and client credentials stay outside
  this foundation slice unless a separately reviewed adapter is added.

## Change discipline

- Keep the source strategy documents and adoption map reviewable.
- Prefer small, reversible changes with a written acceptance check.
- Keep client work, credentials, exports, generated media, and local runtime
  state out of committed source material.
- Use slash-separated project-relative references in contracts and manifests.
- Run the contract validator, unit tests, and portability audit before handoff.
- Run Graphify updates after changing the configured corpus or ontology.

## Studio pipeline

The canonical order is:

`Discovery -> Message -> Direction -> Build -> QA -> Launch`

Do not skip a gate because a visual prototype looks finished. A project may be
presented as a concept while it is blocked from launch.
