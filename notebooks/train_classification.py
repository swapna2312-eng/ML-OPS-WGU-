# Databricks notebook: Training Job
# %pip install mlflow scikit-learn

import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
X, y = load_iris(return_X_y=True)

# Split
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
n_estimators = 50
with mlflow.start_run():
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(Xtr, ytr)
    preds = model.predict(Xte)
    acc = accuracy_score(yte, preds)

    # Log metrics and parameters
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_metric("accuracy", acc)

    # Register model in MLflow
    mlflow.sklearn.log_model(model, "model", registered_model_name="iris_rf_model")

print("✅ Training complete. Accuracy:", acc)

