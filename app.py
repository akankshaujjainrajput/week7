import streamlit as st
import joblib
import numpy as np

# Set page layout
st.set_page_config(page_title="Introvert Personality Predictor", layout="centered")

# --- Sidebar: Model Selection ---
st.sidebar.title("🔍 Choose Model")
model_choice = st.sidebar.radio("Select the model you want to use:", [
    "Logistic Regression", "Random Forest", "SVC", "KNN", "Decision Tree"
])

# Map model names to file paths (ensure these files are saved)
model_files = {
    "Logistic Regression": "logistic_regression.pkl",
    "Random Forest": "random_forest.pkl",
    "SVC": "svc.pkl",
    "KNN": "knn.pkl",
    "Decision Tree": "decision_tree.pkl"
}

# Load selected model
model = joblib.load(model_files[model_choice])

st.title("🧠 Predict if Someone is an Introvert")

# --- Input Feature Interface ---
# Define your actual 7 features
feature_config = {
    "Time_spent_Alone": {"min": 0, "max": 24, "step": 1, "help": "Hours spent alone daily"},
    "Social_event_attendance": {"min": 0, "max": 10, "step": 1, "help": "Events attended weekly"},
    "Going_outside": {"min": 0, "max": 10, "step": 1, "help": "Times going outside weekly"},
    "Friends_circle_size": {"min": 0, "max": 50, "step": 1, "help": "Number of close friends"},
    "Post_frequency": {"min": 0, "max": 50, "step": 1, "help": "Posts per week"},
    "Stage_fear_Yes": {"type": "radio", "options": ["No", "Yes"]},
    "Drained_after_socializing": {"type": "radio", "options": ["No", "Yes"]}
}

st.subheader("📋 Enter User Data")
input_data = []

for feature, config in feature_config.items():
    if "type" not in config:
        val = st.slider(f"{feature}", min_value=config["min"], max_value=config["max"],
                        step=config["step"], help=config.get("help", ""))
    else:
        val = st.radio(f"{feature}", config["options"], horizontal=True)
        val = 1 if val == "Yes" else 0
    input_data.append(val)

# --- Predict Button ---
if st.button("Predict"):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    if prediction == 1:
        st.success("🧠 The person is predicted to be an **Introvert**.")
    else:
        st.success("😄 The person is predicted to be **Extrovert**.")
