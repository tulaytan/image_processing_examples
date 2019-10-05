import cv2
import numbers as np

capture= cv2.VideoCapture(0)# Kamera birden fazlaysa 0,1,2...
#0 yerine video dosyası ismi yazınca onu açıyor.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc:Four Character Code -->It uniquely identfy data formats
#VideoWriter (const String &filename, int fourcc, double fps, Size frameSize, bool isColor=true)
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    retrn, frame =capture.read()
    #'ConvertColor': Renk sistemini değiştirme fonksiyonu
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Çıktı video için frame'leri seçtiğimiz fps'de yaz:
    out.write(frame)

    cv2.imshow('Baslik',frame)
    cv2.imshow('Gray',gray)
    
    #Çıkmak istersek q'ya basarak çıkış:
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

capture.release()
out.release()
cv2.destroyAllWindows()



