"""Contracts for the evidence-backed pattern and anti-pattern cookbook."""

from __future__ import annotations

from datetime import date
from enum import StrEnum
from typing import Literal

from pydantic import Field

from .models import Contract


class PatternStatus(StrEnum):
    approved = "approved"
    pilot = "pilot"
    reference_only = "reference_only"
    avoid = "avoid"


class EvidenceLevel(StrEnum):
    authoritative = "authoritative"
    strong_practitioner = "strong_practitioner"
    observational = "observational"
    inference = "inference"


class EvidenceRef(Contract):
    source_id: str = Field(min_length=2, max_length=80)
    title: str = Field(min_length=2, max_length=240)
    url: str = Field(min_length=8, max_length=500)
    level: EvidenceLevel
    note: str = Field(min_length=10, max_length=1000)


class PatternScores(Contract):
    clarity_impact: float = Field(ge=0, le=10)
    conversion_plausibility: float = Field(ge=0, le=10)
    trust_impact: float = Field(ge=0, le=10)
    mobile_suitability: float = Field(ge=0, le=10)
    accessibility_safety: float = Field(ge=0, le=10)
    performance_safety: float = Field(ge=0, le=10)
    implementation_cost: float = Field(ge=0, le=10)
    maintenance_burden: float = Field(ge=0, le=10)
    legal_safety: float = Field(ge=0, le=10)
    studio_fit: float = Field(ge=0, le=10)


def calculate_pattern_readiness(scores: PatternScores) -> float:
    """Calculate the cookbook score using the declared V1 weights."""

    weights = {
        "clarity_impact": 0.18,
        "conversion_plausibility": 0.15,
        "trust_impact": 0.12,
        "mobile_suitability": 0.12,
        "accessibility_safety": 0.12,
        "performance_safety": 0.10,
        "implementation_cost": 0.07,
        "maintenance_burden": 0.05,
        "legal_safety": 0.05,
        "studio_fit": 0.04,
    }
    return round(sum(getattr(scores, key) * weight for key, weight in weights.items()), 2)


class PatternRecord(Contract):
    schema_version: Literal["studio.pattern-record.v1"] = "studio.pattern-record.v1"
    pattern_id: str = Field(pattern=r"^[A-Z][A-Z0-9]{1,8}-[0-9]{3}$")
    name: str = Field(min_length=3, max_length=160)
    category: str = Field(min_length=3, max_length=80)
    status: PatternStatus
    problem_solves: str = Field(min_length=10, max_length=1000)
    use_only_when: list[str] = Field(min_length=1, max_length=12)
    do_not_use_when: list[str] = Field(min_length=1, max_length=12)
    target_client_fit: list[str] = Field(min_length=1, max_length=8)
    user_conversion_hypothesis: str = Field(min_length=10, max_length=1000)
    evidence_level: EvidenceLevel
    evidence: list[EvidenceRef] = Field(min_length=1, max_length=20)
    implementation: list[str] = Field(min_length=1, max_length=20)
    accessibility_requirements: list[str] = Field(min_length=1, max_length=20)
    performance_budget: list[str] = Field(min_length=1, max_length=20)
    trust_legal_requirements: list[str] = Field(min_length=1, max_length=20)
    low_cost_version: str = Field(min_length=10, max_length=1000)
    premium_version: str = Field(min_length=10, max_length=1000)
    test_method: str = Field(min_length=10, max_length=1000)
    success_signal: str = Field(min_length=5, max_length=500)
    failure_signal: str = Field(min_length=5, max_length=500)
    next_controlled_test: str = Field(min_length=5, max_length=500)
    scores: PatternScores
    readiness_score: float = Field(ge=0, le=10)
    cookbook_tags: list[str] = Field(min_length=1, max_length=20)
    reviewed_by: str | None = None
    reviewed_on: date | None = None


class AntiPatternSeverity(StrEnum):
    blocker = "blocker"
    high = "high"
    medium = "medium"
    low = "low"


class AntiPatternRecord(Contract):
    schema_version: Literal["studio.anti-pattern-record.v1"] = "studio.anti-pattern-record.v1"
    anti_pattern_id: str = Field(pattern=r"^[A-Z][A-Z0-9]{1,8}-AP-[0-9]{3}$")
    name: str = Field(min_length=3, max_length=160)
    category: str = Field(min_length=3, max_length=80)
    why_it_is_tempting: str = Field(min_length=10, max_length=1000)
    why_it_fails: str = Field(min_length=10, max_length=1000)
    harm_type: list[str] = Field(min_length=1, max_length=8)
    early_warning_signal: str = Field(min_length=5, max_length=500)
    detection_method: str = Field(min_length=10, max_length=1000)
    severity: AntiPatternSeverity
    replacement_pattern: str = Field(min_length=3, max_length=160)
    exception: str = Field(min_length=3, max_length=500)
    launch_rule: Literal["block_launch", "human_signoff_required", "allowed_with_test_evidence"]
    evidence: list[EvidenceRef] = Field(min_length=1, max_length=20)
    reviewed_by: str | None = None
    reviewed_on: date | None = None


class ExperimentStatus(StrEnum):
    planned = "planned"
    running = "running"
    complete = "complete"
    inconclusive = "inconclusive"
    stopped = "stopped"


class ExperimentRecord(Contract):
    schema_version: Literal["studio.experiment-record.v1"] = "studio.experiment-record.v1"
    experiment_id: str = Field(pattern=r"^EXP-[0-9]{4,}$")
    subject_id: str = Field(min_length=3, max_length=80)
    hypothesis: str = Field(min_length=10, max_length=1000)
    context: str = Field(min_length=10, max_length=1000)
    method: str = Field(min_length=10, max_length=1000)
    audience: str = Field(min_length=3, max_length=300)
    success_signal: str = Field(min_length=5, max_length=500)
    failure_signal: str = Field(min_length=5, max_length=500)
    result: str | None = None
    status: ExperimentStatus
    evidence: list[str] = Field(min_length=1, max_length=30)
    human_decision: str | None = None
    completed_on: date | None = None
