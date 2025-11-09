import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load(r"C:\Users\91990\Projects\Weather_Prediction_App\models\weather_temp_model.pkl")

# Streamlit UI
st.set_page_config(page_title="🌤️ weather Predictor", layout="centered")
st.title("🌤️ AI-Powered Weather Temperature Predictor")
st.write("Enter weather details below 👇")

humidity = st.number_input("Humidity", min_value=0.0, max_value=1.0, value=0.5)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, value=10.0)
pressure = st.number_input("Pressure (millibars)", min_value=900.0, max_value=1100.0, value=1010.0)

if st.button("Predict Temperature"):
    features = np.array([[humidity, wind_speed, pressure]])
    prediction = model.predict(features)
    st.success(f"🌡️ Predicted Temperature: {prediction[0]:.2f} °C")