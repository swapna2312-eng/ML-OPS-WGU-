model_uri = "models:/iris_rf_model/1"
# Databricks notebook: Inference Job
# %pip install mlflow pandas scikit-learn

import mlflow
import pandas as pd
from sklearn.datasets import load_iris

# Load the latest Production model from MLflow
model_uri = "models:/iris_rf_model/1"

print("Loading model from:", model_uri)
model = mlflow.pyfunc.load_model(model_uri)

# Use sample data for prediction
X, y = load_iris(return_X_y=True, as_frame=True)
preds = model.predict(X)

# Save results to DBFS
df = pd.DataFrame({"prediction": preds})
import os
os.makedirs("outputs", exist_ok=True)
out_path = "outputs/preds.csv"

df.to_csv(out_path, index=False)

print("✅ Inference complete. Saved predictions to", out_path)

