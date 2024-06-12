# Flask ML Application

This project demonstrates a Flask web application for training and testing a machine learning model to predict the spuriosity of alarm cases. The model is trained using a logistic regression algorithm.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Sample Input](#sample-input)
- [File Structure](#file-structure)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-repo/flask-ml-app.git
    cd flask-ml-app
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure you have the dataset `Historical Alarm Cases.xlsx` in the project directory.

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. The application will be available at `http://127.0.0.1:5000`.

## Endpoints

### Train Model
- **URL:** `/train_model`
- **Method:** `GET`
- **Description:** Trains the logistic regression model using the dataset.
- **Response:** "Model trained successfully."

### Test Model
- **URL:** `/test_model`
- **Method:** `POST`
- **Description:** Tests the model with the provided input data.
- **Request Body:** JSON containing the test data.
- **Response:** "No Leakage... False Alarm" or "DANGER !!! LEAKAGE DETECTED !!!"

## Sample Input

### Train Model
- **Request:** 
    ```sh
    curl -X GET http://127.0.0.1:5000/train_model
    ```

### Test Model
- **Request:**
    ```sh
    curl -X POST http://127.0.0.1:5000/test_model -H "Content-Type: application/json" -d '{"Ambient Temperature":7,"Calibration":57.00,"Unwanted substance deposition":0,"Humidity":90,"H2S Content":7,"detected by":38}'
    ```

- **Sample Inputs:**
    ```json
    {"Ambient Temperature":7,"Calibration":57.00,"Unwanted substance deposition":0,"Humidity":90,"H2S Content":7,"detected by":38}
    {"Ambient Temperature":4,"Calibration":134.00,"Unwanted substance deposition":1,"Humidity":83,"H2S Content":4,"detected by":77}
    ```

## File Structure

```plaintext
flask-ml-app/
│
├── app.py                  # Main Flask application file
├── Historical Alarm Cases.xlsx # Dataset file
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
