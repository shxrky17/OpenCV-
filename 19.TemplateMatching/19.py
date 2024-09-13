import cv2
import numpy as np

# Load the main image and convert to grayscale
img = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/19.TemplateMatching/1.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the template and convert to grayscale
template = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/19.TemplateMatching/OIP.jpeg', 0)
w, h = template.shape[::-1]

# Perform template matching
res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)

# Set a threshold for detection
threshold = 0.9
loc = np.where(res >= threshold)
print(loc)

# Draw rectangles around the matches
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

# Display the result image
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
