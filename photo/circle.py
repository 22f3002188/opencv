import cv2

image = cv2.imread("cat.png")

if image is None:
    print("opps here is not available")

else:
    print("image loaded successfully")    

    p1 = (150, 150)
    p2 = 50

    color = (0, 0 , 255)
    thickness = 3

    cv2.circle(image, p1, p2, color, thickness)

    cv2.imshow("circle drawing :", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()