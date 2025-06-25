# 06_visualize.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error

# 📁 Paths
data_dir = r"C:\Users\DELL\Desktop\Cancer Drug System\data\final"
prediction_file = os.path.join(data_dir, "predictions.csv")
true_label_file = os.path.join(data_dir, "labels_y.csv")
output_dir = os.path.join(data_dir, "visualizations")
os.makedirs(output_dir, exist_ok=True)

# 📥 Load data
y_true = pd.read_csv(true_label_file, index_col=0)
y_pred = pd.read_csv(prediction_file, index_col=0)

# 🎨 Plot settings
sns.set(style="whitegrid", font_scale=1.2)

for drug in y_true.columns:
    if drug not in y_pred.columns:
        print(f"⚠️ Skipping {drug} — no predictions available.")
        continue

    true_vals = y_true[drug].dropna()
    pred_vals = y_pred.loc[true_vals.index, drug]

    # 🧮 Metrics
    r2 = r2_score(true_vals, pred_vals)
    mse = mean_squared_error(true_vals, pred_vals)

    # 📈 Scatter plot
    plt.figure(figsize=(6, 6))
    sns.scatterplot(x=true_vals, y=pred_vals, color="blue", s=50, edgecolor="black", alpha=0.7)
    plt.plot([true_vals.min(), true_vals.max()], [true_vals.min(), true_vals.max()], '--', color='gray')

    plt.title(f"{drug} | R²: {r2:.2f}, MSE: {mse:.2f}")
    plt.xlabel("Actual IC50")
    plt.ylabel("Predicted IC50")
    plt.tight_layout()

    save_path = os.path.join(output_dir, f"{drug}_scatter.png")
    plt.savefig(save_path)
    plt.close()

    print(f"📊 Saved plot for {drug}: {save_path}")

print("\n✅ All visualizations complete!")
