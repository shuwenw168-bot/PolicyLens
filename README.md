# PolicyLens 🔍📜

**Automated AI Compliance Gap Mining — From Model Cards to Regulatory Reports**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## The Problem

AI governance today looks like this: a compliance officer opens a 200-page PDF of the EU AI Act, opens a model card, and manually checks requirements one by one. This takes weeks per system, doesn't scale, and misses subtle gaps.

**PolicyLens automates this.** Feed it your AI system's documentation — model cards, evaluation reports, data sheets — and it tells you exactly where you're non-compliant, what's missing, and what to fix.

## How It Works

```
     Your AI System Documentation
     (model card, eval report, datasheet)
                    │
                    ▼
    ┌───────────────────────────────┐
    │   Document Feature Extractor   │
    │   Parses claims, metrics,      │
    │   and coverage signals         │
    └───────────────┬───────────────┘
                    │
        ┌───────────┼───────────────┐
        ▼           ▼               ▼
   ┌─────────┐ ┌─────────┐  ┌───────────┐
   │ EU AI   │ │ NIST AI │  │ Industry  │
   │  Act    │ │   RMF   │  │   Best    │
   │ Mapper  │ │ Mapper  │  │ Practices │
   └────┬────┘ └────┬────┘  └─────┬─────┘
        │           │             │
        └───────────┴─────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │     Compliance Gap Miner       │
    │   • Missing requirements       │
    │   • Weak coverage areas        │
    │   • Cross-framework conflicts  │
    │   • Priority ranking           │
    └───────────────┬───────────────┘
                    │
           ┌────────┴────────┐
           ▼                 ▼
    ┌─────────────┐  ┌─────────────┐
    │  Risk Score  │  │  Compliance │
    │  Dashboard   │  │   Report    │
    │  (per-area)  │  │  (audit-    │
    │              │  │   ready)    │
    └─────────────┘  └─────────────┘
```

## What Makes This Different

| Manual Compliance | PolicyLens |
|---|---|
| Weeks per AI system | **Seconds** per AI system |
| Human reads 200-page regulation | Regulation **encoded as structured requirements** |
| Binary pass/fail checkboxes | **Continuous coverage scores** with gap severity |
| One framework at a time | **Cross-framework analysis** (EU AI Act + NIST + ISO simultaneously) |
| No pattern mining | **Discovers systemic gaps** across multiple AI systems |
| Static report | **Actionable remediation** priorities |

## Quick Start

```bash
git clone https://github.com/shuwenw168-bot/policylens.git
cd policylens
pip install numpy pandas scipy scikit-learn matplotlib seaborn pyyaml tqdm rich jinja2
python experiments/run_full_analysis.py
```

No GPU. No API keys. Runs in under 5 seconds.

## Core Modules

### 1. Regulatory Framework Engine

Encodes EU AI Act, NIST AI RMF, and industry best practices as structured, queryable requirements.

```python
from src.frameworks.eu_ai_act import EUAIActFramework

framework = EUAIActFramework()
requirements = framework.get_requirements(risk_level="high")

# Returns structured requirements:
# [Requirement(id="ART-9.1", area="risk_management", text="..."),
#  Requirement(id="ART-10.2", area="data_governance", text="..."), ...]
```

### 2. Document Analyzer

Extracts compliance-relevant signals from model cards and documentation.

```python
from src.miners.document_analyzer import DocumentAnalyzer

analyzer = DocumentAnalyzer()
coverage = analyzer.analyze(model_card_text)

# Returns what the document covers:
# {"fairness_evaluation": 0.8, "training_data_description": 0.6,
#  "risk_assessment": 0.0, "human_oversight": 0.1, ...}
```

### 3. Compliance Gap Miner

Maps documentation coverage against regulatory requirements to find gaps.

```python
from src.miners.gap_miner import ComplianceGapMiner

miner = ComplianceGapMiner()
gaps = miner.mine(documentation_features, framework="eu_ai_act")

# Returns prioritized gaps:
# Gap 1: "risk_management" — 0% coverage (CRITICAL, Art. 9)
# Gap 2: "human_oversight" — 15% coverage (HIGH, Art. 14)
# Gap 3: "transparency"    — 30% coverage (MEDIUM, Art. 13)
```

### 4. Cross-System Pattern Mining

When auditing multiple AI systems, discovers **systemic compliance gaps** across your organization.

```python
from src.miners.pattern_miner import CrossSystemMiner

miner = CrossSystemMiner()
patterns = miner.mine(all_systems_df)

# "87% of your AI systems lack documented human oversight procedures"
# "None of your high-risk systems have post-deployment monitoring plans"
```

## Supported Frameworks

| Framework | Status | Requirements |
|-----------|--------|-------------|
| EU AI Act (2024) | ✅ Encoded | 42 requirements across 8 areas |
| NIST AI RMF 1.0 | ✅ Encoded | 35 requirements across 4 functions |
| Industry Best Practices | ✅ Encoded | 20 requirements (Model Cards, Datasheets) |

## Project Structure

```
policylens/
├── src/
│   ├── data/
│   │   └── sample_generator.py       # Sample model cards & eval reports
│   ├── frameworks/
│   │   ├── base.py                    # Framework base class
│   │   ├── eu_ai_act.py              # EU AI Act requirements
│   │   ├── nist_rmf.py               # NIST AI RMF requirements
│   │   └── best_practices.py         # Industry best practices
│   ├── miners/
│   │   ├── document_analyzer.py      # Extract coverage from documentation
│   │   ├── gap_miner.py              # Find compliance gaps
│   │   └── pattern_miner.py          # Cross-system gap patterns
│   ├── scoring/
│   │   └── compliance_scorer.py      # Unified scoring engine
│   ├── visualization/
│   │   └── compliance_plots.py       # Dashboards and gap charts
│   └── reporting/
│       └── report_generator.py       # Audit-ready compliance reports
├── experiments/
│   └── run_full_analysis.py
├── config/default_config.yaml
├── tests/test_miners.py
└── results/
```

## Use Cases

- **Pre-deployment compliance check** — Run PolicyLens before launching any AI system
- **Portfolio-wide audit** — Scan all your org's AI systems and find systemic gaps
- **Regulatory change impact** — When regulations update, instantly see which systems are affected
- **Vendor assessment** — Evaluate third-party AI tools against your compliance requirements
- **Board reporting** — Generate executive-level compliance dashboards

## Citation

```bibtex
@software{policylens_2026,
  title={PolicyLens: Automated AI Compliance Gap Mining},
  author={[Shwuen Wang]},
  year={2026},
  url={https://github.com/shuwenw168-bot/policylens}
}
```

## License

MIT — see [LICENSE](LICENSE) for details.
