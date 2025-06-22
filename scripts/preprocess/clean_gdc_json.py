import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Input and Output paths
input_path = r"data/raw/GDC/_file_5.json"
output_dir = "data/processed/gdc_cleaned"
os.makedirs(output_dir, exist_ok=True)

print(f"📂 Processing: {input_path}")
try:
    # Step 1: Load JSON
    df = pd.read_json(input_path, orient='records', lines=False)
    print(f"🔹 Loaded JSON. Shape: {df.shape}")

    # Step 2: Drop fully empty rows and columns
    df.dropna(axis=0, how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)

    # Step 3: Convert to numeric where possible
    df_numeric = df.apply(pd.to_numeric, errors='coerce')
    print(f"🔢 Numeric data shape: {df_numeric.shape}")

    # Step 4: Fill NaNs with column median
    df_filled = df_numeric.apply(lambda col: col.fillna(col.median()), axis=0)

    # Step 5: Log2 transform (if all values >= 0)
    if (df_filled >= 0).all().all():
        df_log = np.log2(df_filled + 1)
    else:
        df_log = df_filled  # skip log if negatives present
        print("⚠️ Skipped log2 due to negative values")

    # Step 6: Z-score standardization
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(
        scaler.fit_transform(df_log),
        columns=df_log.columns,
        index=df_log.index
    )

    # Step 7: Save to CSV
    out_path = os.path.join(output_dir, "_file_5_cleaned.csv")
    df_scaled.to_csv(out_path, index=False)
    print(f"✅ Cleaned data saved to: {out_path}")

except Exception as e:
    print(f"❌ Error processing JSON file: {e}")
