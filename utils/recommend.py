"""
recommend.py

Generates personalized wellness recommendations
based on employee information and burnout risk.
"""


def generate_recommendations(employee_data, risk_level):
    """
    Generate wellness recommendations.

    Parameters
    ----------
    employee_data : dict
        Employee details.

    risk_level : str
        Low / Medium / High

    Returns
    -------
    list
        List of recommendations.
    """

    recommendations = []

    working_hours = employee_data.get("Working Hours", 8)
    mental_fatigue = employee_data.get("Mental Fatigue Score", 5)
    leave_days = employee_data.get("Leave Days", 2)
    sleep_hours = employee_data.get("Sleep Hours", 7)
    job_satisfaction = employee_data.get("Job Satisfaction", 3)
    resource = employee_data.get("Resource Allocation", 5)

    # ------------------------------------------
    # Workload
    # ------------------------------------------

    if working_hours > 10:
        recommendations.append(
            "Reduce daily working hours and avoid excessive overtime."
        )

    if resource > 7:
        recommendations.append(
            "Rebalance workload or redistribute project assignments."
        )

    # ------------------------------------------
    # Mental Health
    # ------------------------------------------

    if mental_fatigue >= 7:
        recommendations.append(
            "Schedule wellness sessions or stress management activities."
        )

    # ------------------------------------------
    # Leave
    # ------------------------------------------

    if leave_days < 2:
        recommendations.append(
            "Plan regular leave to improve work-life balance."
        )

    # ------------------------------------------
    # Sleep
    # ------------------------------------------

    if sleep_hours < 6:
        recommendations.append(
            "Aim for at least 7–8 hours of sleep every night."
        )

    # ------------------------------------------
    # Job Satisfaction
    # ------------------------------------------

    if job_satisfaction <= 2:
        recommendations.append(
            "Discuss concerns with your manager and create a development plan."
        )

    # ------------------------------------------
    # Risk-Based Suggestions
    # ------------------------------------------

    if risk_level == "High":
        recommendations.extend([
            "Schedule an HR wellness meeting immediately.",
            "Reduce workload for the next few weeks.",
            "Encourage counseling or Employee Assistance Program (EAP) support.",
            "Monitor burnout indicators weekly."
        ])

    elif risk_level == "Medium":
        recommendations.extend([
            "Take short breaks during work.",
            "Review workload with your team lead.",
            "Participate in wellness initiatives."
        ])

    else:  # Low
        recommendations.append(
            "Maintain your current healthy work-life balance."
        )

    # ------------------------------------------
    # Remove duplicates while preserving order
    # ------------------------------------------

    recommendations = list(dict.fromkeys(recommendations))

    return recommendations


# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------

if __name__ == "__main__":

    employee = {
        "Working Hours": 11,
        "Mental Fatigue Score": 8.5,
        "Leave Days": 1,
        "Sleep Hours": 5,
        "Job Satisfaction": 2,
        "Resource Allocation": 8
    }

    result = generate_recommendations(employee, "High")

    print("\nWellness Recommendations\n")

    for i, recommendation in enumerate(result, start=1):
        print(f"{i}. {recommendation}")
