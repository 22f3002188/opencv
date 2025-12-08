import cv2

image = cv2.imread('cat.png')

if image is not None:
    cv2.imshow('Cat Image', image)  #open window to display image
    cv2.waitKey(0)   #wait for a key press to close the window
    cv2.destroyAllWindows() #close the window
else:
    print("Error: Could not display image because it was not loaded.")