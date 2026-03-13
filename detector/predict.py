# detector/predict.py

import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load your trained Keras model once
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.h5')
model = load_model(MODEL_PATH)


CLASS_NAMES = [
    "Healthy",
    "Bacterial_Spot",
    "Early_Blight",
    "Late_Blight",
    "Leaf_Mold",
    "Septoria_Leaf_Spot",
    "Spider_Mites",
    "Target_Spot",
    "Mosaic_Virus",
    "Yellow_Leaf_Curl_Virus",
    "Fusarium_Wilt",
    "Verticillium_Wilt",
    "Bacterial_Canker",
    "Gray_Leaf_Spot",
    "Cladosporium_Leaf_Spot",
    "Powdery_Mildew",
    "Southern_Blight",
    "Black_Spot",
    "Nutrient_Deficiency",
    "Magnesium_Deficiency",
    "Calcium_Deficiency",
    "Edema",
    "Rust",
    "Curly_Top_Virus",
    "Whiteflies_Damage",
    "Thrips_Damage",
    "Nematode_Infection",

    # Potato
    "Common_Scab",
    "Soft_Rot",
    "Blackleg",
    "Powdery_Scab",
    "Ring_Rot",
    "Potato_Virus_Y",
    "Potato_Virus_X",
    "Potato_Virus_A",
    "Bacterial_Wilt",
    "Leaf_Roll_Virus",
    "Brown_Rot",

    # Pepper
    "Anthracnose",
    "Phytophthora_Blight",
    "Sunscald",
    "Cercospora_Leaf_Spot",
    "Rhizoctonia_Root_Rot",
    "Scorch",

    # General Problems
    "Heat_Stress",
    "Overwatering",
    "Underwatering",
    "Fungal_Infection",
    "Bacterial_Infection",
    "Viral_Infection"
]

def predict_leaf_disease(image_path):
    """
    Predicts disease from uploaded leaf image.
    Returns: result (str), confidence (float)
    """
    img = image.load_img(image_path, target_size=(224, 224))  # adjust size to your model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # normalize if your model expects

    predictions = model.predict(img_array)
    confidence = float(np.max(predictions))
    result = CLASS_NAMES[np.argmax(predictions)]

    return result, confidence
