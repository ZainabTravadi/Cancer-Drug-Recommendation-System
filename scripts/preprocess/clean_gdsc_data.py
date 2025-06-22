import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# GDSC file paths
file_paths = [
    r"data/raw/GDSC/_file_14.csv",
    r"data/raw/GDSC/_file_15.csv",
    r"data/raw/GDSC/_file_16.csv"
]

# Output directory
output_dir = "data/processed/gdsc_cleaned"
os.makedirs(output_dir, exist_ok=True)

for path in file_paths:
    print(f"\n📂 Processing: {path}")
    try:
        # Step 1: Read CSV
        df = pd.read_csv(path)
        print(f"🔹 Original shape: {df.shape}")

        # Step 2: Drop fully empty rows and columns
        df.dropna(axis=0, how='all', inplace=True)
        df.dropna(axis=1, how='all', inplace=True)

        # Step 3: Convert all columns to numeric (non-numeric → NaN)
        df_numeric = df.apply(pd.to_numeric, errors='coerce')
        print(f"🔢 Numeric data shape: {df_numeric.shape}")

        # Step 4: Fill NaNs with median per column
        df_filled = df_numeric.apply(lambda col: col.fillna(col.median()), axis=0)

        # Step 5: Log2 transformation if no negatives
        if (df_filled >= 0).all().all():
            df_log = np.log2(df_filled + 1)
        else:
            df_log = df_filled
            print("⚠️ Skipped log2 due to negative values")

        # Step 6: Z-score standardization
        scaler = StandardScaler()
        df_scaled = pd.DataFrame(
            scaler.fit_transform(df_log),
            columns=df_log.columns,
            index=df_log.index
        )

        # Step 7: Save cleaned CSV
        out_name = os.path.basename(path).replace(".csv", "_cleaned.csv")
        df_scaled.to_csv(os.path.join(output_dir, out_name), index=False)
        print(f"✅ Saved cleaned file to: {os.path.join(output_dir, out_name)}")

    except Exception as e:
        print(f"❌ Error processing {path}: {e}")
