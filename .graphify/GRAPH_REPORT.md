# Graph Report - .  (2026-09-23)

## Corpus Check
- 128 files · ~59.966 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 206 nodes · 430 edges · 11 communities detected
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 104 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: uses: 104 · contains: 95 · inherits: 54 · MODIFIES: 53 · rationale_for: 34 · method: 33 · calls: 22 · ON_BRANCH: 15 · PARENT_OF: 13 · imports_from: 7


## Input Scope
- Requested: all
- Resolved: all (source: cli)
- Included files: 128 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `a865242`
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
Cohesion: 0.10
Nodes (26): main, main, 13df31c feat: add human-gated outbound intelligence module, 140ed8b feat: adopt research receipts and QA gate, 142dc46 docs: specify Notion portal and Canva templates, 57970cd feat: add business archetype systems, 7bc151b chore: ignore local graphify lifecycle state, 7bf1318 docs: define Notion and Canva integration boundary (+18 more)

### Community 1 - "Community 1"
Cohesion: 0.09
Nodes (21): CalibrationStatus, LayaAdvisoryEngine, LayaDecision, LayaEvaluationRecord, LayaModel, LayaRequest, LayaTask, _normalise_answer() (+13 more)

### Community 2 - "Community 2"
Cohesion: 0.12
Nodes (28): BaseModel, AccessibilityReceipt, AIAssetDetails, ApprovalRecord, ArchetypeRecord, ArchetypeScore, AssetRecord, BuildChecklist (+20 more)

### Community 3 - "Community 3"
Cohesion: 0.12
Nodes (18): Contract, ExperimentRecord, AuditFinding, AuditRecord, calculate_prospect_score(), ConversionLeak, OutreachDraft, OutreachState (+10 more)

### Community 4 - "Community 4"
Cohesion: 0.14
Nodes (17): b89c46f feat: add evidence-backed pattern cookbook, StrEnum, AntiPatternRecord, AntiPatternSeverity, calculate_pattern_readiness(), EvidenceLevel, EvidenceRef, ExperimentStatus (+9 more)

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
Cohesion: 0.32
Nodes (8): evaluate_project(), Append one explicit human decision to a hash-chained local ledger., Append one explicit human decision to a hash-chained local ledger., Return a deterministic, non-authoritative project readiness report., Return a deterministic, non-authoritative project readiness report., record_human_gate(), _result(), StudioProject

### Community 9 - "Community 9"
Cohesion: 0.43
Nodes (6): normalize_relative_path(), PortablePathError, Cross-platform project-relative reference rules., Raised when a contract reference is not portable or project-bounded., safe_project_path(), ValueError

### Community 10 - "Community 10"
Cohesion: 0.50
Nodes (3): Protocol, LayaAdapter, Return the upstream Laya result without granting any authority.

## Knowledge Gaps
- **21 isolated node(s):** `root`, `manifestPath`, `manifest`, `normalized`, `Check the focused repo for unsafe absolute project references.` (+16 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Contract` connect `Community 2` to `Community 4`, `Community 3`, `Community 1`, `Community 10`, `Community 6`, `Community 5`, `Community 8`?**
  _High betweenness centrality (0.555) - this node is a cross-community bridge._
- **Why does `StudioProject` connect `Community 8` to `Community 0`, `Community 6`, `Community 2`?**
  _High betweenness centrality (0.111) - this node is a cross-community bridge._
- **Why does `StudioHarnessTests` connect `Community 2` to `Community 0`, `Community 8`, `Community 9`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **Are the 46 inferred relationships involving `Contract` (e.g. with `AntiPatternRecord` and `AntiPatternSeverity`) actually correct?**
  _`Contract` has 46 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `StudioHarnessTests` (e.g. with `AccessibilityReceipt` and `AIAssetDetails`) actually correct?**
  _`StudioHarnessTests` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `LayaAdvisoryTests` (e.g. with `CalibrationStatus` and `LayaAdvisoryEngine`) actually correct?**
  _`LayaAdvisoryTests` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `FakeLayaAdapter` (e.g. with `CalibrationStatus` and `LayaAdvisoryEngine`) actually correct?**
  _`FakeLayaAdapter` has 7 INFERRED edges - model-reasoned connections that need verification._