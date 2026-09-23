# Acceptance — Feature 140

| ID | Acceptance statement | Evidence | Status |
|---|---|---|---|
| AC-140-01 | Manifest identifies Cherry as an internal desktop control plane with Proofline authority | `config/studio/cherry-control-center.v1.json` | pass |
| AC-140-02 | All five least-privilege profiles are present | manifest + `tests/test_cherry_control_center.py` | pass |
| AC-140-03 | External modules have explicit adapter status and operation boundaries | manifest + architecture note | pass |
| AC-140-04 | Launch, legal, rights, client, and deployment authority is forbidden | manifest + offline test | pass |
| AC-140-05 | Sensitive data and runtime credentials are outside the committed boundary | manifest + architecture note | pass |
| AC-140-06 | Codex and Hermes are marked adapter-required rather than native | manifest + offline test | pass |
| AC-140-07 | Repository contracts, unit tests, portability, QA matrix, and Graphify checks pass | `qa-receipt.md` | pass |
| AC-140-08 | Cherry installation and runtime activation remain explicitly deferred | `tasks.md` + `converge.md` | pass |

The acceptance of this feature authorizes a reviewable contract only. It does
not authorize installing Cherry, connecting accounts, or activating a runtime.
