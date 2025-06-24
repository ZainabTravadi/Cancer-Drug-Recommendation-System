import pandas as pd
import os

# 📁 Define all your directories
directories = {
    "cellminer_cleaned": r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\cellminer_cleaned",
    "gdc_cleaned": r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned",
    "gdsc_cleaned": r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdsc_cleaned",
    "CellMiner_raw": r"C:\Users\DELL\Desktop\Cancer Drug System\data\raw\CellMiner",
    "GDC_raw": r"C:\Users\DELL\Desktop\Cancer Drug System\data\raw\GDC",
    "GDSC_raw": r"C:\Users\DELL\Desktop\Cancer Drug System\data\raw\GDSC",
}

# 🔁 Iterate through all cleaned dirs
for name, cleaned_dir in directories.items():
    print(f"\n🔍 Checking directory: {name}")
    
    for file in os.listdir(cleaned_dir):
        if not file.endswith(".csv"):
            continue

        path = os.path.join(cleaned_dir, file)

        try:
            df = pd.read_csv(path)

            # If already has a proper index, skip
            if df.index.name is not None or df.index.dtype == object:
                print(f"✅ Skipping {file} — index looks okay")
                continue

            # If the first column is a likely ID column
            id_col = df.columns[0]
            id_sample = df[id_col].head(3)

            if id_sample.isnull().all():
                print(f"⚠️ {file} — First column is NaN. Can't fix.")
                continue

            # Fix the index
            df.set_index(id_col, inplace=True)
            df.to_csv(path)
            print(f"🔧 Fixed index for: {file}")

        except Exception as e:
            print(f"❌ Failed to process {file}: {e}")
