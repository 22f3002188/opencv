import cv2

image = cv2.imread('cat.png')

if image is None:
    print("Error: Could not load image.")
else:
    print("Image loaded successfully.")