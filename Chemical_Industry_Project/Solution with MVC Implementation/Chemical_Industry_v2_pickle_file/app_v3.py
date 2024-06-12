from flask import Flask, request
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)


@app.route('/train_model')
def train():
    # Load dataset
    df = pd.read_excel('Historical Alarm Cases.xlsx')

    # Split dataset into features(x) and target(y)
    x = df.iloc[:, 1:7]
    y = df['Spuriosity Index(0/1)']

    # Create an instance of Logistic Regression model
    log_model = LogisticRegression()

    # Train the model
    log_model.fit(x, y)

    # Save Model in pickle file
    joblib.dump(log_model, 'train.pkl')

    return "Model trained successfully"


@app.route('/test_model', methods=['POST'])
def test():
    # Load pickle file
    pkl_file = joblib.load('train.pkl')

    # Get test data from the request in JSON format
    test_data = request.get_json()
    col1 = test_data['Ambient Temperature']
    col2 = test_data['Calibration']
    col3 = test_data['Unwanted substance deposition']
    col4 = test_data['Humidity']
    col5 = test_data['H2S Content']
    col6 = test_data['detected by']

    # Numpy array with the test data and reshape it for the model
    features = np.array([col1, col2, col3, col4, col5, col6]).reshape(1, 6)
    prediction = pkl_file.predict(features)

    if prediction == 1:
        return "No Leakage... False Alarm"
    else:
        return "DANGER !!! LEAKAGE DETECTED !!! "


# Run the Flask application on port 5000
app.run(port=5000)

# URLs for Postman
# http://127.0.0.1:5000/train_model
# http://127.0.0.1:5000/test_model

# User Input for prediction
# {"Ambient Temperature":7,"Calibration":57.00,"Unwanted substance deposition":0,"Humidity":90,"H2S Content":7,"detected by":38}
# {"Ambient Temperature":4,"Calibration":134.00,"Unwanted substance deposition":1,"Humidity":83,"H2S Content":4,"detected by":77}
