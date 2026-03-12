import cv2
import numpy as np

#load a video capture

cap = cv2.VideoCapture(0) #put 0 if only one device else if there are multiple devices then put dev.no
# you can also put cv2.VideoCapture('video source') if you dont want webcam

while True:
    ret, frame = cap.read() #returns an error if there are any and itll return a frame as well which is a numpy array
    
    width = int(cap.get(3)) #cap.get(3) gets you the width of the image
    height = int(cap.get(4)) #cap.get(4) gets you the height of the image, there are total 17 properties of this

    smaller_frame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5) #we want 4 pics in one screen so we reduce width and heigth of the og pic

    image = np.zeros(frame.shape, np.uint8) #create a blank canvas for your pictures with the same shape as frame
    image[:height//2, :width//2] = smaller_frame
    image[height//2:,:width//2] = smaller_frame
    image[:height//2,width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:,width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)

    
     

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'): # here waitkey is in milliseconds and ord'q' means that if we press q on teh keyboard then itll stop and capture. ord means the ascii function
        break

cap.release()
cv2.destroyAllWindows()