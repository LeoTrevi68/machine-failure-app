import streamlit as st
import joblib
import pandas as pd

# cargar modelo
model = joblib.load('model.pkl')

# título e introducción
st.title("Machine Failure Risk Predictor")

st.markdown("""
This tool estimates the probability of machine failure based on key operating conditions.

Adjust the input parameters to evaluate risk in real time.
""")

# inputs
st.write("Enter machine operating conditions:")

air_temp = st.number_input("Air temperature [K]", value=300.0)
process_temp = st.number_input("Process temperature [K]", value=310.0)
rpm = st.number_input("Rotational speed [rpm]", value=1500)
torque = st.number_input("Torque [Nm]", value=40.0)
tool_wear = st.number_input("Tool wear [min]", value=100)

# botón de predicción
if st.button("Predict"):

    input_data = pd.DataFrame([{
        'Air temperature [K]': air_temp,
        'Process temperature [K]': process_temp,
        'Rotational speed [rpm]': rpm,
        'Torque [Nm]': torque,
        'Tool wear [min]': tool_wear
    }])

    prob = model.predict_proba(input_data)[0][1]

    # resultado tipo KPI
    st.metric(label="Failure Probability", value=f"{prob:.2%}")

    # interpretación de riesgo
    if prob < 0.2:
        st.success("Low Risk – Operating conditions are within normal range")
    elif prob < 0.5:
        st.warning("Medium Risk – Monitor conditions closely")
    else:
        st.error("High Risk – Immediate attention recommended")

# firma
st.markdown("---")
st.caption("Developed by José Leopoldo Treviño Martínez | Data Analysis Portfolio")
