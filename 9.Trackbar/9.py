import numpy as np
import cv2 as cv

def nothingh(x):
    print(x)


img=np.zeros((300,512,3),np.uint8)    
cv.namedWindow('image')
cv.createTrackbar('R','image',0,255,nothingh)
cv.createTrackbar('B','image',0,255,nothingh)
cv.createTrackbar('G','image',0,255,nothingh)

while(1):
    cv.imshow('image',img)
    k=cv.waitKey(1)&0xFF
    if k==27:
        break
    
    b=cv.getTrackbarPos('B','image')
    g=cv.getTrackbarPos('G','image')
    r=cv.getTrackbarPos('R','image')
    
    img[:]=[b,g,r]
    
cv.destroyAllWindows()    
 