from fastapi import FastAPI
from app.schemas import PatientData
from app.predictor import predict_heart_disease

app = FastAPI(
    title="CardioScanAI",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "CardioScanAI API Running"}

@app.post("/predict")
def predict(data: PatientData):

    result = predict_heart_disease(data.dict())

    return result