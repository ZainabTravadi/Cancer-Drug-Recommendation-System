import os
import joblib
import pandas as pd

# 📁 Paths
features_path = r"C:\Users\DELL\Desktop\Cancer Drug System\data\final\features_X.csv"
model_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\models"
top_n = 5  # Number of top drugs to recommend

# 📥 Load features
X_all = pd.read_csv(features_path, index_col=0)
patient_sample = X_all.iloc[0:1]  # Choose the first sample (customize this as needed)

print(f"🧬 Predicting for sample: {patient_sample.index[0]}\n")

# 🔍 Predict with all valid model files
predictions = []

for filename in os.listdir(model_dir):
    if not filename.endswith(".pkl"):
        continue
    if "_Drug_" not in filename:
        continue  # Skip files like 'XGBoost_model.pkl'

    model_path = os.path.join(model_dir, filename)

    # Skip suspiciously small/corrupt files
    if os.path.getsize(model_path) < 1000:
        print(f"⚠️ Skipping broken or tiny file: {filename}")
        continue

    try:
        model = joblib.load(model_path)
        drug_name = filename.replace(".pkl", "").split("_", 1)[1]  # Get "Drug_1000_IC50"
        pred = model.predict(patient_sample)[0]
        predictions.append((drug_name, pred))
    except Exception as e:
        print(f"⚠️ Could not load/predict with {filename}: {e}")

# ✅ Show results if predictions exist
if predictions:
    pred_df = pd.DataFrame(predictions, columns=["Drug", "Predicted_IC50"])
    pred_df.sort_values(by="Predicted_IC50", inplace=True)

    print(f"💊 Top {top_n} Recommended Drugs:")
    print(pred_df.head(top_n).to_string(index=False))

    # 💾 Save full predictions
    output_csv = os.path.join(model_dir, "drug_recommendations.csv")
    pred_df.to_csv(output_csv, index=False)
    print(f"\n✅ Full prediction list saved to: {output_csv}")
else:
    print("❌ No predictions were generated. Check model files.")
