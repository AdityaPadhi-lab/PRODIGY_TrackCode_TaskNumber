import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import json

# Define dataset path
dataset_path = "path_to_food101_dataset"

# Image processing parameters
img_size = 128
batch_size = 32
num_classes = 101  # Food-101 dataset has 101 classes

def load_calorie_info():
    # Load a sample calorie dataset mapping food items to calories
    calorie_info = {
        "apple_pie": 265,
        "baby_back_ribs": 474,
        "baklava": 334,
        "beef_carpaccio": 120,
        # Add more food items with estimated calorie values...
    }
    return calorie_info

calorie_dict = load_calorie_info()

# Data Augmentation
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Build CNN Model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(img_size, img_size, 3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

# Compile Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train Model
model.fit(train_generator, epochs=10, validation_data=validation_generator)

# Save Model
model.save("food_recognition_model.h5")

# Function to predict food and estimate calories
def predict_food(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (img_size, img_size))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    food_label = list(train_generator.class_indices.keys())[predicted_class]
    estimated_calories = calorie_dict.get(food_label, "Unknown")
    
    return food_label, estimated_calories