from fastapi import FastAPI
import uvicorn
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI(
    title="Lung Cancer Prediction API",
    description="""An API Machine Learning model that can help in detecting/predicting lung cancer based on the following features: age, gender, blood pressure, smoke, coughing, allergies, fatigue etc.""",
    version="0.1.0", debug=True)


model = joblib.load('lung_cancer_predictor_model.pkl')
@app.get('/')
def home():
    return {'Title': 'Lung Cancer Prediction API'}

class LungCancer(BaseModel):
    GENDER:int	
    AGE:int
    SMOKING:int	
    YELLOW_FINGERS:int	
    ANXIETY:int	
    PEER_PRESSURE:int	
    CHRONIC_DISEASE:int	
    FATIGUE:int	
    ALLERGY:int	
    WHEEZING:int	
    ALCOHOL_CONSUMPTION:int	
    COUGHING:int	
    SHORTNESS_OF_BREATH:int	
    SWALLOWING_DIFFICULTY:int	
    CHEST_PAIN:int

@app.post('/predict')
def predict(data : LungCancer):

    features = np.array([[data.GENDER, data.AGE, data.SMOKING, data.YELLOW_FINGERS, data.ANXIETY, data.PEER_PRESSURE, data.CHRONIC_DISEASE, data.FATIGUE, data.ALLERGY, data.WHEEZING, data.ALCOHOL_CONSUMPTION, data.COUGHING, data.SHORTNESS_OF_BREATH, data.SWALLOWING_DIFFICULTY, data.CHEST_PAIN]])
    model = joblib.load('lung_cancer_predictor_model.pkl')

    predictions = model.predict(features)
    if predictions == 1:
        return {"This Person has lung cancer"}
    elif predictions == 0:
        return {"This Person does not have long cancer"}
