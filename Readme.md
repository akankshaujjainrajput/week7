# 🧠 Introvert vs. Extrovert Personality Classifier

This is a deployed machine learning web application built using **Streamlit**, designed to classify a person as an **Introvert** or **Extrovert** based on behavioral and psychological inputs.

🔗 **Live App:** [Click to Try](https://noyqo9fg3odmrpdytbvgey.streamlit.app/)

---

## 📌 Overview

The model was trained on a synthetic dataset representing traits associated with introverted and extroverted personalities. The app supports 6 ML models, all trained with the best hyperparameters found using `GridSearchCV`.

---

## 💡 Features

- 🎛 Choose from 6 ML models:  
  Logistic Regression, LDA, SVC, KNN, Random Forest, Decision Tree

- 📊 Auto-loaded tuned models with high accuracy
- ✅ Input validation with sliders and Yes/No toggles (no keyboard errors!)
- 💾 Models trained on `scikit-learn 1.7.0` with clean serialization

---

## 🧾 Input Features

| Feature                        | Type    | Description                            |
|-------------------------------|---------|----------------------------------------|
| `Time_spent_Alone`            | Integer | Hours spent alone per day              |
| `Stage_fear`                  | Binary  | Do you have stage fear? (Yes/No)       |
| `Social_event_attendance`     | Integer | How often you attend social events     |
| `Going_outside`               | Integer | How often you go outside weekly        |
| `Drained_after_socializing`  | Binary  | Feel drained after socializing? (Y/N)  |
| `Friends_circle_size`         | Integer | Number of close friends                |
| `Post_frequency`              | Integer | Number of posts shared on social media |

---

## 🧠 Models Used

Each model was tuned with GridSearchCV for optimal performance:

- Logistic Regression (`C=0.1`, `solver='liblinear'`)
- LDA (`solver='eigen'`)
- SVC (`C=0.1`, `kernel='rbf'`)
- KNN (`n_neighbors=15`)
- Random Forest (`n_estimators=50`, `max_depth=10`)
- Decision Tree (`max_depth=5`, `splitter='random'`, `criterion='entropy'`)

All models were trained using `scikit-learn 1.7.0`.

---

## 🛠 Installation (For Local Use)

```bash
# Clone the repo
git clone https://github.com/yourusername/personality-predictor.git
cd personality-predictor

# (Optional) create virtual env
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
