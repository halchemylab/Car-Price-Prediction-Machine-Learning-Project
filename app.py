import streamlit as st
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Customer Car Price Estimator App")

st.divider()

st.write("This app is for getting a price estimation for the customer so a car with the price range given can be advised to the customer")

age = st.number_input("Age", min_value = 0, max_value =100, value = 40, step = 1)
salary = st.number_input("Annual Salary", min_value=1000, max_value = 100000, value = 50000, step = 1000)
networth = st.number_input("Enter the net worth", min_value=1000, max_value = 100000, value = 20000, step = 1000)

X = [age, salary, networth]

calculate_button = st.button("Predict Price")

st.divider()

if calculate_button:
    X_scaled = scaler.transform([X])
    X_array = np.array(X_scaled)

    prediction = model.predict(X_array)

    st.subheader(f"The estimated price is ${round(float(prediction[0]), 2)}")
    st.write("Advice cars in the price range given can be advised to the customer")

else:
    st.write("Please click on the button to predict the price")
