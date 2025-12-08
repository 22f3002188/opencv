import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


CODEC = cv2.VideoWriter_fourcc(*'XVID')
recorded = cv2.VideoWriter("my_video", CODEC, 20, (frame_width, frame_height))

while True:
    ret, frame = camera.read()   #ret = true/false frame = image

    if not ret:
        print("could not read frame")
        break
    
    recorded.write(frame)
    cv2.imshow("webcam Feed" , frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quitting....")
        break

camera.release()    
cv2.destroyAllWindows()