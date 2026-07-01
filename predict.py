"""
predict.py

Loads the trained Employee Burnout Prediction model
and predicts burnout risk for new employee data.
"""

import pickle
import pandas as pd


class BurnoutPredictor:
    """
    Handles loading the trained model and making predictions.
    """

    def __init__(
        self,
        model_path="model/burnout_model.pkl",
        preprocessor_path="model/preprocessor.pkl",
    ):

        with open(model_path, "rb") as file:
            self.model = pickle.load(file)

        with open(preprocessor_path, "rb") as file:
            self.preprocessor = pickle.load(file)

    # ---------------------------------------------------
    # Predict
    # ---------------------------------------------------

    def predict(self, employee_data):
        """
        Parameters
        ----------
        employee_data : dict

        Returns
        -------
        prediction
        probability
        risk_level
        """

        df = pd.DataFrame([employee_data])

        processed = self.preprocessor.transform(df)

        prediction = self.model.predict(processed)[0]

        if hasattr(self.model, "predict_proba"):
            probability = self.model.predict_proba(processed)[0][1] * 100
        else:
            probability = 0

        if probability < 40:
            risk = "Low"

        elif probability < 70:
            risk = "Medium"

        else:
            risk = "High"

        return {
            "prediction": int(prediction),
            "burnout_probability": round(probability, 2),
            "risk_level": risk,
        }


# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------

if __name__ == "__main__":

    sample_employee = {

        "Gender": "Female",

        "Company Type": "Service",

        "WFH Setup Available": "Yes",

        "Designation": 2,

        "Resource Allocation": 6,

        "Mental Fatigue Score": 7.5,

        "Age": 28,

        "Working Hours": 10,

        "Leave Days": 1,

        "Job Satisfaction": 2,

        "Sleep Hours": 5

    }

    predictor = BurnoutPredictor()

    result = predictor.predict(sample_employee)

    print("\nPrediction Result")
    print("------------------------")

    print(f"Prediction          : {result['prediction']}")
    print(f"Burnout Probability : {result['burnout_probability']}%")
    print(f"Risk Level          : {result['risk_level']}")
