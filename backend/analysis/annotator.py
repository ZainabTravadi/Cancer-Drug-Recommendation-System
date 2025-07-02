# C:\Users\DELL\Desktop\Cancer Drug System\backend\analysis\annotator.py

import pandas as pd

# Placeholder database: Variant → Gene mapping (simplified)
VARIANT_GENE_DB = {
    # Format: (chrom, pos, ref, alt): gene
    ("17", 43044295, "A", "G"): "BRCA1",
    ("13", 32914438, "C", "T"): "BRCA2",
    ("7", 55249071, "G", "A"): "EGFR",
    ("12", 25398284, "G", "T"): "KRAS",
    ("3", 178936091, "G", "A"): "PIK3CA"
    # Add more as needed
}

VARIANT_CLINICAL_INFO = {
    "BRCA1": {
        "pathogenicity": "Pathogenic",
        "clinical_use": "Germline cancer predisposition"
    },
    "BRCA2": {
        "pathogenicity": "Pathogenic",
        "clinical_use": "Germline cancer predisposition"
    },
    "EGFR": {
        "pathogenicity": "Likely pathogenic",
        "clinical_use": "Targeted therapy in lung cancer"
    },
    "KRAS": {
        "pathogenicity": "Uncertain significance",
        "clinical_use": "Prognostic biomarker"
    },
    "PIK3CA": {
        "pathogenicity": "Likely pathogenic",
        "clinical_use": "Drug resistance marker"
    }
}

def annotate_variants(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds biological and clinical annotations to each variant.
    Assumes 'chrom', 'pos', 'ref', 'alt' columns exist.
    """

    def get_gene(row):
        key = (str(row['chrom']), int(row['pos']), str(row['ref']), str(row['alt']))
        return VARIANT_GENE_DB.get(key, "Unknown")

    def get_clinical_info(gene):
        info = VARIANT_CLINICAL_INFO.get(gene, {})
        return pd.Series([
            info.get("pathogenicity", "Unknown"),
            info.get("clinical_use", "Unknown")
        ])

    # Map variants to gene names
    df['gene'] = df.apply(get_gene, axis=1)

    # Map gene to clinical metadata
    df[['pathogenicity', 'clinical_use']] = df['gene'].apply(get_clinical_info)

    return df
