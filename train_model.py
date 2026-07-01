"""
train_model.py

Trains the Employee Burnout Prediction model
and saves it inside the model folder.
"""

import os
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split

from utils.preprocess import load_dataset, preprocess_data


# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

print("Loading dataset...")

df = load_dataset("dataset/burnout.csv")

print(f"Dataset Shape : {df.shape}")

# ---------------------------------------------------
# Preprocess Dataset
# ---------------------------------------------------

print("Preprocessing dataset...")

X, y, preprocessor = preprocess_data(df)

# ---------------------------------------------------
# Train-Test Split
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

# ---------------------------------------------------
# Build Model
# ---------------------------------------------------

print("Training Random Forest Model...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    max_depth=10,
)

model.fit(X_train, y_train)

# ---------------------------------------------------
# Evaluation
# ---------------------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Evaluation")
print("-" * 40)
print(f"Accuracy : {accuracy:.4f}")

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("Confusion Matrix")
print(confusion_matrix(y_test, predictions))

# ---------------------------------------------------
# Save Model
# ---------------------------------------------------

os.makedirs("model", exist_ok=True)

with open("model/burnout_model.pkl", "wb") as file:
    pickle.dump(model, file)

with open("model/preprocessor.pkl", "wb") as file:
    pickle.dump(preprocessor, file)

print("\nModel saved successfully!")

print("Saved Files:")
print("   model/burnout_model.pkl")
print("   model/preprocessor.pkl")

print("\nTraining Complete.")
