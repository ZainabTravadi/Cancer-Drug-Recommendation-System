import pandas as pd
import os

gdc_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned"
gdc_files = [f for f in os.listdir(gdc_dir) if f.endswith("_scaled.csv")]

for file in gdc_files:
    path = os.path.join(gdc_dir, file)
    df = pd.read_csv(path)
    df.set_index(df.columns[0], inplace=True)
    print(f"📁 {file} → Rows: {df.shape[0]}, Index samples: {df.index.tolist()[:3]}")
