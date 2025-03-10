import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from tqdm import tqdm

# Define dataset path
dataset_path = "path_to_your_dataset"

# Image processing parameters
img_size = 64
categories = ['cat', 'dog']

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
                data.append(img_resized.flatten())
                labels.append(label)
            except Exception as e:
                pass
    
    return np.array(data), np.array(labels)

# Load dataset
data, labels = load_data()

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Train SVM model
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Predict on test data
y_pred = svm_model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
print(classification_report(y_test, y_pred, target_names=categories))
