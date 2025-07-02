# C:\Users\DELL\Desktop\Cancer Drug System\backend\nlp\parser.py

import scispacy
import spacy
from typing import Dict

# Load the scispaCy model once globally
# Use a lightweight model for now
try:
    nlp = spacy.load("en_core_sci_sm")
except:
    raise Exception("scispaCy model not found. Install with: pip install scispacy && pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_sm-0.5.1.tar.gz")

def extract_medical_entities(text: str) -> Dict[str, list]:
    """
    Extract key medical entities from free-text input using NLP.
    Returns a dictionary with grouped entities (e.g., diseases, drugs).
    """
    doc = nlp(text)
    entities = {
        "diseases": [],
        "drugs": [],
        "mutations": [],
        "other": []
    }

    for ent in doc.ents:
        label = ent.label_.lower()
        value = ent.text.strip()

        # Group known biomedical categories
        if "disease" in label or "disorder" in label:
            entities["diseases"].append(value)
        elif "chemical" in label or "drug" in label or "compound" in label:
            entities["drugs"].append(value)
        elif "gene" in label or "mutation" in label:
            entities["mutations"].append(value)
        else:
            entities["other"].append(value)

    # Remove duplicates
    for key in entities:
        entities[key] = list(set(entities[key]))

    return entities
