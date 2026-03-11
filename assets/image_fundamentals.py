import cv2
import random
img = cv2.imread('assets/pic1.JPG', 1)

print(img)

tag = img[1400:1900, 400:800]
img[500:1000 , 600:1000] = tag


for i in range(6000):
    for j in range(100):
        img[i][j] = [255,random.randint(0,255),random.randint(0,255)]

cv2.imshow('window2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

