"""
AMIR Core - Biomedical Entity Model
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class EntityType(str, Enum):
    DISEASE = "disease"
    GENE = "gene"
    PROTEIN = "protein"
    DRUG = "drug"
    PATHWAY = "pathway"
    CELL_TYPE = "cell_type"
    CYTOKINE = "cytokine"
    CHEMOKINE = "chemokine"
    BIOMARKER = "biomarker"
    PHENOTYPE = "phenotype"
    MECHANISM = "mechanism"
    TREATMENT = "treatment"
    PATHOGEN = "pathogen"
    ANATOMY = "anatomy"
    TEST = "test"
    RISK_FACTOR = "risk_factor"
    SYMPTOM = "symptom"
    GENETIC_VARIANT = "genetic_variant"
    OTHER = "other"


@dataclass
class Entity:
    canonical_name: str
    entity_type: EntityType
    aliases: List[str] = field(default_factory=list)
    ontology_ids: Dict[str, str] = field(default_factory=dict)
    description: str = ""
    entity_id: Optional[str] = None

    def __post_init__(self):
        if isinstance(self.entity_type, str):
            self.entity_type = EntityType(self.entity_type)

        if self.entity_id is None:
            name = self.canonical_name.lower()
            name = name.replace(" ", "_")
            name = name.replace("-", "_")

            self.entity_id = (
                f"{self.entity_type.value}:{name}"
            )

    def matches(self, name: str) -> bool:
        normalized = name.strip().lower()

        if self.canonical_name.lower() == normalized:
            return True

        return any(
            alias.lower() == normalized
            for alias in self.aliases
        )

    def to_dict(self) -> Dict:
        return {
            "entity_id": self.entity_id,
            "canonical_name": self.canonical_name,
            "entity_type": self.entity_type.value,
            "aliases": self.aliases,
            "ontology_ids": self.ontology_ids,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Entity":
        return cls(
            entity_id=data.get("entity_id"),
            canonical_name=data["canonical_name"],
            entity_type=EntityType(data["entity_type"]),
            aliases=data.get("aliases", []),
            ontology_ids=data.get("ontology_ids", {}),
            description=data.get("description", ""),
  )
