"""
preprocess.py

Handles:
1. Loading dataset
2. Data cleaning
3. Feature preprocessing
4. Returning processed features for model training
"""

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

def load_dataset(path):
    """
    Loads the burnout dataset.

    Parameters
    ----------
    path : str

    Returns
    -------
    pandas.DataFrame
    """
    df = pd.read_csv(path)
    return df


# ---------------------------------------------------
# Preprocess Dataset
# ---------------------------------------------------

def preprocess_data(df):
    """
    Cleans and preprocesses the dataset.

    Returns
    -------
    X_processed
    y
    preprocessor
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # -------------------------------
    # Target Variable
    # -------------------------------

    target_column = "Burnout Risk"

    if target_column not in df.columns:
        raise ValueError(
            f"Dataset must contain '{target_column}' column."
        )

    y = df[target_column]

    X = df.drop(columns=[target_column])

    # -------------------------------
    # Feature Types
    # -------------------------------

    categorical_features = [
        "Gender",
        "Company Type",
        "WFH Setup Available"
    ]

    numerical_features = [
        "Designation",
        "Resource Allocation",
        "Mental Fatigue Score",
        "Age",
        "Working Hours",
        "Leave Days",
        "Job Satisfaction",
        "Sleep Hours"
    ]

    # -------------------------------
    # Numeric Pipeline
    # -------------------------------

    numeric_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            ),
            (
                "scaler",
                StandardScaler()
            )
        ]
    )

    # -------------------------------
    # Categorical Pipeline
    # -------------------------------

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent")
            ),
            (
                "encoder",
                OneHotEncoder(handle_unknown="ignore")
            )
        ]
    )

    # -------------------------------
    # Combined Preprocessor
    # -------------------------------

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                numeric_pipeline,
                numerical_features
            ),
            (
                "cat",
                categorical_pipeline,
                categorical_features
            )
        ]
    )

    # Fit and transform
    X_processed = preprocessor.fit_transform(X)

    return X_processed, y, preprocessor
