"""
PolicyLens: Full Compliance Analysis Pipeline
──────────────────────────────────────────────
python experiments/run_full_analysis.py
"""

import sys
import time
from pathlib import Path

import pandas as pd
import yaml

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data.sample_generator import generate_sample_data
from src.frameworks.eu_ai_act import EUAIActFramework
from src.frameworks.nist_rmf import NISTRMFFramework
from src.frameworks.best_practices import BestPracticesFramework
from src.miners.document_analyzer import DocumentAnalyzer
from src.miners.gap_miner import ComplianceGapMiner, CrossSystemMiner
from src.visualization.compliance_plots import CompliancePlotter


def load_config(path="config/default_config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def run_analysis(config_path="config/default_config.yaml"):
    start = time.time()
    config = load_config(config_path)

    print("=" * 60)
    print("  PolicyLens: Automated AI Compliance Gap Mining")
    print("=" * 60)

    results_dir = Path(config["output"]["results_dir"])
    results_dir.mkdir(parents=True, exist_ok=True)

    # ── Step 1: Load Frameworks ──
    print("\n[1/5] Loading regulatory frameworks...")
    eu_act = EUAIActFramework()
    nist = NISTRMFFramework()
    bp = BestPracticesFramework()

    all_requirements = eu_act.requirements + nist.requirements + bp.requirements
    print(f"  EU AI Act: {len(eu_act.requirements)} requirements")
    print(f"  NIST AI RMF: {len(nist.requirements)} requirements")
    print(f"  Best Practices: {len(bp.requirements)} requirements")
    print(f"  Total: {len(all_requirements)}")

    # ── Step 2: Load AI Systems ──
    print("\n[2/5] Loading AI system documentation...")
    systems_df = generate_sample_data()

    # ── Step 3: Analyze Each System ──
    print("\n[3/5] Analyzing compliance coverage...")
    analyzer = DocumentAnalyzer()
    gap_miner = ComplianceGapMiner()

    all_coverage = {}
    all_gaps = {}

    for _, system in systems_df.iterrows():
        name = system["system_name"]
        doc = system["documentation"]
        risk = system["risk_level"]

        print(f"\n  --- {name} (risk: {risk}) ---")

        # Get applicable requirements
        applicable = [r for r in all_requirements if risk in r.applies_to]

        # Analyze coverage
        coverage_df = analyzer.analyze_coverage(doc, applicable)
        all_coverage[name] = coverage_df

        # Find gaps
        gaps = gap_miner.mine(coverage_df, threshold=config["gap_mining"]["threshold"])
        all_gaps[name] = gaps

        # Summary
        avg_coverage = coverage_df["coverage_score"].mean()
        n_gaps = len(gaps)
        critical_gaps = sum(1 for g in gaps if g.severity == "critical")
        print(f"    Average coverage: {avg_coverage:.1%}")
        print(f"    Gaps found: {n_gaps} ({critical_gaps} critical)")

    # ── Step 4: Cross-System Mining ──
    print("\n[4/5] Mining cross-system patterns...")
    cross_miner = CrossSystemMiner()
    gap_freq = cross_miner.mine(all_coverage)
    heatmap_data = cross_miner.get_area_heatmap_data(all_coverage)

    systemic = gap_freq[gap_freq["gap_rate"] > 0.5]
    print(f"\n  Systemic gaps (>50% of systems):")
    for _, row in systemic.iterrows():
        print(f"    [{row['severity'].upper()}] {row['title']} — gap rate: {row['gap_rate']:.0%}")

    # ── Step 5: Visualize & Save ──
    print("\n[5/5] Generating visualizations and saving results...")
    plotter = CompliancePlotter(
        output_dir=config["output"]["figures_dir"],
        dpi=config["output"]["figure_dpi"],
    )
    plotter.generate_all(all_coverage, gap_freq, heatmap_data)

    # Save CSVs
    for name, cov_df in all_coverage.items():
        safe_name = name.replace(" ", "_").lower()
        cov_df.to_csv(results_dir / f"coverage_{safe_name}.csv", index=False)

    for name, gaps in all_gaps.items():
        safe_name = name.replace(" ", "_").lower()
        gap_miner.gaps_to_dataframe(gaps).to_csv(results_dir / f"gaps_{safe_name}.csv", index=False)

    gap_freq.to_csv(results_dir / "cross_system_gaps.csv", index=False)
    heatmap_data.to_csv(results_dir / "coverage_heatmap.csv", index=False)

    # ── Summary Report ──
    total_systems = len(systems_df)
    total_gaps = sum(len(g) for g in all_gaps.values())
    total_critical = sum(sum(1 for g in gaps if g.severity == "critical") for gaps in all_gaps.values())

    report = f"""# PolicyLens Compliance Audit Report

## Scope
- **Systems audited:** {total_systems}
- **Frameworks applied:** EU AI Act, NIST AI RMF, Industry Best Practices
- **Total requirements checked:** {len(all_requirements)}

## Executive Summary
- **Total compliance gaps found:** {total_gaps}
- **Critical gaps:** {total_critical}
- **Systemic gaps** (>50% of systems): {len(systemic)}

## Per-System Results
"""
    for name, gaps in all_gaps.items():
        cov = all_coverage[name]["coverage_score"].mean()
        n_crit = sum(1 for g in gaps if g.severity == "critical")
        report += f"\n### {name}\n- Coverage: {cov:.0%}\n- Gaps: {len(gaps)} ({n_crit} critical)\n"
        if gaps:
            report += "- Top gap: " + str(gaps[0]) + "\n"

    report += f"\n## Systemic Gaps\n"
    report += "These gaps affect more than half of all audited systems:\n\n"
    for _, row in systemic.iterrows():
        report += f"- **{row['title']}** ({row['severity'].upper()}) — {row['gap_rate']:.0%} of systems\n"

    report += f"\n## Recommendations\n"
    report += "1. Address all CRITICAL gaps immediately — these represent regulatory non-compliance risk\n"
    report += "2. Systemic gaps suggest organizational-level policy improvements needed\n"
    report += "3. Systems with <50% coverage need comprehensive documentation overhaul\n"

    (results_dir / "compliance_report.md").write_text(report)

    elapsed = time.time() - start
    print(f"\n{'=' * 60}")
    print(f"  Audit complete in {elapsed:.1f}s")
    print(f"  {total_systems} systems | {total_gaps} gaps ({total_critical} critical)")
    print(f"  Results: {results_dir}/")
    print(f"  Figures: {config['output']['figures_dir']}/")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    run_analysis()
