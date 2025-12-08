import cv2

image = cv2.imread("cat.png")

if image is None:
    print("opps here is not available")

else:
    print("image loaded successfully")    

    p1 = (50, 100)
    p2 = (300, 100)

    color = (255, 0, 0)
    thickness = 4

    cv2.line(image, p1, p2, color, thickness)
    cv2.imshow("line drawing :", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()