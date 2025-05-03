
# Tap30 Demand Prediction API

This project is an API that uses a demand prediction model to predict the demand for Tap30 service. The API is implemented using FastAPI framework.

## Prerequisites

- Python 3.8+
- Required libraries:
  - FastAPI
  - Uvicorn
  - XGBoost (for the model)
  - joblib
  - numpy
  - mysql-connector-python (for MariaDB connection)

## Installation

To set up the project and install required libraries, follow these steps:

1. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install required libraries:
   ```bash
   pip install fastapi uvicorn joblib numpy scikit-learn mysql-connector-python
   ```

4. Place your trained model file (`model.joblib`) in the project directory.

## Using the API

### 1. Running the Server

To start the server, use the following command:

```bash
uvicorn main:app --reload
```

The server will now be running at `http://127.0.0.1:8000`.

### 2. Sending a Request to the API

To send data to the API and get predictions, you can use tools like **Postman** or **curl**.

![image](https://github.com/user-attachments/assets/5717e632-405e-47e5-aacd-84e55415b9dd)


#### POST Request:

- URL: `http://127.0.0.1:8000/predict`
- Method: `POST`
- Request body (JSON):
  ```json
  {
      "day": 100,
      "hour": 8,
      "row": 2,
      "col": 6,
  }
  ```

#### Response:
On success, the response will look like this:
```json
{
  "input_features": {
    "day": 100,
    "hour": 8,
    "row": 2,
    "col": 6,
  },
  "predicted_demand": 50
}
```

### 3. Error Messages

If the input data is missing required fields, the API will return an error message. For example, if a required field is missing:
```json
{
  "detail": [
    {
      "loc": ["body", "day"],
      "msg": "Field required",
      "type": "missing"
    },
    {
      "loc": ["body", "hour"],
      "msg": "Field required",
      "type": "missing"
    }
  ]
}
```

## Important Notes

1. If you are using **MariaDB** to store data, you need to configure the database connection details in the `main.py` file.

2. This project is set up to run locally, but you can deploy it on a server or platforms like Heroku or AWS for production use.

![image](https://github.com/user-attachments/assets/e6755abc-c20e-45e9-8738-67b38590befe)

## Files

- **`main.py`**: FastAPI code for processing the prediction and returning results.
- **`model.joblib`**: The trained model file saved using XGBoost or any other model you have used.
- **`requirements.txt`**: A list of Python dependencies for quick installation.

## Development and Contributing

- If you have any suggestions or issues, feel free to open an issue on the GitHub repository.
- Contributions to the development of this project are welcome.

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/en/latest/)
