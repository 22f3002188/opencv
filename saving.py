import cv2

image = cv2.imread('cat.png')

if image is not None:
    success = cv2.imwrite('cat_copy.png', image)  #save image to new file
    if success:
        print("Image saved successfully.")
    else:
        print("Error: Could not save image.")
else:
    print("Error: Could not save image because it was not loaded.")        