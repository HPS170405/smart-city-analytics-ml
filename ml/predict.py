import joblib
import pandas as pd

# Load model
model = joblib.load("models/traffic_model.pkl")

# Create input with column names
data = pd.DataFrame([{
    "Junction": 2,
    "ID": 150,
    "hour": 18
}])

pred = model.predict(data)

print("🚦 Predicted Vehicles:", int(pred[0]))
