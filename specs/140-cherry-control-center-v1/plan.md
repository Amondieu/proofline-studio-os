# Plan — Feature 140

## Vertical slice

1. Define the machine-readable control-plane manifest and JSON schema.
2. Document the adapter boundary and capability profiles.
3. Add offline tests for authority, profile coverage, forbidden actions, and
   runtime-status honesty.
4. Run the existing contract, unit, portability, QA, and Graphify checks.
5. Keep installation and runtime wiring as a later, separately reviewed slice.

## Design decisions

| Decision | Rationale |
|---|---|
| Cherry is internal-only in V1 | Avoids confusing a desktop workspace with the public production surface. |
| Proofline remains authoritative | Keeps contracts, evidence, and human gates independent of a UI vendor. |
| Capability profiles are explicit | Reduces accidental privilege expansion and makes review testable. |
| Codex/Hermes are adapter-required | Prevents documentation from overstating current Cherry runtime support. |
| Staging is separate from production | Creative and research tools may propose; humans decide rights and release. |
| Credentials are external | Prevents secrets and provider state from entering the repository or exported artifacts. |

## Deferred implementation

- install and pin a Cherry release after license and security review;
- implement local adapters one at a time, starting with read-only Proofline
  reports and the prompt vault;
- add Codex/Hermes adapters only after their process, permission, and output
  contracts are documented;
- add a supervised desktop smoke test with no public endpoint;
- decide whether any Cherry customization is configuration, plugin, or fork
  work after the first pilot.
