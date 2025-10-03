import streamlit as st
import pandas as pd
import joblib
model = joblib.load('heart_disease_model.pkl') 

st.title("❤️ Heart Disease Prediction App")
st.markdown("Enter patient details to predict the risk of heart disease:")

age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["typical angina", "atypical angina", "non-anginal", "asymptomatic"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
rest_ecg = st.selectbox("Resting ECG", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
exercise_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.number_input("ST Depression Induced by Exercise (Oldpeak)", min_value=0.0, max_value=10.0, value=1.0)
st_slope = st.selectbox("Slope of ST Segment", ["Upsloping", "Flat", "Downsloping"])

input_data = pd.DataFrame({
    'Age': [age],
    'Sex': [0 if sex=="Male" else 1],
    'ChestPainType': [0 if cp=="typical angina" else 1 if cp=="atypical angina" else 2 if cp=="non-anginal" else 3],
    'RestingBP': [resting_bp],
    'Cholesterol': [cholesterol],
    'FastingBS': [1 if fbs=="Yes" else 0],
    'RestingECG': [0 if rest_ecg=="Normal" else 1 if rest_ecg=="ST-T wave abnormality" else 2],
    'MaxHR': [max_hr],
    'ExerciseAngina': [1 if exercise_angina=="Yes" else 0],
    'Oldpeak': [oldpeak],
    'ST_Slope': [0 if st_slope=="Upsloping" else 1 if st_slope=="Flat" else 2]
})

if st.button("Predict"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]  # probability of heart disease
    if prediction[0] == 1:
        st.error(f"High risk of Heart Disease! (Probability: {probability:.2f})")
    else:
        st.success(f"Low risk of Heart Disease. (Probability: {probability:.2f})")
