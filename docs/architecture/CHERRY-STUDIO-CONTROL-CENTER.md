# Cherry Studio Control Center

Status: `architecture proposal / internal-only`

Cherry Studio can be useful as a desktop workspace for operators who need one
place to inspect research, prompt candidates, local creative jobs, QA receipts,
and bounded agent actions. In Proofline it is a surface, not the operating
authority.

In this repository Cherry is an internal desktop control plane, not a public
application or an autonomous agent authority.

## Position in the system

```text
Cherry Studio (desktop UI)
       |
       +-- read-only Proofline reports and gate history
       +-- reviewed MCP/local adapters
       +-- staged prompt and asset proposals
       |
       v
Proofline contracts + harness + human-gate ledger
       |
       v
human decision: discovery / message / direction / legal-rights / launch
```

The public `site/` and any future production client site remain outside Cherry.
Cherry must not become a public backend, a deployment credential holder, or a
replacement for the harness.

## Capability map

| Area | Cherry may surface | Proofline still controls |
|---|---|---|
| Research | Agent-Reach findings, Screenpipe-derived local notes, source-register candidates | source provenance, privacy, retention, factual interpretation |
| Creative | prompt-vault candidates, Lykos/ComfyUI staging jobs, Higgsfield prompt packs | asset rights, disclosure, accessibility, production approval |
| Build | workspace context, Codex task proposals, local test commands | repository contracts, reviewable changes, deployment boundary |
| QA | readiness, contrast, portable, Graphify, and harness receipts | interpretation of blockers and launch decision |
| Launch | read-only status and human-gate history | named human/client approval and actual release |

## Adapter rules

Every adapter must declare:

- its transport (`local`, `MCP`, or another explicitly reviewed boundary);
- the data classes it receives and returns;
- allowed operations and forbidden operations;
- whether it can write only staging artifacts or can touch a workspace;
- redaction and retention behavior;
- a deterministic test receipt and a human activation decision.

The current manifest intentionally marks Codex and Hermes as
`adapter_required`. This means the concept is reserved in the architecture;
it is not a claim that Cherry currently ships those integrations.

## Data and license boundary

Provider credentials, raw screen/audio/OCR captures, client secrets, generated
exports, and local model/runtime state stay outside Git. Only derived,
reviewable evidence should enter the repository, and only after the relevant
privacy, rights, and source review.

Cherry's community/enterprise licensing and every connected provider, model,
MCP server, and creative service must be reviewed independently. A UI
connection does not grant rights to copy, redistribute, publish, or use an
output commercially.

## Activation sequence

1. Review the manifest and the selected Cherry release.
2. Keep all profiles disabled by default.
3. Activate one read-only adapter in a local pilot.
4. Run contract, privacy, portability, and security checks.
5. Record human approval for the specific adapter and scope.
6. Expand capabilities only through a new versioned contract.
