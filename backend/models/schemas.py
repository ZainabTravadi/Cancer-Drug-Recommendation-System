# models/schemas.py
from pydantic import BaseModel
from typing import Optional

class RecommendationRequest(BaseModel):
    cancer_type: str
    notes: Optional[str] = None

class DrugRecommendation(BaseModel):
    rank: int
    name: str
    confidence: str
    IC50: str
    description: str
    mechanism: str
    side_effects: str
    clinical_evidence: str
