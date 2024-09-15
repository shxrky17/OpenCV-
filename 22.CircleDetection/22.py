import cv2
import numpy as np

img = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/10.HUE/OIP.jpeg')
output=img.copy()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)
circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
detectcircles=np.uint16(np.around(circles))

for (x,y,r) in detectcircles[0,:]:
    cv2.circle(output,(x,y),r,(0,255,0),2)
    

cv2.imshow("image",output)
cv2.waitKey(0)
cv2.destroyAllWindows()