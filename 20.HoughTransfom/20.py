import cv2
import numpy as np

# Load the image
img = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/20.HoughTransfom/3.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge detection using Canny
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# Draw the lines on the image
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = rho * a
        y0 = rho * b
        x1 = int(x0 + 100 * (-b))
        y1 = int(y0 + 100 * (a))
        x2 = int(x0 - 100 * (-b))
        y2 = int(y0 - 100 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the image with the detected lines
cv2.imshow('Hough Line Transform', img)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
