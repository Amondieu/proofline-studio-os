# Feature 140 — Cherry Studio Control Center V1

Status: `proposed / internal pilot contract only`

Define Cherry Studio as an optional internal desktop control plane for
Proofline Studio. Cherry may present context and route work to reviewed local
adapters, but it is never the source of truth for project contracts, rights,
legal status, client consent, or launch authority.

## Scope

This feature covers the capability boundary, adapter vocabulary, data boundary,
and review evidence needed before any Cherry deployment. It does not install
Cherry, fork Cherry, add provider credentials, expose a public endpoint, or
claim that Codex or Hermes are native Cherry runtimes.

## Requirements

- FR-140-01: Cherry is labelled as an `internal_desktop_control_plane`; the
  Proofline harness and versioned contracts remain authoritative.
- FR-140-02: The control plane exposes least-privilege profiles for research,
  creative, build, QA, and launch-read-only work.
- FR-140-03: Every external capability is reached through an explicit adapter
  with a declared transport, data class, allowed operations, and forbidden
  operations.
- FR-140-04: Discovery, message, direction, rights/legal, client, and launch
  decisions remain human-gated. No profile can approve or override them.
- FR-140-05: Credentials, raw Screenpipe captures, client secrets, and local
  runtime state remain outside committed source material and are not exported
  through the control plane.
- FR-140-06: Prompt routing and model selection may propose a route or retrieve
  a versioned prompt, but may not silently send sensitive context or promote a
  draft prompt/asset to production.
- FR-140-07: Codex and Hermes are represented as adapter-required runtimes in
  V1; the manifest must not imply a native integration that has not been
  implemented and reviewed.
- FR-140-08: The launch-read-only profile can inspect reports and gate history,
  but cannot write, deploy, approve, or publish.
- FR-140-09: Any future adapter activation must produce a reviewable capability
  manifest and a deterministic contract/test receipt before use.
- FR-140-10: Cherry's applicable AGPL/community license, enterprise terms, and
  each provider/model license remain separate review items; the control-plane
  contract does not grant redistribution or production-use rights.

## Non-goals

- autonomous publishing, deployment, outreach, or client communication;
- replacing the Proofline harness or human-gate ledger;
- storing provider credentials, client data, or generated exports in Git;
- making Cherry the public Proofline website or its production backend;
- assuming that an MCP connection establishes factuality, rights,
  accessibility, or launch readiness.

## Authority rule

```text
Cherry UI -> reviewed adapter -> Proofline contract / staging artifact
                                      |
                                      v
                             deterministic checks
                                      |
                                      v
                              human gate decision
```

The UI can make work discoverable and faster. It cannot turn a recommendation
into approval.
