import cv2
import numpy as np

#Aynı boyutlardaki resimler:
img1 = cv2.imread('data/3D-Matplotlib.png',cv2.IMREAD_COLOR)
img2 = cv2.imread('data/mainsvmimage.png',cv2.IMREAD_COLOR)
#Farklı boyutta bir resim:
img3 = cv2.imread('data/mainlogo.png',cv2.IMREAD_COLOR)

#Toplama
 #add = img1 + img2 #Böyle iki RESİM toplanıyor
 #add = cv2.add(img1,img2) #Burada tüm PİXEL değerleri karşılıklı toplanıyor
 #weighted = cv2.addWeighted(img1,0.6,img2,0.4,0) #Yüzde değerler veriyoruz; toplamı 1 olmalı!

rows, cols, channels = img3.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)#Mark
#Thresholding-Eşikleme
 #threshold(src, thresh(altsınır), maxval, type, dst=None, /) -> retval, dst
ret, mask =cv2.threshold(img2gray,220, 255, cv2.THRESH_BINARY_INV)
 #Alt sınırı geçen değerler maxval değerine dönüştürülüyor.
 #Alt sınırın altında olan değerlerl siyaha dönüştürülüyor.
 #Ama bu _INV(inverse) olduğu için tam tersi olacak
cv2.imshow('mask',mask) #Şu anda hem im3(orjinal resim), hem de mask'e sahibiz

mask_invisiable = cv2.bitwise_not(mask)#Maske olmayan yerler, yani bizim resmimizdeki siyah yerler
 #OpenCV bitwise_ işlemleri aynı normal mantık işlemleri gibi sadece daha derin,
 # sonuçları _'dan sonraki kısımdan tahmin edilebilir.

#bitwise_and(src1, src2[, dst[, mask]]) -> dst
img1_background = cv2.bitwise_and(roi,roi,mask=mask_invisiable)
img3_foreground = cv2.bitwise_and(img3, img3,mask=mask)

dst = cv2.add(img1_background, img3_foreground)
img1[0:rows,0:cols] = dst

cv2.imshow('res', img1)
cv2.imshow('mask_inv', mask_invisiable)
cv2.imshow('img1_bg', img1_background)
cv2.imshow('img3_fg', img3_foreground)
cv2.imshow('dst', dst)


cv2.imshow('image',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
