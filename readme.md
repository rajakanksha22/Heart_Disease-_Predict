Heart Disease Prediction App
This project provides a simple, interactive web application built with Streamlit to predict the risk of heart disease in patients based on various clinical parameters. The prediction is powered by a pre-trained Machine Learning model.

The primary goal of this application is to offer a user-friendly interface for medical professionals or students to input patient data and instantly receive a prediction on whether the patient has a low or high risk of heart disease.

Technology Stack
Frontend/Web Framework: Streamlit

Machine Learning Library: Scikit-learn (or equivalent, saved via joblib)

Data Handling: Pandas

Model Persistence: joblib

📂 Project Files
File Name

Description

app.py

The main Streamlit application script containing the UI and prediction logic.

code.py

(Assumed) Script used for data cleaning, model training, and saving the .pkl file.

heart_disease_model.pkl

The pre-trained Machine Learning model file (e.g., Logistic Regression, Random Forest) saved using joblib.

heart_disease_prediction.csv

The raw or pre-processed dataset used to train the model.

requirements.txt

Lists all necessary Python packages and their versions required to run the application.

▶How to Run the Application
Prerequisites
You need to have Python installed on your system.

Clone the Repository:

git clone [https://github.com/rajakanksha22/Heart_Disease-\_Predict.git](https://github.com/rajakanksha22/Heart_Disease-_Predict.git)
cd Heart_Disease-\_Predict

Install Dependencies:
Use the provided requirements.txt file to install all necessary Python libraries.

pip install -r requirements.txt

Run the Streamlit App:
Execute the main application file using the Streamlit CLI.

streamlit run app.py

Access the App:
The application will automatically open in your default web browser (usually at http://localhost:8501).

Model Details
The application uses a classification model trained on a heart disease dataset (e.g., UCI Heart Disease Dataset). The model expects input features such as:

Age

Sex

Chest Pain Type

Resting Blood Pressure

Cholesterol

...and other relevant clinical factors.

The output is a binary prediction (0: Low Risk, 1: High Risk) along with the prediction probability.
