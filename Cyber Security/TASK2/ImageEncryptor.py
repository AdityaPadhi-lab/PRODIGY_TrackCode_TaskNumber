import cv2
import numpy as np

def encrypt_image(image_path, key):
    image = cv2.imread(image_path)
    encrypted = image ^ key
    cv2.imwrite("encrypted_image.png", encrypted)

def decrypt_image(image_path, key):
    image = cv2.imread(image_path)
    decrypted = image ^ key
    cv2.imwrite("decrypted_image.png", decrypted)

if __name__ == "__main__":
    key = 42  # Example key
    encrypt_image("input.png", key)
    decrypt_image("encrypted_image.png", key)
