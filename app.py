import streamlit as st
import pandas as pd
import joblib

# Load saved model
model = joblib.load("fraud_detection_model.pkl")

st.title("🚨 Insurance Claim Fraud Prediction App")

st.write("Enter insurance claim details below to predict if it's Fraudulent or Not.")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
policy_type = st.selectbox("Policy Type", ["Comprehensive", "Third-Party"])
claim_amount = st.number_input("Claim Amount", min_value=0, value=5000)
num_claims_history = st.number_input("Number of Previous Claims", min_value=0, value=1)
incident_severity = st.selectbox("Incident Severity", ["Minor", "Major", "Critical"])
hospital_name = st.selectbox("Hospital Name", ["City Hospital", "General Hospital", "St. Marys"])
doctor_fee = st.number_input("Doctor Fee", min_value=0, value=800)
vehicle_age = st.selectbox("Vehicle Age", ["<1 Year", "1-3 Years", "3-5 Years", "5+ Years"])

# Collect inputs into dataframe
input_data = pd.DataFrame({
    "age": [age],
    "gender": [gender],
    "policy_type": [policy_type],
    "claim_amount": [claim_amount],
    "num_claims_history": [num_claims_history],
    "incident_severity": [incident_severity],
    "hospital_name": [hospital_name],
    "doctor_fee": [doctor_fee],
    "vehicle_age": [vehicle_age]
})

# Prediction
if st.button("Predict Fraud"):
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Fraudulent Claim Detected! (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Genuine Claim (Probability of Fraud: {prob:.2f})")
