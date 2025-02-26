from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import joblib

# Load the trained model
model = load_model("diabetes_model.h5")

# Load the scaler used during training
scaler = joblib.load("scaler.pkl")  # Ensure you've saved and loaded the same scaler

app = Flask(__name__)

@app.route('/')
def home():
    return "Diabetes Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json()

        # Convert input into numpy array
        input_data = np.array(data["features"]).reshape(1, -1)

        # Normalize using the saved scaler
        input_data = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_data)
        result = int(prediction[0][0] > 0.5)  # Convert probability to 0 or 1

        return jsonify({"prediction": result, "probability": float(prediction[0][0])})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get port from environment variables
    app.run(host="0.0.0.0", port=port)  # Run Flask on the specified port