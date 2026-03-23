"""NIST AI Risk Management Framework 1.0 — Encoded Requirements"""

from .base import BaseFramework, Requirement, Severity


class NISTRMFFramework(BaseFramework):
    """NIST AI RMF organized by GOVERN, MAP, MEASURE, MANAGE functions."""

    def _build_requirements(self):
        self.requirements = [
            # ── GOVERN ──
            Requirement("NIST-GV.1", "nist_rmf", "govern", "AI governance structure",
                "Policies, processes, procedures, and practices are in place for governing AI risks",
                Severity.HIGH, ["high", "limited", "minimal"], ["governance", "policy", "procedure", "accountability"],
                ["AI governance policy", "roles and responsibilities"]),
            Requirement("NIST-GV.2", "nist_rmf", "govern", "Accountability structure",
                "Clear accountability structures and defined roles for AI risk management",
                Severity.HIGH, ["high", "limited"], ["accountability", "roles", "responsibility", "oversight"],
                ["RACI matrix", "accountability documentation"]),
            Requirement("NIST-GV.3", "nist_rmf", "govern", "Workforce diversity",
                "Workforce diversity, equity, inclusion and accessibility processes are prioritized",
                Severity.MEDIUM, ["high", "limited"], ["diversity", "equity", "inclusion", "DEI"],
                ["DEI policy", "team composition disclosure"]),
            Requirement("NIST-GV.4", "nist_rmf", "govern", "Organizational risk tolerance",
                "Organizational risk tolerances are defined and documented",
                Severity.HIGH, ["high"], ["risk tolerance", "risk appetite", "threshold"],
                ["risk tolerance statement", "risk appetite framework"]),
            Requirement("NIST-GV.5", "nist_rmf", "govern", "Third-party risk",
                "Processes for managing AI risks from third-party entities",
                Severity.MEDIUM, ["high"], ["third party", "vendor", "supply chain", "external"],
                ["vendor assessment", "third-party risk policy"]),

            # ── MAP ──
            Requirement("NIST-MP.1", "nist_rmf", "map", "Context establishment",
                "Context is established and understood including intended deployment, users, and affected groups",
                Severity.HIGH, ["high", "limited"], ["context", "intended use", "deployment", "stakeholder", "affected"],
                ["context analysis", "stakeholder mapping", "use case definition"]),
            Requirement("NIST-MP.2", "nist_rmf", "map", "Risk categorization",
                "AI system is categorized according to risk level based on potential impact",
                Severity.HIGH, ["high", "limited"], ["categorization", "risk level", "impact", "classification"],
                ["risk categorization", "impact assessment"]),
            Requirement("NIST-MP.3", "nist_rmf", "map", "Benefits and costs",
                "Benefits and costs of AI system compared to alternatives including non-AI approaches",
                Severity.MEDIUM, ["high"], ["benefits", "costs", "alternatives", "impact"],
                ["cost-benefit analysis", "alternatives assessment"]),
            Requirement("NIST-MP.4", "nist_rmf", "map", "Impact on individuals",
                "Risks and impacts to individuals, communities, and the environment are characterized",
                Severity.HIGH, ["high"], ["impact", "individuals", "communities", "environment", "societal"],
                ["impact assessment", "societal impact analysis"]),

            # ── MEASURE ──
            Requirement("NIST-MS.1", "nist_rmf", "measure", "Appropriate metrics",
                "Appropriate metrics, methods, and tools are identified for measuring AI risks",
                Severity.HIGH, ["high", "limited"], ["metrics", "measurement", "evaluation", "benchmark"],
                ["evaluation metrics", "measurement methodology"]),
            Requirement("NIST-MS.2", "nist_rmf", "measure", "Fairness evaluation",
                "AI systems are evaluated for trustworthy characteristics including fairness",
                Severity.HIGH, ["high"], ["fairness", "bias", "equity", "discrimination", "demographic parity"],
                ["fairness evaluation", "bias audit", "disaggregated metrics"]),
            Requirement("NIST-MS.3", "nist_rmf", "measure", "Explainability evaluation",
                "AI system outputs and decisions are evaluated for explainability",
                Severity.MEDIUM, ["high", "limited"], ["explainability", "interpretability", "explanation"],
                ["explainability assessment", "interpretation documentation"]),
            Requirement("NIST-MS.4", "nist_rmf", "measure", "Safety evaluation",
                "AI system safety is evaluated including potential for harm",
                Severity.HIGH, ["high"], ["safety", "harm", "dangerous", "adverse"],
                ["safety evaluation", "harm assessment"]),
            Requirement("NIST-MS.5", "nist_rmf", "measure", "Security and resilience",
                "AI system security and resilience are evaluated against adversarial threats",
                Severity.HIGH, ["high"], ["security", "resilience", "adversarial", "robustness", "attack"],
                ["security assessment", "adversarial testing", "red teaming"]),

            # ── MANAGE ──
            Requirement("NIST-MG.1", "nist_rmf", "manage", "Risk response",
                "AI risks are prioritized, responded to, and managed based on assessed risk levels",
                Severity.HIGH, ["high", "limited"], ["risk response", "mitigation", "risk management"],
                ["risk treatment plan", "mitigation actions"]),
            Requirement("NIST-MG.2", "nist_rmf", "manage", "Continuous monitoring",
                "Strategies for monitoring AI risks over time are implemented",
                Severity.HIGH, ["high"], ["monitoring", "continuous", "ongoing", "drift", "degradation"],
                ["monitoring plan", "drift detection", "performance tracking"]),
            Requirement("NIST-MG.3", "nist_rmf", "manage", "Incident response",
                "Responses to identified AI risks include mechanisms for decommissioning or appeals",
                Severity.MEDIUM, ["high"], ["incident", "decommission", "appeal", "rollback", "response"],
                ["incident response plan", "rollback procedure"]),
            Requirement("NIST-MG.4", "nist_rmf", "manage", "Risk communication",
                "AI risk management results are communicated to relevant stakeholders",
                Severity.MEDIUM, ["high", "limited"], ["communication", "stakeholder", "reporting", "disclosure"],
                ["stakeholder communication plan", "risk report"]),
        ]
