import cv2
import numpy as np

# Load the image
img = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/23.FaceDetection/1.jpeg')


if img is None:
    print("Error: Could not load image.")
    exit()

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/23.FaceDetection/haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("Error: Could not load Haar Cascade XML file.")
    exit()

# Convert the image to grayscale (needed for face detection)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform face detection
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

# Display the result
cv2.imshow('Face Detection', img)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
