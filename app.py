from flask import Flask, request, jsonify
import joblib
import sys
import traceback
import pandas as pd
from flask_cors import CORS

# Your API definition
app = Flask(__name__)
CORS(app)

# Load the model and model columns
try:
    clf = joblib.load("model.pkl")  # Load "model.pkl"
    print('Model loaded')
    model_columns = joblib.load("model_columns.pkl")  # Load "model_columns.pkl"
    print('Model columns loaded')
except Exception as e:
    print(f"Error loading model: {e}")
    clf = None
    model_columns = None

@app.route('/predict', methods=['POST'])
def predict():
    if clf and model_columns:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = clf.predict(query)

            return jsonify({'prediction': str(prediction)})

        except Exception as e:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])  # This is for a command-line input
    except Exception as e:
        print(f"Error reading port from command-line arguments: {e}")
        port = 12345  # If you don't provide any port, the port will be set to 12345

    app.run(host = '127.0.0.1', port=12345,debug=True)