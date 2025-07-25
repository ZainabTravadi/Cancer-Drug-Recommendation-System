from pydantic import BaseModel, Field

class DrugRecommendation(BaseModel):
    rank: int
    name: str
    confidence: str
    IC50: str
    description: str
    mechanism: str
    side_effects: str
    clinical_evidence: str = Field(..., alias="clinical_evidence")

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
