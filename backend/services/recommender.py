import json
import os

# Path to your drug DB
DRUG_DB_PATH = os.path.join(os.path.dirname(__file__), '../constants/drug_db.json')

# Load it once when this module is imported
with open(DRUG_DB_PATH, 'r', encoding='utf-8') as f:
    DRUG_DATABASE = json.load(f)

def recommend_top_drugs(drug_scores, top_n=5):
    """
    Select top N drugs from DRUG_DATABASE based on `drug_scores` dict.
    `drug_scores` = {'DrugName': score, ...}
    """
    # Attach score to each drug in DB
    scored_drugs = []
    for drug in DRUG_DATABASE:
        name = drug.get("name")
        if name in drug_scores:
            drug_copy = drug.copy()
            drug_copy["confidence"] = round(drug_scores[name], 2)
            scored_drugs.append(drug_copy)

    # Sort by score and return top N
    scored_drugs.sort(key=lambda x: x['confidence'], reverse=True)
    return scored_drugs[:top_n]
