import numpy as np
import cv2

#Cascade dedection yapabilmek için ilk önce cascade dosyalarına ihtiyacımız var

# Değişik Cascedeler: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detectMultiScale(image, scaleFactor=None, minNeighbors=None, flags=None, minSize=None, maxSize=None)
    #https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html#cascadeclassifier-detectmultiscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]#İmpoze ettiğimizde kullanmak için
        eyes = eye_cascade.detectMultiScale(roi_gray)
        #Gözleri yüzün içinde armamız gerektiği için bu for diğerinin içinde
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

#Kod ağızı da göz olara algılılayabiliyor!
#Kendi Haar Cascademizi yapmak mümkün
#Ama tabi ki de zor olabilir.
#Bunun için; çok cpu, çok ram ve çok zaman ihtiyaç var

#! https://cvdazzle.com/ !:Yüz tannımadan kaçınma için.