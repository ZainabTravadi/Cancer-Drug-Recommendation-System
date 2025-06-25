# 07_evaluate.py

import os
import joblib
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

# 📁 Paths
data_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\data\final"
model_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\models"
output_file = os.path.join(model_dir, "model_evaluation_summary.csv")

# 📥 Load Data
X = pd.read_csv(os.path.join(data_dir, "features_X.csv"), index_col=0)
y = pd.read_csv(os.path.join(data_dir, "labels_y.csv"), index_col=0)

# 🔁 Evaluate each model
results = []

for col in y.columns:
    y_col = y[col].dropna()
    X_col = X.loc[y_col.index]

    # Split again like before
    X_train, X_test, y_train, y_test = train_test_split(
        X_col, y_col, test_size=0.2, random_state=42
    )

    for model_type in ["RandomForest", "XGBoost", "Ridge"]:
        model_name = f"{model_type}_{col}.pkl"
        model_path = os.path.join(model_dir, model_name)

        if not os.path.exists(model_path):
            print(f"❌ Model not found: {model_name}")
            continue

        # 🔄 Load model
        model = joblib.load(model_path)

        # 🔍 Evaluate
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)

        results.append({
            "Drug": col,
            "Model": model_type,
            "Test R2": r2,
            "Test MSE": mse
        })

        print(f"📊 {model_type} | {col} | R2: {r2:.4f} | MSE: {mse:.4f}")

# 💾 Save results
results_df = pd.DataFrame(results)
results_df.to_csv(output_file, index=False)

print("\n✅ Evaluation summary saved to:", output_file)
