from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import random
import string
import os

load_dotenv(dotenv_path=".env")

# Function to generate synthetic image with random text
def generate_synthetic_image(text, size=(128, 32)):
    font = ImageFont.load_default() 
    image = Image.new('L', size, color=255) 
    draw = ImageDraw.Draw(image)
    
    bbox = draw.textbbox((0, 0), text, font=font) 
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]  
    
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)  
    
    # Draw text in black color
    draw.text(position, text, font=font, fill=0)
    return np.array(image) / 255.0 

output_dir = os.getenv("SYNTHETIC_IMAGES_DIR")
labels_dir = os.getenv("SYNTHETIC_LABELS_PATH")

if not output_dir or not labels_dir:
    raise EnvironmentError("Both 'SYNTHETIC_IMAGES_DIR' and 'SYNTHETIC_LABELS_PATH' must be set as environment variables.")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if not os.path.exists(labels_dir):
    os.makedirs(labels_dir)

# Function to generate dataset and save images and labels
def generate_synthetic_dataset(num_images=100, output_dir=output_dir, labels_dir=labels_dir):
    dataset_images = []
    dataset_labels = []
    
    for i in range(num_images):
        text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        image = generate_synthetic_image(text)
        
        # Save the image to the directory
        image_filename = os.path.join(output_dir, f"{i}_{text}.png")
        Image.fromarray((image * 255).astype(np.uint8)).save(image_filename) 
        
        dataset_images.append(image)
        dataset_labels.append(text)
    
    # Save labels to a CSV file outside the "synthetic_images" folder
    labels_df = pd.DataFrame({"filename": [f"{i}_{text}.png" for i, text in enumerate(dataset_labels)],
                               "label": dataset_labels})
    labels_df.to_csv(os.path.join(labels_dir, "labels.csv"), index=False) 

    return dataset_images, dataset_labels

images, labels = generate_synthetic_dataset(100)

print("Images and labels saved successfully.")
