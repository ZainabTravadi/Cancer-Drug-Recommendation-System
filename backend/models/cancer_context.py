# C:\Users\DELL\Desktop\Cancer Drug System\backend\models\cancer_context.py

import pandas as pd

# Example gene–cancer relevance dictionary (real version should come from a database or CSV)
CANCER_GENE_MAP = {
    "breast cancer": {"BRCA1", "BRCA2", "TP53", "PIK3CA"},
    "lung cancer": {"EGFR", "ALK", "KRAS", "TP53"},
    "colorectal cancer": {"APC", "KRAS", "TP53", "PIK3CA"},
    "prostate cancer": {"AR", "TP53", "PTEN"},
    "melanoma": {"BRAF", "NRAS", "KIT"},
    # Add more types and genes as needed
}

def filter_by_cancer_type(df: pd.DataFrame, cancer_type: str) -> pd.DataFrame:
    """
    Filters variants based on genes relevant to the given cancer type.
    Assumes that a 'gene' column is present or annotated beforehand.
    """
    cancer_type = cancer_type.lower()

    if 'gene' not in df.columns:
        raise ValueError("Gene column not found in data. Run annotation before filtering by cancer type.")

    if cancer_type not in CANCER_GENE_MAP:
        raise ValueError(f"Unsupported cancer type: {cancer_type}. Please add it to CANCER_GENE_MAP.")

    relevant_genes = CANCER_GENE_MAP[cancer_type]
    filtered_df = df[df['gene'].isin(relevant_genes)].copy()

    return filtered_df
