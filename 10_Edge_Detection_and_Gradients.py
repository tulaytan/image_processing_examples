import cv2
import numpy as np 


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() 
    
    #Laplacian(src, ddepth, dst=None, ksize=None, scale=None, delta=None, borderType=None)
    #İki yöne de gidebilir: x,y
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    
    #Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

    #Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
    edges = cv2.Canny(frame,100,100)

    cv2.imshow('original',frame)
    cv2.imshow('laplacion',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('CannyEdgesDetection',Edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: #ESC'nin kodu, Çıkmak için ESC ye bas
        break


cv2.destroyAllWindows()
cap.release()
