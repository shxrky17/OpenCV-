import cv2
from matplotlib import pyplot as plt

# Read the image in grayscale
img = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/11.Thresholding/download.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply different thresholding methods
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_TRUNC)
_, th3 = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO)
_, th4 = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO_INV)

# Store images and titles for plotting
images = [th1, th2, th3, th4]
titles = ['Binary', 'Truncate', 'Tozero', 'Tozero Inv']

# Plotting the images with matplotlib
plt.figure(figsize=(10, 6))  # Optional: adjust figure size for better readability
for i in range(4):
    plt.subplot(2, 2, i+1)  # 2x2 grid, i+1 for the subplot index
    plt.imshow(images[i], cmap='gray')  # Use 'gray' colormap for grayscale images
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  # Hide ticks

plt.show()
