# Graph Report - .  (2026-09-23)

## Corpus Check
- 128 files · ~59.771 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 205 nodes · 424 edges · 10 communities detected
- Extraction: 75% EXTRACTED · 25% INFERRED · 0% AMBIGUOUS · INFERRED: 104 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: uses: 104 · contains: 95 · inherits: 54 · MODIFIES: 49 · rationale_for: 34 · method: 33 · calls: 22 · ON_BRANCH: 14 · PARENT_OF: 12 · imports_from: 7


## Input Scope
- Requested: all
- Resolved: all (source: cli)
- Included files: 128 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `13df31c`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Contract` - 69 edges
2. `StudioHarnessTests` - 23 edges
3. `LayaAdvisoryTests` - 16 edges
4. `FakeLayaAdapter` - 13 edges
5. `StudioProject` - 11 edges
6. `LayaAdvisoryEngine` - 10 edges
7. `LayaRequest` - 8 edges
8. `LayaDecision` - 8 edges
9. `CookbookContractTests` - 8 edges
10. `Operator CLI for the read-only studio harness.` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Dependency-light structural checks for the focused studio repo.` --uses--> `StudioProject`  [INFERRED]
  scripts/validate_studio_contracts.py → studio/models.py
- `FakeLayaAdapter` --uses--> `CalibrationStatus`  [INFERRED]
  tests/test_laya.py → studio/laya.py
- `FakeLayaAdapter` --uses--> `LayaTask`  [INFERRED]
  tests/test_laya.py → studio/laya.py
- `LayaAdvisoryTests` --uses--> `CalibrationStatus`  [INFERRED]
  tests/test_laya.py → studio/laya.py
- `LayaAdvisoryTests` --uses--> `LayaTask`  [INFERRED]
  tests/test_laya.py → studio/laya.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (33): main, main, 13df31c feat: add human-gated outbound intelligence module, 140ed8b feat: adopt research receipts and QA gate, 142dc46 docs: specify Notion portal and Canva templates, 57970cd feat: add business archetype systems, 7bc151b chore: ignore local graphify lifecycle state, 7bf1318 docs: define Notion and Canva integration boundary (+25 more)

### Community 1 - "Community 1"
Cohesion: 0.09
Nodes (19): LayaAdvisoryEngine, LayaDecision, LayaEvaluationRecord, LayaModel, LayaRequest, _normalise_answer(), Optional Laya advisory layer with hard Proofline authority boundaries., Human-labelled feedback used to measure agreement and calibration. (+11 more)

### Community 2 - "Community 2"
Cohesion: 0.12
Nodes (28): BaseModel, AccessibilityReceipt, AIAssetDetails, ApprovalRecord, ArchetypeRecord, ArchetypeScore, AssetRecord, BuildChecklist (+20 more)

### Community 3 - "Community 3"
Cohesion: 0.12
Nodes (18): Contract, ExperimentRecord, AuditFinding, AuditRecord, calculate_prospect_score(), ConversionLeak, OutreachDraft, OutreachState (+10 more)

### Community 4 - "Community 4"
Cohesion: 0.13
Nodes (19): b89c46f feat: add evidence-backed pattern cookbook, StrEnum, AntiPatternRecord, AntiPatternSeverity, calculate_pattern_readiness(), EvidenceLevel, EvidenceRef, ExperimentStatus (+11 more)

### Community 5 - "Community 5"
Cohesion: 0.20
Nodes (6): Business-archetype contracts and deterministic recommendation helpers., Return a recommendation and confidence without confirming fit or approval., recommend_archetype(), ClientArchetypeAssessment, A recommendation record; it cannot approve a direction, offer, or launch., ArchetypeContractTests

### Community 6 - "Community 6"
Cohesion: 0.22
Nodes (6): RuntimeError, Operator CLI for the read-only studio harness., LayaPackageAdapter, LayaUnavailableError, Raised when optional Laya runtime dependencies are not installed., Lazy adapter for the optional `laya` package and its Router API.

### Community 7 - "Community 7"
Cohesion: 0.20
Nodes (8): artDirection, buttons, directionCta, directionData, previewBody, previewEyebrow, previewTitle, stageLabel

### Community 8 - "Community 8"
Cohesion: 0.43
Nodes (6): normalize_relative_path(), PortablePathError, Cross-platform project-relative reference rules., Raised when a contract reference is not portable or project-bounded., safe_project_path(), ValueError

### Community 9 - "Community 9"
Cohesion: 0.50
Nodes (3): Protocol, LayaAdapter, Return the upstream Laya result without granting any authority.

## Knowledge Gaps
- **21 isolated node(s):** `root`, `manifestPath`, `manifest`, `normalized`, `Check the focused repo for unsafe absolute project references.` (+16 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Contract` connect `Community 2` to `Community 4`, `Community 3`, `Community 9`, `Community 1`, `Community 6`, `Community 5`, `Community 0`?**
  _High betweenness centrality (0.581) - this node is a cross-community bridge._
- **Why does `StudioProject` connect `Community 0` to `Community 6`, `Community 2`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Why does `StudioHarnessTests` connect `Community 2` to `Community 0`, `Community 8`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Are the 46 inferred relationships involving `Contract` (e.g. with `AntiPatternRecord` and `AntiPatternSeverity`) actually correct?**
  _`Contract` has 46 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `StudioHarnessTests` (e.g. with `AccessibilityReceipt` and `AIAssetDetails`) actually correct?**
  _`StudioHarnessTests` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `LayaAdvisoryTests` (e.g. with `CalibrationStatus` and `LayaAdvisoryEngine`) actually correct?**
  _`LayaAdvisoryTests` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `FakeLayaAdapter` (e.g. with `CalibrationStatus` and `LayaAdvisoryEngine`) actually correct?**
  _`FakeLayaAdapter` has 7 INFERRED edges - model-reasoned connections that need verification._