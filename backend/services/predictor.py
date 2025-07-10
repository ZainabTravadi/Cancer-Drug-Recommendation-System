# services/predictor.py

from typing import List, Dict

def predict_drug_scores(gene_features: List[str]) -> Dict[str, float]:
    """
    Mock predictor that assigns scores to drugs based on presence of specific genes.
    """
    # Mock rules for assigning scores
    score_table = {
        "TP53": {"Pembrolizumab (Keytruda)": 0.9},
        "EGFR": {"Erlotinib": 0.95},
        "BRCA1": {"Olaparib": 0.92},
        "KRAS": {"Sotorasib": 0.89}
    }

    drug_scores = {}

    for gene in gene_features:
        if gene in score_table:
            for drug, score in score_table[gene].items():
                drug_scores[drug] = max(drug_scores.get(drug, 0), score)

    return drug_scores
