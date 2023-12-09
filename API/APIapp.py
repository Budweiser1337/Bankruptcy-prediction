from flask import Flask, request, jsonify

import numpy as np
import joblib

app = Flask(__name__)

# Charger votre modèle pré-entraîné MLPClassifier ici
model = joblib.load('MLPClassifier.pkl')

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Extract features from the URL parameters
        features_str = request.args.getlist('features')
        features = [float(feature) for feature in features_str]
        # Check if features are provided
        if not features:
            raise ValueError("Features not provided in the URL.")

        # Convert features to a numpy array
        features_array = np.array(features).reshape(1, -1)

        # Make the prediction with the model
        prediction = model.predict(features_array)

        # Return the prediction to the client
        return jsonify({'prediction': int(prediction[0])})
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/')
def home():
    return 'Hello, this is the home page!'
if __name__ == '__main__':
    app.run(port=5000, debug=True)