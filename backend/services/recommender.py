# services/recommender.py

import json
from typing import Dict, List
from models.schemas import DrugRecommendation

DRUG_DB_PATH = "constants/drug_db.json"

def recommend_top_drugs(drug_scores: Dict[str, float]) -> List[DrugRecommendation]:
    """
    Match drug scores with drug info from JSON and return top 5 recommendations.
    """
    with open(DRUG_DB_PATH, "r", encoding="utf-8") as f:
        drug_db = json.load(f)

    recommendations = []

    for drug_name, score in drug_scores.items():
        # Find drug info from DB
        drug_info = next((drug for drug in drug_db if drug["name"] == drug_name), None)
        if not drug_info:
            continue

        recommendation = DrugRecommendation(
            rank=0,  # Will be assigned later
            name=drug_name,
            confidence=f"{round(score * 100)}%",
            IC50=drug_info.get("IC50", "N/A"),
            description=drug_info.get("description", ""),
            mechanism=drug_info.get("mechanism", ""),
            side_effects=drug_info.get("side_effects", ""),
            clinical_evidence=drug_info.get("clinical_evidence", "")
        )
        recommendations.append(recommendation)

    # Sort and assign rank
    recommendations.sort(key=lambda x: float(x.confidence.strip('%')), reverse=True)
    for idx, rec in enumerate(recommendations[:5]):
        rec.rank = idx + 1

    return recommendations[:5]
