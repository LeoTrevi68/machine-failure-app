import streamlit as st
import joblib
import pandas as pd

# cargar modelo
model = joblib.load('model.pkl')

st.title("Machine Failure Risk Predictor")

st.write("Enter machine operating conditions:")

# inputs
air_temp = st.number_input("Air temperature [K]", value=300.0)
process_temp = st.number_input("Process temperature [K]", value=310.0)
rpm = st.number_input("Rotational speed [rpm]", value=1500)
torque = st.number_input("Torque [Nm]", value=40.0)
tool_wear = st.number_input("Tool wear [min]", value=100)

# botón
if st.button("Predict"):

    input_data = pd.DataFrame([{
        'Air temperature [K]': air_temp,
        'Process temperature [K]': process_temp,
        'Rotational speed [rpm]': rpm,
        'Torque [Nm]': torque,
        'Tool wear [min]': tool_wear
    }])

    prob = model.predict_proba(input_data)[0][1]

    st.subheader(f"Failure Probability: {prob:.2%}")

    if prob < 0.2:
        st.success("Low Risk")
    elif prob < 0.5:
        st.warning("Medium Risk")
    else:
        st.error("High Risk")