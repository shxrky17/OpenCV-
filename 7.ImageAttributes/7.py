import numpy as np
import cv2

img = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/7/lena2.jpg')

img2 = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/7/th.jpeg')

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
ball=img[280:340,330:390]
img[273:333,100:160]=ball

img2=cv2.resize(img2,(512,512))
img=cv2.resize(img,(512,512))

dst=cv2.addWeighted(img,.5,img2,.5,0)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()