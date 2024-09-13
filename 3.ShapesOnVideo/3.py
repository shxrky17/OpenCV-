import cv2
import os
import numpy as np
# Specify the full path to the image
image_path = r'c:\Users\chafl\OneDrive\Desktop\yash\OPENCV\3.ShapesOnVideo\lena2.jpg'

# Check if the image file exists at the specified path
if not os.path.exists(image_path):
    print(f"Error: The file at {image_path} does not exist.")
else:
    # Load the image
    #img = cv2.imread(image_path, 1)
    img=np.zeros([512,512,3],np.uint8)

    if img is None:
        print("Error: Image not found or unable to load.")
    else:
        # Draw a line on the image
        img = cv2.line(img, (111,1), (255, 255), (147, 96, 44), 10)
        img = cv2.arrowedLine(img, (0,255), (255, 255), (147, 96, 44), 10) 
        img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),20)
        img=cv2.circle(img,(447,63),63,(0,255,0),-1)
        font=cv2.FONT_HERSHEY_SIMPLEX
        img=cv2.putText(img,'OpenCV',(10,500),font,4,(0,255,255),10,cv2.LINE_AA)
        cv2.imshow('image', img)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
