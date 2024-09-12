import cv2
import numpy as np

# Create a blank image (black image)
img = np.zeros((250, 500, 3), np.uint8)

# Load another image from a file
img2 = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/8.ImageBITOPERATIONS/12.png')

# Ensure that img2 was loaded successfully and both images are the same size
if img2 is None:
    print("Error: '12.png' could not be loaded. Check the file path.")
else:
    # Resize img2 to match the dimensions of img (if necessary)
    img2 = cv2.resize(img2, (img.shape[1], img.shape[0]))

    # Perform bitwise AND operation
    bitAnd = cv2.bitwise_and(img, img2)
    bitAnd = cv2.bitwise_or(img, img2)
    bitAnd = cv2.bitwise_xor(img, img2)
    # Display the result
    cv2.imshow('bitand', bitAnd)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
