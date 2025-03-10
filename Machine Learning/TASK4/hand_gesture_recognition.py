import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tqdm import tqdm

# Define dataset path
dataset_path = "path_to_your_dataset"

# Image processing parameters
img_size = 64
categories = os.listdir(dataset_path)

def load_data():
    data = []
    labels = []
    
    for category in categories:
        path = os.path.join(dataset_path, category)
        label = categories.index(category)
        
        for img in tqdm(os.listdir(path)):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                img_resized = cv2.resize(img_array, (img_size, img_size))
                data.append(img_resized)
                labels.append(label)
            except Exception as e:
                pass
    
    return np.array(data), np.array(labels)

# Load dataset
data, labels = load_data()

# Normalize and reshape data
data = data / 255.0  # Normalize pixel values
data = data.reshape(-1, img_size, img_size, 1)  # Reshape for CNN
labels = to_categorical(labels, num_classes=len(categories))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Build CNN model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(img_size, img_size, 1)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(len(categories), activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), batch_size=32)

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Accuracy: {accuracy * 100:.2f}%')
