import numpy as np
import cv2

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        print(x,' ' ,y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY=str(x)+' '+str(y)
        cv2.putText(img,strXY,(x,y),font,1,(255,255,0),2)
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,0,0),5)
        cv2.imshow('image',img)
        print(points)
    if event == cv2.EVENT_RBUTTONDOWN:    
        blue=img[x,y,0]
        green=img[x,y,1] 
        red=img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        img1 = np.zeros((512,512,3),np.uint8)
        img1[:]=[blue,green,red]
        cv2.imshow('color',img1) 


img = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/OPENCV/6.MoreMouseEvents/lena2.jpg')
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()