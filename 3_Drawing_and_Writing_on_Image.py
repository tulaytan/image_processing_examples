import cv2
import numpy as np

img = cv2.imread('data/watch.jpg',cv2.IMREAD_COLOR)

#Çizgi çizme:
#line(img, pt1, pt2, color(bgr), thickness, lineType, shift, /)
cv2.line(img,(0,0),(150,150),(100,100,100),10)

#Şekillerde Tickness'e negatif verirsen içini dolduruyor!

#Dikdörtgen çizme:
#rectangle(img, pt1, pt2, color, thickness, lineType,shift, /)
#İki çapraz köşeyi veriyoruz
cv2.rectangle(img,(10,15),(50,155),(100,10,100),-5)

#Daire çizme:
#circle(img, center, radius, color, thickness, lineType, shift, /)
cv2.circle(img, (100,100),60,(100,10,10),-4)

#Çokgen çizme:
points = np.array([[10,5],[3,6],[19,55],[100,9],[66,88]], np.int32)
#polylines(img, pts, isClosed, color, thickness, lineType, shift, /)
cv2.polylines(img,[points],True,(0,200,200),3)
#Tickness >= 0, diğerleri gibi negatift değerlerde içini doldurmuyor
#isClosed: Kapatmak zorunda değilsin

#YAZI YAZMA:
font = cv2.FONT_HERSHEY_PLAIN
#putText(img, text, org(origin), fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin, /)
cv2.putText(img,'TulayTan!',(10,100),font,3,(120,200,130),5)
#org(origin?):Yazının başlangıç alt-sol köşesi
#FontScale: Onluk sayıları da kabul ediyor


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
