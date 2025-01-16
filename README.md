# Digital Text Recognition: Using Deep learning algorithms such as CNN and RNN

This project focuses on handwritten text recognition using deep learning models such as CNN (Convolutional Neural Networks) and RNN (Recurrent Neural Networks) with CTC Loss for live predictions. The application supports both an HTTP API for server-based inference and live predictions using a camera feed via OpenCV.

## Features

- Preprocessing pipeline for image preprocessing (grayscale, resizing, etc.).
- Training and evaluation of deep learning models for handwritten text recognition.
- Fast API to expose model prediction as an HTTP endpoint for text recognition from images.
- Live camera prediction using OpenCV to capture images from the camera feed and send them to the Flask API for real-time recognition.
- Trained model stored as a .pkl file, ready to be used for prediction.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourname/DigitTextRecognition-CNN-RNN

2. Create virtual environment:
   ```bash
   python3 -m venv yourvenvname   

3. Activate the venv (for linux):
   ```bash
   source yourvenv/bin/activate

4. Install dependencies on venv:
   ```bash 
   pip install -r requirements.txt

5. Run the main.py:
   ```bash
   python main.py
   ```
   * This will launch a Fast Api server at :5500 Port, exposing the /predict endpoint for recognition.

6. Run the Camera Feed for Live Prediction:   
   * To capture live handwriting using your webcam and send the frames for prediction, run the following command: 
   ```bash
   python camera/capture.py
   ```
   * This script captures frames from your camera, processes the images, and sends them to the Flask API for real-time handwritten text recognition. The recognized text will be displayed on the video feed.

## Api Prediction:
   * Set up a POST request in Postman to http://127.0.0.1:5000/predict
   * In the body, choose raw and JSON, and provide the image in base64 format.
   * Send the request to get the predicted text in the response.

### Request Body:
   To predict the text from an image using the API, you need to send a POST request with the image in Base64 encoded format.
   #### Example Request:
   ```bash
   {
     "image": "<Base64_encoded_image_data>"
   }
   ```
   #### Response:
   The API will return a JSON response with the predicted text.
   #### Example Response:
   ```bash
   {
     "predicted_text": "Hello World"
   }
   ```   
    
## Usage:
   * The application processes the input data (either from an image via the API or from the live camera feed) and uses the trained deep learning model to predict the handwritten text.
   * Results can be viewed via the live feed in real-time or accessed through the API.

## Model Training:   
  If you'd like to train the model on your own dataset:
  * Prepare your dataset of handwritten text (e.g., MNIST, IAM).
  * Modify the training script on .ipynb file to fit your dataset and fine-tune the model.
  * Save the trained model to a .pkl file for use with the Fast API.

## Note:
   * **API Performance**: The speed of predictions might vary based on the input image size and the server's processing power.
   * **Camera Performance**: The live camera feed might lag slightly depending on the resolution and performance of the system running the application also Ensure you have OpenCV properly installed for camera functionality (opencv-python package).

## Additional Notes:
   * **Fork & Contribute:** If you are interested in contributing to the project, please feel free to fork the repository and submit a pull request (PR) with improvements. Specifically, it would be great if you could add test cases to improve the reliability of the project. I will review and merge the PRs once they are thoroughly tested.