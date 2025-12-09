import cv2
import numpy as np

image = cv2.imread("harsh_photo.jpeg")

sharpen_kernel  = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
#gaussian blurr #average value
# blurred = cv2.GaussianBlur(image, (7,7), 3)  #kernel size always in odd (7,7) 3 quamtity for blurr

#median blurr #median value of neighbour pixels
# median = cv2.medianBlur(image, 11)

sharp = cv2.filter2D(image, -1, sharpen_kernel)

cv2.imshow("sharpen image: ", sharp)
cv2.imshow("original image :", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
