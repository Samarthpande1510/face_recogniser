import cv2

img = cv2.imread('assets/football1.jpg', 0)
temp = cv2.imread('assets/template.png', 0)
h, w = temp.shape #if it is a GrayScale image then it is a 2D array instead of a 3D ARRAY

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED
           , cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] #try each method and see which one gets you the best results
#read the docs for these

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, temp, method)
    # size of the resultant array will be (W - w + 1, H - h + 1)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #this tells us the min value of the array and max value plus its location which is very important
    print(min_loc, max_loc)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc #if you use these 2 methods then you must use the min value
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location,bottom_right,255,5)
    cv2.imshow('window',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
