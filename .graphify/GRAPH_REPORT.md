# Graph Report - .  (2026-09-23)

## Corpus Check
- Corpus is ~45.437 words - fits in a single context window. You may not need a graph.

## Summary
- 108 nodes · 193 edges · 15 communities detected
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 41 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: contains: 60 · uses: 41 · inherits: 31 · MODIFIES: 18 · rationale_for: 17 · calls: 8 · method: 7 · imports_from: 4 · ON_BRANCH: 4 · PARENT_OF: 3


## Input Scope
- Requested: all
- Resolved: all (source: cli)
- Included files: 90 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `80a73c6`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Contract` - 31 edges
2. `StudioHarnessTests` - 23 edges
3. `StudioProject` - 11 edges
4. `CookbookContractTests` - 8 edges
5. `PortablePathError` - 6 edges
6. `EvidenceLevel` - 4 edges
7. `EvidenceRef` - 4 edges
8. `PatternScores` - 4 edges
9. `PatternRecord` - 4 edges
10. `AntiPatternRecord` - 4 edges

## Surprising Connections (you probably didn't know these)
- `Dependency-light structural checks for the focused studio repo.` --uses--> `StudioProject`  [INFERRED]
  scripts/validate_studio_contracts.py → studio/models.py
- `StudioHarnessTests` --uses--> `AccessibilityReceipt`  [INFERRED]
  tests/test_studio_harness.py → studio/models.py
- `StudioHarnessTests` --uses--> `AIAssetDetails`  [INFERRED]
  tests/test_studio_harness.py → studio/models.py
- `StudioHarnessTests` --uses--> `AssetRecord`  [INFERRED]
  tests/test_studio_harness.py → studio/models.py
- `StudioHarnessTests` --uses--> `BuildChecklist`  [INFERRED]
  tests/test_studio_harness.py → studio/models.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.15
Nodes (18): Contract, StrEnum, AntiPatternRecord, AntiPatternSeverity, calculate_pattern_readiness(), EvidenceLevel, EvidenceRef, ExperimentRecord (+10 more)

### Community 1 - "Community 1"
Cohesion: 0.25
Nodes (13): BaseModel, AccessibilityReceipt, AIAssetDetails, BuildChecklist, Contract, DesignDirection, FormReceipt, LaunchReview (+5 more)

### Community 2 - "Community 2"
Cohesion: 0.27
Nodes (9): evaluate_project(), Read-only gate evaluation and explicit human gate recording.  The evaluator is i, Append one explicit human decision to a hash-chained local ledger., Append one explicit human decision to a hash-chained local ledger., Return a deterministic, non-authoritative project readiness report., Return a deterministic, non-authoritative project readiness report., record_human_gate(), _result() (+1 more)

### Community 3 - "Community 3"
Cohesion: 0.20
Nodes (8): artDirection, buttons, directionCta, directionData, previewBody, previewEyebrow, previewTitle, stageLabel

### Community 4 - "Community 4"
Cohesion: 0.25
Nodes (5): DiscoveryBrief, LegalReceipt, PerformanceReceipt, RollbackReceipt, StudioHarnessTests

### Community 5 - "Community 5"
Cohesion: 0.29
Nodes (3): cb77a61 feat: create focused landing studio foundation, Operator CLI for the read-only studio harness., Proofline Studio's human-governed delivery harness.

### Community 6 - "Community 6"
Cohesion: 0.43
Nodes (6): normalize_relative_path(), PortablePathError, Cross-platform project-relative reference rules., Raised when a contract reference is not portable or project-bounded., safe_project_path(), ValueError

### Community 7 - "Community 7"
Cohesion: 0.60
Nodes (4): main, 140ed8b feat: adopt research receipts and QA gate, 7bc151b chore: ignore local graphify lifecycle state, 80a73c6 chore: separate Graphify profile and code refresh

### Community 8 - "Community 8"
Cohesion: 0.40
Nodes (4): manifest, manifestPath, normalized, root

### Community 9 - "Community 9"
Cohesion: 0.67
Nodes (3): _load(), Dependency-light structural checks for the focused studio repo., validate()

### Community 11 - "Community 11"
Cohesion: 0.67
Nodes (1): Check the focused repo for unsafe absolute project references.

### Community 12 - "Community 12"
Cohesion: 0.67
Nodes (1): make_project()

### Community 13 - "Community 13"
Cohesion: 1.00
Nodes (2): ApprovalRecord, Detailed, append-only human approval that supplements the gate hash ledger.

### Community 14 - "Community 14"
Cohesion: 1.00
Nodes (2): AssetRecord, Traceable asset rights record; AI client material is rejected by contract.

### Community 15 - "Community 15"
Cohesion: 1.00
Nodes (2): QAReceipt, Human-authored evidence receipt; passing it never grants launch authority.

## Knowledge Gaps
- **19 isolated node(s):** `root`, `manifestPath`, `manifest`, `normalized`, `Check the focused repo for unsafe absolute project references.` (+14 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 11`** (1 nodes): `Check the focused repo for unsafe absolute project references.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (1 nodes): `make_project()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (2 nodes): `ApprovalRecord`, `Detailed, append-only human approval that supplements the gate hash ledger.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (2 nodes): `AssetRecord`, `Traceable asset rights record; AI client material is rejected by contract.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (2 nodes): `QAReceipt`, `Human-authored evidence receipt; passing it never grants launch authority.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Contract` connect `Community 1` to `Community 0`, `Community 13`, `Community 14`, `Community 4`, `Community 15`, `Community 2`?**
  _High betweenness centrality (0.335) - this node is a cross-community bridge._
- **Why does `StudioHarnessTests` connect `Community 4` to `Community 2`, `Community 1`, `Community 14`, `Community 15`, `Community 6`, `Community 12`?**
  _High betweenness centrality (0.217) - this node is a cross-community bridge._
- **Why does `StudioProject` connect `Community 2` to `Community 9`, `Community 5`, `Community 1`, `Community 4`?**
  _High betweenness centrality (0.180) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `Contract` (e.g. with `AntiPatternRecord` and `AntiPatternSeverity`) actually correct?**
  _`Contract` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `StudioHarnessTests` (e.g. with `AccessibilityReceipt` and `AIAssetDetails`) actually correct?**
  _`StudioHarnessTests` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `StudioProject` (e.g. with `Dependency-light structural checks for the focused studio repo.` and `Operator CLI for the read-only studio harness.`) actually correct?**
  _`StudioProject` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `root`, `manifestPath`, `manifest` to the rest of the system?**
  _19 weakly-connected nodes found - possible documentation gaps or missing edges._