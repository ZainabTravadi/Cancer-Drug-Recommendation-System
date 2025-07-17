import pandas as pd
import json
import os

input_csv = r"C:\Users\DELL\Desktop\Cancer Drug System\data\cancer_drug_db_clean.csv"
output_json = r"C:\Users\DELL\Desktop\Cancer Drug System\constants\drug_db.json"

# Read the cleaned CSV
df = pd.read_csv(input_csv)

# Convert to list of dictionaries
records = df.to_dict(orient="records")

# Ensure output directory exists
os.makedirs(os.path.dirname(output_json), exist_ok=True)

# Save as JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2)

print(f"✅ Converted to JSON: {output_json}")
