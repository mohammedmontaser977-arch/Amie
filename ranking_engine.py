"""
AMIR Hypothesis Ranking Engine
"""

class RankingEngine:

    def rank(self, hypotheses):

        for h in hypotheses:
            h["score"] = len(h["statement"])

        hypotheses.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return hypotheses
