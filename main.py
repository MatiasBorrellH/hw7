
from fastapi import FastAPI, File, UploadFile
import joblib
import pandas as pd
import json

app = FastAPI()

# Cargar el modelo entrenado
lg_model = joblib.load("trained_lg_model.joblib")

@app.post("/prediction")
async def make_prediction(file: UploadFile = File("prediction_1.json")):
    # Leer el contenido del archivo JSON sin verificaciones adicionales
    contents = await file.read()
    data = json.loads(contents)
    
    # Convertir el JSON a un DataFrame
    entry = pd.DataFrame([data])
    
    # Hacer la predicción
    prediction = lg_model.predict(entry)
    
    return {"prediction": int(prediction[0])}