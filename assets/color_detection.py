import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #WE WANNA CONVERT A BGR IMAGE TO AN HSV IMAGE
    lower_blue = np.array([110,50,50]) #THIS IS THE COLOUR WE WANNA EXTRACT AND THERE IS A RANGE YOU CAN INITIALIZE
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue) #only keeps the pixels in our range and masks the other values

    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()