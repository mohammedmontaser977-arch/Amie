from .entities import Entity

class EntityRegistry:

    def __init__(self):
        self.entities = {}

    def register(self, entity: Entity):
        self.entities[entity.canonical_name] = entity

    def get(self, name):
        return self.entities.get(name)

    def all(self):
        return list(self.entities.values())
