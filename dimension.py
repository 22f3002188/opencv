import cv2

image = cv2.imread('cat.png')

if image is not None:
    h, w, c = image.shape
    print(f"Image dimensions: Width={w}, Height={h}, Channels={c}")
else:
    print("Error: Could not retrieve dimensions because image was not loaded.")