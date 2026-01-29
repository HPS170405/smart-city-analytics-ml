from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("models/traffic_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    df = pd.DataFrame([data])

    pred = model.predict(df)[0]

    return jsonify({
        "predicted_vehicles": int(pred)
    })

if __name__ == "__main__":
    app.run(debug=True)
