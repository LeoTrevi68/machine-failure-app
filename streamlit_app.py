import streamlit as st
import joblib
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# cargar modelo
model = joblib.load('model.pkl')

# límites operativos (basados en condiciones sin falla)
limits = {
    'Torque [Nm]': (23.6, 54.8),
    'Tool wear [min]': (9.0, 204.0),
    'Air temperature [K]': (297.1, 303.5),
    'Process temperature [K]': (307.7, 312.5),
    'Rotational speed [rpm]': (1339, 1863)
}

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

    # KPI
    st.metric(label="Failure Probability", value=f"{prob:.2%}")

    # interpretación de riesgo
    if prob < 0.2:
        st.success("Low Risk – Operating conditions are within normal range")
    elif prob < 0.5:
        st.warning("Medium Risk – Monitor conditions closely")
    else:
        st.error("High Risk – Immediate attention recommended")

    # -----------------------------
    # SPC: Torque Control Chart
    # -----------------------------
    st.markdown("### Torque Control Chart (SPC)")

    # datos simulados
    torque_data = np.random.normal(loc=40, scale=5, size=50)

    lower, upper = limits['Torque [Nm]']

    # color del punto según condición
    if torque < lower or torque > upper:
        point_color = "red"
    else:
        point_color = "green"

    fig = go.Figure()

    # datos históricos
    fig.add_trace(go.Scatter(
        y=torque_data,
        mode='lines+markers',
        name='Historical Data'
    ))

    # límite superior
    fig.add_trace(go.Scatter(
        y=[upper]*len(torque_data),
        mode='lines',
        name='Upper Limit',
        line=dict(dash='dash')
    ))

    # límite inferior
    fig.add_trace(go.Scatter(
        y=[lower]*len(torque_data),
        mode='lines',
        name='Lower Limit',
        line=dict(dash='dash')
    ))

    # punto actual
    fig.add_trace(go.Scatter(
        y=[torque],
        x=[len(torque_data)],
        mode='markers',
        name='Current Value',
        marker=dict(size=12, color=point_color)
    ))

    fig.update_layout(
        title="Torque SPC Monitoring",
        xaxis_title="Sample",
        yaxis_title="Torque [Nm]"
    )

    st.plotly_chart(fig)

# firma
st.markdown("---")
st.caption("Developed by José Leopoldo Treviño Martínez | Data Analysis Portfolio")
