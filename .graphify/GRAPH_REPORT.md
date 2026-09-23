# Graph Report - .  (2026-09-23)

## Corpus Check
- 103 files · ~52.452 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 131 nodes · 258 edges · 8 communities detected
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 47 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: contains: 65 · uses: 47 · MODIFIES: 46 · inherits: 34 · rationale_for: 21 · ON_BRANCH: 12 · method: 10 · PARENT_OF: 10 · calls: 8 · imports_from: 5


## Input Scope
- Requested: all
- Resolved: all (source: cli)
- Included files: 103 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `7bf1318`
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
Cohesion: 0.13
Nodes (25): BaseModel, AccessibilityReceipt, AIAssetDetails, ApprovalRecord, AssetRecord, BuildChecklist, Contract, DesignDirection (+17 more)

### Community 1 - "Community 1"
Cohesion: 0.14
Nodes (14): main, 140ed8b feat: adopt research receipts and QA gate, 7bc151b chore: ignore local graphify lifecycle state, cb77a61 feat: create focused landing studio foundation, 140ed8b feat: adopt research receipts and QA gate, 7bc151b chore: ignore local graphify lifecycle state, 80a73c6 chore: separate Graphify profile and code refresh, b89c46f feat: add evidence-backed pattern cookbook (+6 more)

### Community 2 - "Community 2"
Cohesion: 0.15
Nodes (18): Contract, StrEnum, AntiPatternRecord, AntiPatternSeverity, calculate_pattern_readiness(), EvidenceLevel, EvidenceRef, ExperimentRecord (+10 more)

### Community 3 - "Community 3"
Cohesion: 0.15
Nodes (14): main, 57970cd feat: add business archetype systems, 7bf1318 docs: define Notion and Canva integration boundary, 80a73c6 chore: separate Graphify profile and code refresh, b89c46f feat: add evidence-backed pattern cookbook, Business-archetype contracts and deterministic recommendation helpers., Return a recommendation and confidence without confirming fit or approval., recommend_archetype() (+6 more)

### Community 4 - "Community 4"
Cohesion: 0.27
Nodes (10): evaluate_project(), Read-only gate evaluation and explicit human gate recording.  The evaluator is i, Append one explicit human decision to a hash-chained local ledger., Append one explicit human decision to a hash-chained local ledger., Return a deterministic, non-authoritative project readiness report., Return a deterministic, non-authoritative project readiness report., record_human_gate(), _result() (+2 more)

### Community 5 - "Community 5"
Cohesion: 0.20
Nodes (8): artDirection, buttons, directionCta, directionData, previewBody, previewEyebrow, previewTitle, stageLabel

### Community 6 - "Community 6"
Cohesion: 0.43
Nodes (6): normalize_relative_path(), PortablePathError, Cross-platform project-relative reference rules., Raised when a contract reference is not portable or project-bounded., safe_project_path(), ValueError

### Community 7 - "Community 7"
Cohesion: 0.40
Nodes (4): manifest, manifestPath, normalized, root

## Knowledge Gaps
- **21 isolated node(s):** `root`, `manifestPath`, `manifest`, `normalized`, `Check the focused repo for unsafe absolute project references.` (+16 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Contract` connect `Community 0` to `Community 2`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.264) - this node is a cross-community bridge._
- **Why does `StudioHarnessTests` connect `Community 0` to `Community 1`, `Community 4`, `Community 6`?**
  _High betweenness centrality (0.165) - this node is a cross-community bridge._
- **Why does `StudioProject` connect `Community 4` to `Community 1`, `Community 0`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `Contract` (e.g. with `AntiPatternRecord` and `AntiPatternSeverity`) actually correct?**
  _`Contract` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `StudioHarnessTests` (e.g. with `AccessibilityReceipt` and `AIAssetDetails`) actually correct?**
  _`StudioHarnessTests` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `StudioProject` (e.g. with `Dependency-light structural checks for the focused studio repo.` and `Operator CLI for the read-only studio harness.`) actually correct?**
  _`StudioProject` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `root`, `manifestPath`, `manifest` to the rest of the system?**
  _21 weakly-connected nodes found - possible documentation gaps or missing edges._