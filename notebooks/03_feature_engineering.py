import pandas as pd
import numpy as np
import os
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler

# 📁 Paths
gdc_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned"
gdsc_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdsc_cleaned"
ic50_path = r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\cellminer_cleaned\downloaded_IC50.csv"
output_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\data\final"
os.makedirs(output_dir, exist_ok=True)

# ✅ Load IC50 Labels
y_df = pd.read_csv(ic50_path)
y_df.set_index(y_df.columns[0], inplace=True)
print(f"✅ IC50 labels shape: {y_df.shape}")

# 🔄 Function to load and clean features
def load_feature_data(directory):
    feature_dfs = []
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            path = os.path.join(directory, file)
            df = pd.read_csv(path)

            if df.columns[0].lower() in ['id', 'sample_id', 'sampleid', 'unnamed: 0']:
                df.set_index(df.columns[0], inplace=True)
            else:
                continue

            df.index = df.index.astype(str)
            df = df.loc[~df.index.duplicated(keep='first')]
            feature_dfs.append(df)

    if not feature_dfs:
        raise ValueError(f"❌ No valid files found in {directory}")
    
    return pd.concat(feature_dfs, axis=1, join="inner")

# ✅ Load features
print("📥 Loading GDC...")
gdc = load_feature_data(gdc_dir)

print("📥 Loading GDSC...")
gdsc = load_feature_data(gdsc_dir)

# ✅ Merge features
X_raw = pd.concat([gdc, gdsc], axis=1, join="inner")
print("✅ Raw merged features shape:", X_raw.shape)

# ✅ Align with IC50
X = X_raw[X_raw.index.isin(y_df.index)]
y = y_df.loc[X.index]

if X.empty or y.empty:
    raise ValueError("❌ No overlapping samples between features and IC50 data")

print(f"✅ Aligned X shape: {X.shape}, y shape: {y.shape}")

# ✅ Scale features
X_scaled = pd.DataFrame(StandardScaler().fit_transform(X), columns=X.columns, index=X.index)

# ✅ Variance threshold
selector = VarianceThreshold(threshold=0.01)
X_high_var = pd.DataFrame(selector.fit_transform(X_scaled),
                          columns=X_scaled.columns[selector.get_support()],
                          index=X_scaled.index)
print("✅ After variance filter:", X_high_var.shape)

# ✅ Remove NaN-heavy columns
nan_threshold = 0.2
valid_cols = X_high_var.columns[X_high_var.isnull().mean() < nan_threshold]
X_final = X_high_var[valid_cols].dropna()
y_final = y.loc[X_final.index]
print("✅ Final features shape:", X_final.shape)

# ✅ Save outputs
X_final.to_csv(os.path.join(output_dir, "features_X.csv"))
y_final.to_csv(os.path.join(output_dir, "labels_y.csv"))
Xy_final = X_final.copy()
Xy_final[y_final.columns] = y_final
Xy_final.to_csv(os.path.join(output_dir, "Xy_final.csv"))

print("✅ Feature engineering complete! Files saved:")
print("📁 features_X.csv")
print("📁 labels_y.csv")
print("📁 Xy_final.csv")
