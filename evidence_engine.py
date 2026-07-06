"""
Evidence Scoring Engine
"""

class EvidenceEngine:

    def evidence_score(
        self,
        publications,
        contradictions
    ):

        score = publications * 10
        score -= contradictions * 5

        if score < 0:
            score = 0

        return score
