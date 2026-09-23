# Graph Report - .  (2026-09-23)

## Corpus Check
- 175 files · ~125.529 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 248 nodes · 521 edges · 14 communities detected
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 121 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: uses: 121 · contains: 117 · MODIFIES: 62 · inherits: 61 · method: 40 · rationale_for: 39 · calls: 38 · ON_BRANCH: 18 · PARENT_OF: 16 · imports_from: 9


## Input Scope
- Requested: all
- Resolved: all (source: cli)
- Included files: 175 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `e5749a3`
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
10. `ArchetypeTemplateEvaluation` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Dependency-light structural checks for the focused studio repo.` --uses--> `StudioProject`  [INFERRED]
  scripts/validate_studio_contracts.py → studio/models.py
- `Dependency-light structural checks for the focused studio repo.` --uses--> `ArchetypeTemplateEvaluation`  [INFERRED]
  scripts/validate_studio_contracts.py → studio/quality_research.py
- `StudioHarnessTests` --uses--> `StudioProject`  [INFERRED]
  tests/test_studio_harness.py → studio/models.py
- `StudioHarnessTests` --uses--> `PortablePathError`  [INFERRED]
  tests/test_studio_harness.py → studio/portability.py
- `Contracts for the evidence-backed pattern and anti-pattern cookbook.` --uses--> `Contract`  [INFERRED]
  studio/cookbook.py → studio/models.py

## Communities

### Community 11 - "Community 11"
Cohesion: 0.90
Nodes (4): parse_checklist(), check(), markdown(), main()

### Community 10 - "Community 10"
Cohesion: 0.73
Nodes (5): luminance(), ratio(), parse_tokens(), main(), audit()

### Community 12 - "Community 12"
Cohesion: 0.90
Nodes (4): parse_checklist(), check(), markdown(), main()

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (29): root, manifestPath, manifest, normalized, Check the focused repo for unsafe absolute project references., Proofline Studio's human-governed delivery harness., _result(), evaluate_project() (+21 more)

### Community 6 - "Community 6"
Cohesion: 0.26
Nodes (14): _load(), validate(), Dependency-light structural checks for the focused studio repo., 0ecf304 feat: integrate NewLLM prospecting and quality loop, 13df31c feat: add human-gated outbound intelligence module, 142dc46 docs: specify Notion portal and Canva templates, 57970cd feat: add business archetype systems, 7bf1318 docs: define Notion and Canva integration boundary (+6 more)

### Community 9 - "Community 9"
Cohesion: 0.20
Nodes (8): directionData, buttons, stageLabel, previewEyebrow, previewTitle, previewBody, directionCta, artDirection

### Community 7 - "Community 7"
Cohesion: 0.20
Nodes (6): recommend_archetype(), Business-archetype contracts and deterministic recommendation helpers., Return a recommendation and confidence without confirming fit or approval., ClientArchetypeAssessment, A recommendation record; it cannot approve a direction, offer, or launch., ArchetypeContractTests

### Community 8 - "Community 8"
Cohesion: 0.22
Nodes (6): Operator CLI for the read-only studio harness., LayaUnavailableError, RuntimeError, LayaPackageAdapter, Raised when optional Laya runtime dependencies are not installed., Lazy adapter for the optional `laya` package and its Router API.

### Community 4 - "Community 4"
Cohesion: 0.13
Nodes (18): PatternStatus, StrEnum, EvidenceLevel, EvidenceRef, PatternScores, calculate_pattern_readiness(), PatternRecord, AntiPatternSeverity (+10 more)

### Community 3 - "Community 3"
Cohesion: 0.12
Nodes (19): Contract, ProfessionalContact, SourceRecord, SignalRecord, ConversionLeak, ProspectScore, OutreachState, ProspectRecord (+11 more)

### Community 1 - "Community 1"
Cohesion: 0.09
Nodes (21): LayaTask, LayaModel, CalibrationStatus, LayaRequest, LayaDecision, LayaEvaluationRecord, sanitize_state(), request_hash() (+13 more)

### Community 13 - "Community 13"
Cohesion: 0.50
Nodes (3): LayaAdapter, Protocol, Return the upstream Laya result without granting any authority.

### Community 2 - "Community 2"
Cohesion: 0.12
Nodes (28): Contract, BaseModel, DiscoveryBrief, MessageMap, DesignDirection, BuildChecklist, AIAssetDetails, AssetRecord (+20 more)

### Community 5 - "Community 5"
Cohesion: 0.13
Nodes (11): QualitySourceClass, QualityEvidenceLevel, QualityReuseDecision, QualitySourceRecord, TemplateQualityScores, ArchetypeTemplateEvaluation, Contracts for archetype quality intelligence and template evaluation., A source that can inform a rule without silently becoming a rule. (+3 more)

## Knowledge Gaps
- **21 isolated node(s):** `root`, `manifestPath`, `manifest`, `normalized`, `Check the focused repo for unsafe absolute project references.` (+16 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Contract` connect `Community 2` to `Community 4`, `Community 1`, `Community 13`, `Community 8`, `Community 7`, `Community 0`, `Community 3`, `Community 5`?**
  _High betweenness centrality (0.558) - this node is a cross-community bridge._
- **Why does `StudioProject` connect `Community 0` to `Community 6`, `Community 8`, `Community 2`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._
- **Why does `StudioHarnessTests` connect `Community 2` to `Community 0`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 57 inferred relationships involving `Contract` (e.g. with `AntiPatternRecord` and `AntiPatternSeverity`) actually correct?**
  _`Contract` has 57 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `StudioHarnessTests` (e.g. with `AccessibilityReceipt` and `AIAssetDetails`) actually correct?**
  _`StudioHarnessTests` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `LayaAdvisoryTests` (e.g. with `CalibrationStatus` and `LayaAdvisoryEngine`) actually correct?**
  _`LayaAdvisoryTests` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `FakeLayaAdapter` (e.g. with `CalibrationStatus` and `LayaAdvisoryEngine`) actually correct?**
  _`FakeLayaAdapter` has 7 INFERRED edges - model-reasoned connections that need verification._