"""
AMIR Hypothesis Engine
Generates research hypotheses from the knowledge graph.
"""

class HypothesisEngine:

    def __init__(self):
        self.hypotheses = []

    def generate(self, graph):
        self.hypotheses.clear()

        for edge in graph.edges:
            hypothesis = {
                "statement":
                f"{edge['source']} may influence {edge['target']} through {edge['relation']}",
                "score": 0
            }

            self.hypotheses.append(hypothesis)

        return self.hypotheses
