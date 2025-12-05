import cv2

image = cv2.imread('cat.png')

# 0 vertcally - top to bottom
# 1 horizontally- left to right
#-1 both horizontally and vertically

if image is None:
    print("could not load image")
else:
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)    
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("original :", image)
    cv2.imshow("flipped horizontally :", flipped_horizontal)
    cv2.imshow("flipped vertically: ", flipped_vertical)
    cv2.imshow("flipped both: ", flipped_both)


    cv2.waitKey(0)
    cv2.destroyAllWindows