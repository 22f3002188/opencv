# import cv2

# image = cv2.imread('cat.png')

# if image is not None:
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('Gray Cat Image', gray)  #open window to display grayscale image
#     cv2.imwrite('cat_gray.png', gray)  #save grayscale image to new file
#     cv2.waitKey(0)   #wait for a key press to close the window
#     cv2.destroyAllWindows() #close the window
# else:
#     print("Error: Could not display image because it was not loaded.")

import cv2

# Load the image
image = cv2.imread('cat.png')

if image is None:
    print("Error: Could not load image.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("What do you want to do?")
print("1. Show the grayscale image")
print("2. Save the grayscale image")
print("3. Both show and save")
print("4. Exit")

choice = input("Enter your choice (1/2/3/4): ")

if choice == "1":
    cv2.imshow('Gray Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif choice == "2":
    cv2.imwrite('cat_gray.png', gray)
    print("Image saved as cat_gray.png")

elif choice == "3":
    cv2.imshow('Gray Image', gray)
    cv2.imwrite('cat_gray.png', gray)
    print("Image saved as cat_gray.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif choice == "4":
    print("Exiting program...")

else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")
