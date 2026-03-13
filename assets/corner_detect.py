import numpy as np
import cv2

img = cv2.imread("assets/chess1.png", -1) #whenever we try to detect a corner its better to use a grayscale image
img= cv2.resize(img,(0,0),fx = 1.5, fy = 1.5)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(gray,100, 0.1, 10)
#first enter the img name then the enter the no. of best corners you'd want like if there are 500 corners youd'd like the 100 best ones. 
#then is the quality of the corners between 0-1 with 1 being 100% corner
#last thing is the min eucledian distance between 2 corners if theyre too close

print(corners) #returns the float values and we need to return them in int
corners = np.int_(corners) #we need to ravel this

for corner in corners:
    x, y = corner.ravel() # if input is [[[2,3,4]] --> [2,3,4]
    cv2.circle(img, (x,y), 5, (255,0,0), -1)

#draw lines between each corner
for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x),np.random.randint(0,255,size = 3)))
        cv2.line(img,corner1,corner2,color,1)
cv2.imshow("frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()