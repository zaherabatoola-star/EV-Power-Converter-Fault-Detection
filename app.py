## How to run
  streamlit run app.py
## code
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('ev_fault_detection_model.pkl')

st.title(" EV Power Converter Optimization Predictor")

st.sidebar.header("Input Parameters")

V_in = st.sidebar.number_input("Input Voltage (V)", 0.0, 1000.0, 200.0)
V_out = st.sidebar.number_input("Output Voltage (V)", 0.0, 1000.0, 150.0)
I_out = st.sidebar.number_input("Output Current (A)", 0.0, 500.0, 50.0)
f_sw = st.sidebar.number_input("Switching Frequency (Hz)", 0.0, 1e6, 50000.0)
R_load = st.sidebar.number_input("Load Resistance (Ω)", 0.1, 1000.0, 5.0)
T_ambient = st.sidebar.number_input("Ambient Temperature (°C)", -20.0, 80.0, 25.0)
P_loss = st.sidebar.number_input("Power Loss (W)", 0.0, 100.0, 10.0)
T_converter = st.sidebar.number_input("Converter Temp (°C)", 0.0, 150.0, 50.0)
efficiency = st.sidebar.number_input("Efficiency (%)", 0.0, 100.0, 90.0)

data = pd.DataFrame({
    'V_in (V)': [V_in],
    'V_out (V)': [V_out],
    'I_out (A)': [I_out],
    'f_sw (Hz)': [f_sw],
    'R_load (Ω)': [R_load],
    'T_ambient (°C)': [T_ambient],
    'P_loss (W)': [P_loss],
    'T_converter (°C)': [T_converter],
    'Efficiency (η%)': [efficiency]
})

if st.button("Predict Optimization Result"):
    prediction = model.predict(data)
    if prediction[0] == 1:
        st.success("Optimization Successful!")
    else:
        st.error(" Optimization Failed.")
