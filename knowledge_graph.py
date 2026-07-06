class KnowledgeGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node_id, node_type):
        self.nodes[node_id] = {
            "type": node_type
        }

    def add_edge(self, source, relation, target):
        self.edges.append({
            "source": source,
            "relation": relation,
            "target": target
        })

    def summary(self):
        return {
            "nodes": len(self.nodes),
            "edges": len(self.edges)
        }
