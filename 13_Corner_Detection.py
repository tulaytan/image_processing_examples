import numpy as np
import cv2

#Kenar bulma, haraket algılama ve bir çok farklı şeyde kullanılabilir
img = cv2.imread('data/opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, corners=None, mask=None, blockSize=None, useHarrisDetector=None, k=None)
 #Algoritma verilen resimdeki güçlü köşeleri belirliyor
#Yeterince köşenin bulunmasına izin verdiğinden emin ol:maxCorners!^
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-2)
    
cv2.imshow('Corner',img)
cv2.waitKey(0)
cv2.destroyAllWindows()