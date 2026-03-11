import cv2

img = cv2.imread('assets/pic1.JPG', 1)

#-1 ,cv2.IMREAD_COLOR: Loads a color image, Any transparency of image will be neglected. It is the default flag 
#0 , cv2.IMREAD_GREYSCALE: Loads image in grayscale mode
#1 , cv2.IMREAD_UNCHANGED: Loads image as such including alpha channel

# img = cv2.resize(img, (400,900)) this is the normal method to resize
img = cv2.resize(img, (0,0), fx= 0.2, fy = 0.2)

img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

#How to save changes to an image
cv2.imwrite('new_img.jpg', img) #it'll create a new file with the saved changes


cv2.imshow('Image1',img) #first parameter is for the window name where the image will be displayed
cv2.waitKey(0) # wait an infinite amount of time till i press a key ( 0 means infinite time, eg: 5 secs means wait 5 seconds on this window and then skip it )
cv2.destroyAllWindows() #Once the timer is done do then itll destory it 
cv2
