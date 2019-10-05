import numpy as np
import cv2

cap = cv2.VideoCapture('data/people-walking.mp4')

#createBackgroundSubtractorMOG2(, history=None, varThreshold=None, detectShadows=None)
fgbg = cv2.createBackgroundSubtractorMOG2()
 #Algoritma frameler arasında değişen kısımları buluyor,
 # bunun sonucunda değişen kısımlar 'foreground' olarak, 
 # değişmeyenler ise 'background' olarak işlenecek ve değişmeyenler kaldıracak.

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('original',frame)
    cv2.imshow('fg',fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()