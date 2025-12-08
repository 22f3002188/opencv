import cv2

image = cv2.imread("cat.png")

if image is None:
    print("opps here is not available")

else:
    print("image loaded successfully")  

    cv2.putText(image, "hello python student", (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,255), 2) 


   

    cv2.imshow("text drawing :", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()