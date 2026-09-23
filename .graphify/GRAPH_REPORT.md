# Graph Report - .  (2026-09-23)

## Corpus Check
- 101 files · ~50.366 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 130 nodes · 256 edges · 9 communities detected
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 47 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: contains: 65 · uses: 47 · MODIFIES: 46 · inherits: 34 · rationale_for: 21 · ON_BRANCH: 11 · method: 10 · PARENT_OF: 9 · calls: 8 · imports_from: 5


## Input Scope
- Requested: all
- Resolved: all (source: cli)
- Included files: 101 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `57970cd`
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
- `Contracts for the evidence-backed pattern and anti-pattern cookbook.` --uses--> `Contract`  [INFERRED]
  studio/cookbook.py → studio/models.py
- `Calculate the cookbook score using the declared V1 weights.` --uses--> `Contract`  [INFERRED]
  studio/cookbook.py → studio/models.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.13
Nodes (19): main, main, 140ed8b feat: adopt research receipts and QA gate, 57970cd feat: add business archetype systems, 7bc151b chore: ignore local graphify lifecycle state, 80a73c6 chore: separate Graphify profile and code refresh, b89c46f feat: add evidence-backed pattern cookbook, cb77a61 feat: create focused landing studio foundation (+11 more)

### Community 1 - "Community 1"
Cohesion: 0.15
Nodes (25): BaseModel, AccessibilityReceipt, AIAssetDetails, ApprovalRecord, ArchetypeScore, AssetRecord, BuildChecklist, Contract (+17 more)

### Community 2 - "Community 2"
Cohesion: 0.15
Nodes (18): Contract, StrEnum, AntiPatternRecord, AntiPatternSeverity, calculate_pattern_readiness(), EvidenceLevel, EvidenceRef, ExperimentRecord (+10 more)

### Community 3 - "Community 3"
Cohesion: 0.18
Nodes (8): Business-archetype contracts and deterministic recommendation helpers., Return a recommendation and confidence without confirming fit or approval., recommend_archetype(), ArchetypeRecord, ClientArchetypeAssessment, A human-reviewed business archetype blueprint, not an industry template., A recommendation record; it cannot approve a direction, offer, or launch., ArchetypeContractTests

### Community 4 - "Community 4"
Cohesion: 0.22
Nodes (9): Operator CLI for the read-only studio harness., evaluate_project(), Append one explicit human decision to a hash-chained local ledger., Append one explicit human decision to a hash-chained local ledger., Return a deterministic, non-authoritative project readiness report., Return a deterministic, non-authoritative project readiness report., record_human_gate(), _result() (+1 more)

### Community 5 - "Community 5"
Cohesion: 0.20
Nodes (8): artDirection, buttons, directionCta, directionData, previewBody, previewEyebrow, previewTitle, stageLabel

### Community 6 - "Community 6"
Cohesion: 0.43
Nodes (6): normalize_relative_path(), PortablePathError, Cross-platform project-relative reference rules., Raised when a contract reference is not portable or project-bounded., safe_project_path(), ValueError

### Community 7 - "Community 7"
Cohesion: 0.40
Nodes (4): manifest, manifestPath, normalized, root

### Community 8 - "Community 8"
Cohesion: 0.67
Nodes (1): make_project()

## Knowledge Gaps
- **21 isolated node(s):** `root`, `manifestPath`, `manifest`, `normalized`, `Check the focused repo for unsafe absolute project references.` (+16 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 8`** (1 nodes): `make_project()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Contract` connect `Community 1` to `Community 2`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.266) - this node is a cross-community bridge._
- **Why does `StudioHarnessTests` connect `Community 1` to `Community 0`, `Community 4`, `Community 6`, `Community 8`?**
  _High betweenness centrality (0.166) - this node is a cross-community bridge._
- **Why does `StudioProject` connect `Community 4` to `Community 0`, `Community 1`?**
  _High betweenness centrality (0.139) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `Contract` (e.g. with `AntiPatternRecord` and `AntiPatternSeverity`) actually correct?**
  _`Contract` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `StudioHarnessTests` (e.g. with `AccessibilityReceipt` and `AIAssetDetails`) actually correct?**
  _`StudioHarnessTests` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `StudioProject` (e.g. with `Dependency-light structural checks for the focused studio repo.` and `Operator CLI for the read-only studio harness.`) actually correct?**
  _`StudioProject` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `root`, `manifestPath`, `manifest` to the rest of the system?**
  _21 weakly-connected nodes found - possible documentation gaps or missing edges._