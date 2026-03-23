"""Compliance Gap Visualizations — Dashboards and Gap Charts"""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import seaborn as sns

plt.rcParams.update({"figure.facecolor": "white", "axes.grid": True, "grid.alpha": 0.3, "font.size": 11, "figure.dpi": 150})

SEVERITY_COLORS = {"critical": "#c0392b", "high": "#e74c3c", "medium": "#f39c12", "low": "#3498db"}
COVERAGE_COLORS = {"GOOD": "#2ecc71", "PARTIAL": "#f39c12", "WEAK": "#e67e22", "MISSING": "#e74c3c"}


class CompliancePlotter:
    def __init__(self, output_dir="results/figures", dpi=300):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.dpi = dpi

    def _save(self, fig, name):
        path = self.output_dir / f"{name}.png"
        fig.savefig(path, dpi=self.dpi, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        print(f"  Saved: {path}")

    def plot_system_compliance_radar(self, coverage_df: pd.DataFrame, system_name: str):
        """Radar chart of coverage by area for one system."""
        area_scores = coverage_df.groupby("area")["coverage_score"].mean()
        areas = area_scores.index.tolist()
        scores = area_scores.values.tolist()

        # Close the radar
        areas += [areas[0]]
        scores += [scores[0]]

        angles = np.linspace(0, 2 * np.pi, len(areas), endpoint=True)

        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        ax.plot(angles, scores, 'b-', linewidth=2)
        ax.fill(angles, scores, alpha=0.2)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([a.replace("_", "\n") for a in areas[:-1]], fontsize=9)
        ax.set_ylim(0, 1)
        ax.set_title(f"Compliance Coverage: {system_name}", pad=20, fontsize=13)
        self._save(fig, f"radar_{system_name.replace(' ', '_').lower()}")

    def plot_gap_severity_chart(self, gaps_df: pd.DataFrame, system_name: str):
        """Horizontal bar chart of gaps sorted by severity × coverage."""
        if len(gaps_df) == 0:
            return
        gaps_df = gaps_df.head(15).sort_values("coverage_score")
        colors = [SEVERITY_COLORS.get(s, "#95a5a6") for s in gaps_df["severity"]]

        fig, ax = plt.subplots(figsize=(11, max(4, len(gaps_df) * 0.4)))
        bars = ax.barh(gaps_df["title"], 1 - gaps_df["coverage_score"], color=colors, edgecolor="white")
        ax.set_xlabel("Gap Severity (1 - coverage)")
        ax.set_title(f"Compliance Gaps: {system_name}")
        ax.set_xlim(0, 1)

        patches = [mpatches.Patch(color=c, label=s.title()) for s, c in SEVERITY_COLORS.items()]
        ax.legend(handles=patches, loc="lower right")
        self._save(fig, f"gaps_{system_name.replace(' ', '_').lower()}")

    def plot_cross_system_heatmap(self, heatmap_df: pd.DataFrame):
        """Heatmap of coverage: systems × compliance areas."""
        if len(heatmap_df) == 0:
            return
        pivot = heatmap_df.pivot_table(values="coverage", index="system", columns="area", aggfunc="mean")
        fig, ax = plt.subplots(figsize=(14, max(4, len(pivot) * 0.8)))
        sns.heatmap(pivot, annot=True, fmt=".2f", cmap="RdYlGn", vmin=0, vmax=1,
                    linewidths=0.5, ax=ax)
        ax.set_title("Cross-System Compliance Coverage Heatmap")
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        self._save(fig, "cross_system_heatmap")

    def plot_systemic_gaps(self, gap_freq_df: pd.DataFrame):
        """Bar chart of most common gaps across systems."""
        systemic = gap_freq_df[gap_freq_df["gap_rate"] > 0.3].head(12).sort_values("gap_rate")
        if len(systemic) == 0:
            return
        colors = [SEVERITY_COLORS.get(s, "#95a5a6") for s in systemic["severity"]]
        fig, ax = plt.subplots(figsize=(11, max(4, len(systemic) * 0.45)))
        ax.barh(systemic["title"], systemic["gap_rate"], color=colors, edgecolor="white")
        ax.set_xlabel("Gap Rate (fraction of systems)")
        ax.set_title("Systemic Compliance Gaps Across All Systems")
        ax.set_xlim(0, 1)
        ax.axvline(0.5, color="red", linestyle="--", alpha=0.5, label="50% threshold")
        ax.legend()
        self._save(fig, "systemic_gaps")

    def plot_framework_comparison(self, all_coverage: dict):
        """Compare compliance scores across frameworks for each system."""
        rows = []
        for system, cov_df in all_coverage.items():
            for fw in cov_df["framework"].unique():
                fw_data = cov_df[cov_df["framework"] == fw]
                rows.append({"system": system, "framework": fw, "avg_coverage": fw_data["coverage_score"].mean()})
        df = pd.DataFrame(rows)
        if len(df) == 0:
            return

        pivot = df.pivot_table(values="avg_coverage", index="system", columns="framework")
        fig, ax = plt.subplots(figsize=(10, max(4, len(pivot) * 0.7)))
        pivot.plot(kind="barh", ax=ax, edgecolor="white")
        ax.set_xlabel("Average Coverage Score")
        ax.set_title("Compliance by Framework and System")
        ax.set_xlim(0, 1)
        ax.legend(title="Framework")
        self._save(fig, "framework_comparison")

    def generate_all(self, systems_coverage: dict, gap_freq_df=None, heatmap_df=None):
        print("\nGenerating visualizations...")
        for system_name, cov_df in systems_coverage.items():
            self.plot_system_compliance_radar(cov_df, system_name)
            gaps = cov_df[cov_df["coverage_score"] < 0.5]
            if len(gaps) > 0:
                self.plot_gap_severity_chart(gaps, system_name)
        if heatmap_df is not None and len(heatmap_df) > 0:
            self.plot_cross_system_heatmap(heatmap_df)
        if gap_freq_df is not None and len(gap_freq_df) > 0:
            self.plot_systemic_gaps(gap_freq_df)
        self.plot_framework_comparison(systems_coverage)
        print(f"All figures saved to {self.output_dir}/")
