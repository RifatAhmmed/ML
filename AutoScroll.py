import cv2
import numpy as np
import pyautogui as gui

cap = cv2.VideoCapture(0)

lower_blue = np.array([100,150,0])
upper_blue = np.array([140,255,255])

pre_y = 0
pre_x = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        area = cv2.contourArea(c)
        if area > 30:
            x, y, w, h = cv2.boundingRect(c)
            #cv2.drawContours(frame, c, -1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y+h), (0, 0, 255), 2)
            
            if y < pre_y:
                print("Moving Down...!!")
                gui.press('space')
                pre_y = y
                
            """if y > pre_y:
                print("Moving Down...!!")
                gui.press('up')
                pre_y = y"""
                
        
            
        
    
    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

