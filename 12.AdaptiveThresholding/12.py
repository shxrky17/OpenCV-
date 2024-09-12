import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/10.HUE/OIP.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply adaptive thresholding
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Display the original image and the adaptive thresholding result
cv2.imshow('Original Image', img)
cv2.imshow('Adaptive Thresholding', th2)

# Wait until a key is pressed and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
