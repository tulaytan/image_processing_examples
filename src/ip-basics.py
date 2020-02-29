import cv2
import numpy as np
import matplotlib.pyplot as plt

# İmge İşleme
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1
#IMREAD_GRAYSCALE = 0
#img = cv2.imread('../img/ataturk.jpg', cv2.IMREAD_GRAYSCALE)

#OpenCV ile İmge ve Gösterme
#BGR gösterir
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Matplotlib ile İmge Okuma ve Gösterme
#RGB gösterir
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.show()

# Video İşleme
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     out.write(frame)
#     cv2.imshow('Frame',frame)
#     cv2.imshow('Gray', gray)
#     if (cv2.waitKey(1) & 0xFF == ord('q')):
#         break
# cap.release()
# out.release()
# cv2.destroyAllWindow()

# OpenCV'de COLOR "BGR" sırasındadır.
# 15 pixellik beyaz renkte bir çizgi çizen algortima
img = cv2.imread('../img/apricot.jpg',cv2.IMREAD_COLOR)

# cv2.line(img, (0,0), (0, 50), (255, 255, 255), 5)
# cv2.line(img, (0,0), (50, 0), (255, 255, 255), 5)
# cv2.line(img, (50,0), (50, 50), (255, 255, 255), 5)
# cv2.line(img, (0,50), (50, 50), (255, 255, 255), 5)
# cv2.rectangle(img, (0,0), (50, 50), (255, 255, 255), 1)
# i=0
# while i != 400:
#     i = i+5
#     cv2.rectangle(img, (i,i), (i*2,i*2), (255, 255, 255), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



