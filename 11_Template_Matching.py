import cv2
import numpy as np 

# Uyuşma sınırını geçen değerler dikdörtgen içine alınacak

img_bgr = cv2.imread('data/template-match.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

templat = cv2.imread('data/template.jpg')
template= cv2.cvtColor(templat,cv2.COLOR_BGR2GRAY)
w, h = template.shape[::-1]

result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# Uyuşma sınır oranını ayarlayabiliyoruz burada en az %80:
threshold = 0.8
 #Daha çok eşleşme almak için; sınırı düşürmektense 
 # sınırı geçmeyenlerin resmini alıp 
 # birden fazla template e sahip olmak daha iyi
loc = np.where(result >= threshold)

#zip(iter1: Iterable[Any], iter2: Iterable[Any], iter3: Iterable[Any],
# iter4: Iterable[Any], iter5: Iterable[Any], iter6: Iterable[Any],
#  *iterables: Iterable[Any])
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w,pt[1]+h),(0,225,225),2)

cv2.imshow('matched',img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()