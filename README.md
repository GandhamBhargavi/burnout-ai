# 🔥 BurnOutAI - Employee Burnout Prediction System

## 📌 Overview

BurnOutAI is an AI-powered Employee Burnout Prediction System that helps organizations identify employees who may be at risk of burnout before it affects their productivity and well-being.

Using Machine Learning, the system predicts burnout risk based on employee work-related factors and provides personalized wellness recommendations along with explainable AI insights.

---

## 🚀 Features

- AI-based Burnout Prediction
- Employee Burnout Risk Score
- Low / Medium / High Risk Classification
- Explainable AI (Prediction Reasons)
- Personalized Wellness Recommendations
- Interactive Streamlit Dashboard
- Excel Report Generation
- HR-Friendly Interface

---

## 🧠 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 📂 Project Structure

```
BurnOutAI/

│── app.py
│── train_model.py
│── predict.py
│── requirements.txt
│── README.md

├── dataset/
│      burnout.csv

├── model/
│      burnout_model.pkl

├── utils/
│      preprocess.py
│      recommend.py
│      explain.py

├── output/
│      predictions.xlsx

└── screenshots/
```

---

## 📊 Dataset

Dataset contains employee-related information such as:

- Age
- Gender
- Company Type
- Work From Home Availability
- Designation
- Resource Allocation
- Mental Fatigue Score
- Working Hours
- Leave Days
- Job Satisfaction
- Sleep Hours

Target:

- Burnout Risk

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project:

```bash
cd BurnOutAI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
python train_model.py
```

This generates:

```
model/
    burnout_model.pkl
    preprocessor.pkl
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📈 Workflow

```
Employee Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Random Forest Model
        │
        ▼
Burnout Prediction
        │
        ▼
Explainable AI
        │
        ▼
Recommendation Engine
        │
        ▼
Dashboard
```

---

## 📷 Screenshots

Store application screenshots inside:

```
screenshots/
```

Example:

- Dashboard
- Prediction Result
- Recommendation Panel
- Charts

---

## 💡 Future Enhancements

- Deep Learning Models
- XGBoost Integration
- Real-time Employee Monitoring
- HR Analytics Dashboard
- Email Notifications
- PDF Report Generation
- Cloud Deployment
- Employee Chatbot

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- SHAP
- OpenPyXL

---

## 👩‍💻 Author

Bhargavi G

MCA Student

Artificial Intelligence & Python Enthusiast

---

## 📄 License

This project is developed for educational and hackathon purposes.
