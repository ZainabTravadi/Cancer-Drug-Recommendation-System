import pandas as pd
import os

# ✅ List of cleaned file paths
file_paths = [
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\cellminer_cleaned\downloaded_IC50.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned\_file_2_scaled.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdsc_cleaned\_file_14_cleaned.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdsc_cleaned\_file_15_cleaned.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdsc_cleaned\_file_16_cleaned.csv"
]

# 🧾 Metadata records list
metadata_records = []

for path in file_paths:
    try:
        df = pd.read_csv(path)

        # Set index if column name hints at it
        if df.columns[0].lower() in ["sample_id", "id", "unnamed: 0"]:
            df.set_index(df.columns[0], inplace=True)

        # Ensure index is string (for consistency)
        df.index = df.index.astype(str)

        file_name = os.path.basename(path)

        # 🔍 Determine data source
        if "cellminer" in path.lower():
            source = "CellMiner"
        elif "gdc" in path.lower():
            source = "GDC"
        elif "gdsc" in path.lower():
            source = "GDSC"
        else:
            source = "Unknown"

        dataset_name = os.path.splitext(file_name)[0]

        # 🧬 Add metadata row for each sample
        for sample in df.index:
            metadata_records.append({
                "Sample_ID": sample,
                "Dataset_Name": dataset_name,
                "Data_Source": source,
                "File_Name": file_name,
                "File_Path": path
            })

    except Exception as e:
        print(f"⚠️ Could not process {path}: {e}")

# 💾 Create DataFrame and save metadata
meta_df = pd.DataFrame(metadata_records)
output_path = r"C:\Users\DELL\Desktop\Cancer Drug System\data\metadata\master_metadata.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
meta_df.to_csv(output_path, index=False)

print(f"✅ Metadata saved to: {output_path}")
