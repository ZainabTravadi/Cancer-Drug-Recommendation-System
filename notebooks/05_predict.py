import os
import pandas as pd
import joblib
from glob import glob

# 📁 Paths
data_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\data\final"
model_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\models"
output_path = os.path.join(data_dir, "predictions.csv")

# 📥 Load features
X = pd.read_csv(os.path.join(data_dir, "features_X.csv"), index_col=0)

# 📦 Get all model files
model_files = glob(os.path.join(model_dir, "*.pkl"))

# 📊 Prediction results
all_predictions = pd.DataFrame(index=X.index)

for model_file in model_files:
    model_name = os.path.basename(model_file)

    # Skip empty files
    if os.path.getsize(model_file) < 1000:
        print(f"⚠️ Skipping corrupted or empty model file: {model_name}")
        continue

    try:
        model = joblib.load(model_file)
    except Exception as e:
        print(f"❌ Failed to load model {model_name}: {e}")
        continue

    drug_name = model_name.replace(".pkl", "").split("_", 1)[1]
    print(f"🔍 Predicting for: {drug_name}")

    try:
        preds = model.predict(X)
        all_predictions[drug_name] = preds
    except Exception as e:
        print(f"❌ Failed to predict with model {model_name}: {e}")

# 💾 Save predictions
if not all_predictions.empty:
    all_predictions.to_csv(output_path)
    print(f"\n✅ Predictions saved to: {output_path}")
else:
    print("❌ No predictions made — check your model files.")
