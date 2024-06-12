from flask import Flask, request
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np


class AlarmHandler:
    def __init__(self):
        self.model = None
        self.scaler = None

    def train_model(self):
        # Load dataset
        dataset = pd.read_excel('Historical Alarm Cases.xlsx')

        # Split dataset into features(x) and target(y)
        x = dataset.iloc[:, 1:7]
        y = dataset['Spuriosity Index(0/1)']

        # Perform train-test split
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        # Preprocess features
        self.scaler = StandardScaler()
        x_scaled = self.scaler.fit_transform(x_train)

        # Create an instance of Logistic Regression model
        log_model = LogisticRegression()

        # Train the model
        log_model.fit(x_scaled, y_train)

        # Assign the trained model to the instance variable
        self.model = log_model

    def test_model(self, test_data):
        # Check if model is ready for testing
        if self.model is None or self.scaler is None:
            return "Model not found. Please train the model first."

        # Get test data from the request in JSON format
        col1 = test_data['Ambient Temperature']
        col2 = test_data['Calibration']
        col3 = test_data['Unwanted substance deposition']
        col4 = test_data['Humidity']
        col5 = test_data['H2S Content']
        col6 = test_data['detected by']

        # Numpy array with the test data and reshape it for the model
        features = np.array([col1, col2, col3, col4, col5, col6]).reshape(1, -1)

        # Preprocess the input features using the scaler
        scaled_features = self.scaler.transform(features)

        # Prediction using the trained model
        prediction = self.model.predict(scaled_features)

        # Prediction result
        if prediction == 1:
            return "No Leakage... False Alarm"
        else:
            return "DANGER !!! LEAKAGE DETECTED !!!"


# Flask application instance
app = Flask(__name__)

# AlarmHandler instance
alarm = AlarmHandler()


# Train the model, use GET method via Postman
@app.route('/train_model', methods=['GET', 'POST'])
def train_model():
    if request.method == 'GET':
        alarm.train_model()
        return "Model trained successfully."
    else:
        return "Method Not Allowed, please use GET method."


# Test the model, pass the test data via POST method
@app.route('/test_model', methods=['POST'])
def test_model():
    test_data = request.get_json()
    return alarm.test_model(test_data)


if __name__ == "__main__":
    # Run the Flask application on port 5000
    app.run(port=5000)

# URLs for Postman
# http://127.0.0.1:5000/train_model
# http://127.0.0.1:5000/test_model

# User Input for prediction
# {"Ambient Temperature":7,"Calibration":57.00,"Unwanted substance deposition":0,"Humidity":90,"H2S Content":7,"detected by":38}
# {"Ambient Temperature":4,"Calibration":134.00,"Unwanted substance deposition":1,"Humidity":83,"H2S Content":4,"detected by":77}
