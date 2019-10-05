import numpy as np
import cv2
import matplotlib.pyplot as plt

#Bu 'kaba kuvvetle' çalışan bir algoritma, 
#Eşleşme yapabilmek için bütün her yere teker teker bakarak çalışıyor

#Siyah beyaz aç
img1 = cv2.imread('data/opencv-feature-matching-template.jpg',0)
img2 = cv2.imread('data/opencv-feature-matching-image.jpg',0)

#Benzerlik algılayıcısı:
orb = cv2.ORB_create()
 # Oriented FAST and Rotated BRIEF
 #ORB; FAST keypoint detector ve BRIEF descriptor algoritmalarının 
 # performansı iyileştirici değişiklikler yapılarak birleştirilmiş şekli.

#Key points:
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)


bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
 #Brute-force descriptor matcher algoritması
 #Bu algoritma, 1. kümedeki her 'descriptor'(tanımlayıcı, anahtar nokta için)
 #2. kümedeki en yakın eşleşmeyi elemanların hepsi ile teker teker deneyerek bulmaya çalışıyor. 
 # Bu descriptor matcher , tanımlayıcı kümelerdeki olası eşleşmeleri maskelemeye izin veriyor

#Eşleşmeleri uyum düzeyine göre sırala
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

#drawMatches(img1, keypoints1, img2, keypoints2, matches1to2, outImg, matchColor=None, singlePointColor=None, matchesMask=None, flags=None)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
#Kaç tane eşleşme göstereceğine dikkat et, 
# bir yerden sonra kötü eşleşmeler göstermeye başlayacak
plt.imshow(img3)
plt.show()