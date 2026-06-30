import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("water_usage.csv")

# Features
X = data[["water_level", "motor"]]

# Target
y = data["prediction"]

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the trained model
joblib.dump(model, "water_model.pkl")

print("Model trained successfully!")