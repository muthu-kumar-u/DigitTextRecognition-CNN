from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi import FastAPI
from pathlib import Path
from router import model
import uvicorn
import os

# Load environment variables from .env file
load_dotenv(dotenv_path=".env")

# Define app and version
app = FastAPI(openapi_url="")
version = os.getenv("VERSION")

# Define paths
DATA_PATH = os.getenv("DATASET_PATH")
MODEL_DIR = os.getenv("MODEL_DIR")
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)

# Create model directory if it doesn't exist
Path(MODEL_DIR).mkdir(parents=True, exist_ok=True)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include the model router
app.include_router(model.router, prefix=f"/api/{version}")

# Run the app
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
