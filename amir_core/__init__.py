from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Entity:
    canonical_name: str
    entity_type: str
    aliases: List[str] = field(default_factory=list)
    ontology_ids: Dict[str, str] = field(default_factory=dict)
    description: str = ""
