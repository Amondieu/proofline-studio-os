"""Business-archetype contracts and deterministic recommendation helpers."""

from __future__ import annotations

from typing import Sequence

from .models import ArchetypeRecord, ArchetypeScore, ClientArchetypeAssessment

__all__ = [
    "ArchetypeRecord",
    "ArchetypeScore",
    "ClientArchetypeAssessment",
    "recommend_archetype",
]


def recommend_archetype(scores: Sequence[ArchetypeScore]) -> tuple[str | None, str]:
    """Return a recommendation and confidence without confirming fit or approval.

    Scores must be supplied by a human or a separately reviewed assessment step.
    A close result intentionally remains low-confidence so Discovery can resolve it.
    """

    ordered = sorted(scores, key=lambda item: item.score, reverse=True)
    if not ordered:
        return None, "low"
    if len(ordered) == 1:
        return ordered[0].archetype_id, "low"
    gap = ordered[0].score - ordered[1].score
    confidence = "high" if gap >= 15 else "medium" if gap >= 5 else "low"
    return ordered[0].archetype_id, confidence
