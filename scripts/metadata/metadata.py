import pandas as pd
import os

# List of cleaned file paths
file_paths = [
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\cellminer_cleaned\downloaded_IC50.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned\_file_2_scaled.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned\_file_3_scaled.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned\_file_4_scaled.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned\_file_5_scaled.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned\_file_7_scaled.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned\_file_8_scaled.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned\_file_11_scaled.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned\_file_12_scaled.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdsc_cleaned\_file_14_cleaned.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdsc_cleaned\_file_15_cleaned.csv",
    r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdsc_cleaned\_file_16_cleaned.csv"
]

# Store metadata here
metadata_records = []

for path in file_paths:
    try:
        df = pd.read_csv(path)
        file_name = os.path.basename(path)
        sample_ids = list(df.columns)

        # Identify source
        if "cellminer" in path.lower():
            source = "CellMiner"
        elif "gdc" in path.lower():
            source = "GDC"
        elif "gdsc" in path.lower():
            source = "GDSC"
        else:
            source = "Unknown"

        # Use file name (without extension) as a proxy for drug or data type
        dataset_name = os.path.splitext(file_name)[0]

        # Add a record for each column/sample
        for sample in sample_ids:
            metadata_records.append({
                "Sample_ID": sample,
                "Dataset_Name": dataset_name,
                "Data_Source": source,
                "File_Path": path
            })

    except Exception as e:
        print(f"⚠️ Could not read {path}: {e}")

# Create and save metadata dataframe
meta_df = pd.DataFrame(metadata_records)
output_path = r"C:\Users\DELL\Desktop\Cancer Drug System\data\metadata\master_metadata.csv"
meta_df.to_csv(output_path, index=False)

print(f"✅ Metadata saved to: {output_path}")
