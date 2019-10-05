import cv2
import numpy as np 


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() 

    #HSV formatındaki frameler:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Kırmızı için seçtiğimiz alt sınır:
    lower_red = np.array([150,150,0])
    #Kırmızı için seçtiğimiz üst sınır:
    upper_red = np.array([180,255,255])

    #inRange(src, lowerb, upperb, dst=None)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame,frame,mask = mask)
    #Üstteki kod 7_Color_Filtering ile aynıdır.

    #Pürüz giderme için:

    #Sadece ortalamasını alsak olur:
    kernel = np.ones((15,15), np.float32)/(15*15)
     #verilen şekil ve türde, birlerle dolu yeni bir dizi döndürüyor.

    #filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None)
    smoothed = cv2.filter2D(result, -1, kernel)
     #Verdiğimiz resim ile kernel'in konvolüsyonunu alıyor.

    #Ya da gaussian uygulayabiliriz:
    #GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
    blur = cv2.GaussianBlur(result, (15,15), 0)

    #Ya da median:
    #medianBlur(src, ksize, dst=None, /)
    median = cv2.medianBlur(result,15)

    #ya da bilateral:
    #bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType, /)
    bilateral = cv2.bilateralFilter(result,15,75,75)


#SHOW
    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', result)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('Gblur', blur)
    cv2.imshow('Median', median)
    cv2.imshow('Bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: #ESC'nin kodu, Çıkmak için ESC ye bas
        break


cv2.destroyAllWindows()
cap.release()
