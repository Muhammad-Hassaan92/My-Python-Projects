import pandas as pd
import joblib

# Load the saved model

# Load model
model = joblib.load('diabetes_model.joblib')

# Example data for a person with no diabetes (prediction should be 0)
test_data = pd.DataFrame({
    'gender': [2],  # Female encoded as 2
    'age': [80.0],
    'hypertension': [0],
    'heart_disease': [1],
    'smoking_history': [5],  # 'No Info' encoded as 5
    'bmi': [25.19],
    'HbA1c_level': [6.6],
    'blood_glucose_level': [140]
})

# Make prediction
prediction = model.predict(test_data)

# Check the result
print("Prediction (0 for No Diabetes, 1 for Diabetes):", prediction[0])

# Verify if it predicts no diabetes
if prediction[0] == 0:
    print("The model correctly predicts no diabetes.")
else:
    print("The model incorrectly predicts diabetes.")
