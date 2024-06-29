#open camera using opencv

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
else:
    while True:
        ret,frame=cap.read()                                      #frame=framepixelvalues ret=true/false

        if not ret:
            print("Could not read camera")
            break
        
        points = np.array([(125,250),(350,450),(250,300)])     #drawing contour
        cv2.putText(frame,'hello',(100,100),cv2.FONT_HERSHEY_DUPLEX,5,(0,255,0))        #BGR FORMAT    for putting text on the frame
        cv2.circle(frame,(100,100),50,(125,125,125),3)            #to draw circle 
        cv2.line(frame,(120,250),(150,300),(255,0,0),3)
        cv2.rectangle(frame,(100,150),(300,250),(255,0,0),-1)

        cv2.drawContours(frame,[points],-1,(0,255,0),3)

        cv2.imshow('hello',frame)
        if cv2.waitKey(1) & 0xFF == ord('n'):   
           break 

cap.release()
cv2.destroyAllWindows()
