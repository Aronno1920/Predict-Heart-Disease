import numpy as np
from fastapi import FastAPI
from app.schemas import HeartInput

import joblib

app = FastAPI(title="API: Predict Heart Disease")

#Load Model
model = joblib.load("model/heart_model.joblib")



##########################################
@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/info")
def info():
    return {
        "model": "Random Forest Classifier",
        "features": [
            "age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak",
            "slope", "ca", "thal"
        ]
    }
    

@app.post("/predict")
def predict(data: HeartInput):
    input_data = np.array([[data.age, data.sex, data.cp, data.trestbps,
                            data.chol, data.fbs, data.restecg, data.thalach,
                            data.exang, data.oldpeak, data.slope,
                            data.ca, data.thal]])
    prediction = model.predict(input_data)[0]
    return {"heart_disease": bool(prediction)}
##########################################