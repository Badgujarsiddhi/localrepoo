import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Crop Recommendation System", layout="centered")

# Title
st.title("🌾 Crop Recommendation System")
st.write("Enter soil and climate details to get the best crop recommendation.")

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# User Inputs
N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=50)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=50)
K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=50)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0)

# Prediction
if st.button("🌱 Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)

    st.success(f"✅ Recommended Crop: **{prediction[0]}**")

    # Graph
    st.subheader("Soil Nutrient Levels")
    fig, ax = plt.subplots()
    ax.bar(["Nitrogen", "Phosphorus", "Potassium"], [N, P, K])
    ax.set_ylabel("Value")
    ax.set_title("NPK Levels")
    st.pyplot(fig)
