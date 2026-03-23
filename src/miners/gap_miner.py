"""Compliance Gap Miner — Find and prioritize compliance gaps."""

from dataclasses import dataclass
import pandas as pd
import numpy as np


@dataclass
class ComplianceGap:
    """A detected compliance gap."""
    requirement_id: str
    area: str
    title: str
    severity: str
    coverage_score: float
    framework: str
    recommendation: str

    def __str__(self):
        return f"[{self.severity.upper()}] {self.requirement_id}: {self.title} — coverage: {self.coverage_score:.0%}"


class ComplianceGapMiner:
    """Identify and prioritize compliance gaps from coverage analysis."""

    SEVERITY_WEIGHTS = {"critical": 4, "high": 3, "medium": 2, "low": 1}

    def mine(self, coverage_df: pd.DataFrame, threshold: float = 0.5) -> list[ComplianceGap]:
        """Find requirements with coverage below threshold."""
        gaps = []
        for _, row in coverage_df.iterrows():
            if row["coverage_score"] < threshold:
                gaps.append(ComplianceGap(
                    requirement_id=row["requirement_id"],
                    area=row["area"],
                    title=row["title"],
                    severity=row["severity"],
                    coverage_score=row["coverage_score"],
                    framework=row["framework"],
                    recommendation=self._generate_recommendation(row),
                ))
        # Sort by severity weight × (1 - coverage)
        gaps.sort(key=lambda g: self.SEVERITY_WEIGHTS.get(g.severity, 1) * (1 - g.coverage_score), reverse=True)
        return gaps

    def _generate_recommendation(self, row) -> str:
        level = row["coverage_level"]
        area = row["area"]
        if level == "MISSING":
            return f"No documentation found for {area}. Create a dedicated section addressing {row['title']}."
        elif level == "WEAK":
            return f"Minimal coverage of {area}. Expand documentation with specific evidence and metrics."
        else:
            return f"Partial coverage of {area}. Add missing details to strengthen compliance."

    def gaps_to_dataframe(self, gaps: list[ComplianceGap]) -> pd.DataFrame:
        return pd.DataFrame([{
            "requirement_id": g.requirement_id, "area": g.area, "title": g.title,
            "severity": g.severity, "coverage": g.coverage_score,
            "framework": g.framework, "recommendation": g.recommendation,
        } for g in gaps])

    def summarize(self, gaps: list[ComplianceGap]) -> str:
        if not gaps:
            return "No compliance gaps found."
        by_severity = {}
        for g in gaps:
            by_severity.setdefault(g.severity, []).append(g)
        lines = [f"Found {len(gaps)} compliance gaps:\n"]
        for sev in ["critical", "high", "medium", "low"]:
            if sev in by_severity:
                lines.append(f"  {sev.upper()}: {len(by_severity[sev])} gaps")
        lines.append(f"\nTop 5 gaps:")
        for i, g in enumerate(gaps[:5], 1):
            lines.append(f"  {i}. {g}")
        return "\n".join(lines)


class CrossSystemMiner:
    """Mine compliance patterns across multiple AI systems."""

    def mine(self, all_coverage: dict[str, pd.DataFrame]) -> pd.DataFrame:
        """Find systemic gaps across all systems.

        Args:
            all_coverage: dict of {system_name: coverage_df}

        Returns:
            DataFrame showing gap frequency across systems.
        """
        print(f"Cross-system mining across {len(all_coverage)} AI systems")

        # Collect all requirement coverage across systems
        records = []
        for system_name, cov_df in all_coverage.items():
            for _, row in cov_df.iterrows():
                records.append({
                    "system": system_name,
                    "requirement_id": row["requirement_id"],
                    "area": row["area"],
                    "title": row["title"],
                    "severity": row["severity"],
                    "coverage": row["coverage_score"],
                    "is_gap": row["coverage_score"] < 0.5,
                })

        records_df = pd.DataFrame(records)

        # Compute gap frequency per requirement
        gap_freq = records_df.groupby(["requirement_id", "area", "title", "severity"]).agg(
            n_systems=("system", "count"),
            n_gaps=("is_gap", "sum"),
            avg_coverage=("coverage", "mean"),
            min_coverage=("coverage", "min"),
        ).reset_index()

        gap_freq["gap_rate"] = gap_freq["n_gaps"] / gap_freq["n_systems"]
        gap_freq = gap_freq.sort_values("gap_rate", ascending=False)

        # Systemic gaps (>50% of systems have this gap)
        systemic = gap_freq[gap_freq["gap_rate"] > 0.5]
        print(f"  Systemic gaps (>50% of systems): {len(systemic)}")

        return gap_freq

    def get_area_heatmap_data(self, all_coverage: dict) -> pd.DataFrame:
        """Create system × area coverage matrix for heatmap."""
        rows = []
        for system_name, cov_df in all_coverage.items():
            area_scores = cov_df.groupby("area")["coverage_score"].mean()
            for area, score in area_scores.items():
                rows.append({"system": system_name, "area": area, "coverage": score})
        return pd.DataFrame(rows)
