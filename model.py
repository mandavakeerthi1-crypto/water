import joblib
import numpy as np

model = joblib.load("models/water_model.pkl")

def predict_water_usage(hour, users):
    data = np.array([[hour, users]])
    prediction = model.predict(data)
    return round(prediction[0], 2)