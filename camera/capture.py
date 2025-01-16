from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from dotenv import load_dotenv
from helpers.model import preprocess_image
import numpy as np
import cv2
import os
from PIL import Image
import base64
import os
import io

load_dotenv(dotenv_path=".env")

# Load the pre-trained CNN model
model = load_model(os.path.join(os.getenv("MODEL_DIR"), os.getenv("MODEL_NAME")))  

# Open the laptop's camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not accessible!")
    exit()

print("Press 'Space' to capture an image or 'Esc' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27: 
        print("Exiting...")
        break
    elif key == 32:  # Press 'Space' to capture image
        print("Image captured!")
        captured_image = frame
        cv2.imwrite("image.jpg", captured_image) 
        print("Image saved as 'image.jpg'.")

        # Preprocess the captured image
        preprocessed_image = preprocess_image(captured_image)

        # Predict using the model
        prediction = model.predict(preprocessed_image)
        print(f"Prediction: {prediction}")

        break

cap.release()
cv2.destroyAllWindows()