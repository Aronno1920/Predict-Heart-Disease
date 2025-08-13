###### Import Required Library
import numpy as np
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib

from .schemas import HeartInput
import pathlib
##########################################



###### Initial FastAPI
app = FastAPI(title="API: Predict Heart Disease", version="1.0")
model = joblib.load("model/heart_model.joblib")
templates = Jinja2Templates(directory="app/templates")
##########################################



###### API Endpoints
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



###### FRONTEND ROUTES
@app.get("/", response_class=HTMLResponse)
def home():
    html_file = pathlib.Path(__file__).parent / "templates" / "index.html"
    return HTMLResponse(content=html_file.read_text(encoding="utf-8"), status_code=200)
##########################################