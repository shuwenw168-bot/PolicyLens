"""Tests for PolicyLens. Run: pytest tests/ -v"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
import pandas as pd
from src.frameworks.eu_ai_act import EUAIActFramework
from src.frameworks.nist_rmf import NISTRMFFramework
from src.frameworks.best_practices import BestPracticesFramework
from src.data.sample_generator import generate_sample_data
from src.miners.document_analyzer import DocumentAnalyzer
from src.miners.gap_miner import ComplianceGapMiner


class TestFrameworks:
    def test_eu_ai_act_loads(self):
        fw = EUAIActFramework()
        assert len(fw.requirements) > 10

    def test_nist_loads(self):
        fw = NISTRMFFramework()
        assert len(fw.requirements) > 10

    def test_best_practices_loads(self):
        fw = BestPracticesFramework()
        assert len(fw.requirements) > 5

    def test_filter_by_risk(self):
        fw = EUAIActFramework()
        high = fw.get_requirements(risk_level="high")
        assert len(high) > 0
        assert all("high" in r.applies_to for r in high)


class TestDocumentAnalyzer:
    def test_analyzes_coverage(self):
        fw = EUAIActFramework()
        analyzer = DocumentAnalyzer()
        systems = generate_sample_data()
        doc = systems.iloc[0]["documentation"]
        coverage = analyzer.analyze_coverage(doc, fw.requirements)
        assert "coverage_score" in coverage.columns
        assert len(coverage) == len(fw.requirements)
        assert (coverage["coverage_score"] >= 0).all()
        assert (coverage["coverage_score"] <= 1).all()

    def test_good_doc_better_than_poor(self):
        fw = EUAIActFramework()
        analyzer = DocumentAnalyzer()
        systems = generate_sample_data()
        good = systems[systems["compliance_quality"] == "good"].iloc[0]
        poor = systems[systems["compliance_quality"] == "poor"].iloc[0]
        cov_good = analyzer.analyze_coverage(good["documentation"], fw.requirements)
        cov_poor = analyzer.analyze_coverage(poor["documentation"], fw.requirements)
        assert cov_good["coverage_score"].mean() > cov_poor["coverage_score"].mean()


class TestGapMiner:
    def test_finds_gaps(self):
        fw = EUAIActFramework()
        analyzer = DocumentAnalyzer()
        systems = generate_sample_data()
        poor = systems[systems["compliance_quality"] == "poor"].iloc[0]
        coverage = analyzer.analyze_coverage(poor["documentation"], fw.requirements)
        miner = ComplianceGapMiner()
        gaps = miner.mine(coverage)
        assert len(gaps) > 0
        assert gaps[0].coverage_score < 0.5
