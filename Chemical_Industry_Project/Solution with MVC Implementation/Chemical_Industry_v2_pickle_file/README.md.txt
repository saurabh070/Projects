# Flask Application for Leakage Detection

This Flask application serves as an API for training and testing a logistic regression model to detect leakage based on provided parameters.

## Setup Instructions

1. Install the required dependencies by running:
pip install -r requirements.txt


2. Run the Flask application by executing the `app.py` file.

## Usage

### Training the Model

- **Endpoint:** `/train_model`
- **Method:** GET
- **Description:** Trains the logistic regression model using the dataset provided in `Historical Alarm Cases.xlsx`.
- **Response:** Returns "Model trained successfully" upon successful training.

### Testing the Model

- **Endpoint:** `/test_model`
- **Method:** POST
- **Description:** Tests the trained model by providing input parameters in JSON format.
- **Response:** Returns either "No Leakage... False Alarm" or "DANGER !!! LEAKAGE DETECTED !!!" based on the prediction of the model.

### Postman Usage

You can use Postman to interact with the API using the following endpoints:

- **Training Endpoint:** `http://127.0.0.1:5000/train_model`
- **Testing Endpoint:** `http://127.0.0.1:5000/test_model`

### Sample Input for Prediction

```json
{
"Ambient Temperature": 7,
"Calibration": 57.00,
"Unwanted substance deposition": 0,
"Humidity": 90,
"H2S Content": 7,
"detected by": 38
}

```json
{
  "Ambient Temperature": 4,
  "Calibration": 134.00,
  "Unwanted substance deposition": 1,
  "Humidity": 83,
  "H2S Content": 4,
  "detected by": 77
}

