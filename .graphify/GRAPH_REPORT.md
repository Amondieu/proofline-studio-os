# Graph Report - .  (2026-09-23)

## Corpus Check
- 165 files · ~122.876 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 243 nodes · 510 edges · 14 communities detected
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 119 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: uses: 119 · contains: 116 · inherits: 61 · MODIFIES: 59 · rationale_for: 39 · calls: 38 · method: 38 · ON_BRANCH: 17 · PARENT_OF: 15 · imports_from: 8


## Input Scope
- Requested: all
- Resolved: all (source: cli)
- Included files: 165 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `0ecf304`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Contract` - 80 edges
2. `StudioHarnessTests` - 23 edges
3. `LayaAdvisoryTests` - 16 edges
4. `FakeLayaAdapter` - 13 edges
5. `StudioProject` - 11 edges
6. `LayaAdvisoryEngine` - 10 edges
7. `OutboundContractTests` - 9 edges
8. `LayaRequest` - 8 edges
9. `LayaDecision` - 8 edges
10. `CookbookContractTests` - 8 edges

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
Nodes (33): BaseModel, Business-archetype contracts and deterministic recommendation helpers., Return a recommendation and confidence without confirming fit or approval., recommend_archetype(), AccessibilityReceipt, AIAssetDetails, ApprovalRecord, ArchetypeRecord (+25 more)

### Community 1 - "Community 1"
Cohesion: 0.09
Nodes (27): main, 140ed8b feat: adopt research receipts and QA gate, 7bc151b chore: ignore local graphify lifecycle state, cb77a61 feat: create focused landing studio foundation, 140ed8b feat: adopt research receipts and QA gate, 7bc151b chore: ignore local graphify lifecycle state, 80a73c6 chore: separate Graphify profile and code refresh, b89c46f feat: add evidence-backed pattern cookbook (+19 more)

### Community 2 - "Community 2"
Cohesion: 0.09
Nodes (21): CalibrationStatus, LayaAdvisoryEngine, LayaDecision, LayaEvaluationRecord, LayaModel, LayaRequest, LayaTask, _normalise_answer() (+13 more)

### Community 3 - "Community 3"
Cohesion: 0.12
Nodes (19): Contract, AuditFinding, AuditRecord, calculate_prospect_score(), ConversionLeak, OutreachDraft, OutreachState, ProfessionalContact (+11 more)

### Community 4 - "Community 4"
Cohesion: 0.14
Nodes (17): StrEnum, AntiPatternRecord, AntiPatternSeverity, calculate_pattern_readiness(), EvidenceLevel, EvidenceRef, ExperimentRecord, ExperimentStatus (+9 more)

### Community 5 - "Community 5"
Cohesion: 0.21
Nodes (11): main, 0ecf304 feat: integrate NewLLM prospecting and quality loop, 13df31c feat: add human-gated outbound intelligence module, 142dc46 docs: specify Notion portal and Canva templates, 57970cd feat: add business archetype systems, 7bf1318 docs: define Notion and Canva integration boundary, 80a73c6 chore: separate Graphify profile and code refresh, 955a1db docs: record preliminary Laya model evaluation (+3 more)

### Community 6 - "Community 6"
Cohesion: 0.16
Nodes (10): ArchetypeTemplateEvaluation, QualityEvidenceLevel, QualityReuseDecision, QualitySourceClass, QualitySourceRecord, Contracts for archetype quality intelligence and template evaluation., A source that can inform a rule without silently becoming a rule., Human-reviewed evaluation; ``gold_candidate`` is never self-approving. (+2 more)

### Community 7 - "Community 7"
Cohesion: 0.22
Nodes (6): RuntimeError, Operator CLI for the read-only studio harness., LayaPackageAdapter, LayaUnavailableError, Raised when optional Laya runtime dependencies are not installed., Lazy adapter for the optional `laya` package and its Router API.

### Community 8 - "Community 8"
Cohesion: 0.20
Nodes (8): artDirection, buttons, directionCta, directionData, previewBody, previewEyebrow, previewTitle, stageLabel

### Community 9 - "Community 9"
Cohesion: 0.43
Nodes (6): normalize_relative_path(), PortablePathError, Cross-platform project-relative reference rules., Raised when a contract reference is not portable or project-bounded., safe_project_path(), ValueError

### Community 10 - "Community 10"
Cohesion: 0.73
Nodes (5): audit(), luminance(), main(), parse_tokens(), ratio()

### Community 11 - "Community 11"
Cohesion: 0.90
Nodes (4): check(), main(), markdown(), parse_checklist()

### Community 12 - "Community 12"
Cohesion: 0.90
Nodes (4): check(), main(), markdown(), parse_checklist()

### Community 13 - "Community 13"
Cohesion: 0.50
Nodes (3): Protocol, LayaAdapter, Return the upstream Laya result without granting any authority.

## Knowledge Gaps
- **21 isolated node(s):** `root`, `manifestPath`, `manifest`, `normalized`, `Check the focused repo for unsafe absolute project references.` (+16 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Contract` connect `Community 0` to `Community 4`, `Community 2`, `Community 13`, `Community 7`, `Community 1`, `Community 3`, `Community 6`?**
  _High betweenness centrality (0.582) - this node is a cross-community bridge._
- **Why does `StudioProject` connect `Community 1` to `Community 7`, `Community 0`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Why does `StudioHarnessTests` connect `Community 0` to `Community 1`, `Community 9`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Are the 57 inferred relationships involving `Contract` (e.g. with `AntiPatternRecord` and `AntiPatternSeverity`) actually correct?**
  _`Contract` has 57 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `StudioHarnessTests` (e.g. with `AccessibilityReceipt` and `AIAssetDetails`) actually correct?**
  _`StudioHarnessTests` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `LayaAdvisoryTests` (e.g. with `CalibrationStatus` and `LayaAdvisoryEngine`) actually correct?**
  _`LayaAdvisoryTests` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `FakeLayaAdapter` (e.g. with `CalibrationStatus` and `LayaAdvisoryEngine`) actually correct?**
  _`FakeLayaAdapter` has 7 INFERRED edges - model-reasoned connections that need verification._