import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame,(0,0), (width,height), (255,100,255), 10) #to draw a line we first specify the image we draw it in and then the pixels: start point, end point. (0,0) is the top left
    #last two are line color and line width that is being drawn
    img  = cv2.line(img,(width,0),(0,height),(0,255,255),10)

    #draw rectangles
    img = cv2.rectangle(img, (100,100),(200,200),(128,128,128), -1) #here we pass the top left first and then the bottom right co-ordinate, if you put -1 as the thickness then it fills up the entire screen/solid rectangle

    #draw circles
    img = cv2.circle(img,(width//2,height//2),200,(255,255,0),-1) #here its center then radius then again the color and all and then thickness
    
    #for text it is a bit tricky because we need to assign a font to it first
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, "Samarth MC", (200,height-10), font, 4, (0,0,0), 5, cv2.LINE_AA ) #you need to first add the img then the text you want then the position of the text(this is taken from the bottom left not the top left) then font and then the font scale then lastly Line_AA is to make it pretty

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('1'):
        break

cap.release()
cv2.destroyAllWindows()
