from dataclasses import dataclass

@dataclass
class Evidence:

    title: str
    source: str
    year: int
    confidence: float
