import cv2 
import numpy as np

FRAME_WIDTH = 320
FRAME_HEIGHT = 150

cap = cv2.VideoCapture(0)
cap.set(3,FRAME_WIDTH)
cap.set(4,FRAME_HEIGHT)

def empty(a):
    pass

cv2.namedWindow("HSV Manager")
cv2.resizeWindow("HSV Manager" , 640,240)
cv2.createTrackbar("HUE MIN", "HSV Manager" , 0,179,empty)
cv2.createTrackbar("HUE MAX", "HSV Manager" , 179,179,empty)
cv2.createTrackbar("SAT MIN", "HSV Manager" , 0,255,empty)
cv2.createTrackbar("SAT MAX", "HSV Manager" , 255,255,empty)
cv2.createTrackbar("VAL MIN", "HSV Manager" , 0,255,empty)
cv2.createTrackbar("VAL MAX", "HSV Manager" , 255,255,empty)


while(True):
    _,img = cap.read()  
    img = cv2.flip(img,1)
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE MIN","HSV Manager")
    h_max = cv2.getTrackbarPos("HUE MAX","HSV Manager")
    s_min = cv2.getTrackbarPos("SAT MIN","HSV Manager")
    s_max = cv2.getTrackbarPos("SAT MAX","HSV Manager")
    v_min = cv2.getTrackbarPos("VAL MIN","HSV Manager")
    v_max = cv2.getTrackbarPos("VAL MAX","HSV Manager")


    lower = np.array([h_min,s_min,v_min])
    upper= np.array([h_max,s_max,v_max])
    

    mask = cv2.inRange(imgHsv,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)

    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img,mask,result])

    # cv2.imshow("Original",img)
    # cv2.imshow("Hsv Picture",imgHsv)
    # cv2.imshow("Mask",mask)
    cv2.imshow("Horizontal Stack",hStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

cap.release() 
cv2.destroyAllWindows()
