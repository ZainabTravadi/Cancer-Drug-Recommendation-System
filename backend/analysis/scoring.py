# C:\Users\DELL\Desktop\Cancer Drug System\backend\analysis\scoring.py

import pandas as pd
from typing import List, Dict

# Drug knowledge base (mockup for now)
DRUG_DATABASE = {
    "Pembrolizumab (Keytruda)": {
        "confidence": 94,
        "ic50": "0.12 nM",
        "mechanism": "Immune checkpoint inhibitor",
        "side_effects": "Mild to moderate immune-related adverse events",
        "clinical_evidence": "Phase III KEYNOTE-189",
        "description": "PD-1 inhibitor that enhances immune system response against cancer cells. Highly effective for tumors with high PD-L1 expression."
    },
    "Trastuzumab (Herceptin)": {
        "confidence": 89,
        "ic50": "1.8 nM",
        "mechanism": "HER2 receptor antagonist",
        "side_effects": "Cardiotoxicity, fever, chills",
        "clinical_evidence": "Phase III CLEOPATRA",
        "description": "Monoclonal antibody targeting HER2 receptor, effective in HER2-positive breast cancers."
    },
    # Add more drug entries...
}

def generate_scores(annotated_df: pd.DataFrame, extracted_context: Dict[str, List[str]]) -> List[Dict]:
    """
    Scores drugs based on annotations and patient history.
    Returns a list of drug recommendation dicts.
    """

    # Placeholder: Assume one top drug for demo purposes
    # Later: Match gene–drug pairs, cancer types, mutation effects, etc.

    results = []

    for drug, data in DRUG_DATABASE.items():
        recommendation = {
            "name": drug,
            "confidence": f"{data['confidence']}% Confidence",
            "ic50": data["ic50"],
            "mechanism": data["mechanism"],
            "side_effects": data["side_effects"],
            "clinical_evidence": data["clinical_evidence"],
            "description": data["description"]
        }

        results.append(recommendation)

    # Sort descending by confidence
    results = sorted(results, key=lambda x: int(x["confidence"].replace("% Confidence", "").strip()), reverse=True)

    return results
