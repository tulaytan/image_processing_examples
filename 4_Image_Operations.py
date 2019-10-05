import cv2
import numpy as np

img = cv2.imread('data/watch.jpg',cv2.IMREAD_COLOR)

#Bir pixele ulaşma:
pixel = img[55,55]
print(pixel)

#Pixeli değişitrme:
img[55,55]=[255,255,255]

#Region of Image:ROI
roi = img[100:150,100:150]
print(roi)
 #Böüm değiştirme:
img[100:150,100:150]=[255,255,255]
 #Bölüm kopyala-yapıştır:
watch_face = img[37:111,107:194]
img[0:74,0:87] = watch_face
 ##Aynı boyutta olmalarına dikkat et! Yoksa hata veriyor!

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
