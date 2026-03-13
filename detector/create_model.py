import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import os

# --- DATASET PATH (Important) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # detector/
DATASET_DIR = os.path.join(BASE_DIR, "dataset")        # detector/dataset/

# Image settings
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# 1) Data Augmentation + Normalization
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

train_generator = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_generator = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# 2) Simple CNN Model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(train_generator.num_classes, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 3) Train
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=15
)

# 4) Save model
MODEL_PATH = os.path.join(BASE_DIR, "model.h5")
model.save(MODEL_PATH)

print("\n==============================")
print("Training completed successfully!")
print(f"Model saved at: {MODEL_PATH}")
print("==============================")
