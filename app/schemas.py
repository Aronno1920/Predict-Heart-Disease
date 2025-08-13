from pydantic import BaseModel

class HeartInput(BaseModel):
    age: int = 50
    sex: int = 1
    cp: int = 0
    trestbps: int = 120
    chol: int = 200
    fbs: int = 0
    restecg: int = 1
    thalach: int = 150
    exang: int = 0
    oldpeak: float = 1.0
    slope: int = 2
    ca: int = 0
    thal: int = 2