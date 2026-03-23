"""
Regulatory Framework Base Class
────────────────────────────────
Provides the interface for encoding regulatory frameworks
as structured, queryable requirement sets.
"""

from dataclasses import dataclass, field
from enum import Enum


class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RiskLevel(Enum):
    UNACCEPTABLE = "unacceptable"
    HIGH = "high"
    LIMITED = "limited"
    MINIMAL = "minimal"


@dataclass
class Requirement:
    """A single regulatory requirement."""
    id: str                   # e.g., "ART-9.1"
    framework: str            # e.g., "eu_ai_act"
    area: str                 # e.g., "risk_management"
    title: str                # Short title
    description: str          # Full requirement text
    severity: Severity        # How critical for compliance
    applies_to: list[str]     # Risk levels this applies to
    keywords: list[str]       # Keywords to match in documentation
    evidence_needed: list[str]  # What documentation satisfies this

    def __str__(self):
        return f"[{self.id}] {self.title} ({self.severity.value})"


class BaseFramework:
    """Base class for regulatory frameworks."""

    def __init__(self):
        self.requirements: list[Requirement] = []
        self._build_requirements()

    def _build_requirements(self):
        raise NotImplementedError

    def get_requirements(self, risk_level: str = None, area: str = None) -> list[Requirement]:
        reqs = self.requirements
        if risk_level:
            reqs = [r for r in reqs if risk_level in r.applies_to]
        if area:
            reqs = [r for r in reqs if r.area == area]
        return reqs

    def get_areas(self) -> list[str]:
        return sorted(set(r.area for r in self.requirements))

    def summary(self) -> str:
        areas = {}
        for r in self.requirements:
            areas.setdefault(r.area, []).append(r)
        lines = [f"{self.__class__.__name__}: {len(self.requirements)} requirements across {len(areas)} areas\n"]
        for area, reqs in sorted(areas.items()):
            lines.append(f"  {area}: {len(reqs)} requirements")
        return "\n".join(lines)
