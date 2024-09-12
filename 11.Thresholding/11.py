import cv2
import numpy as np

img=cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/11.Thresholding/download.jpeg')
_,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)
_,th3=cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
_,th4=cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('Image',img)
cv2.imshow('res',th1)
cv2.imshow('trunc',th2)
cv2.imshow('torezo',th3)
cv2.imshow('torezo',th4)
cv2.waitKey(0)
cv2.dstroyAllWindows()