"""Versioned, provider-neutral contracts for a landing-page project."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Contract(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class Stage(StrEnum):
    discovery = "discovery"
    message = "message"
    direction = "direction"
    build = "build"
    qa = "qa"
    launch = "launch"


class DiscoveryBrief(Contract):
    company_name: str = Field(min_length=2, max_length=160)
    website_url: str | None = None
    market: str = Field(min_length=2, max_length=160)
    offer: str = Field(min_length=10, max_length=1000)
    average_order_value: str = Field(min_length=1, max_length=160)
    target_buyer: str = Field(min_length=10, max_length=1000)
    buying_situation: str = Field(min_length=10, max_length=1000)
    expensive_problem: str = Field(min_length=10, max_length=1000)
    current_alternatives: list[str] = Field(min_length=1, max_length=8)
    buyer_hesitations: list[str] = Field(min_length=1, max_length=8)
    primary_conversion: str = Field(min_length=3, max_length=120)
    secondary_conversion: str | None = None
    current_traffic: str | None = None
    current_conversion_rate: str | None = None
    existing_tools: list[str] = Field(default_factory=list, max_length=20)
    proof: list[str] = Field(default_factory=list, max_length=20)
    brand_assets: list[str] = Field(default_factory=list, max_length=30)
    tone_of_voice: list[str] = Field(min_length=1, max_length=8)
    legal_constraints: list[str] = Field(default_factory=list, max_length=20)
    assumption_map: list[str] = Field(default_factory=list, max_length=30)


class MessageMap(Contract):
    target_audience: str = Field(min_length=10, max_length=1000)
    primary_job_to_be_done: str = Field(min_length=10, max_length=1000)
    core_pain: str = Field(min_length=10, max_length=1000)
    desired_outcome: str = Field(min_length=10, max_length=1000)
    mechanism: str = Field(min_length=10, max_length=1000)
    primary_promise: str = Field(min_length=10, max_length=1000)
    primary_cta: str = Field(min_length=3, max_length=120)
    proof: list[str] = Field(default_factory=list, max_length=20)
    top_objections: list[str] = Field(min_length=3, max_length=8)
    required_sections: list[str] = Field(min_length=6, max_length=14)
    assumptions_to_confirm: list[str] = Field(default_factory=list, max_length=30)
    client_signoff: bool = False
    signed_off_by: str | None = None
    signed_off_at: datetime | None = None


class DesignDirection(Contract):
    direction_id: Literal["precision", "cinematic", "editorial"]
    label: str = Field(min_length=3, max_length=100)
    intended_audience: str = Field(min_length=10, max_length=300)
    visual_principle: str = Field(min_length=10, max_length=600)
    palette: list[str] = Field(min_length=3, max_length=12)
    typography: list[str] = Field(min_length=2, max_length=8)
    motion_principle: str = Field(min_length=10, max_length=300)
    desktop_asset_ref: str | None = None
    mobile_asset_ref: str | None = None
    mobile_preview_reviewed: bool = False
    selected_by_client: bool = False
    selected_by: str | None = None
    selected_at: datetime | None = None


class BuildChecklist(Contract):
    responsive_viewports: list[Literal["360", "390", "768", "1024", "1440"]] = Field(default_factory=list)
    navigation_works: bool = False
    ctas_route_correctly: bool = False
    form_validation_works: bool = False
    form_delivery_tested: bool = False
    calendar_or_secondary_flow_tested: bool = False
    metadata_present: bool = False
    open_graph_present: bool = False
    alt_text_reviewed: bool = False
    privacy_and_legal_links_present: bool = False
    analytics_consent_configured: bool = False
    assets_rights_confirmed: bool = False
    no_fabricated_claims: bool = False
    client_admin_access_ready: bool = False
    backup_export_supplied: bool = False


class LaunchReview(Contract):
    mobile_conversion_pass: bool = False
    technical_pass: bool = False
    trust_pass: bool = False
    legal_pass: bool = False
    reviewer: str | None = None
    client_approval: bool = False
    review_notes: list[str] = Field(default_factory=list, max_length=30)
    reviewed_at: datetime | None = None


class StudioProject(Contract):
    schema_version: Literal["studio.project.v1"] = "studio.project.v1"
    project_id: str = Field(pattern=r"^studio_[a-z0-9_-]{4,80}$")
    client_slug: str = Field(pattern=r"^[a-z0-9][a-z0-9-]{2,60}$")
    current_stage: Stage = Stage.discovery
    discovery: DiscoveryBrief
    message_map: MessageMap | None = None
    design_direction: DesignDirection | None = None
    build: BuildChecklist | None = None
    launch_review: LaunchReview | None = None
