"""
Knowledge Inbox
Stores new scientific evidence before integration.
"""

class KnowledgeInbox:

    def __init__(self):
        self.items = []

    def add(self, title, source, evidence_level):
        self.items.append({
            "title": title,
            "source": source,
            "evidence_level": evidence_level
        })

    def all(self):
        return self.items
