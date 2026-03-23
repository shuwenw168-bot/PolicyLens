"""Document Analyzer — Extract compliance coverage from AI documentation."""

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from src.frameworks.base import Requirement


class DocumentAnalyzer:
    """Analyze AI system documentation for regulatory coverage."""

    def analyze_coverage(self, doc_text: str, requirements: list[Requirement]) -> pd.DataFrame:
        """Score how well documentation covers each requirement.

        Uses keyword matching + TF-IDF semantic similarity.

        Returns DataFrame with one row per requirement and coverage score.
        """
        doc_lower = doc_text.lower()
        doc_sections = self._split_sections(doc_text)
        results = []

        for req in requirements:
            # Method 1: Keyword match score (check individual words too)
            keyword_hits = 0
            for kw in req.keywords:
                if kw.lower() in doc_lower:
                    keyword_hits += 1
                else:
                    # Partial match: check if individual words from the keyword appear
                    kw_words = kw.lower().split()
                    if len(kw_words) > 1 and all(w in doc_lower for w in kw_words):
                        keyword_hits += 0.7
                    elif any(w in doc_lower for w in kw_words if len(w) > 3):
                        keyword_hits += 0.3
            keyword_score = min(keyword_hits / max(len(req.keywords), 1), 1.0)

            # Method 2: Evidence match (check for specific evidence types)
            evidence_hits = 0
            for ev in req.evidence_needed:
                ev_lower = ev.lower()
                if ev_lower in doc_lower:
                    evidence_hits += 1
                else:
                    ev_words = ev_lower.split()
                    if any(w in doc_lower for w in ev_words if len(w) > 4):
                        evidence_hits += 0.5
            evidence_score = min(evidence_hits / max(len(req.evidence_needed), 1), 1.0)

            # Method 3: Semantic similarity to requirement description
            semantic_score = self._compute_semantic_similarity(doc_text, req.description)

            # Composite coverage score
            coverage = 0.4 * keyword_score + 0.35 * evidence_score + 0.25 * semantic_score

            # Find best matching section
            best_section = self._find_best_section(doc_sections, req)

            results.append({
                "requirement_id": req.id,
                "framework": req.framework,
                "area": req.area,
                "title": req.title,
                "severity": req.severity.value,
                "keyword_score": round(keyword_score, 3),
                "evidence_score": round(evidence_score, 3),
                "semantic_score": round(semantic_score, 3),
                "coverage_score": round(coverage, 3),
                "coverage_level": self._coverage_level(coverage),
                "best_matching_section": best_section[:100] if best_section else "None found",
            })

        return pd.DataFrame(results)

    def _split_sections(self, text: str) -> list[str]:
        sections = re.split(r'\n#{1,3}\s', text)
        return [s.strip() for s in sections if len(s.strip()) > 20]

    def _compute_semantic_similarity(self, doc: str, requirement: str) -> float:
        try:
            tfidf = TfidfVectorizer(max_features=500, stop_words="english")
            vectors = tfidf.fit_transform([doc, requirement])
            return float(cosine_similarity(vectors[0:1], vectors[1:2])[0, 0])
        except ValueError:
            return 0.0

    def _find_best_section(self, sections: list[str], req: Requirement) -> str:
        if not sections:
            return ""
        scores = []
        for section in sections:
            score = sum(1 for kw in req.keywords if kw.lower() in section.lower())
            scores.append(score)
        best_idx = np.argmax(scores)
        return sections[best_idx] if scores[best_idx] > 0 else ""

    def _coverage_level(self, score: float) -> str:
        if score >= 0.7:
            return "GOOD"
        elif score >= 0.4:
            return "PARTIAL"
        elif score > 0.1:
            return "WEAK"
        else:
            return "MISSING"
