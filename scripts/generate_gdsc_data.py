import pandas as pd
import numpy as np
import os

# Set output directory
output_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdsc_cleaned"
os.makedirs(output_dir, exist_ok=True)

# Common sample IDs
num_samples = 500
sample_ids = [f"Sample_{i}" for i in range(num_samples)]

# File specs: filename → number of features
files = {
    "_file_14_cleaned.csv": 10,
    "_file_15_cleaned.csv": 15,
    "_file_16_cleaned.csv": 20
}

np.random.seed(42)  # for reproducibility

for file_name, num_features in files.items():
    features = [f"Feature_{i}" for i in range(num_features)]
    data = np.random.rand(num_samples, num_features)

    df = pd.DataFrame(data, columns=features, index=sample_ids)
    df.index.name = "Sample_ID"

    save_path = os.path.join(output_dir, file_name)
    df.to_csv(save_path)
    print(f"✅ Generated: {save_path} — shape: {df.shape}")
