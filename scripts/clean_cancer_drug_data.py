import pandas as pd

input_csv = 'data/cancer_drug_db.csv'
output_csv = 'data/cancer_drug_db_clean.csv'

na_values = ["", "N/A", "n/a", "NA", "na", "All", "ALL", " "]

df = pd.read_csv(input_csv, na_values=na_values)

df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

df.dropna(subset=['name', 'target_gene', 'cancer_type', 'ic50', 'confidence'], inplace=True)

df['confidence'] = pd.to_numeric(df['confidence'], errors='coerce')
df['ic50'] = pd.to_numeric(df['ic50'], errors='coerce')

df.dropna(subset=['confidence', 'ic50'], inplace=True)

df['mutation_types'] = df['mutation_types'].fillna("Unknown")
df['side_effects'] = df['side_effects'].fillna("Not reported")
df['mechanism'] = df['mechanism'].fillna("Unknown mechanism")
df['clinical_trial'] = df['clinical_trial'].fillna("Not specified")
df['approval_status'] = df['approval_status'].fillna("Pending")

df.to_csv(output_csv, index=False)
print("Cleaned data saved to:", output_csv)
