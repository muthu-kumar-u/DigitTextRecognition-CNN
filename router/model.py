from helpers.model import load_model, preprocess_image, decode_prediction
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel, validator
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")
MODEL_DIR = os.getenv("MODEL_DIR") 
MODEL_NAME = os.getenv("MODEL_NAME")

router = APIRouter()

# Define the request body model using Pydantic
class Request(BaseModel):
    image: str

    # Validate that the image field is not empty
    @validator('image')
    def validate_non_empty(cls, v):
        if not v or v.strip() == "":
            raise ValueError('Image cannot be empty or just whitespace')
        return v

async def predict_from_model(image_data: str):
    try:
        # Load the model (only once during the app's startup to optimize performance)
        model = await load_model(os.path.join(MODEL_DIR, MODEL_NAME))

        # Preprocess the image before passing to the model
        processed_image = await preprocess_image(image_data)

        # Predict using the model
        prediction = model.predict(processed_image)

        # Decode the prediction 
        result = await decode_prediction(prediction)

        return {"predicted_text": result}
    
    except Exception as e:
        print(str(e))
        return {"error": "Internal Server Error"}

@router.post('/predict')
async def predict(features: Request):
    return await predict_from_model(features)

