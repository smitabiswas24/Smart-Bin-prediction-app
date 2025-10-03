import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open('rf_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.set_page_config(page_title="Smart Bin Overflow Prediction", layout="centered")

st.title("🧠 Smart Bin Overflow Predictor")
st.markdown("Simulate bin conditions and predict whether overflow is likely.")

# User inputs
bin_level = st.slider("🗑 Bin Fill Level (%)", 0, 100, 50)
temperature = st.slider("🌡 Temperature (°C)", 10, 45, 25)
humidity = st.slider("💧 Humidity (%)", 10, 100, 60)
waste_type = st.selectbox("♻ Waste Type", ['Organic', 'Plastic', 'Paper', 'Mixed'])

# Encode categorical input
waste_map = {'Organic': 0, 'Plastic': 1, 'Paper': 2, 'Mixed': 3}
waste_encoded = waste_map[waste_type]

# Prepare input
input_data = np.array([[bin_level, temperature, humidity, waste_encoded]])
scaled_input = scaler.transform(input_data)

# Predict
prediction = model.predict(scaled_input)

# Display result
if prediction[0] == 1:
    st.error("⚠ Overflow likely – Schedule collection!")
else:
    st.success("✅ Bin is within safe limits.")