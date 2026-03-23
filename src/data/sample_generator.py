"""
Sample Data Generator — Synthetic AI System Documentation
─────────────────────────────────────────────────────────
Generates fake but realistic model cards and documentation
for multiple AI systems with varying levels of compliance.
"""

import random
import pandas as pd


# ── Synthetic AI Systems with varying compliance levels ──
SYSTEMS = [
    {
        "name": "FraudDetect Pro",
        "type": "classification",
        "risk_level": "high",
        "domain": "finance",
        "compliance_quality": "good",
        "documentation": """
# FraudDetect Pro - Model Card

## Model Details
- **Developer:** FinanceAI Corp, Version 3.2, Released 2025-01
- **Type:** Gradient Boosted Decision Tree ensemble for transaction fraud detection
- **License:** Proprietary, internal use only
- **Architecture:** XGBoost with 500 estimators, max_depth=8

## Intended Use
- **Primary use:** Real-time fraud detection for credit card transactions
- **Intended users:** Bank fraud investigation teams
- **Out-of-scope:** Not designed for insurance fraud or identity theft detection

## Training Data
- 12M transactions from 2020-2024, 2.3% positive fraud rate
- Sourced from US and European card networks
- PII removed; transactions pseudonymized
- Known limitation: underrepresents transactions from emerging markets

## Evaluation Results
- Precision: 0.94, Recall: 0.87, F1: 0.90, AUC-ROC: 0.96
- Performance by demographic: tested across cardholder age groups and geographic regions
- False positive rate: 3.2% overall, 4.1% for transactions under $50

## Fairness Assessment
- Demographic parity evaluated across cardholder income brackets
- Equalized odds tested across geographic regions
- Known disparity: 12% higher false positive rate for rural cardholders

## Limitations
- Performance degrades on transaction types not seen in training data
- Not validated for real-time latency requirements below 50ms
- May produce higher false positives during holiday shopping seasons

## Risk Management
- Monthly model retraining on latest transaction data
- Human review required for all fraud flags above $10,000
- Automated monitoring for prediction drift with alerts at 5% threshold

## Human Oversight
- All automated fraud blocks can be overridden by Level 2 analysts
- Customer dispute resolution process in place
- Escalation path to senior fraud investigators
""",
    },
    {
        "name": "ResumeRanker AI",
        "type": "ranking",
        "risk_level": "high",
        "domain": "employment",
        "compliance_quality": "poor",
        "documentation": """
# ResumeRanker AI

## Overview
AI system that ranks job applicants based on resume analysis. Uses NLP to extract skills and match to job descriptions. Trained on historical hiring data from partner companies.

## Performance
Achieves 82% agreement with human recruiters on top-10 candidate selection.

## Technical Details
Built with BERT-base fine-tuned on 500K resume-job pairs. Deployed as REST API.
""",
    },
    {
        "name": "MedAssist Triage",
        "type": "classification",
        "risk_level": "high",
        "domain": "healthcare",
        "compliance_quality": "medium",
        "documentation": """
# MedAssist Triage System - Model Card

## Model Details
- **Developer:** HealthTech Solutions, v2.1
- **Type:** Multi-class classifier for emergency department triage prioritization
- **Architecture:** Fine-tuned clinical BERT model

## Intended Use
Assists ED nurses in triaging incoming patients by analyzing symptom descriptions and vital signs. Not intended as a standalone diagnostic tool.

## Training Data
- 2.1M ED visit records from 15 hospitals (2018-2023)
- Includes demographics, chief complaints, vitals, and triage outcomes
- Approved by IRB #2023-0456

## Evaluation
- Overall accuracy: 89.3% on held-out test set
- Sensitivity for critical cases (ESI 1-2): 94.7%
- Known performance gap: 6% lower accuracy for pediatric patients

## Ethical Considerations
- Potential for demographic bias in triage recommendations
- Model should never override clinical judgment
- Regular bias audits planned but not yet conducted

## Limitations
- Trained primarily on English-language chief complaints
- Performance not validated on populations over age 85
- Does not account for social determinants of health
""",
    },
    {
        "name": "ContentMod v5",
        "type": "classification",
        "risk_level": "limited",
        "domain": "social_media",
        "compliance_quality": "good",
        "documentation": """
# ContentMod v5 - Model Card

## Model Details
- **Developer:** SocialPlatform Inc., v5.0.3
- **Type:** Multi-label content moderation classifier
- **License:** Apache 2.0
- **Architecture:** RoBERTa-large with custom classification heads

## Intended Use
- Automated content moderation for user-generated text content
- Flags content for human review in categories: hate speech, violence, harassment, spam
- Intended as a first-pass filter, not a sole decision maker

## Training Data
- 5M labeled examples from human moderators
- Active learning pipeline for edge cases
- Quarterly data refresh with new content patterns
- Annotation guidelines: 450-page internal document, 3-annotator agreement required

## Evaluation
- Macro F1: 0.88 across all categories
- Hate speech F1: 0.91, Violence F1: 0.87, Harassment F1: 0.85, Spam F1: 0.93
- Cross-lingual evaluation: English (0.88), Spanish (0.82), French (0.80)
- Disaggregated by dialect: AAVE detection false positive rate monitored

## Fairness
- Regular audits for disparate impact across demographic groups
- Dedicated fairness team reviews monthly metrics
- Known issue: 15% higher false positive rate for AAVE content
- Mitigation: AAVE-specific training data augmentation in progress

## Transparency
- Users are informed that content is subject to automated review
- Appeal process available for all moderation decisions
- Quarterly transparency report published

## Human Oversight
- All permanent account actions require human moderator approval
- Automated actions limited to content hiding pending review
- 24-hour human review SLA for appeals

## Monitoring
- Real-time dashboard tracking precision/recall by category
- Drift detection with weekly statistical tests
- Incident response team on-call 24/7

## Limitations
- Image and video content not covered (separate system)
- Sarcasm and context-dependent content remain challenging
- New slang and coded language requires continuous updating
""",
    },
    {
        "name": "LoanDecision Engine",
        "type": "regression",
        "risk_level": "high",
        "domain": "finance",
        "compliance_quality": "medium",
        "documentation": """
# LoanDecision Engine

## About
ML model for consumer loan approval recommendations. Predicts default probability and suggests approval/denial with interest rate.

## Model
Ensemble of logistic regression and gradient boosting. Features include credit history, income, employment, and loan characteristics. No demographic features used directly.

## Performance
- AUC: 0.91 on holdout test set
- Calibration: Hosmer-Lemeshow p=0.34

## Data
Trained on 3 years of loan application data. Includes approved and denied applications.

## Compliance Notes
- ECOA and fair lending compliance review completed
- Adverse action notices generated with top contributing factors
- Annual disparate impact analysis performed
""",
    },
    {
        "name": "ChatHelper Bot",
        "type": "generative",
        "risk_level": "limited",
        "domain": "customer_service",
        "compliance_quality": "poor",
        "documentation": """
# ChatHelper Bot
Customer service chatbot powered by LLM. Answers product questions and handles basic support tickets. Fine-tuned on company FAQ and support history.
""",
    },
]


def generate_sample_data(seed: int = 42) -> pd.DataFrame:
    """Generate sample AI system documentation for compliance analysis."""
    random.seed(seed)

    rows = []
    for system in SYSTEMS:
        rows.append({
            "system_name": system["name"],
            "system_type": system["type"],
            "risk_level": system["risk_level"],
            "domain": system["domain"],
            "compliance_quality": system["compliance_quality"],
            "documentation": system["documentation"].strip(),
            "doc_word_count": len(system["documentation"].split()),
        })

    df = pd.DataFrame(rows)
    print(f"Generated documentation for {len(df)} AI systems")
    print(f"  Risk levels: {df['risk_level'].value_counts().to_dict()}")
    print(f"  Quality: {df['compliance_quality'].value_counts().to_dict()}")
    return df
