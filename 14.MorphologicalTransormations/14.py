import cv2
from matplotlib import pyplot as plt 
import numpy as np

img = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/10.HUE/OIP.jpeg', cv2.IMREAD_GRAYSCALE)

_,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV) 
kernal=np.ones((2,2),np.uint8)

dilation=cv2.dilate(mask,kernal,iterations=2)
epsilon=cv2.erode(mask,kernal,iterations=5)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)

titles=['image','mask','dilation','epsilon','opening','closing']
images=[img,mask,dilation,epsilon,opening,closing]

for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()