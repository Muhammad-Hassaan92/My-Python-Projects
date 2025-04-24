import gradio as gr
import pickle
import numpy as np

with open('diabetes_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

import pandas as pd
import numpy as np

# Example data (just like the two examples I showed)
test_data = pd.DataFrame({
    'gender': [2],  # Female encoded as 2
    'age': [44.0],
    'hypertension': [0],
    'heart_disease': [0],
    'smoking_history': [0],  # 'never' encoded as 0
    'bmi': [19.31],
    'HbA1c_level': [6.5],
    'blood_glucose_level': [200]
})

# Make predictions
prediction = model.predict(test_data)
print("Prediction (0 for No Diabetes, 1 for Diabetes):", prediction[0])

# Define the prediction function
def predict_diabetes(gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level):
    # Map categorical inputs to numeric values expected by the model
    gender_map = {"Male": 1, "Female": 0}
    hypertension_map = {"Yes": 1, "No": 0}
    heart_disease_map = {"Yes": 1, "No": 0}
    smoking_map = {
        "No Info": 0.0,
        "Current": 1.0,
        "Ever": 2.0,
        "Former": 3.0,
        "Never": 4.0
    }

    features = np.array([[
        gender_map[gender],
        age,
        hypertension_map[hypertension],
        heart_disease_map[heart_disease],
        smoking_map[smoking_history],
        bmi,
        hba1c_level,
        blood_glucose_level
    ]])
    prediction = model.predict(features)[0]
    return "Diabetic" if prediction == 1 else "Not Diabetic"

# Gradio interface
interface = gr.Interface(
    fn=predict_diabetes,
    inputs=[
        gr.Dropdown(["Male", "Female"], label="Gender"),
        gr.Slider(0, 100, label="Age"),
        gr.Dropdown(["Yes", "No"], label="Hypertension"),
        gr.Dropdown(["Yes", "No"], label="Heart Disease"),
        gr.Dropdown(["No Info", "Current", "Ever", "Former", "Never"], label="Smoking History"),
        gr.Slider(10.0, 100.0, label="BMI"),
        gr.Slider(1.5, 10.0, label="HbA1c Level"),
        gr.Slider(50, 350, label="Blood Glucose Level"),
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="Diabetes Prediction App by Muhammad Hassaan"
)

if __name__ == "__main__":
    interface.launch()