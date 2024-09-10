import cv2
import datetime
cap=cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1280)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,720)
while(True):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_SIMPLEX
        text='Width:'+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+'Height:'+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        
    
        cv2.imshow('frame',frame)

        if cv2.waitKey(1)&0xFF==ord('q'):
            break
    else:
        break    
    
    
cap.realease()