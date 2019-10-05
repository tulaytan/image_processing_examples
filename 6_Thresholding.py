import cv2
import numpy as np 

#Eşiklemeyi resmi basitleştirmek için kullanıyoruz.

img = cv2.imread('data/bookpage.jpg')
#threshold(src, threshval, maxval, type, dst=None, /) -> retval, dst
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
 #Resmimiz karanlık bir resim olduğu için sınır 12,
 # eğer daha açık bir resim olsaydı bu sayıyı arttırabilirdik.
 # İhtiyacımıza göre değerler veriyoruz.
#cv2.imshow('threshold',threshold)
 # Renkli bir resimle başlayıp ona hiç işlem yapmadan, mesela siyah beyaz yapma,
 # filtre uyguladığmız için sonuçta değişik renkler bulunuyor.

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold2', threshold2)

#GAUS threshold
#adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None, /) -> dst
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
cv2.imshow('gausAdaptive', gaus)

#OTSU Threshold
  #Bu resim için doğru bir filtre değil.
retval3,threshold3 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu threshold',threshold3)

cv2.imshow('origina', img)
cv2.imshow('gray', grayscaled)

cv2.waitKey(0)
cv2.destroyAllWindows()
