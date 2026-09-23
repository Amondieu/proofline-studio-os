"""Contracts for archetype quality intelligence and template evaluation."""

from __future__ import annotations

from datetime import date
from enum import StrEnum
from typing import Literal

from pydantic import Field, model_validator

from .models import Contract


class QualitySourceClass(StrEnum):
    normative = "normative"
    ux_research = "ux_research"
    technical_research = "technical_research"
    real_website = "real_website"
    practitioner_case_study = "practitioner_case_study"
    curated_award = "curated_award"
    community_critique = "community_critique"
    gallery_inspiration = "gallery_inspiration"


class QualityEvidenceLevel(StrEnum):
    gate = "gate"
    tested_research = "tested_research"
    practitioner = "practitioner"
    observational = "observational"
    inspiration = "inspiration"


class QualityReuseDecision(StrEnum):
    adopt_as_gate = "adopt_as_gate"
    adopt_as_test = "adopt_as_test"
    hypothesis_only = "hypothesis_only"
    inspiration_only = "inspiration_only"
    reject = "reject"


class QualitySourceRecord(Contract):
    """A source that can inform a rule without silently becoming a rule."""

    schema_version: Literal["studio.quality-source-record.v1"] = "studio.quality-source-record.v1"
    source_id: str = Field(pattern=r"^src_[a-z0-9_-]{4,80}$")
    title: str = Field(min_length=3, max_length=240)
    url: str = Field(min_length=8, max_length=1000)
    source_class: QualitySourceClass
    evidence_level: QualityEvidenceLevel
    applicable_archetypes: list[str] = Field(min_length=1, max_length=8)
    quality_signal: str = Field(min_length=20, max_length=600)
    extracts: list[str] = Field(min_length=1, max_length=12)
    limitations: list[str] = Field(min_length=1, max_length=8)
    reuse_decision: QualityReuseDecision
    reviewed_by: str = Field(min_length=2, max_length=160)
    reviewed_on: date


class TemplateQualityScores(Contract):
    decision_clarity: int = Field(ge=0, le=5)
    buyer_confidence: int = Field(ge=0, le=5)
    action_path: int = Field(ge=0, le=5)
    accessibility: int = Field(ge=0, le=5)
    performance: int = Field(ge=0, le=5)
    archetype_fit: int = Field(ge=0, le=5)
    craft_and_distinctiveness: int = Field(ge=0, le=5)
    maintainability: int = Field(ge=0, le=5)


class ArchetypeTemplateEvaluation(Contract):
    """Human-reviewed evaluation; ``gold_candidate`` is never self-approving."""

    schema_version: Literal["studio.archetype-template-evaluation.v1"] = "studio.archetype-template-evaluation.v1"
    evaluation_id: str = Field(pattern=r"^eval_[a-z0-9_-]{4,80}$")
    archetype_id: str = Field(min_length=3, max_length=120)
    template_ref: str = Field(min_length=3, max_length=240)
    source_ids: list[str] = Field(min_length=2, max_length=20)
    scores: TemplateQualityScores
    normative_gates_passed: bool = False
    functional_gates_passed: bool = False
    human_test_completed: bool = False
    human_reviewed: bool = False
    decision: Literal["candidate", "pilot", "gold_candidate", "revise", "reject"] = "candidate"
    rationale: str = Field(min_length=20, max_length=1200)
    reviewed_by: str | None = None
    reviewed_on: date | None = None

    @model_validator(mode="after")
    def gold_requires_evidence_and_human(self) -> "ArchetypeTemplateEvaluation":
        if self.decision == "gold_candidate":
            if not self.human_reviewed or not self.human_test_completed:
                raise ValueError("gold_candidate requires a human review and a completed human test")
            if not self.normative_gates_passed or not self.functional_gates_passed:
                raise ValueError("gold_candidate requires normative and functional gates to pass")
        return self
