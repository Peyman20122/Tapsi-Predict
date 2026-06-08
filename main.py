from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import mysql.connector as msql
from mysql.connector import Error

model = joblib.load("model.joblib")
app = FastAPI(title="Tap30 Demand Prediction API")

class DemandRequest(BaseModel):
    day: int
    hour: int
    row: int
    col: int

@app.post("/predict")
def predict_demand(data: DemandRequest):
    features = np.array([[data.day, data.hour, data.row, data.col]])
    prediction = int(model.predict(features)[0])
    try:
        conn = msql.connect(
            host='127.0.0.1',
            user='root',
            password='peiman2012',
            database='tap30db'
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS demand_predictions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    Day INT,
                    Hour INT,
                    row_val INT,
                    col_val INT,
                    predicted_demand INT
                )
            """)
            insert_query = """
                INSERT INTO demand_predictions (Day, Hour,row_val, col_val, predicted_demand)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (data.day, data.hour, data.row, data.col, prediction))
            conn.commit()

    except Error as e:
        return {"error": str(e)}

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

    return {
        "input_features": data.dict(),
        "predicted_demand": prediction
    }

