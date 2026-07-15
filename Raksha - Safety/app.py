
from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
import datetime
import os

app = Flask(__name__)

# ML Model Load
MODEL_PATH = 'model.h5'
if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
else:
    model = None

@app.route('/')
def home():
    return render_template('index.html', app_name="Result Raksha Extreme")

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not found"})

    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)

    result = "Safe" if prediction[0][0] > 0.5 else "Alert"
    return jsonify({"status": "Success", "result": result, "confidence": float(prediction[0][0])})

@app.route('/sos', methods=['POST'])
def sos():
    location = request.form.get('location')
    contact = request.form.get('contact')
    time = str(datetime.datetime.now())
    # Yaha SMS/Email alert ka logic add kar dena
    return jsonify({"status": "SOS Sent", "location": location, "contact": contact, "time": time})

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=False)
