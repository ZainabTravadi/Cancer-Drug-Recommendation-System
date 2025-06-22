import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Define paths to raw GDC files
file_paths = [
    r"data/raw/GDC/2ebbca96-cf79-4d4c-bc2b-ed719501e41f/_file_7.txt",
    r"data/raw/GDC/a4a6823a-fe7c-4af1-a331-3234f3a2ba15/_file_11.txt",
    r"data/raw/GDC/_file_3.txt",
    r"data/raw/GDC/_file_4.txt"
]

# Output folder
output_dir = "data/processed/gdc_cleaned"
os.makedirs(output_dir, exist_ok=True)

# Process each file
for path in file_paths:
    print(f"\n📂 Processing: {path}")
    try:
        df = pd.read_csv(path, sep='\t', comment='#', low_memory=False)
        print(f"🔹 Original shape: {df.shape}")

        # Drop fully empty rows & columns
        df.dropna(axis=0, how='all', inplace=True)
        df.dropna(axis=1, how='all', inplace=True)

        # Convert columns to numeric when possible
        df_numeric = df.apply(pd.to_numeric, errors='coerce')

        print(f"🔢 Numeric shape before filling NaNs: {df_numeric.shape}")

        # Fill NaNs with median
        df_filled = df_numeric.apply(lambda col: col.fillna(col.median()), axis=0)

        # Log2 normalization
        df_log = np.log2(df_filled + 1)

        # Z-score standardization
        scaler = StandardScaler()
        df_scaled = pd.DataFrame(
            scaler.fit_transform(df_log),
            index=df_log.index,
            columns=df_log.columns
        )

        # Save to CSV
        filename = os.path.basename(path).replace(".txt", "_scaled.csv")
        df_scaled.to_csv(os.path.join(output_dir, filename), index=False)
        print(f"✅ Cleaned + scaled data saved to: {os.path.join(output_dir, filename)}")

    except Exception as e:
        print(f"❌ Error processing {path}: {e}")
