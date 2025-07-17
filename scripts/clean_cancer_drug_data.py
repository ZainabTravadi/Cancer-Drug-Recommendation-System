import pandas as pd

input_csv = 'data/cancer_drug_db.csv'
output_csv = 'data/cancer_drug_db_clean.csv'

# Define custom missing values
na_values = ["", "N/A", "n/a", "NA", "na", "All", "ALL", " "]

# Load data
df = pd.read_csv(input_csv, na_values=na_values)

# Strip all strings
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Drop rows missing critical fields
df.dropna(subset=['name', 'target_gene', 'cancer_type', 'ic50', 'confidence'], inplace=True)

# Optional: convert columns to proper types
df['confidence'] = pd.to_numeric(df['confidence'], errors='coerce')
df['ic50'] = pd.to_numeric(df['ic50'], errors='coerce')

# Drop rows with invalid numbers
df.dropna(subset=['confidence', 'ic50'], inplace=True)

# Save clean file
df.to_csv(output_csv, index=False)
print("✅ Cleaned data saved to:", output_csv)
