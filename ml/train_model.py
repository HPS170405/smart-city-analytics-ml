import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Load data
df = pd.read_csv("data/clean/traffic_clean.csv")

print("Columns:", df.columns.tolist())
print("Dataset shape:", df.shape)

# Target
target = "Vehicles"

# Features
X = df[['Junction', 'ID', 'hour']]
y = df[target]

print("Using features:", X.columns.tolist())

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
print("Training model...")
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=20,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("RMSE:", rmse)
print("R2 Score:", r2)

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/traffic_model.pkl")

print("✅ Model saved at models/traffic_model.pkl")
