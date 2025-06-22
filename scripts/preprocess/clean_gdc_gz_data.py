import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# GDC .gz file paths
file_paths = [
    r"data/raw/GDC/5f460393-1616-4b5a-8f4a-f500777ce7d0/_file_9.gz",
    r"data/raw/GDC/_file_2.gz"
]

output_dir = "data/processed/gdc_cleaned"
os.makedirs(output_dir, exist_ok=True)

for path in file_paths:
    print(f"\n📂 Processing: {path}")
    try:
        # Try reading file with proper encoding and fallback
        try:
            df = pd.read_csv(
                path, sep='\t', compression='gzip', comment='#', 
                encoding='utf-8', engine='python', on_bad_lines='skip'
            )
        except UnicodeDecodeError:
            df = pd.read_csv(
                path, sep='\t', compression='gzip', comment='#', 
                encoding='ISO-8859-1', engine='python', on_bad_lines='skip'
            )

        print(f"🔹 Original shape: {df.shape}")

        # Drop empty rows/cols
        df.dropna(axis=0, how='all', inplace=True)
        df.dropna(axis=1, how='all', inplace=True)

        # Convert to numeric
        df_numeric = df.apply(pd.to_numeric, errors='coerce')

        # Replace infinities with NaN
        df_numeric.replace([np.inf, -np.inf], np.nan, inplace=True)

        # Cap extreme large values (to avoid float64 crash)
        df_numeric = df_numeric.clip(upper=1e6)

        print(f"🔢 Numeric shape before filling NaNs: {df_numeric.shape}")

        # Fill NaNs with median
        df_filled = df_numeric.apply(lambda col: col.fillna(col.median()), axis=0)

        # Log2 transform
        df_log = np.log2(df_filled + 1)

        # Z-score scaling
        scaler = StandardScaler()
        df_scaled = pd.DataFrame(
            scaler.fit_transform(df_log),
            index=df_log.index,
            columns=df_log.columns
        )

        # Save to CSV
        filename = os.path.basename(path).replace(".gz", "_scaled.csv")
        df_scaled.to_csv(os.path.join(output_dir, filename), index=False)
        print(f"✅ Cleaned + scaled data saved to: {os.path.join(output_dir, filename)}")

    except Exception as e:
        print(f"❌ Error processing {path}: {e}")
