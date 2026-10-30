import streamlit as st
import pandas as pd
import pickle

# Load model (agar model file nahi hai to ye simple UI chalega)
st.title("Medical Insurance Cost Prediction")

st.write("Enter patient details to predict insurance cost")

age = st.number_input("Age", 18, 100, 25)
bmi = st.number_input("BMI", 10.0, 60.0, 28.0)
children = st.number_input("Children", 0, 5, 1)
smoker = st.selectbox("Smoker", ["yes", "no"])
sex = st.selectbox("Gender", ["male", "female"])

if st.button("Predict Cost"):
    # Simple logic for demo - tumhara trained model yahan ayega
    base_cost = 3000 + (age * 50) + (bmi * 100)
    if smoker == "yes":
        base_cost += 15000
    base_cost += children * 500
    st.success(f"Predicted Insurance Cost: ${base_cost:.2f}")
