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
        # Ensures output uses the exact field names as defined above (snake_case)
        orm_mode = True
