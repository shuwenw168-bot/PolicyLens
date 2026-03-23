"""Industry Best Practices — Model Cards, Datasheets, etc."""

from .base import BaseFramework, Requirement, Severity


class BestPracticesFramework(BaseFramework):
    """Requirements from Model Cards (Mitchell et al.) and Datasheets (Gebru et al.)."""

    def _build_requirements(self):
        self.requirements = [
            Requirement("BP-MC.1", "best_practices", "model_card", "Model details",
                "Basic facts about the model: developer, type, version, license",
                Severity.HIGH, ["high", "limited", "minimal"], ["model", "developer", "version", "license", "type", "architecture"],
                ["model card", "model description"]),
            Requirement("BP-MC.2", "best_practices", "model_card", "Intended use",
                "Primary intended uses and users; out-of-scope use cases",
                Severity.HIGH, ["high", "limited", "minimal"], ["intended use", "intended purpose", "out of scope", "use case"],
                ["intended use statement", "use case documentation"]),
            Requirement("BP-MC.3", "best_practices", "model_card", "Factors and metrics",
                "Relevant factors (demographic groups, instruments), metrics, and decision thresholds",
                Severity.HIGH, ["high", "limited"], ["factors", "demographic", "metrics", "threshold", "subgroup"],
                ["evaluation factors", "disaggregated metrics"]),
            Requirement("BP-MC.4", "best_practices", "model_card", "Evaluation results",
                "Results on chosen metrics disaggregated by relevant factors",
                Severity.HIGH, ["high", "limited"], ["evaluation", "results", "performance", "accuracy", "benchmark"],
                ["evaluation results", "benchmark scores", "disaggregated results"]),
            Requirement("BP-MC.5", "best_practices", "model_card", "Ethical considerations",
                "Ethical considerations including potential harms and mitigations",
                Severity.MEDIUM, ["high", "limited"], ["ethical", "harm", "social impact", "considerations", "mitigation"],
                ["ethical review", "impact assessment"]),
            Requirement("BP-MC.6", "best_practices", "model_card", "Limitations and caveats",
                "Known limitations, failure modes, and recommended caveats",
                Severity.HIGH, ["high", "limited", "minimal"], ["limitation", "caveat", "failure", "known issue", "weakness"],
                ["limitations section", "known issues"]),
            Requirement("BP-DS.1", "best_practices", "datasheet", "Dataset motivation",
                "Why was the dataset created? What tasks is it intended for?",
                Severity.HIGH, ["high"], ["dataset", "motivation", "purpose", "task", "created"],
                ["datasheet", "dataset documentation"]),
            Requirement("BP-DS.2", "best_practices", "datasheet", "Dataset composition",
                "What do instances consist of? How many instances? Is there sensitive data?",
                Severity.HIGH, ["high"], ["composition", "instances", "samples", "sensitive data", "size"],
                ["dataset description", "data composition"]),
            Requirement("BP-DS.3", "best_practices", "datasheet", "Collection process",
                "How was data collected? Who was involved? Was consent obtained?",
                Severity.MEDIUM, ["high"], ["collection", "consent", "annotation", "labeling", "crowd"],
                ["collection methodology", "consent documentation"]),
            Requirement("BP-DS.4", "best_practices", "datasheet", "Preprocessing and labeling",
                "Was data preprocessed, cleaned, or labeled? How?",
                Severity.MEDIUM, ["high", "limited"], ["preprocessing", "cleaning", "labeling", "annotation"],
                ["preprocessing pipeline", "labeling guidelines"]),
        ]
