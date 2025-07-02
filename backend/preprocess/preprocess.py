# C:\Users\DELL\Desktop\Cancer Drug System\backend\preprocessing\preprocess.py

import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleanup: drop empty rows/columns, remove obvious noise,
    and standardize column names.
    """
    # Drop fully empty rows and columns
    df.dropna(axis=0, how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)

    # Strip column names of whitespace
    df.columns = [col.strip().lower() for col in df.columns]

    # Remove rows with missing essential fields if they exist
    essential_cols = ['chrom', 'pos', 'ref', 'alt']
    for col in essential_cols:
        if col in df.columns:
            df = df[df[col].notna()]

    return df


def normalize_variants(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure consistency in mutation/variant representation:
    - Create unified 'variant_id' column
    - Standardize chromosome notation
    """
    # Add variant ID if not present
    if 'variant_id' not in df.columns:
        df['variant_id'] = df.apply(
            lambda row: f"{row.get('chrom', 'NA')}-{row.get('pos', 'NA')}-{row.get('ref', '')}>{row.get('alt', '')}", axis=1
        )

    # Normalize chromosome format (e.g., "chr1" → "1")
    if 'chrom' in df.columns:
        df['chrom'] = df['chrom'].astype(str).str.replace('chr', '', case=False)

    return df
