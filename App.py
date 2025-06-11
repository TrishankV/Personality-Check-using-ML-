import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Load model and scaler
scaler = joblib.load('scaler.pkl')
model = load_model('neural_network_model.h5')

# App title and styling
st.set_page_config(page_title="Personality Predictor", page_icon="🧠", layout="centered")
st.markdown("""
    <style>
    .stApp {
        background-color: #0f0f0f;
        color: #f0f0f0;
        font-family: 'Courier New', monospace;
    }
    h1, h2, h3 {
        color: #00ffd0;
    }
    .stButton>button {
        background-color: #00ffd0;
        color: black;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🧠 AI Personality Predictor")
st.markdown("Enter the following details and let the neural network guess your personality!")

# Input fields
time_spent_alone = st.slider("🕰️ Time spent alone (hours/day)", 0, 24, 2)
stage_fear = st.selectbox("🎤 Do you have stage fear?", ['Yes', 'No'])
social_event_attendance = st.slider("🎉 Social event attendance (times/month)", 0, 30, 5)
going_outside = st.slider("🌳 Frequency of going outside (days/week)", 0, 7, 4)
drained_after_socializing = st.selectbox("💤 Do you feel drained after socializing?", ['Yes', 'No'])
friends_circle_size = st.slider("👥 Friends circle size", 0, 100, 10)
post_frequency = st.slider("📱 Social media post frequency (per week)", 0, 50, 3)

def yesandno(string):
    return 1 if string.lower().startswith('y') else 0

# Predict button
if st.button("🔥 Predict Personality"):
    # Prepare input
    numeric = [time_spent_alone, social_event_attendance, going_outside, friends_circle_size, post_frequency]
    yn = [yesandno(stage_fear), yesandno(drained_after_socializing)]

    scaled = scaler.transform([numeric]).flatten().tolist()

    final_input = [
        scaled[0],      # Time_spent_alone
        yn[0],          # Stage_fear
        scaled[1],      # Social_event_attendance
        scaled[2],      # Going_outside
        yn[1],          # Drained_after_socializing
        scaled[3],      # Friends_circle_size
        scaled[4]       # Post_frequency
    ]

    input_array = np.array(final_input).reshape(1, -1)
    prediction = model.predict(input_array)

    # Interpret result
    result = "🦋 Extrovert" if prediction[0][0] < 0.5 else "🦉 Introvert"
    confidence = prediction[0][0] if prediction[0][0] > 0.5 else 1 - prediction[0][0]

    # Show result
    st.success(f"### 🎯 Prediction: {result}")
    st.markdown(f"**Confidence:** `{confidence:.2%}`")

    st.balloons()
