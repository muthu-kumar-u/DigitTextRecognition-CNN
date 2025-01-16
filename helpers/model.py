from dotenv import load_dotenv
from PIL import Image
import numpy as np
import cv2
import base64
import os
import io

# Function to load the model
async def load_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    model = load_model(model_path)
    
    return model
    
# Function to decode the model prediction
async def decode_prediction(prediction):
    # Decode the predicted sequence into text
    return ''.join([str(c) for c in np.argmax(prediction, axis=-1)])

# Function to preprocess image data
async def preprocess_image(image_data: str):
    img_data = base64.b64decode(image_data)
    img = Image.open(io.BytesIO(img_data))
    img = np.array(img.convert('L'))  # Convert to grayscale
    img = cv2.resize(img, (128, 64))  # Resize image to match model's input size
    img = np.expand_dims(img, axis=-1)  # Add channel dimension
    img = img / 255.0  # Normalize
    return np.expand_dims(img, axis=0)  # Add batch dimension