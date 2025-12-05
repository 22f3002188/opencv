import cv2

image = cv2.imread('cat.png')
#width #height

if image is None:
    print("Error: Could not load image.")
else:
    print("Image loaded successfully.")

    resized = cv2.resize(image, (200, 200))  # Resize image to 200x200 pixels
    cv2.imshow('original Image', image)  # Display original image
    cv2.imshow('Resized Image', resized)  # Display resized image
    cv2.imwrite('resized_cat.png', resized)  # Save resized image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
