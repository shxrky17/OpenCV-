import cv2
import numpy as np

def nothingh(x):
    pass

cap=cv2.VideoCapture(1)
cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothingh)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothingh)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothingh)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothingh)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothingh)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothingh)

while True:
    _,frame=cap.read()
    
    # Check if image was loaded correctly
    if frame is None:
        print("Error: Unable to load image.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for the color range in HSV
   
    l_h=cv2.getTrackbarPos("LH",'Tracking')
    l_s=cv2.getTrackbarPos("LS",'Tracking')
    l_v=cv2.getTrackbarPos("LV",'Tracking')
    
    u_h=cv2.getTrackbarPos("UH",'Tracking')
    u_s=cv2.getTrackbarPos("US",'Tracking')
    u_v=cv2.getTrackbarPos("UV",'Tracking')


    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    # Create a mask using the HSV bounds
    mask = cv2.inRange(hsv, l_b, u_b)

    # Apply the mask to the original frame
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, mask, and result
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break
    
cap.release()
cv2.destroyAllWindows()
