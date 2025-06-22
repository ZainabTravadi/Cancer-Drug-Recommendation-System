import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# List of GDC TSV files
file_paths = [
    r"data/raw/GDC/3e9ef4c8-67e7-4d67-a65b-cae63c4b1221/_file_8.tsv",
    r"data/raw/GDC/cc707618-7fb0-4f22-8c0d-4687ed4d2c93/_file_12.tsv"
]

# Output folder
output_dir = "data/processed/gdc_cleaned"
os.makedirs(output_dir, exist_ok=True)

for path in file_paths:
    print(f"\n📂 Processing: {path}")
    try:
        # Step 1: Load TSV file
        df = pd.read_csv(path, sep='\t', comment='#', low_memory=False)
        print(f"🔹 Original shape: {df.shape}")

        # Step 2: Drop fully empty rows & columns
        df.dropna(axis=0, how='all', inplace=True)
        df.dropna(axis=1, how='all', inplace=True)

        # Step 3: Try to convert to numeric (non-numeric cells become NaN)
        df_numeric = df.apply(pd.to_numeric, errors='coerce')
        print(f"🔢 Numeric shape before filling NaNs: {df_numeric.shape}")

        # Step 4: Fill NaNs with median
        df_filled = df_numeric.apply(lambda col: col.fillna(col.median()), axis=0)

        # Step 5: Log2 normalization
        df_log = np.log2(df_filled + 1)

        # Step 6: Z-score standardization
        scaler = StandardScaler()
        df_scaled = pd.DataFrame(
            scaler.fit_transform(df_log),
            index=df_log.index,
            columns=df_log.columns
        )

        # Step 7: Save to CSV
        filename = os.path.basename(path).replace(".tsv", "_scaled.csv")
        df_scaled.to_csv(os.path.join(output_dir, filename), index=False)
        print(f"✅ Cleaned + scaled data saved to: {os.path.join(output_dir, filename)}")

    except Exception as e:
        print(f"❌ Error processing {path}: {e}")
