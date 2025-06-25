# 04_model_training.py

import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score

# 📁 Paths
data_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\data\final"
model_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\models"
os.makedirs(model_dir, exist_ok=True)

# 📥 Load data
X = pd.read_csv(os.path.join(data_dir, "features_X.csv"), index_col=0)
y = pd.read_csv(os.path.join(data_dir, "labels_y.csv"), index_col=0)

# 📊 Models to train
models = {
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
    "XGBoost": XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42, verbosity=0),
    "Ridge": Ridge(alpha=1.0)
}

# 📌 Train per drug
for drug in y.columns:
    print(f"\n💊 Training models for: {drug}")
    
    y_drug = y[drug].dropna()
    X_drug = X.loc[y_drug.index]

    if X_drug.empty or y_drug.empty:
        print(f"⚠️ Skipping {drug} due to no data.")
        continue

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X_drug, y_drug, test_size=0.2, random_state=42
    )
    print(f"✅ Train shape: {X_train.shape}, Test shape: {X_test.shape}")

    for name, model in models.items():
        print(f"🚀 Training {name}...")

        model.fit(X_train, y_train)

        # Evaluation
        cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print(f"📊 {name} | CV R²: {cv_scores.mean():.4f} | Test R²: {r2:.4f} | Test MSE: {mse:.4f}")

        # Save model
        model_name = f"{name}_{drug}.pkl"
        model_path = os.path.join(model_dir, model_name)
        joblib.dump(model, model_path)
        print(f"✅ Saved: {model_name}")

print("\n🏁 All models trained and saved.")
