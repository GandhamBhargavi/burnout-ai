"""
explain.py

Generates human-readable explanations for
Employee Burnout Prediction.
"""


def generate_explanation(employee_data, risk_level):
    """
    Generates reasons for burnout prediction.

    Parameters
    ----------
    employee_data : dict
        Employee details.

    risk_level : str
        Low / Medium / High

    Returns
    -------
    list
        List of explanation strings.
    """

    reasons = []

    working_hours = employee_data.get("Working Hours", 8)
    mental_fatigue = employee_data.get("Mental Fatigue Score", 5)
    leave_days = employee_data.get("Leave Days", 2)
    sleep_hours = employee_data.get("Sleep Hours", 7)
    job_satisfaction = employee_data.get("Job Satisfaction", 3)
    resource = employee_data.get("Resource Allocation", 5)
    designation = employee_data.get("Designation", 1)
    age = employee_data.get("Age", 30)

    # ---------------------------------------
    # Working Hours
    # ---------------------------------------

    if working_hours > 10:
        reasons.append(
            "Employee is working more than 10 hours per day."
        )

    elif working_hours >= 9:
        reasons.append(
            "Working hours are slightly above the recommended limit."
        )

    # ---------------------------------------
    # Mental Fatigue
    # ---------------------------------------

    if mental_fatigue >= 8:
        reasons.append(
            "Mental fatigue score is very high."
        )

    elif mental_fatigue >= 6:
        reasons.append(
            "Mental fatigue is moderately high."
        )

    # ---------------------------------------
    # Leave
    # ---------------------------------------

    if leave_days <= 1:
        reasons.append(
            "Employee has taken very few leave days recently."
        )

    # ---------------------------------------
    # Sleep
    # ---------------------------------------

    if sleep_hours < 6:
        reasons.append(
            "Insufficient sleep may be increasing stress."
        )

    # ---------------------------------------
    # Job Satisfaction
    # ---------------------------------------

    if job_satisfaction <= 2:
        reasons.append(
            "Low job satisfaction contributes to burnout risk."
        )

    # ---------------------------------------
    # Workload
    # ---------------------------------------

    if resource >= 8:
        reasons.append(
            "High resource allocation indicates a heavy workload."
        )

    # ---------------------------------------
    # Senior Role
    # ---------------------------------------

    if designation >= 4:
        reasons.append(
            "Higher designation may involve greater responsibilities."
        )

    # ---------------------------------------
    # Age
    # ---------------------------------------

    if age < 25:
        reasons.append(
            "Early-career employees may require additional mentoring and support."
        )

    # ---------------------------------------
    # Risk Summary
    # ---------------------------------------

    if risk_level == "High":
        reasons.append(
            "Multiple burnout indicators suggest a high burnout risk."
        )

    elif risk_level == "Medium":
        reasons.append(
            "Several moderate burnout indicators were detected."
        )

    else:
        reasons.append(
            "Current work patterns indicate a relatively healthy balance."
        )

    # Remove duplicate explanations
    reasons = list(dict.fromkeys(reasons))

    return reasons


# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------

if __name__ == "__main__":

    employee = {
        "Age": 24,
        "Designation": 2,
        "Working Hours": 11,
        "Mental Fatigue Score": 8.7,
        "Leave Days": 1,
        "Sleep Hours": 5,
        "Job Satisfaction": 2,
        "Resource Allocation": 8
    }

    explanations = generate_explanation(
        employee,
        "High"
    )

    print("\nPrediction Explanation\n")

    for i, reason in enumerate(explanations, start=1):
        print(f"{i}. {reason}")
