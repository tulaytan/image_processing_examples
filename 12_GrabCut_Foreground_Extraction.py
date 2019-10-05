import cv2
import numpy as np 
from matplotlib import pyplot as plt

#Bu yöntem biraz manuel!
#Yöntem mantığı:https://www.geeksforgeeks.org/python-foreground-extraction-in-an-image-using-grabcut-algorithm/

img = cv2.imread('data/opencv-python-foreground-extraction-tutorial.jpg')

mask = np.zeros(img.shape[:2],np.uint8)
#np.zeros: Verilen boyutlarda ve türde sıfırlarla dolu dizler yapıyor.
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

#rectangle = (start_x, start_y, width, height).
rect = (161,79,150,150)

#grabCut(img, mask, rect, bgdModel, fgdModel, iterCount, mode=None)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
#Mask için diğer seçenekler 1 ve 3 
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

#Dikdörtgenin şekillerini kendimize göre ayarlayarak
# bu aynı kodu istedidğimiz yerde kullanabiliriz. 

# Eğer bunu daha az manual bir şekilde,daha dinamik,
# otomatik bir şekilde yapmak istiyorsak 
# dikdörtgenin değerlerini sayı vermek yerine değişkenlere bağlayabiliriz. 
# Mesela başlangıç noktası resmin boyutunun %10'nu, genişlik %90'ı vb.
