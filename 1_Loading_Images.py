import cv2
import numpy as np
import matplotlib.pyplot as plt

#IMREAD_GRAYSCALE--> 0
img = cv2.imread('data/watch.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR --> 1
#IMREAD_UNCHANGED --> -1

#Opencv ile:
cv2.imshow('WatchImage',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 #Resmi kaydetme:
cv2.imwrite('watchgray.png',img)

# Opencv, BGR kullanıyor.
# Matplotlib, ise RGB kullanıyor.

#Matplotlib ile gösterme:
plt.imshow(img, cmap='gray',interpolation='bicubic')
 #Matplotlib ile resim üzerinde çizgi çizme:
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()
