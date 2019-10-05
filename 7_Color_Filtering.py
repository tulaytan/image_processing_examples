import cv2
import numpy as np 

#Belli bir rengi bul veya sadece o rengi göster 
# veya sadece o renk haricindekileri göster vb....
# gibi işlemleri yapmak için kullanılıyor.

cap = cv2.VideoCapture(0)
 #Video yerine resim kullanıyorsak while kullanmamıza gerek yok
while True:
    _, frame = cap.read() 
     # Dönüş değişkeinini _ olarak isimlendirerek; bu değişkenin önemsiz olduğunu 
     # ve verilmesi gerekli olmakla birlikte başka yerde kullanılmadığını belirtmiş oluyoruz
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
     # Hue, saturation, value
    lower_red = np.array([150,150,0])
    upper_red = np.array([180,255,255])

    #inRange(src, lowerb, upperb, dst=None, /)
    mask = cv2.inRange(hsv, lower_red, upper_red)
     # inRange true ise 1 olacak o da beyaz demek olacak
     # öyle olunca da aşağıdaki AND işlemi kaynak1'in
     # kaynak2'ye eşit olduğu yerlerde istenen rengi(burada kırmızı) gösterecek
     #Range nin dışında ise 0 olacak ve bu yerler siyah gösterilecek
    #bitwise_and(src1, src2, dst=None, mask=None)
    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: #ESC'nin kodu, Çıkmak için ESC ye bas
        break

#FILTERING
#Range yi değiştirerek istediğimiz filreyi belirleyebiliriz

cv2.destroyAllWindows()
cap.release()
