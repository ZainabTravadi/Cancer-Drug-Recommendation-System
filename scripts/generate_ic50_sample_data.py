import pandas as pd
import numpy as np

# ✅ Create 500 sample IDs
sample_ids = [f"Sample_{i}" for i in range(500)]

# Simulate 5 drug responses (IC50 values)
num_drugs = 5
columns = [f"Drug_{1000 + i}_IC50" for i in range(num_drugs)]

# Generate random IC50 values (0 to 10)
np.random.seed(0)
data = np.random.rand(500, num_drugs) * 10

# Create DataFrame
df_ic50 = pd.DataFrame(data, columns=columns, index=sample_ids)
df_ic50.index.name = "Sample_ID"

# Save to CSV
output_path = r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\cellminer_cleaned\downloaded_IC50.csv"
df_ic50.to_csv(output_path)

print(f"✅ IC50 data saved to: {output_path} — Shape: {df_ic50.shape}")
