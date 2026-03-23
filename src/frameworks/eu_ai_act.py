"""
EU AI Act — Encoded as Structured Requirements
───────────────────────────────────────────────
Based on the EU AI Act (Regulation 2024/1689).
Encodes key requirements for high-risk AI systems.
"""

from .base import BaseFramework, Requirement, Severity


class EUAIActFramework(BaseFramework):
    """EU AI Act requirements for high-risk AI systems."""

    def _build_requirements(self):
        self.requirements = [
            # ── Article 9: Risk Management System ──
            Requirement("EU-9.1", "eu_ai_act", "risk_management",
                "Risk management system", "Establish and maintain a risk management system throughout the lifecycle of the high-risk AI system",
                Severity.CRITICAL, ["high"], ["risk management", "risk assessment", "lifecycle", "continuous"],
                ["risk management plan", "risk register", "risk assessment methodology"]),
            Requirement("EU-9.2", "eu_ai_act", "risk_management",
                "Risk identification and analysis", "Identify and analyze known and reasonably foreseeable risks that the AI system may pose to health, safety, or fundamental rights",
                Severity.CRITICAL, ["high"], ["risk identification", "foreseeable risks", "health", "safety", "fundamental rights"],
                ["risk analysis document", "identified risks list", "risk categorization"]),
            Requirement("EU-9.3", "eu_ai_act", "risk_management",
                "Risk mitigation measures", "Adopt suitable risk management measures including design choices, testing, and validation",
                Severity.CRITICAL, ["high"], ["mitigation", "risk reduction", "residual risk", "design"],
                ["mitigation strategies", "residual risk assessment"]),
            Requirement("EU-9.4", "eu_ai_act", "risk_management",
                "Testing for risk management", "Testing shall be performed against clearly defined metrics and probabilistic thresholds",
                Severity.HIGH, ["high"], ["testing", "metrics", "threshold", "probabilistic", "validation"],
                ["test plan", "test results", "performance metrics"]),

            # ── Article 10: Data and Data Governance ──
            Requirement("EU-10.1", "eu_ai_act", "data_governance",
                "Training data governance", "Training, validation and testing data sets shall be subject to appropriate data governance and management practices",
                Severity.CRITICAL, ["high"], ["training data", "data governance", "data management", "data quality"],
                ["data governance policy", "data management plan"]),
            Requirement("EU-10.2", "eu_ai_act", "data_governance",
                "Data representativeness", "Data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete",
                Severity.HIGH, ["high"], ["representative", "bias", "completeness", "errors", "data quality"],
                ["data quality assessment", "representativeness analysis", "bias assessment"]),
            Requirement("EU-10.3", "eu_ai_act", "data_governance",
                "Bias examination", "Appropriate measures to detect, prevent and mitigate possible biases in data sets",
                Severity.HIGH, ["high"], ["bias", "fairness", "discrimination", "protected", "demographic"],
                ["bias audit report", "fairness metrics", "demographic analysis"]),
            Requirement("EU-10.4", "eu_ai_act", "data_governance",
                "Personal data processing", "Appropriate safeguards for processing of personal data, including purpose limitation and data minimization",
                Severity.HIGH, ["high"], ["personal data", "privacy", "GDPR", "data protection", "consent"],
                ["privacy impact assessment", "data protection policy", "DPIA"]),

            # ── Article 11: Technical Documentation ──
            Requirement("EU-11.1", "eu_ai_act", "documentation",
                "Technical documentation", "Technical documentation shall be drawn up before the system is placed on the market and shall be kept up to date",
                Severity.CRITICAL, ["high"], ["technical documentation", "documentation", "model card"],
                ["technical documentation", "model card", "system description"]),
            Requirement("EU-11.2", "eu_ai_act", "documentation",
                "System description", "General description of the AI system including intended purpose, developers, version, and interaction with other systems",
                Severity.HIGH, ["high"], ["system description", "intended purpose", "version", "developer"],
                ["system description document", "intended use statement"]),

            # ── Article 12: Record-keeping ──
            Requirement("EU-12.1", "eu_ai_act", "record_keeping",
                "Automatic logging", "High-risk AI systems shall be designed with logging capabilities that enable monitoring of operation",
                Severity.HIGH, ["high"], ["logging", "audit trail", "monitoring", "record", "traceability"],
                ["logging specification", "audit log design", "monitoring plan"]),

            # ── Article 13: Transparency and Provision of Information ──
            Requirement("EU-13.1", "eu_ai_act", "transparency",
                "Transparency obligations", "High-risk AI systems shall be designed to ensure their operation is sufficiently transparent to enable users to interpret output",
                Severity.HIGH, ["high", "limited"], ["transparency", "interpretability", "explainability", "understand"],
                ["transparency statement", "explainability documentation"]),
            Requirement("EU-13.2", "eu_ai_act", "transparency",
                "Instructions for use", "Accompanied by instructions for use including characteristics, capabilities, and limitations",
                Severity.HIGH, ["high"], ["instructions", "capabilities", "limitations", "user guide"],
                ["user instructions", "limitations disclosure", "capability statement"]),
            Requirement("EU-13.3", "eu_ai_act", "transparency",
                "Performance disclosure", "Disclosure of known or foreseeable circumstances in which use may lead to risks to health, safety, or fundamental rights",
                Severity.MEDIUM, ["high", "limited"], ["performance", "accuracy", "error rate", "limitations"],
                ["performance metrics", "known limitations", "failure modes"]),

            # ── Article 14: Human Oversight ──
            Requirement("EU-14.1", "eu_ai_act", "human_oversight",
                "Human oversight design", "High-risk AI systems shall be designed to be effectively overseen by natural persons during use",
                Severity.CRITICAL, ["high"], ["human oversight", "human-in-the-loop", "human review", "override"],
                ["human oversight plan", "override mechanism", "escalation procedure"]),
            Requirement("EU-14.2", "eu_ai_act", "human_oversight",
                "Ability to override", "Individuals shall be able to decide not to use the system or to override the output",
                Severity.HIGH, ["high"], ["override", "opt-out", "human decision", "intervention"],
                ["override mechanism design", "opt-out procedure"]),

            # ── Article 15: Accuracy, Robustness, Cybersecurity ──
            Requirement("EU-15.1", "eu_ai_act", "accuracy_robustness",
                "Accuracy levels", "High-risk AI systems shall be designed to achieve appropriate levels of accuracy for their intended purpose",
                Severity.HIGH, ["high"], ["accuracy", "performance", "precision", "recall", "f1"],
                ["accuracy metrics", "performance benchmarks", "evaluation results"]),
            Requirement("EU-15.2", "eu_ai_act", "accuracy_robustness",
                "Robustness", "High-risk AI systems shall be resilient regarding errors, faults, or inconsistencies",
                Severity.HIGH, ["high"], ["robustness", "resilience", "adversarial", "edge cases", "stress test"],
                ["robustness testing", "adversarial evaluation", "stress test results"]),
            Requirement("EU-15.3", "eu_ai_act", "accuracy_robustness",
                "Cybersecurity", "Appropriate measures against unauthorized third-party manipulation of training data",
                Severity.HIGH, ["high"], ["cybersecurity", "security", "attack", "adversarial", "manipulation"],
                ["security assessment", "threat model", "cybersecurity measures"]),

            # ── Article 72: Post-market Monitoring ──
            Requirement("EU-72.1", "eu_ai_act", "post_deployment",
                "Post-market monitoring system", "Providers shall establish and document a post-market monitoring system proportionate to the nature of the AI system",
                Severity.HIGH, ["high"], ["monitoring", "post-market", "post-deployment", "continuous", "drift"],
                ["monitoring plan", "post-deployment monitoring", "performance tracking"]),
            Requirement("EU-72.2", "eu_ai_act", "post_deployment",
                "Incident reporting", "Providers shall report serious incidents to market surveillance authorities",
                Severity.HIGH, ["high"], ["incident", "reporting", "serious incident", "malfunction"],
                ["incident response plan", "reporting procedure"]),

            # ── Articles 50: Transparency for Limited Risk ──
            Requirement("EU-50.1", "eu_ai_act", "ai_interaction_disclosure",
                "AI interaction disclosure", "Providers shall ensure that AI systems intended to interact with persons are designed so that persons are informed they are interacting with AI",
                Severity.MEDIUM, ["high", "limited"], ["disclosure", "inform", "ai interaction", "chatbot", "automated"],
                ["AI disclosure notice", "user notification"]),

            # ── Annex IV: Technical Documentation Contents ──
            Requirement("EU-A4.1", "eu_ai_act", "documentation",
                "Training methodology", "Description of the training methodology and techniques and the training data used",
                Severity.HIGH, ["high"], ["training", "methodology", "technique", "architecture", "hyperparameter"],
                ["training procedure", "methodology description", "architecture documentation"]),
            Requirement("EU-A4.2", "eu_ai_act", "documentation",
                "Validation and testing procedures", "Description of the validation and testing procedures used including data used and metrics",
                Severity.HIGH, ["high"], ["validation", "testing", "evaluation", "benchmark", "test set"],
                ["evaluation methodology", "test results", "validation procedure"]),
        ]
