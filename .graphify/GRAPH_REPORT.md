# Graph Report - .  (2026-09-23)

## Corpus Check
- Corpus is ~49.005 words - fits in a single context window. You may not need a graph.

## Summary
- 123 nodes · 220 edges · 13 communities detected
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 47 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: contains: 65 · uses: 47 · inherits: 34 · MODIFIES: 21 · rationale_for: 21 · method: 10 · calls: 8 · imports_from: 5 · ON_BRANCH: 5 · PARENT_OF: 4


## Input Scope
- Requested: all
- Resolved: all (source: cli)
- Included files: 100 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `b89c46f`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Contract` - 34 edges
2. `StudioHarnessTests` - 23 edges
3. `StudioProject` - 11 edges
4. `CookbookContractTests` - 8 edges
5. `ClientArchetypeAssessment` - 6 edges
6. `PortablePathError` - 6 edges
7. `ArchetypeRecord` - 5 edges
8. `Business-archetype contracts and deterministic recommendation helpers.` - 4 edges
9. `Return a recommendation and confidence without confirming fit or approval.` - 4 edges
10. `EvidenceLevel` - 4 edges

## Surprising Connections (you probably didn't know these)
- `Dependency-light structural checks for the focused studio repo.` --uses--> `StudioProject`  [INFERRED]
  scripts/validate_studio_contracts.py → studio/models.py
- `StudioHarnessTests` --uses--> `StudioProject`  [INFERRED]
  tests/test_studio_harness.py → studio/models.py
- `StudioHarnessTests` --uses--> `PortablePathError`  [INFERRED]
  tests/test_studio_harness.py → studio/portability.py
- `Operator CLI for the read-only studio harness.` --uses--> `StudioProject`  [INFERRED]
  studio/cli.py → studio/models.py
- `Contracts for the evidence-backed pattern and anti-pattern cookbook.` --uses--> `Contract`  [INFERRED]
  studio/cookbook.py → studio/models.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.15
Nodes (25): BaseModel, AccessibilityReceipt, AIAssetDetails, ApprovalRecord, ArchetypeScore, AssetRecord, BuildChecklist, Contract (+17 more)

### Community 1 - "Community 1"
Cohesion: 0.15
Nodes (18): Contract, StrEnum, AntiPatternRecord, AntiPatternSeverity, calculate_pattern_readiness(), EvidenceLevel, EvidenceRef, ExperimentRecord (+10 more)

### Community 2 - "Community 2"
Cohesion: 0.18
Nodes (8): Business-archetype contracts and deterministic recommendation helpers., Return a recommendation and confidence without confirming fit or approval., recommend_archetype(), ArchetypeRecord, ClientArchetypeAssessment, A human-reviewed business archetype blueprint, not an industry template., A recommendation record; it cannot approve a direction, offer, or launch., ArchetypeContractTests

### Community 3 - "Community 3"
Cohesion: 0.20
Nodes (8): artDirection, buttons, directionCta, directionData, previewBody, previewEyebrow, previewTitle, stageLabel

### Community 4 - "Community 4"
Cohesion: 0.32
Nodes (8): evaluate_project(), Append one explicit human decision to a hash-chained local ledger., Append one explicit human decision to a hash-chained local ledger., Return a deterministic, non-authoritative project readiness report., Return a deterministic, non-authoritative project readiness report., record_human_gate(), _result(), StudioProject

### Community 5 - "Community 5"
Cohesion: 0.33
Nodes (3): cb77a61 feat: create focused landing studio foundation, Read-only gate evaluation and explicit human gate recording.  The evaluator is i, Proofline Studio's human-governed delivery harness.

### Community 6 - "Community 6"
Cohesion: 0.43
Nodes (6): normalize_relative_path(), PortablePathError, Cross-platform project-relative reference rules., Raised when a contract reference is not portable or project-bounded., safe_project_path(), ValueError

### Community 7 - "Community 7"
Cohesion: 0.53
Nodes (5): main, 140ed8b feat: adopt research receipts and QA gate, 7bc151b chore: ignore local graphify lifecycle state, 80a73c6 chore: separate Graphify profile and code refresh, b89c46f feat: add evidence-backed pattern cookbook

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
Nodes (1): Operator CLI for the read-only studio harness.

### Community 13 - "Community 13"
Cohesion: 0.67
Nodes (1): make_project()

## Knowledge Gaps
- **21 isolated node(s):** `root`, `manifestPath`, `manifest`, `normalized`, `Check the focused repo for unsafe absolute project references.` (+16 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 11`** (1 nodes): `Check the focused repo for unsafe absolute project references.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (1 nodes): `Operator CLI for the read-only studio harness.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (1 nodes): `make_project()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Contract` connect `Community 0` to `Community 1`, `Community 2`, `Community 4`?**
  _High betweenness centrality (0.310) - this node is a cross-community bridge._
- **Why does `StudioHarnessTests` connect `Community 0` to `Community 5`, `Community 4`, `Community 6`, `Community 13`?**
  _High betweenness centrality (0.181) - this node is a cross-community bridge._
- **Why does `StudioProject` connect `Community 4` to `Community 9`, `Community 12`, `Community 5`, `Community 0`?**
  _High betweenness centrality (0.150) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `Contract` (e.g. with `AntiPatternRecord` and `AntiPatternSeverity`) actually correct?**
  _`Contract` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `StudioHarnessTests` (e.g. with `AccessibilityReceipt` and `AIAssetDetails`) actually correct?**
  _`StudioHarnessTests` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `StudioProject` (e.g. with `Dependency-light structural checks for the focused studio repo.` and `Operator CLI for the read-only studio harness.`) actually correct?**
  _`StudioProject` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `root`, `manifestPath`, `manifest` to the rest of the system?**
  _21 weakly-connected nodes found - possible documentation gaps or missing edges._