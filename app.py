import streamlit as st
import pandas as pd
import pickle

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------
with open("model/burnout_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("model/preprocessor.pkl", "rb") as file:
    preprocessor = pickle.load(file)

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="BurnOutAI",
    page_icon="🔥",
    layout="wide"
)

st.title("🔥 BurnOutAI")
st.subheader("AI Powered Employee Burnout Prediction System")

st.markdown("---")

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.header("Employee Details")

employee_id = st.sidebar.text_input("Employee ID", "EMP101")

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

company_type = st.sidebar.selectbox(
    "Company Type",
    ["Service", "Product"]
)

wfh = st.sidebar.selectbox(
    "Work From Home",
    ["Yes", "No"]
)

designation = st.sidebar.slider(
    "Designation Level",
    0,
    5,
    2
)

resource = st.sidebar.slider(
    "Resource Allocation",
    1.0,
    10.0,
    5.0
)

mental_fatigue = st.sidebar.slider(
    "Mental Fatigue Score",
    0.0,
    10.0,
    5.0
)

age = st.sidebar.slider(
    "Age",
    20,
    60,
    30
)

working_hours = st.sidebar.slider(
    "Working Hours / Day",
    4,
    16,
    8
)

leave_days = st.sidebar.slider(
    "Leave Days This Month",
    0,
    10,
    2
)

job_satisfaction = st.sidebar.slider(
    "Job Satisfaction",
    1,
    5,
    3
)

sleep_hours = st.sidebar.slider(
    "Sleep Hours",
    3,
    10,
    7
)

predict = st.sidebar.button("Predict Burnout")

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------
if predict:

    input_df = pd.DataFrame({
        "Gender":[gender],
        "Company Type":[company_type],
        "WFH Setup Available":[wfh],
        "Designation":[designation],
        "Resource Allocation":[resource],
        "Mental Fatigue Score":[mental_fatigue],
        "Age":[age],
        "Working Hours":[working_hours],
        "Leave Days":[leave_days],
        "Job Satisfaction":[job_satisfaction],
        "Sleep Hours":[sleep_hours]
    })

    processed = preprocessor.transform(input_df)

    prediction = model.predict(processed)[0]

    probability = model.predict_proba(processed)[0][1] * 100

    st.markdown("## Prediction Result")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Employee",
            employee_id
        )

        st.metric(
            "Burnout Risk",
            f"{probability:.2f}%"
        )

    with col2:

        if probability < 40:
            st.success("🟢 LOW RISK")

        elif probability < 70:
            st.warning("🟡 MEDIUM RISK")

        else:
            st.error("🔴 HIGH RISK")

    st.markdown("---")

    st.subheader("Why this prediction?")

    reasons = []

    if working_hours > 10:
        reasons.append("Working hours are very high.")

    if mental_fatigue > 7:
        reasons.append("Mental fatigue score is high.")

    if leave_days < 2:
        reasons.append("Employee has taken very few leave days.")

    if job_satisfaction <= 2:
        reasons.append("Job satisfaction is low.")

    if sleep_hours < 6:
        reasons.append("Insufficient sleep.")

    if resource > 7:
        reasons.append("Heavy resource allocation.")

    if len(reasons) == 0:
        reasons.append("Employee work-life balance looks healthy.")

    for r in reasons:
        st.write("✔", r)

    st.markdown("---")

    st.subheader("AI Wellness Recommendations")

    recommendations = []

    if working_hours > 10:
        recommendations.append("Reduce working hours.")

    if mental_fatigue > 7:
        recommendations.append("Schedule wellness sessions.")

    if leave_days < 2:
        recommendations.append("Take planned leave.")

    if sleep_hours < 6:
        recommendations.append("Improve sleep routine.")

    if job_satisfaction <= 2:
        recommendations.append("Discuss concerns with manager.")

    if resource > 7:
        recommendations.append("Balance workload.")

    if probability < 40:
        recommendations.append("Maintain current healthy routine.")

    for rec in recommendations:
        st.info(rec)

    st.markdown("---")

    st.subheader("Employee Summary")

    summary = pd.DataFrame({
        "Parameter":[
            "Working Hours",
            "Mental Fatigue",
            "Leave Days",
            "Job Satisfaction",
            "Sleep Hours",
            "Burnout Risk"
        ],
        "Value":[
            working_hours,
            mental_fatigue,
            leave_days,
            job_satisfaction,
            sleep_hours,
            f"{probability:.2f}%"
        ]
    })

    st.table(summary)

else:

    st.info("Enter employee information from the sidebar and click **Predict Burnout**.")
