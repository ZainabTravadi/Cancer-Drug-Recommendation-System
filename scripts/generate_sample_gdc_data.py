import pandas as pd
import numpy as np

# Number of samples and features
num_samples = 500
num_features = 20

# Create a random dataframe with values between 0 and 1
np.random.seed(42)  # for reproducibility
data = np.random.rand(num_samples, num_features)

# Create column names like Gene_1, Gene_2, ...
columns = [f"Gene_{i+1}" for i in range(num_features)]

# Create sample IDs like Sample_0, Sample_1, ...
index = [f"Sample_{i}" for i in range(num_samples)]

# Create DataFrame
df = pd.DataFrame(data, columns=columns, index=index)

# Save the file
output_path = r"C:\Users\DELL\Desktop\Cancer Drug System\data\processed\gdc_cleaned\_file_2_scaled.csv"
df.to_csv(output_path)

print(f"✅ Generated synthetic data: {output_path}")
