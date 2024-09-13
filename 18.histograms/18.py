import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load the image in color (to be able to split into b, g, r channels)
img1 = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/11.Thresholding/download.jpeg', cv2.IMREAD_COLOR)

# Create a blank image and draw rectangles on it
img = np.zeros((200, 200), np.uint8)
cv2.rectangle(img, (0, 100), (200, 200), (255), -1)  # White rectangle
cv2.rectangle(img, (50, 100), (150, 150), (127), -1)  # Grey rectangle

# Split the color image into b, g, r channels
b, g, r = cv2.split(img1)

# Display the images using OpenCV
cv2.imshow("Original Image", img1)
cv2.imshow("B channel", b)
cv2.imshow("G channel", g)
cv2.imshow("R channel", r)

# Plot histograms for the grayscale image and the color channels
plt.figure(figsize=(10, 8))

# Histogram for grayscale version of the image
plt.subplot(2, 2, 1)
plt.hist(img1.ravel(), 256, [0, 256])
plt.title('Histogram for Grayscale Image')

# Histogram for blue channel
plt.subplot(2, 2, 2)
plt.hist(b.ravel(), 256, [0, 256], color='blue')
plt.title('Histogram for Blue Channel')

# Histogram for green channel
plt.subplot(2, 2, 3)
plt.hist(g.ravel(), 256, [0, 256], color='green')
plt.title('Histogram for Green Channel')

# Histogram for red channel
plt.subplot(2, 2, 4)
plt.hist(r.ravel(), 256, [0, 256], color='red')
plt.title('Histogram for Red Channel')

# Display the histograms
plt.tight_layout()
plt.show()

# Wait and destroy windows
cv2.waitKey(0)
cv2.destroyAllWindows()
