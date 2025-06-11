# 🧠 AI Personality Predictor

Welcome to the **AI Personality Predictor**, a sleek and intelligent web app powered by a trained Neural Network and built with Streamlit. Just answer a few quick questions about your social habits, and let the AI determine whether you're more of an **introvert** 🦉 or an **extrovert** 🦋 — all in real-time.

---

## 🌟 Features

- 🔍 **7-input Personality Prediction** based on behavioral traits  
- 🧠 Powered by a trained **Neural Network model**  
- 📊 Uses **StandardScaler** for robust input preprocessing  
- 🖤 Sexy dark-themed UI with emojis, sliders, and smooth UX  
- 🎯 Outputs confidence score + prediction label  
- ✅ Easily deployable with **Streamlit**

---

## 🚀  Demo
<img width="1470" alt="Screenshot 2025-06-12 at 12 58 12 AM" src="https://github.com/user-attachments/assets/206394fc-5f3e-434f-9fa2-03ef0ee92421" />

><img width="1470" alt="Screenshot 2025-06-12 at 12 58 17 AM" src="https://github.com/user-attachments/assets/c0e93756-6a4e-485b-92a8-fcfed4984508" />


---

## 📦 Installation

### 1. Clone the repo:
bash
git clone https://github.com/your-username/ai-personality-predictor.git
cd ai-personality-predictor

### 2. Install dependencies:
pip install -r requirements.txt
Or manually:
pip install streamlit tensorflow scikit-learn joblib
### 3. Add your model files:
model.h5 – Trained Keras neural network
scaler.pkl – Fitted StandardScaler object
## ▶️ Usage
Run the app locally:
streamlit run app.py
Then open http://localhost:8501 in your browser.
## 📊 Input Format
The model uses the following 7 user inputs:
Feature	Type	Description
Time spent alone	Numeric	Hours/day
Stage fear	Yes/No	Fear of public speaking
Social event attendance	Numeric	Times/month
Going outside	Numeric	Days/week outdoors
Drained after socializing	Yes/No	Fatigue after interactions
Friends circle size	Numeric	Count of known friends
Social media post frequency	Numeric	Posts per week
## 📁 Project Structure
.
├── app.py               # Streamlit app
├── model.h5             # Trained neural network
├── scaler.pkl           # Saved StandardScaler
├── README.md            # This file
├── requirements.txt     # All dependencies
🧠 Model Info
Built with: TensorFlow / Keras
Input shape: (1, 7)
Output: Binary classification (Extrovert / Introvert)
## 🙌 Credits
Created with ❤️ using:
Streamlit
TensorFlow
Scikit-learn
