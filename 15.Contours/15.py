import cv2
import numpy as np

# Load the image
img = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/10.HUE/OIP.jpeg')

# Convert to grayscale
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Print details about the first contour (instead of printing all points)
print(f"Number of points in first contour: {len(contours[0])}")
print(f"Area of first contour: {cv2.contourArea(contours[0])}")
print(f"Perimeter of first contour: {cv2.arcLength(contours[0], True)}")

# Draw all contours on the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Display the original image with contours and the grayscale image
cv2.imshow('Original Image with Contours', img)
cv2.imshow('Grayscale Image', imgray)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
