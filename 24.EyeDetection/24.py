import cv2
import numpy as np

# Load the image
img = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/23.FaceDetection/2.jpeg')
if img is None:
    print("Error: Could not load image.")
    exit()

# Load the Haar Cascades for face and eye detection
face_cascade = cv2.CascadeClassifier('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/23.FaceDetection/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/23.FaceDetection/haarcascade_eye_tree_eyeglasses.xml')

# Check if the classifiers have been loaded properly
if face_cascade.empty() or eye_cascade.empty():
    print("Error: Could not load Haar Cascade XML files.")
    exit()

# Convert the image to grayscale (needed for face detection)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform face detection
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

# Draw rectangles around detected faces and detect eyes within the face region
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)  # Blue rectangle around face
    
    # Region of interest (ROI) for eyes (within the face region)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    # Detect eyes within the face region
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
    # Draw rectangles around detected eyes
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 4)  # Green rectangle around eyes

# Display the result
cv2.imshow('Face and Eye Detection', img)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
